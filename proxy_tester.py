
##############################"#

from requests import *
from random import choice
import yaml
from os import popen
##############################"#

############### variables ###############"#

cl=popen('clear').read()
url ='http://httpbin.org/ip'
# fprox = input("proxies file : ")
fprox="output-9753.txt"

#########################################"#

a=fprox=open(fprox,"r+")
proxies=fprox.read().replace("{",'').replace("}",'')
proxies=proxies.split(',')
# print(proxies)
a.close
def chose(proxies):
	proxie="{"+choice(proxies)+"}"
	proxie=yaml.load(proxie)
	return(proxie)

#########################################"#

for a in range(20):
	proxie = chose(proxies)
	print(proxie)
	try:
		req = get(url,proxies=proxie,timeout=2)
		print(req.status_code)
	except ConnectionError as conerr:
		print("timeout error","[ die ] ",proxie)
	except HTTPError as httperr:
		print("timeout error","[ die ] ",proxie)
	except KeyboardInterrupt:
		print("Exiting...")



# proxie = "{'http':'103.214.202.142:33423'}"
# print(proxie)
# try:
# 	req = get(url,proxies=proxie,timeout=2)
# 	print(req.text)
# except :
# 	print("timeout error","[ die ] "+proxie)
# 	exit()
