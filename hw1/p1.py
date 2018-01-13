import pandas as pd
import numpy as np
import time

from copy import deepcopy

# constants
DATA_LOC = "/home/ubuntu/projects/datasets/AP_train.txt"

# data formats
FORMAT_ID = "#index"
FORMAT_PAPER_TITLE = "#*"
FORMAT_AUTHORS = "#@"
FORMAT_YEAR = "#t"
FORMAT_VENUE = "#c"
FORMAT_CITATIONS = "#%"
FORMAT_ABSTRACT = "#!"

# data keys
ID = "id"
TITLE = "title"
AUTHOR = "author"
YEAR = "year"
VENUE = "venue"
CITATION = "citation"
ABSTRACT = "abstract"

DATA = list()

def generatetuples():
    datum = dict()
    with open(DATA_LOC, "r", encoding='utf-8') as file:
        for line in file.readlines():            
            if FORMAT_ID in line:
                # yield already existing datum and continue
                if len(datum.keys()) > 0:
                    yield datum
#                     for author in datum.get(AUTHOR, []):
#                         for citation in datum.get(CITATION, []):
#                             tmp_datum = deepcopy(datum)
#                             tmp_datum[AUTHOR] = author
#                             tmp_datum[CITATION] = citation
#                             yield tmp_datum
                datum = dict() # re-initialize local datum
                datum[ID] = line.strip(FORMAT_ID).strip()
            elif FORMAT_PAPER_TITLE in line:
                datum[TITLE] = line.strip(FORMAT_PAPER_TITLE).strip()
            elif FORMAT_CITATIONS in line:
                if CITATION not in datum:
                    datum[CITATION] = []
                datum[CITATION].append(line.strip(FORMAT_CITATIONS).strip())
            elif FORMAT_AUTHORS in line: 
                datum[AUTHOR] = line.strip(FORMAT_AUTHORS).strip().split(';')
            elif FORMAT_YEAR in line: 
                datum[YEAR] = line.strip(FORMAT_YEAR).strip()
            elif FORMAT_VENUE in line: 
                datum[VENUE] = line.strip(FORMAT_VENUE).strip()
            elif FORMAT_ABSTRACT in line: 
                datum[ABSTRACT] = line.strip(FORMAT_ABSTRACT).strip()

start = time.time()
print(len([data for data in generatetuples()]))
print(time.time()-start)
