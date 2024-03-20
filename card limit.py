try :
	import requests
except :
	import os
	os.system('pip install requests')
try :
	import pyfiglet
except :
	import os
	os.system('pip install pyfiglet')

import os
os.system('clear')
	
import requests,json,random,string,time
import pyfiglet

logo = f"""
\033[39m-----------------------------------------------------------  \033[32m                            

  
{pyfiglet.figlet_format("AJvip", font="3d-ascii")}   
\033[39m-----------------------------------------------------------  

"""
for line in logo.splitlines():
    print(line)
    time.sleep(0.1)

correct_password = "anaspro7"

while True:
    password_attempt = input("\033[1;32mEnter password \033[1;34m:\033[1;39m ")
    print()
    if password_attempt == correct_password:
        print("✅ \033[1;32mPassword Accepted")
        print()
        time.sleep(1)
        import os
        os.system('clear')
        break
    else:
        print("❌ \033[1;31mError Password, Please try again.")
        print()
logo = f"""
\033[39m-----------------------------------------------------------  \033[32m                            

  
{pyfiglet.figlet_format("AJvip", font="3d-ascii")}   
\033[39m-----------------------------------------------------------  

"""
for line in logo.splitlines():
    print(line)
    time.sleep(0.1)          
number = input('\033[1;32mEnter Your Number \033[1;34m: \033[1;39m')
password = input('\033[1;32mEnter Yor Password \033[1;34m:\033[1;39m ')
lmt = float(input('\033[1;32mEnter The Minimum \033[1;34m :\033[1;39m '))

print()
url="https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"
headers={
	    "Accept":"application/json, text/plain, */*",
	    "Connection":"keep-alive",
	    "x-dynatrace":"MT_3_17_998679495_45-0_a556db1b-4506-43f3-854a-1d2527767923_0_18957_273",
	    "x-agent-operatingsystem":"1630483957",
	    "clientId":"AnaVodafoneAndroid",
	    "x-agent-device":"RMX1911",
	    "x-agent-version":"2021.12.2",
	    "x-agent-build":"493",
	    "Content-Type":"application/x-www-form-urlencoded",
	    "Content-Length":"143",
	    "Host":"mobile.vodafone.com.eg",
	    "Accept-Encoding":"gzip",
	    "User-Agent":"okhttp/4.9.1"
	    }   
data={
	"username":number,
	"password":password,
	"grant_type":"password",
	"client_secret":"a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3",
	"client_id":"my-vodafone-app"
	    }      
res=requests.post(url, headers=headers, data=data)

if res.status_code == 200:
	    token = res.json()["access_token"]
	    print("✅ \033[1;32mLogin success")
	    print()
else:
	    print("❌ \033[1;31mError in The Number or Password ")
	    exit('\033[1;39m') 
########

hd2={'Host':'web.vodafone.com.eg','Connection':'keep-alive','Pragma':'no-cache','Cache-Control':'no-cache','msisdn':number,'api-host':'PromotionHost','Accept-Language':'AR','Authorization':'Bearer '+token,'Content-Type':'application/json','Accept':'application/json','clientId':'WebsiteConsumer','User-Agent':'Mozilla/5.0 (Linux; Android 9; SM-J610F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.73 Mobile Safari/537.36','channel':'WEB','X-Requested-With':'com.emeint.android.myservices','Sec-Fetch-Site':'same-origin','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://web.vodafone.com.eg/spa/portal/hub','Accept-Encoding':'gzip, deflate'}
while True:
    r2 = requests.get("https://web.vodafone.com.eg/services/dxl/ramadanpromo/promotion?@type=RamadanHub&channel=website&msisdn="+number,headers=hd2)
    try :
    	s = (r2.json()[1]['pattern'])
    except :
    	print('🕧  \033[1;31mTry again Tomorrow')
    	exit('\033[1;39m')
    for x in s:
        amount = (x['action'][0]['characteristics'][2]['value'])
        units = (x['action'][0]['characteristics'][1]['value'])
        card =  (x['action'][0]['characteristics'][3]['value'])
        if float(units) >= lmt :
                url3 = "https://web.vodafone.com.eg/services/promo/unifiedAssignPromo"
                headers3= {
    'Host': 'web.vodafone.com.eg',
    'Connection': 'keep-alive',
    'Content-Length': '151',
    'msisdn': number,
    'Accept-Language': 'AR',
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'clientId': 'WebsiteConsumer',
    'x-dtpc': '22$345329703_815h13vMFITCIRARKRCCIISRITFSEHHKPDUAKCJ-0e0',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Infinix X657B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36',
    'Sec-Fetch-Dest': 'empty',
    'channel': 'WEB',
    'Origin': 'https://web.vodafone.com.eg',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://web.vodafone.com.eg/spa/hub',
    'Accept-Encoding': 'gzip, deflate, br',
}

                payload3 ={
  "msisdn": number,
  "promoId": "4940",
  "channelId": 1,
  "param1": card,
  "param2": "4",
  "wlistId": "4661",
  "category": "Contextual",
  "triggerId": "876"
}
                response3 = requests.post(url3, headers=headers3,json=payload3).json()
                #print(response3['eDescription'])
                if response3['eDescription'] == 'Success' :
                	print(f'\n\n✅ \033[1;32mSuccessful Charging of \033[1;34m{units} \033[1;32mUnits ')
                	exit('\033[1;39m')
                else :
                	print('\n\n\033[1;31m❌ Error')
                	exit('\033[1;39m')
    import sys
    import time
    for i in range(5):
        sys.stdout.write('\r' + '⏳\033[1;34m Loading\033[0m ' + '█' * (i * 3) + '▒' * ((4 - i) * 3))
        sys.stdout.flush()
        time.sleep(0.09)
