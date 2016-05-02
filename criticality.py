import numpy as np


def fr2spike(f,th):
	rows,cols = f.shape
	s = np.zeros((rows,cols),dtype=np.int)
	for r in range(rows):
		for c in range(cols):
			if abs(f[r,c]) >= th: s[r,c]=1
			else: s[r,c] = 0
	return s

def SimActiveUnits(s):
	rows,cols=s.shape
	sau = np.zeros(cols,dtype=np.int)
	for r in range(rows):
		for c in range(cols):
			sau[c] += s[r,c]
	return sau

def avalancheSize(sau):
	av = []
	tm = sau.shape[0]
	avSize=0
	for i in range(tm):
		if sau[i] != 0:
			avSize += sau[i]
		else:
			if avSize != 0:
				av.append(avSize)
			avSize = 0
	return np.asarray(av)





