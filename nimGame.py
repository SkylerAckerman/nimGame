import random

numQuarters = 10

def take(num):
	global numQuarters
	numQuarters-=num

def computerTurn():
	for i in range(1,4):
		if((numQuarters-i)%4==0):
			take(i)
			print("Computer takes",i)
	checkState("Computer")
	humanTurn()

def humanTurn():
	global numQuarters
	took=random.choice([1,2,3])
	take(took)
	print("Human takes", took)
	checkState("Human")
	computerTurn()

def checkState(turn):
	global numQuarters
	print(numQuarters,"quarters left.")
	if(numQuarters<=0):
		print(turn,"wins!")
		quit()

humanTurn()