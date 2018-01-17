import numpy as np
import pandas as pd
from sklearn.datasets import fetch_mldata
from sklearn.metrics.pairwise import cosine_similarity

import logger

log = logger.getLogger('p3-mnist')

mnist = fetch_mldata('MNIST original')

log.info('Dumping vectors into df..')
df = pd.DataFrame(mnist.data.astype('float64'))
log.info('Done dumping vectors into df..')

DUMP_DIR = 'home/ubuntu/projects/6220/hw1/tmp/'
DF_FILE = DUMP_DIR + 'mnist-df.pkl'

log.info('Storing sparse-df in {}'.format(DF_FILE))
df.to_pickle(DF_FILE)

# all normalizations
shift_scale = lambda df: (df - df.min()) / (df.max() - df.min())
std_norm = lambda df: (df - df.mean()) / df.std()

log.info('mean normal df compute')
stdnorm_df = std_norm(df)
log.info('mean normal df compute done')


log.info('Storing sparse-df in {}'.format(DUMP_DIR+'mnist-stdnorm'))
stdnorm_df.to_pickle(DUMP_DIR+'mnist-stdnorm')
log.info('done')