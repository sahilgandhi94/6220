import numpy as np
import pandas as pd
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import logger

log = logger.getLogger('p3-20ng')

remove = ('headers', 'footers', 'quotes')

data_train = fetch_20newsgroups(subset='train', remove=remove)
data_test = fetch_20newsgroups(subset='test', remove=remove)

log.info('Vectorizing data..')
# analyzer='word', ngram_range=(1,6), min_df = 0, stop_words = 'english', sublinear_tf=True
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(data_train.data)
vectors.shape

# t0 = time()
# log.info('Begin vectorizing training data')
# vectorizer = TfidfVectorizer()
# vectors = vectorizer.fit_transform(data_train)
# log.info('Data vectorized in {}s'.format(time()-t0))

# corpus = list()
# for doc in range(tfidf_matrix.shape[0]):
#     feature_index = tfidf_matrix[doc,:].nonzero()[1]
#     tfidf_scores = zip(feature_index, [tfidf_matrix[doc, x] for x in feature_index])
#     corpus.append({feature_names[i]: s for (i, s) in tfidf_scores})
    
# train_df = pd.DataFrame(corpus)

# train_df['wondering'].describe()

log.info('Dumping tfidf matrinx into df..')
train_df = pd.SparseDataFrame(vectors, columns=vectorizer.get_feature_names(), default_fill_value=0)
log.info('Done dumping tfidf matrinx into df..')

DUMP_DIR = 'home/ubuntu/projects/6220/hw1/tmp/'
SPARSE_FILE = DUMP_DIR + 'sparse-df.pkl'
DENSE_FILE = DUMP_DIR + 'dense-df.pkl'
log.info('Storing sparse-df in {}'.format(SPARSE_FILE))
train_df.to_pickle(SPARSE_FILE)

# all normalizations
shift_scale = lambda df: (df - df.min()) / (df.max() - df.min())
mean_normal = lambda df: (df - df.mean()) / (df.max() - df.min())

# log.info(
# mn_train_df = mean_normal(train_df)