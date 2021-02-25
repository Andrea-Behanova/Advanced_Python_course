
import register_example_with_adam as reg
from skimage import io
import numpy as np
from os import listdir
import scipy.ndimage
from os.path import isfile, join
import multiprocessing as mp
from scipy import ndimage
import filters

paths = 'C:/Users/andre/Desktop/10ms3500ill_cropped'
onlyfiles = [f for f in listdir(paths) if isfile(join(paths, f))]

mid_index = len(onlyfiles) // 2
ref_paths = onlyfiles[mid_index]
flo_paths = onlyfiles[0:mid_index] + onlyfiles[mid_index+1:]
out_paths = 'C:/Users/andre/Desktop/10ms3500ill_cropped/registered/reg'


#print(ref_paths)
def sharpen(im,alpha,sigma1,sigma2):
    im = im.astype('float')
    im = filters.normalize(im, 0, None) * 0.5 + 0.25

    blurred_f = ndimage.gaussian_filter(im, sigma1)
    filter_blurred_f = ndimage.gaussian_filter(blurred_f, sigma2)
    sharpened = im + alpha * (blurred_f - filter_blurred_f)
    return np.clip(sharpened, a_min = 0.0, a_max = 1.0)


def registr(all_paths):
    ref = all_paths[0]
    flo = all_paths[1]
    out = all_paths[2]
    reg.run(ref,flo,out)

def vol_3D(regfiles, sharpening, alpha, sigma1, sigma2, ref_im, sharpened, regpath):
    final_vol[0,:,:] = sharpened
    x_start = 1
    x_end = len(ref_im[0])
    y_start = 1
    y_end = len(ref_im[1])

    for i in range(len(regfiles)):
        filee = regpath + regfiles[i]
        reg_im = io.imread(filee, as_gray=True)

        #sharpening
        if sharpening == 1:
            sharpened = sharpen(reg_im,alpha,sigma1,sigma2)
        else:
            sharpened = reg_im
        

        final_vol[i+1,:,:] = sharpened
        sum_act_mask = len(np.where(reg_im == 0)[0])

        crop_idx = np.nonzero(reg_im)
        x_act_start = min(crop_idx[0])
        x_act_end = max(crop_idx[0])
        y_act_start = min(crop_idx[1])
        y_act_end = max(crop_idx[1])

        if x_act_start > x_start:
            x_start = x_act_start

        if x_act_end < x_end:
            x_end = x_act_end

        if y_act_start > y_start:
            y_start = y_act_start

        if y_act_end < y_end:
            y_end = y_act_end

    #crop mask in 3D
    crop_vol = final_vol[:,x_start+1:x_end-1,y_start+1:y_end-1]
    return crop_vol


def aggregation(crop_vol):
    # Aggregation
    agg_im_mean = np.zeros((crop_vol.shape[1],crop_vol.shape[2]))
    agg_im_median = np.zeros((crop_vol.shape[1],crop_vol.shape[2]))
    for i in range(crop_vol.shape[1]):
        print(i)
        for j in range(crop_vol.shape[2]):
            agg_im_mean[i,j] = np.mean(crop_vol[:,i,j])
            agg_im_median[i,j] = np.median(crop_vol[:,i,j])
    return agg_im_mean, agg_im_median

if __name__ == '__main__':
    all_p = []
    for i in range(len(flo_paths)):
        p = [join(paths,ref_paths), join(paths,flo_paths[i]), out_paths+str(i+2).zfill(3)+'.tiff']
        all_p.append(p)

    #parallel registration
    with mp.Pool(4) as p:
        p.map(registr, all_p)

    # merging registered images into 3D volume
    regpath = out_paths[:-3]
    regfiles = [f for f in listdir(regpath) if isfile(join(regpath, f))]

    ref_file = join(paths,ref_paths)
    ref_im = io.imread(ref_file, as_gray=True)
    final_vol = np.zeros((len(onlyfiles),ref_im.shape[0],ref_im.shape[1]))

    #sharpening
    sharpening = 0
    sigma1 = 1
    sigma2 = 0.5
    alpha = 50

    if sharpening == 1:
        sharpened = sharpen(ref_im,alpha,sigma1,sigma2)
    else:
        sharpened = ref_im

    crop_vol = vol_3D(regfiles, sharpening, alpha, sigma1, sigma2, ref_im, sharpened, regpath)

    io.imsave('./dataset/3Dvol_pattern.tiff', (crop_vol).astype('uint16')) #*65535 if shapening

    [agg_im_mean, agg_im_median] = aggregation(crop_vol)

    io.imsave('./dataset/agg_im_pattern_mean.tiff', (agg_im_mean).astype('uint16')) #*65535 if shapening
    io.imsave('./dataset/agg_im_pattern_median.tiff', (agg_im_median).astype('uint16')) #*65535 if shapening


