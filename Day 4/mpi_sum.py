from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
a = sum([4,5])

if rank == 0:
    print('rank 0: sum='+str(a))