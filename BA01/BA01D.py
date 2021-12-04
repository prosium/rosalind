"""
> 전체 Sequence에서 특정 Sequence가 나오는 위치 찾기

"""

# coding: utf-8

import os
os.chdir("C:/Data/LAB9_ML/002_ROSALIND_211117/PART01")


def FindOccurrences(filename):
	SubSeq, TotalSeq = open(filename).read().strip().split("\n")
	
	AllPos = len(TotalSeq) - len(SubSeq) + 1
	ansBag = []

	for i in range(AllPos):

		if TotalSeq[i:i+len(SubSeq)] == SubSeq:
			ansBag.append(i)
			# print(i)

	return print(" ".join(map(str,ansBag)))
	
inputfilename = 'BA04.txt'
FindOccurrences(inputfilename)

