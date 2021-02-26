import filters
from scipy import ndimage
import numpy as np

def sharpen(im,alpha,sigma1,sigma2):
    ''' Image sharpening. Sigmas should in principle be tuned so that they suppress noise, amplify small 
    structures that we aim to enhance visibility of, while avoiding amplification of larger structures.

    Parameters:
    im: Input image.
    alpha: controls the magnitude of the sharpening.
    sigma1: Parameter for first gaussian filtering.
    sigma2: Parameter for second gaussian filtering.

    Return:
    sharpened_im: Resulting sharpened image.
    '''

    # Image normalization
    im = im.astype('float')
    im = filters.normalize(im, 0, None) * 0.5 + 0.25

    # Unsharp masking by gaussian blurring.
    blurred_f = ndimage.gaussian_filter(im, sigma1)
    filter_blurred_f = ndimage.gaussian_filter(blurred_f, sigma2)
    sharpened = im + alpha * (blurred_f - filter_blurred_f)
    sharpened_im = np.clip(sharpened, a_min = 0.0, a_max = 1.0)
    return sharpened_im