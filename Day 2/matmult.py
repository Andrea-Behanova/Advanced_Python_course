# import line_profiler
# import atexit
# profile = line_profiler.LineProfiler()
# atexit.register(profile.print_stats)

# Program to multiply two matrices using nested loops
import random
import numpy as np

N = 250
@profile
def Xmat(N):
    # NxN matrix
    X = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])
    return X

@profile
def Ymat(N):
    # Nx(N+1) matrix
    Y = []
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])
    return Y

@profile
def Amat(N):
    # result is Nx(N+1)
    result = []
    for i in range(N):
        result.append([0] * (N+1))
    return result

@profile
def multmat(X, Y, result):
    # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            #Matrix multiply
            #result[i][j] = np.dot(X[i], Y[:,j])
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
#    return result

X = Xmat(N)
Y = Ymat(N)
result = Amat(N)

npX = np.array(X)
npY = np.array(Y)
np_res = np.array(result)

multmat(npX, npY, np_res)