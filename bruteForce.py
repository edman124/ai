import sys,time
lookuprow = [
set([1,2,3,4,5]),
set([6,7,8,9,10,11,12]),
set([13,14,15,16,17,18,19]),
set([20,21,22,23,24]),
set([1,2,13,6,7]),
set([20,14,15,8,9,3,4]),
set([21,22,16,17,10,11,5]),
set([23,24,18,19,12]),
set([4,5,11,12,19]),
set([2,3,9,10,17,18,24]),
set([1,7,8,15,16,22,23]),
set([6,13,14,20,21])
]
lookuphex = [
set([1,2,3,7,8,9]),
set([3,4,5,9,10,11]),
set([6,7,8,13,14,15]),
set([10,11,12,17,18,19]),
set([14,15,16,20,21,22]),
set([16,17,18,22,23,24]),
set([8,9,10,15,16,17])
]
middlehex = [8,9,10,15,16,17]
pzl=[]
lettertracker = [1]*6
c=0
for i in range(24):
	if i+1 in middlehex:
		pzl.append(c)
		c+=1
	else:
		pzl.append('.')
print(pzl)
def bruteForce(pzl,lettertracker):
	# print(pzl)
	if not isValid(pzl):
		return ""
	if isSolved(pzl,lettertracker):
		return pzl
	if '.' in pzl:
		unfilled=pzl.index('.')
		for i in numbers(lettertracker):
			pzl[unfilled]=i
			lettertracker[i]+=1
			bf = bruteForce(pzl,lettertracker)
			if bf:
				return pzl
			pzl[unfilled]='.'
			lettertracker[i]-=1
	return ""
		 
def isSolved(pzl,lettertracker):
	if isValid:
		if '.' not in pzl and lettertracker[0]==5:
			return True
	return False
def numbers(lettertracker):
	ret=[]
	if lettertracker[0]<6:
		ret.append(0)
	for i in range(1,6):
		if lettertracker[i]<5:
			ret.append(i)
	return ret
def isValid(pzl):
	for hexagon in lookuphex:
		mem=set()
		for ind in hexagon:
			if pzl[ind-1]!='.' and pzl[ind-1] in mem:
				return False
			mem.add(pzl[ind-1])
	return True
bf = bruteForce(pzl,lettertracker)
print(bf if bf != '' else "impossible")