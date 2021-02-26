import numpy as np
from sharpen import sharpen
from skimage import io

def vol_3D(regfiles, sharpening, alpha, sigma1, sigma2, regpath):
    final_vol = np.array([sharpen(io.imread(regpath + p, as_gray=True),alpha,sigma1,sigma2) for p in regfiles])
    crop_vol = final_vol[:,21:437,50:398]
    return crop_vol