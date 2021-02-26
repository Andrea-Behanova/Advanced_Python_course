import register_example_with_adam as reg

def registration(all_paths):
    ''' Registration of two images. 
    
    Parameters:
    all_paths: list of triplets (ref, flo, out)
    ref: reference image
    flo: floating image
    out: output path, where the registereg image will be saved
    '''
    ref = all_paths[0]
    flo = all_paths[1]
    out = all_paths[2]
    reg.run(ref,flo,out)