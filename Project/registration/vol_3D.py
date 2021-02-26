import numpy as np
from sharpen import sharpen
from skimage import io

def vol_3D(regfiles, regpath):
    ''' Builds 3D Volume from stack of images and crops out the black sides. 

    Parameters:
    regfiles: file names of registered images
    regpath: path to registered images

    Return:
    cropped_volume_3D: Resulting cropped 3D volume.
    '''
    # Parameters for sharpening.
    sigma1 = 1
    sigma2 = 0.5
    alpha = 50

    Volume_3D = np.array([sharpen(io.imread(regpath + p, as_gray=True),alpha,sigma1,sigma2) for p in regfiles])
    cropped_volume_3D = Volume_3D[:,21:420,50:370]
    return cropped_volume_3D