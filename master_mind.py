CENTER = 40

def getInput():
	allowed = set(range(1,9))
	while True:
		try:
			s = input('Select the colors by their number: '.center(0))
			s = set([int(n) for n in s])
			if len(s) == 4 and s.issubset(allowed): 
				return s
		except ValueError:
			pass


def game():
	print(getInput())



if __name__ == "__main__":
	game()