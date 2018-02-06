import sys,time
adjacent = [
[1,4,6],
[0,2,8],
[1,3,10],
[2,4,12],
[3,0,14],
[14,6,15],
[0,5,7],
[6,16,8],
[7,1,9],
[8,10,17],
[9,2,11],
[10,12,18],
[11,3,13],
[12,19,14],
[13,4,5],
[19,5,16],
[15,7,17],
[16,9,18],
[17,11,19],
[18,13,15]
]
state=[0] + ["."]*19
def bruteForce(state, colors):
	print(state)
	if not isValid(state):
		return ""
	if isSolved(state):
		return state
	unfilled=state.index('.')
	for i in range(colors):
		state[unfilled]=i
		bf = bruteForce(state, colors)
		if bf:
			return state
		state[unfilled]='.'
	return ""
def isSolved(state):
	if isValid:
		if '.' not in state:
			return True
	return False
def isValid(state):
	for target, targetAdj in enumerate(adjacent):
		targetNeighbors=set()
	
		for neighbor in targetAdj:
			targetNeighbors.add(state[neighbor])
		if state[target] != '.' and state[target] in targetNeighbors:
			return False
	return True
bf = bruteForce(state,int(sys.argv[1]))
print(bf if bf != '' else "impossible")