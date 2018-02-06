import time
from random import randint
lookUpChildren = [[1,4],[0,2,5],[1,3,6],[2,7],[0,5,8],[1,4,6,9],[2,5,7,10],[3,6,11],[4,9,12],[5,8,10,13],[6,9,11,14],[7,10,15],[8,13],[9,12,14],[10,13,15],[11,14]]
lookUpManhattan = {"1":[0,0],"2":[0,1],"3": [0,2],"4":[0,3],"5":[1,0],"6":[1,1],"7":[1,2],"8":[1,3],"9":[2,0],"A":[2,1],"B":[2,2],"C":[2,3],"D":[3,0],"E":[3,1],"F":[3,2]}
def heur(puz):
	dist = 0
	for i in range(16):
		if puz[i]=='_':continue
		dist+=abs((i&3)-lookUpManhattan[puz[i]][1])+abs((i>>2)-lookUpManhattan[puz[i]][0])
	return dist
def swapChar(string, ind1, ind2):
	maxI = max(ind1,ind2)
	minI = min(ind1,ind2)
	return string[0:minI] + string[maxI] + string[minI+1:maxI] + string[minI] + string[maxI+1:]
def spacerand(puz):
	t=time.time()
	n=1
	tmppuz=puz
	prevmanhat=heur(tmppuz)
	mantot=prevmanhat
	spaceInd=puz.index('_')
	while float(time.time())-t<14:
		tmpind=lookUpChildren[spaceInd]
		ind=spaceInd
		spaceInd=tmpind[randint(0,len(tmpind)-1)]
		tmppuz=swapChar(tmppuz,ind,spaceInd)
		prevmanhat+=abs((ind&3)-lookUpManhattan[tmppuz[ind]][1])+abs((ind>>2)-lookUpManhattan[tmppuz[ind]][0])-abs((spaceInd&3)-lookUpManhattan[tmppuz[ind]][1])-abs((spaceInd>>2)-lookUpManhattan[tmppuz[ind]][0])
		mantot+=prevmanhat
		n+=1
	ctime=time.time()-t
	print("n: "+str(n))
	print("time: "+str(ctime)+"sec")
	print("manhattan distance avg: "+str(mantot/n))
	print("runs per sec: "+str(n/ctime))
spacerand('123456789ABCDEF_')
# n: 2246090
# time: 14.000240087509155sec
# manhattan distance avg: 37.070085793534545
# runs per sec: 160432.24873007243


