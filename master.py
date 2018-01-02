from main import test
from main import c
from main import compare
from random import randint
import sys
import os

class table:
	s=' '
	empty='>< >< >< ><'
	pin='  '
	backGround='\033[40m'
	limit=8
	currentPlay=[]
	chess=[]
	roundNum=0
	c=c()
	key=0
	colorKey=[]

def gameInit():
	os.system('clear')
	print('MasterMind')
	while table.roundNum < table.limit:

		table.currentPlay = chooseSeq()
		table.chess+=table.currentPlay
		table.roundNum+=1
		os.system('clear')
		printChess()
		

def lstToStr(lst):
	st=''
	for i in lst:
		st+=i
	return st

def chooseSeq():
	print(test())
	inp=input('choose 4 colors sequece \tEx: [1,2,3,4]')
	a,b,c,d=str(inp)
	lst=[]
	for i in [a,b,c,d]:
		lst+= getColor(int(i)-1)
	lst+='\t'+compare(int(inp),int(table.key))+'\n'
	return lst
	
def printChess():	
	print(lstToStr(table.chess))
	for i in range(table.roundNum,table.limit):
		print(table.empty)

def getColor(i):
        return table.c.colors[i][2]+table.pin+table.c.END+table.s

def genSeq():
	lst=[]
	for i in range(4):
		aux =1
		while aux!=0:
			r = randint(1,8)
			if getColor(r-1) not in lst:
				table.key=table.key*10+r
				lst+=[getColor(r-1)]
				aux=0
	return lst
table.colorKey=genSeq()
gameInit()
print(lstToStr(table.colorKey))
