import sys,time
adjacent = [
[1,2,3,4,5],
[0,2,6,10,5],
[0,1,6,7,3],
[0,2,7,8,4],
[0,3,8,9,5],
[0,4,9,10,1],
[1,2,7,11,10],
[6,2,3,8,11],
[7,3,4,9,11],
[8,4,5,10,11],
[9,5,1,6,11],
[6,7,8,9,10]
]
state=[0] + ["."]*11 #0 is independent face
def bruteForce(state, colors, cap):
	if not isValid(state):
		return ""
	if isSolved(state,cap):
		return state
	if '.' not in state:
		return ""
	unfilled=state.index('.')
	for i in range(colors):
		state[unfilled]=i
		bf = bruteForce(state, colors, cap)
		if bf:
			return state
		state[unfilled]='.'
	return ""
def isSolved(state, cap):
	if isValid:
		c=0
		for face in state:
			if face == 0:
				c+=1
		if c==cap:
			return True
	return False
def isValid(state):
	for target, targetAdj in enumerate(adjacent):
		if state[target] == 0:
			for adjInd in targetAdj:
				if state[adjInd]==0:
					return False
	return True
bf = bruteForce(state, 2, int(sys.argv[1]))
print(bf if bf != '' else "impossible")