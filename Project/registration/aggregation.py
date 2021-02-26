import numpy as np

def aggregation(crop_vol):
    # Aggregation
    agg_im_mean = np.mean(crop_vol, axis=0)
    agg_im_median = np.median(crop_vol, axis=0)
    return agg_im_mean, agg_im_median


