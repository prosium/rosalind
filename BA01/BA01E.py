"""

> 전체 Sequence에서 특정 Sequence가 나오는 위치 찾기

"""

# coding: utf-8

def PatternsInClumps(filename):
	InputData = open(filename).read().strip().split("\n")
	Seq = InputData[0]
	k, L, t = map(int, InputData[1].split(" ")) # k=찾고 싶은 seq 길이, L=target으로 보는 seq 길이, t=반복횟수
	
	
	ansBag = []
	for i in range(len(Seq) - L + 1): # 전체 Seq 중에 target으로 보는 Seq 자르기
		SubSeq = Seq[i:i+L]

		for j in range(len(SubSeq) - k + 1): # 잘린 Seq에서 kmer 찾기
			kmer = SubSeq[j:j+k]
			if SubSeq.count(kmer) == t:
				ansBag.append(kmer)

	return print(" ".join(set(list(ansBag))))


inputfilename = 'BA05.txt'
PatternsInClumps(inputfilename)

