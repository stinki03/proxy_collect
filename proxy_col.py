from urllib.request import *
#from requests import Request
from bs4 import BeautifulSoup

############################################[ Variables ]###########################################
l=[]
prox=[]
results=[]
a=1
# url='https://hidemyna.me/en/proxy-list/'
url= "https://free-proxy-list.net/"
headers={"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:65.0) Gecko/20100101 Firefox/65.0"}
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


print("""
	Press :
	1) for save proxies for proxy chains
	2) for save proxies for python 
	#3) Not Found yet :)
	
""")

choice = input(' {+} ')

###########################################################
fileop=open("file.txt","w")
if choice == "1" :
	for i in results:
		print(i[0]+":"+i[1])
elif choice == "2" :
	for i in results:
		proxy="{ "+i[6]+':"'+i[0]+":"+i[1]+'" }'
		prox.append(proxy)
	fileop.write(str(prox))
fileop.close()


