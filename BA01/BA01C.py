"""

> Reverse complement sequence 변환하기

"""

# coding: utf-8


def GetRevCompSeq(file):
	from Bio.Seq import Seq

	seq = open(file).read().strip()
	return print(Seq(seq).reverse_complement())
    


inputfilename = 'BA03.txt'
GetRevCompSeq(inputfilename)

