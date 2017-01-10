

class c:
	colors=[[1,'blue','\033[44m'],[2,'green','\033[42m'],[3,'red','\033[41m'],[4,'yellow','\033[43m'],[5,'cyan','\033[46m'],[6,'purple','\033[45m'],[7,'gray','\033[48;5;8m'],[8,'white','\033[48;5;15m']]
	END='\033[0m'

def test():
	result="\t"
	for i in c.colors:
		result+=str(i[0])+i[2]+4*" "+c.END
	return result

def compare(inp,key):
	colors=0
	place=0
	l=[1,10,10**2,10**3,10**4]
	for i in range(1,len(l)):
#		print('\t'+str(inp%l[i]/l[i-1])+' --- '+str(key%l[i]/l[i-1]))
		if int(inp%l[i]/l[i-1])==int(key%l[i]/l[i-1]):
			place+=1
		for j in range(1,len(l)):
			if int(inp%l[i]/l[i-1])==int(key%l[j]/l[j-1]):
				colors+=1
	return 'you have '+c.colors[7][2]+str(colors)+c.END+'\t'+c.colors[2][2]+str(place)+c.END+' in the right place'
