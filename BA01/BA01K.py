"""

> 주어진 길이 k의 모든 nt 종류에 대해 특정 서열 내 존재하는 Sequence에 대한 k-mer count를 mapping 하기


"""

# coding: utf-8

import os
from itertools import product
from collections import Counter

def AllPossibility(Sequence,k):
	Allbag = []
	for i in range(len(Sequence) - k + 1):
		kmer = Sequence[i: i+k]
		Allbag.append(kmer)
		# print(kmer)
	return Allbag

def MappingCount(inputfile):
	Seq, k= open(inputfile).read().strip().split("\n")
	k = int(k)
	AllSubSeq = AllPossibility(Seq,k)

	counter = Counter()
	ansbag = []
	for s in product("ACGT", repeat=k):
		kmer = ''.join(s)

		if kmer in Seq:
			counter[kmer] = AllSubSeq.count(kmer)
			# print(kmer, counter[kmer])
			# print(counter[kmer])

		elif counter[kmer] == 0:
			# print(kmer, counter[kmer])
			counter[kmer] = 0


	for i in counter.values():
		ansbag.append(str(i))

	return print(" ".join(ansbag))


inputfilename = 'BA01K.txt'
MappingCount(inputfilename)
