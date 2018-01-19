
import numpy as np
import time
from sklearn.datasets import fetch_mldata
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances

X = fetch_mldata('MNIST original').data.astype('float64')
print(X.shape)


csfile = '/home/ubuntu/projects/datasets/mnist-cs.dat'
fp = np.memmap(csfile, dtype='float32', mode='w+', shape=(X.shape[0],X.shape[0]))

step = 10
start_index = 0
t0 = time.time()
for end_index in range(0, X.shape[0]+1, step)[1:]:
    fp[start_index:end_index,] = cosine_similarity(X[start_index:end_index,], X)
    start_index = end_index
    if end_index % 500 == 0:
        print('Finished:',end_index, time.time()-t0)