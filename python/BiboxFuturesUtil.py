# -*- coding: utf-8 -*-

import hmac
import hashlib
import json

import urllib
import requests
#import urlparse   # urllib.parse in python 3

# timeout in 5 seconds:
TIMEOUT = 5

#各种请求,获取数据方式
def http_get_request(url, params, add_to_headers=None):
    r = requests.get(url, params, timeout=TIMEOUT)
    try:
       if r.status_code == 200:
          return r.json()
       else:
          return
    except BaseException as e:
        print("httpGet failed, detail is:%s,%s" % (r.text, e))
        return
def http_post_request(url, params, add_to_headers=None):
    r = requests.post(url, data=params, timeout=TIMEOUT)
    if r.status_code == 200:
        return r.json()
    else:
        return


# -----  签名 ---------
def getSign(data, secret):
    result = hmac.new(secret.encode("utf-8"), data.encode("utf-8"), hashlib.md5).hexdigest()
    return result

def api_key_post(url, cmds, api_key, api_secret):
    s_cmds = json.dumps(cmds)
    sign = getSign(s_cmds, api_secret)
    params = {'cmds': s_cmds, 'apikey': api_key, 'sign': sign}
    r = http_post_request(url, params)
    return r