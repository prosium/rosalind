"""

> 같은 길이의 두 서열이 주어졌을때 hamming distance 구하기

"""

# coding: utf-8

def hmm_score(inputfile):
    
    SeqA, SeqB = open(inputfile).read().strip().split('\n')

    hmmScore=0
    
    for i in range(len(SeqA)): # or SeqB
        if SeqA[i] != SeqB[i]:
            hmmScore += 1

    
    return print(hmmScore)

inputfilename = 'BA01G.txt'
hmm_score(inputfilename)

