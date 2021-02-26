from skimage import io
from os import listdir
from os.path import isfile, join
import multiprocessing as mp
from aggregation import aggregation
from vol_3D import vol_3D
from registration import registration


path_image_stack = 'C:/Users/andre/Desktop/10ms3500ill_cropped'
onlyfiles = [f for f in listdir(path_image_stack) if isfile(join(path_image_stack, f))]

mid_index = len(onlyfiles) // 2
ref_paths = onlyfiles[mid_index]
flo_paths = onlyfiles[0:mid_index] + onlyfiles[mid_index+1:]
out_paths = 'C:/Users/andre/Desktop/10ms3500ill_cropped/registered/reg'


if __name__ == '__main__':
    all_p = []
    for i in range(len(flo_paths)):
        p = [join(path_image_stack,ref_paths), join(path_image_stack,flo_paths[i]), out_paths+str(i+2).zfill(3)+'.tiff']
        all_p.append(p)

    #parallel registration
    with mp.Pool(4) as p:
        p.map(registration, all_p)

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


