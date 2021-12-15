"""

> 특정 서열 내에 존재하는 k 길이의 subsequence + revsese complement of sequence 에서 d (hamming distance) 이하로 있는 sequence 찾기

> Query를 SubSequence에 비교가 아니라 SubSequence 먼저 만들어놓고 Query에 비교하는 아이디어


"""

# coding: utf-8

import os
import itertools
from collections import Counter



def GetRevCompSeq(seq):
    from Bio.Seq import Seq

    seq = Seq(seq).reverse_complement()
    return seq
    

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
                Bagkmer[kk] += 1
    
    mx = 0
    ss = []


    for seq in Bagkmer:
        

        Revseq = GetRevCompSeq(seq)

        if Bagkmer[seq]+Bagkmer[Revseq] > mx:
            mx = Bagkmer[seq]+Bagkmer[Revseq]
            ss = [seq]

        elif Bagkmer[seq]+Bagkmer[Revseq] == mx:
            ss.append(seq)

    
    return print(" ".join(ss))





inputfilename = 'BA01J.txt'
Most_Freq(inputfilename)
