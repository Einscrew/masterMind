#! /usr/bin/python3

from os import system as system

CENTER = 25
N_CLRS = 4
N_MAX_CLRS = 8
BOARD = {
			"pins":["  ".join([ "><" for c in range(0,N_CLRS)]) for i in range(0,N_MAX_CLRS) ],
			"key":()
		}

def getInput(allowed = set(range(1,9))):
	while True:
		try:
			s = input('Select the colors by their number: ')
			s = [int(n) for n in s]
			if len(s) == N_CLRS and set(s).issubset(allowed): 
				return s
		except ValueError:
			pass


def genSeq(allowed = list(range(1,9))):
	return tuple([allowed.pop(randint(0,len(allowed)-1)) for x in range(0,4)])


def match(t, k):
	return 	{ 
				"placed":[ list(t)[x]==list(k)[x] for x in range(0,len(k)) ].count(True),
				"right":len(set(k).intersection(set(t)))
			}


def printElement(s='', c='-', f='-', w=CENTER):
	print(f+s.center(w,c)+f)


def printBoard(r={"right":-1,"placed":-1}):
	n = r.get("right")
	p = r.get("placed")
	printElement('', f='+')
	for i in BOARD.get("pins"):
		printElement(i, c=' ', f='|')

	printElement('', f='+')
	result= ['Matched colors: ']
	result.append(str(n) if n != -1 else 'X')
	printElement( "".join(result) , c=' ', f='|')
	result = ['In the right place: ']
	result.append(str(p) if p != -1 else 'X')
	printElement( "".join(result) , c=' ', f='|')
	printElement('', f='+')


def getColorStr(t):
	f= '\033[1;48;5;{}m{}\033[0m'
	s = "  "
	s = s.join([f.format(x,'  ') for x in t])
	rhs=((CENTER-16)//2)+(1 if CENTER%2==0 else 2)
	lhs= CENTER-16-rhs+2
	s=" "*rhs+s+" "*lhs
	return s


def updateBoard(i, t):
	#BOARD["pins"][i]= "  ".join([ " "+str(c) for c in t])
	BOARD["pins"][i]= getColorStr(t)


def game():
	iteration = 0	
	BOARD["key"]=genSeq()
	system('clear')
	printBoard()
	while iteration < 8:
		t=getInput()
		system('clear')
		r=match(t,BOARD.get("key"))
		updateBoard(iteration, t)
		printBoard(r=r)
		if r["placed"] == N_CLRS:
			break
		iteration = iteration+1
	else:
		printElement("You lost!", c=' ',f='|')
		printElement('', c='-',f='+')
		return
	printElement("You won!", c=' ',f='|')
	printElement(getColorStr(BOARD["key"]), c=' ',f='|')
	printElement('', c='-',f='+')
	
if __name__ == "__main__":
	from random import randint as randint
	game()