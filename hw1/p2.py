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

arfffile.write('@relation kosarak\n\n')
[arfffile.write('@attribute {} NUMERIC\n'.format(attr)) for attr in sorted(attributes)]

datfile.seek(0)
arfffile.write('\n\n@data\n')

dataline = lambda x: '{{{}}}\n'.format(x)

for line in datfile.readlines():
    attributes = set()
    [attributes.add(int(x.strip())-1) for x in line.strip().split(' ')]
    s = ''
    for x in sorted(attributes):
        s += '{} 1,'.format(x)
    s = s[:-1]
    print(dataline(s))
    arfffile.write(dataline(s))

datfile.close()
print('Total time to parse: {}'.format(time.time()-start))