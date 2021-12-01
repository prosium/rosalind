
"""

> Sequence에서 주어진 길이로 가장 많이 반복되는 sequence 찾기

"""

# coding: utf-8

def MostFrequent(file):
    seq, k = open(file).read().strip().split("\n")
    k=int(k)
    kmer_dict={}
    for i in range(0,len(seq)-int(k)+1):
    	kmer = seq[i:i+k]
    	if kmer in kmer_dict:
    		kmer_dict[kmer] += 1
    	else:
    		kmer_dict[kmer] = 1

    MFcount = max(kmer_dict.values())

    for key, value in kmer_dict.items():
    	if value == MFcount:
    		print(key, end=' ')


inputfilename = 'BA02.txt'
MostFrequent(inputfilename)

