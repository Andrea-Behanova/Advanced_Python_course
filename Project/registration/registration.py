import register_example_with_adam as reg

def registration(all_paths):
    ref = all_paths[0]
    flo = all_paths[1]
    out = all_paths[2]
    reg.run(ref,flo,out)