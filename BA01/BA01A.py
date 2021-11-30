
"""

> 전체 sequence에서 특정 sequence가 포함되는 부분이 몇개인지 출력하기

"""

# coding: utf-8

def PatternCount(file):
    refseq, queryseq = open(file).read().strip().split("\n")

    attempt = len(refseq) - len(queryseq) + 1
    cnt=0
    for i in range(attempt):

        if refseq[i:i+len(queryseq)]==queryseq:
        	cnt+=1

    return print(cnt)


inputfilename = 'BA01.txt'
PatternCount(inputfilename)

