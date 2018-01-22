import os
import numpy as np
import time
import logger
from sklearn.datasets import fetch_mldata
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances

log = logger.getLogger('mnist-full-cosine')

X = fetch_mldata('MNIST original').data.astype('float64')
print(X.shape)

csfile = 'submission/mnist-cs.dat'
print(csfile)

if os.path.isfile(csfile):
    print('Found existing database, renaming it..')
    os.rename(csfile, 'csfile'+str(int(time.time()))+'dat')

fp = np.memmap(csfile, dtype='float32', mode='w+', shape=(X.shape[0],X.shape[0]))

print('dummy file created..')

print('init dump..')
step = 10
start_index = 0
t0 = time.time()
for end_index in range(0, X.shape[0]+1, step)[1:]:
    fp[start_index:end_index,] = cosine_similarity(X[start_index:end_index,], X)
    start_index = end_index
    if end_index % 500 == 0:
        print('Finished: {} {}'.format(end_index, time.time()-t0))
