import numpy as np
import time
import os
import pandas as pd
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances


data_consolidated = data_test = fetch_20newsgroups(subset='all')
vectorizer = TfidfVectorizer(stop_words='english')
vectors = vectorizer.fit_transform(data_consolidated.data)

print(vectors.shape)

csfile = 'submission/20ng-cs.dat'
print(csfile)

if os.path.isfile(csfile):
    print('Found existing database, renaming it..')
    os.rename(csfile, '20ng-cs'+str(int(time.time()))+'dat')

fp = np.memmap(csfile, dtype='float32', mode='w+', shape=(vectors.shape[0], vectors.shape[0]))

print('dummy file created..')

print('init dump..')
step = 10
start_index = 0
t0 = time.time()
for end_index in range(0, vectors.shape[0]+1, step)[1:]:
    fp[start_index:end_index,] = cosine_similarity(vectors[start_index:end_index,], vectors)
    start_index = end_index
    if end_index % 500 == 0:
        print('Finished: {} {}'.format(end_index, time.time()-t0))
