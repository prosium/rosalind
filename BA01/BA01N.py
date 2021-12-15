"""

> 숫자를 반대로 돌리고 나머지만큼 ACGT 할당 후 정수부분으로 다시 반복

"""

# coding: utf-8



import os

def AllKmer_list(k):
    kmer = ['A', 'C', 'G', 'T']
    array = kmer
    for n in range(k-1):
        array = [i+j for i in array for j in kmer]
    return array


def HammingDistance(s1, s2):
    d = sum([1 for i in range(len(s1)) if s1[i]!=s2[i]])
    return d

# def Neighbors(pattern, d):
#     array = GenerateArray(len(pattern))
#     neighbors = []
#     for i in array:
#         if HammingDistance(pattern, i) <= d:
#             neighbors.append(i)
#     return neighbors

def Neighbor(inputfile):
	inputdata = open(inputfile).read().strip().split('\n')
	pattern = inputdata[0]
	distance = int(inputdata[1])

	allKmer = AllKmer_list(len(pattern))
	neighbors = []

	for i in allKmer:
		if HammingDistance(pattern, i)<=distance:
			neighbors.append(i)

	return print("\n".join(neighbors))
	



inputfilename = 'BA01N.txt'
Neighbor(inputfilename)
