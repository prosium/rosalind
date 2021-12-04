"""

> Sequence 내에서 Subsequence와 hamming distance 이하 떨어진 sequence의 index찾기

"""

# coding: utf-8

def hmm_score(SequenceA, SequenceB):
    
    hmmScore=0
    
    for i in range(len(SequenceA)): # or SeqB
        if SequenceA[i] != SequenceB[i]:
            hmmScore += 1

    return hmmScore

def ApproxOccurrence(inputfile):
    Subseq, Sequence, RefhmmDist = open(inputfile).read().strip().split('\n')
    RefhmmDist = int(RefhmmDist)
    ansBag = []
    for i in range(len(Sequence)-len(Subseq)+1):
        TargetSeq = Sequence[i:i+len(Subseq)]

        if int(hmm_score(TargetSeq, Subseq)) <= RefhmmDist:
            ansBag.append(str(i))

    return print(" ".join(ansBag))
            

inputfilename = 'BA01H.txt'
ApproxOccurrence(inputfilename)

