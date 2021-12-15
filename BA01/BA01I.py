"""

> 특정 서열 내에 존재하는 k 길이의 subsequence에서 d (hamming distance) 이하로 있는 sequence 찾기

> Query를 SubSequence에 비교가 아니라 SubSequence 먼저 만들어놓고 Query에 비교하는 아이디어

> Step1. 모든 kmer의 dictionary
> Step2. 주어진 길이만큼의 substring과 모든 kmer와 hamming distance 계산 후 d 이하면 +1
> Step3. max value의 key값 가져오기


"""

# coding: utf-8

import os
import itertools


def Get_all_kmers(k):
    dt = {}
    for s in map(''.join, itertools.product('ACTG', repeat=k)):
        dt[s] = 0
    return dt

def hmm_score(SequenceA, SequenceB):
    hmmScore=0
    for i in range(len(SequenceA)): # or SeqB
        if SequenceA[i] != SequenceB[i]:
            hmmScore += 1

    return hmmScore

def Most_Freq(inputfile):
    a = open(inputfile).read().strip().split('\n')
    Sequence = a[0]
    k, d = a[1].split(" ")
    k = int(k); d=int(d)

    Bagkmer = Get_all_kmers(k)
  
    for i in range(k-1, len(Sequence)):
        s = Sequence[i-k+1:i+1]

        for kk in Bagkmer:
            if hmm_score(kk, s) <= d:
                Bagkmer [kk] += 1

    mx = max(dt.values())

    ansBag = []
    for k in dt:
        if Bagkmer [k] == mx:
            ansBag.append(k)
    return print(" ".join(ansBag))

inputfilename = 'BA01I.txt'
Most_Freq(inputfilename)
