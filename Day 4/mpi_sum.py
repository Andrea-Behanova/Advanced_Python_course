from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
import numpy as np

v = np.array(rank,'b')
sum_v = np.array(0.0,'b')

comm.Reduce(v, sum_v, op=MPI.SUM, root=0)

if rank == 0:
    print('rank 0: the sum is: ',sum_v)