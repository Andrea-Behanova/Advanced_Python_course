import numpy as np

def aggregation(Stack3D):
    ''' Aggregation of 3D volume into 1 single image by mean and median. 

    Parameters:
    Stack3D: Stack of images (3D)

    Return:
    agg_im_mean: aggregated image by mean
    agg_im_median: aggregated image by median
    '''
    agg_im_mean = np.mean(Stack3D, axis=0)
    agg_im_median = np.median(Stack3D, axis=0)
    return agg_im_mean, agg_im_median


