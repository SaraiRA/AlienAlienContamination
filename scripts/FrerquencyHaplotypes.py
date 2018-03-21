import sys, os, re
import pysam
from collections import Counter
import decimal
import collections
from datetime import datetime

start_time = datetime.now()

if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print '''

        FrequencyNucleotidesInBamFiles

        Sarai Reyes

        usage:
        python FrequencyNucleotidesInBamFiles.py --help
        python FrequencyNucleotidesInBamFiles.py [reference.fasta] [mapFile.bam] [sample name]
        '''
        exit(0)

refseq_ids=sys.argv[1]
BamFile=sys.argv[2]
sampleName=sys.argv[3]


scaffoldNames=[]
refseq=open(sys.argv[1])
for line in refseq:
    line=line.rstrip()
    if line=="":
        continue
    else:
        scaffoldNames.append(line.split()[0])
