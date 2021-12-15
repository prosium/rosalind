"""

> 특정 서열 내에 존재하는 k 길이의 subsequence + revsese complement of sequence 에서 d (hamming distance) 이하로 있는 sequence 찾기

> Query를 SubSequence에 비교가 아니라 SubSequence 먼저 만들어놓고 Query에 비교하는 아이디어


"""

# coding: utf-8



import os


def PatternToNumber(inputfile):
	PatternSeq = open(inputfile).read().strip().split('\n')[0]
     

	if len(PatternSeq) == 0:
		return 0
	Rev_pattern = PatternSeq[::-1]

	ansbag = []
	for i in enumerate(Rev_pattern):
		# print(i, i[0], i[1], (4**int(i))*symbolToNumber*i[1])		
		number = 4**int(i[0]) * symbolToNumber(i[1])
		
		ansbag.append(number)
		# print(number)
	return print(sum(ansbag))

def symbolToNumber(symbol):
	if symbol == "A":
		return 0
	if symbol == "C":
		return 1
	if symbol == "G":
		return 2
	if symbol == "T":
		return 3

inputfilename = 'BA01L.txt'
PatternToNumber(inputfilename)
