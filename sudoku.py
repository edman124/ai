import sys,time
def generateLookup(): #add up to 405
	lookup = [set() for i in range(81)]
	for num in range(81):
		row=int(num/9)
		col=int(num%9)
		for ind in range(9*(row),9*(row)+9): #row
			lookup[num].add(ind)
		for ind in range(col,81,9): #col
			lookup[num].add(ind)
		boxrow=int(row/3)
		boxcol=int(col/3)
		for ind in range(27*boxrow+3*boxcol,27*boxrow+3*boxcol+3):
			lookup[num].add(ind)
		for ind in range(27*boxrow+3*boxcol+9,27*boxrow+3*boxcol+12):
			lookup[num].add(ind)
		for ind in range(27*boxrow+3*boxcol+18,27*boxrow+3*boxcol+21):
			lookup[num].add(ind)
		lookup[num] = lookup[num]-set([num])
	return lookup
# def generateCheck():
# 	check = []
# 	for row in range(9):
# 		check.append(set(range(9*row,9*row+9)))
# 	for col in range(9):
# 		check.append(set(range(9*col,81,9)))
# 	for box in range(9):
# 		boxInd = set()
# 		boxrow=int(box/3)
# 		boxcol=int(box%3)
# 		for ind in range(27*boxrow+3*boxcol,27*boxrow+3*boxcol+3):
# 			boxInd.add(ind)
# 		for ind in range(27*boxrow+3*boxcol+9,27*boxrow+3*boxcol+12):
# 			boxInd.add(ind)
# 		for ind in range(27*boxrow+3*boxcol+18,27*boxrow+3*boxcol+21):
# 			boxInd.add(ind)
# 		check.append(boxInd)
# 	return check

def bruteForce(state, lookup):
	# if not isValid(state, check):
	# 	return ""
	if isSolved(state):
		return state
	unfilled=state.index('.')
	potVal=findVals(state, lookup, unfilled)
	if potVal==set():
		return ""
	else:
		for i in potVal:
			state[unfilled]=i
			bf = bruteForce(state, lookup)
			if bf:
				return state
			state[unfilled]='.'
	return ""
def isSolved(state):
	if '.' not in state:
		return True
	return False
def findVals(state, lookup, current):
	orig = set(['1','2','3','4','5','6','7','8','9'])
	already = set()
	for ind in lookup[current]:
		already.add(str(state[ind]))
	return orig-already
# def isValid(state, check):
# 	for current, relSudokuPos in enumerate(check):
# 		answers=set()
# 		for neighbor in relSudokuPos:
# 			answers.add(state[neighbor])
# 		if state[current] != '.' and state[current] in (answers-set([state[current]])):
# 			return False
# 	return True
t=time.time()
pzltxt = open("puzzles.txt", "r")
lookup = generateLookup()
# n=int(sys.argv[1])
# for i, line in enumerate(pzltxt):
# 	if i==n:
# 		break
# 	state=list(line.replace("\n",''))
# 	bf = bruteForce(state, lookup)
# 	# if not isValid(bf,check):
# 	# 	print("Resultant puzzle was invalid!!")
# 	# 	exit(1)
# 	print(i)
# 	print(bf if bf != '' else "impossible")
# print(time.time()-t)

state=['2', '.', '.', '.', '8', '.', '3', '.', '.', '.', '6', '.', '.', '7', '.', '.', '8', '4', '.', '3', '.', '5', '6', '.', '2', '.', '9', '.', '.', '.', '1', '.', '5', '4', '.', '8', '.', '.', '.', '.', '.', '.', '.', '.', '.', '4', '.', '2', '7', '.', '6', '.', '.', '.', '3', '.', '1', '.', '.', '7', '.', '4', '.', '7', '2', '.', '.', '4', '.', '.', '6', '.', '.', '.', '4', '.', '1', '.', '.', '.', '3']
bf = bruteForce(state, lookup)
print(bf if bf != '' else "impossible") 