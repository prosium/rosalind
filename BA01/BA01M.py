"""

> 숫자를 반대로 돌리고 나머지만큼 ACGT 할당 후 정수부분으로 다시 반복

"""

# coding: utf-8



import os

def NumberToPattern(Number, length):
	bases = ['A', 'C', 'G', 'T']
	pattern = ''
	for i in range(length):
		pattern = pattern + bases[Number % 4]
		Number = Number // 4 # 정수부분
	return pattern[::-1]


def ReadFile(inputfile):
	PatternSeq = open(inputfile).read().strip().split('\n')
	Number = int(PatternSeq[0])
	length = int(PatternSeq[1])
	
	print(NumberToPattern(Number, length))
	

inputfilename = 'BA01M.txt'
ReadFile(inputfilename)
