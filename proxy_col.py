from urllib.request import *
#from requests import Request
from bs4 import BeautifulSoup
from os import popen,path
import time
############################################[ Variables ]###########################################
tm = time.ctime(int(time.time()))
# tim=print(tm)
tx=str(time.time())[-4:]
# exit()
l=[]
prox=[]
results=[]
a=1
# url='https://hidemyna.me/en/proxy-list/'
url= "https://free-proxy-list.net/"
headers={"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:65.0) Gecko/20100101 Firefox/65.0"}
cl=popen("clear").read() # clear command
####################################################################################################

rep=Request(url,headers=headers)
rep=urlopen(rep)
con=rep.read()
soup=BeautifulSoup(con,'html.parser')

for i in soup.find_all('tr'):
	p=i.find_all('td')
	p=list(p)
	if len(p) == 0:
		continue
	# if "ago" in p:
	for b in p:
		l.append(b.get_text())
	# print(l[6])
	try:
		if l[6] == "no":
			l[6]="http"
		else:
			l[6]="https"
	except Exception as a:
			b=1
	else:
		try :
			int(l[1])
			#print(l) # print th result
			results.append(l)
		except Exception as a:
			b=1
	# print(l)
	l=[]

	# a=a+1
	# if a ==5 :
	# 	break

###########################################################

print(cl)
print("""
	Press :
	1) for save proxies for proxy chains
	2) for save proxies for python 
	3) for sqlmap :)
	
""")

choice = input(' {+} ')
file = input("[ File output name ] : ")
reslen = input("[ number of proxies ] : ")

###########################################################
	
		# File Name 

if file == None or file == "":
	file="output-"+tx+".txt"
elif path.isfile(file):
	file=file.split(".")
	if len(file)=="2":
		file=file[0]+'-'+tx+".txt"
	print(file)


if reslen == None or reslen == "":
	reslen=10;
rl=0
print(file,reslen)
fileop=open(file,"w")
if choice == "1" :
	for i in results:
		proxy=i[0]+":"+i[1]+'\n'
		fileop.write(proxy)
		rl=rl+1
		if rl == reslen:
			break
elif choice == "2" :
	for i in results:
		proxy='"'+i[6]+"\":\""+i[0]+":"+i[1]+'"'
		prox.append(proxy)
		print(proxy)
		rl=rl+1
		if rl == reslen:
			break
	resl=str(prox).replace("[","{").replace("]","}").replace("'","")
	fileop.write(resl)
	print(resl)
elif choice == "3" :
	for i in results:
		proxy=i[6]+'://'+i[0]+":"+i[1]+'\n'
		fileop.write(proxy)
		rl=rl+1
		if rl == reslen:
			break
print(cl,'result saved in >> ',file)
print(tm)
fileop.close()


