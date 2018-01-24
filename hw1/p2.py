import time 
import sys


start = time.time()
datfilepath = sys.argv[-1]
arfffilepath = datfilepath.split('.')[0] + ".arff"

datfile = open(datfilepath, 'r')
arfffile = open(arfffilepath, 'w+')

attributes = set()
for line in datfile.readlines():
    [attributes.add(int(x.strip())) for x in line.strip().split(' ')]

arfffile.write('@relation kosarak\n')
[arfffile.write('@attribute i{} {{0, 1}}\n'.format(attr)) for attr in range(1, max(attributes)+1)]

datfile.seek(0)
arfffile.write('@DATA\n')

dataline = lambda x: '{{{}}}\n'.format(x)

for line in datfile.readlines():
    attributes = set()
    [attributes.add(int(x.strip())-1) for x in line.strip().split(' ')]
    s = ''
    for x in sorted(attributes):
        s += '{} 1, '.format(x)
    s = s[:-2]
    arfffile.write(dataline(s))

datfile.close()
print('Total time to parse: {}'.format(time.time()-start))