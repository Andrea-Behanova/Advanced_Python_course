from skimage import io
from os import listdir
from os.path import isfile, join
import multiprocessing as mp
from aggregation import aggregation
from vol_3D import vol_3D
from registration import registration

# Path to the stack of short exposure images.
path_image_stack = 'C:/Users/andre/Desktop/10ms3500ill_cropped'
file_names = [f for f in listdir(path_image_stack) if isfile(join(path_image_stack, f))]     #list of file names

# File names divided into reference image (middle in stack) and rest of the images.
mid_index = len(file_names) // 2
ref_im_name = file_names[mid_index]
rest_im_name = file_names[0:mid_index] + file_names[mid_index+1:]

# Output path for the registered images.
output_path = 'C:/Users/andre/Desktop/10ms3500ill_cropped/registered/reg'


if __name__ == '__main__':

    # Input to a regstration is a triplet of paths (reference image, floating image, output path).
    # In to following code we create a list of triplets with all the combinations.
    all_paths = []
    for i in range(len(rest_im_name)):
        path = [join(path_image_stack,ref_im_name), join(path_image_stack,rest_im_name[i]), output_path+str(i+2).zfill(3)+'.tiff']
        all_paths.append(path)

    # Registration adapted into parallel computing (8 cores)
    with mp.Pool(8) as p:
        p.map(registration, all_paths)

    # List of registered images.
    regfiles = [f for f in listdir(output_path[:-3]) if isfile(join(output_path[:-3], f))]

    # Merging registered images into 3D volume + sharpening.
    crop_vol = vol_3D(regfiles, output_path[:-3])

    # Save 3D stack of registered sharpened images.
    io.imsave('./dataset/3Dvol_pattern.tiff', (crop_vol*65535).astype('uint16'))

    # Aggregation of the 3D stack into mean and median.
    [agg_im_mean, agg_im_median] = aggregation(crop_vol)

    # Saving aggregated mean and median.
    io.imsave('./dataset/agg_im_pattern_mean.tiff', (agg_im_mean*65535).astype('uint16'))
    io.imsave('./dataset/agg_im_pattern_median.tiff', (agg_im_median*65535).astype('uint16'))


