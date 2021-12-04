"""

> 전체 Sequence에서 특정 Sequence가 나오는 위치 찾기

"""

# coding: utf-8

def MinimumSkew(inputfile):

	Seq = open(inputfile).readline().strip()

	Skew_score = [0]
	
	for i in range(len(Seq)):

		# print(Skew_score)
		if Seq[i] == "G":
			Skew_score.append(Skew_score[-1]+1) # 최종 score + 1

		elif Seq[i] == "C":
			Skew_score.append(Skew_score[-1]-1) # 최종 score - 1

		else:
			Skew_score.append(Skew_score[-1]) # 최종 score 유지

	Min_SkewScore = min(Skew_score)
	# print(Skew_score)

	ansBag = []

	for i in range(len(Skew_score)):
		if Skew_score[i] == Min_SkewScore:
			ansBag.append(i)
	
	return print(" ".join(map(str,ansBag)))

inputfilename = 'BA06.txt'
MinimumSkew(inputfilename)

