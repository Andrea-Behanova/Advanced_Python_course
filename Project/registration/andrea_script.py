
import register_example_with_adam as reg
from skimage import io
import numpy as np
from os import listdir
from os.path import isfile, join
import multiprocessing as mp
from scipy import ndimage
import filters

import line_profiler
import atexit
profile = line_profiler.LineProfiler()
atexit.register(profile.print_stats)

paths = 'C:/Users/andre/Desktop/10ms3500ill_cropped'
onlyfiles = [f for f in listdir(paths) if isfile(join(paths, f))]

mid_index = len(onlyfiles) // 2
ref_paths = onlyfiles[mid_index]
flo_paths = onlyfiles[0:mid_index] + onlyfiles[mid_index+1:]
out_paths = 'C:/Users/andre/Desktop/10ms3500ill_cropped/registered/reg'

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

def vol_3D(regfiles, sharpening, alpha, sigma1, sigma2, regpath):
    final_vol = np.array([sharpen(io.imread(regpath + p, as_gray=True),alpha,sigma1,sigma2) for p in regfiles])
    crop_vol = final_vol[:,21:437,50:398]
    return crop_vol

def aggregation(crop_vol):
    # Aggregation
    agg_im_mean = np.mean(crop_vol, axis=0)
    agg_im_median = np.median(crop_vol, axis=0)
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
    regfiles = [f for f in listdir(out_paths[:-3]) if isfile(join(out_paths[:-3], f))]

    #sharpening
    sharpening = 1
    sigma1 = 1
    sigma2 = 0.5
    alpha = 50

    crop_vol = vol_3D(regfiles, sharpening, alpha, sigma1, sigma2, out_paths[:-3])

    io.imsave('./dataset/3Dvol_pattern.tiff', (crop_vol*65535).astype('uint16')) #*65535 if shapening

    [agg_im_mean, agg_im_median] = aggregation(crop_vol)

    io.imsave('./dataset/agg_im_pattern_mean.tiff', (agg_im_mean*65535).astype('uint16')) #*65535 if shapening
    io.imsave('./dataset/agg_im_pattern_median.tiff', (agg_im_median*65535).astype('uint16')) #*65535 if shapening


