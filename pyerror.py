# -*- coding: utf-8 -*-


import urllib.error
import urllib.request
#url_str="http://www.whatismyip.com/"
url_str="https://www.python.org/"
try:
    f=urllib.request.urlopen(url_str,timeout=10)
except urllib.error.HTTPError as e:
    print("Http Error Code:",e.code,",","Http Error Reason",e.reason)
except urllib.error.URLError as e:
    print("URL Error Reason",e.reason)
else:
    print("ok")



import urllib.error
import urllib.request
url_str="http://www.whatismyip.com/"
try:
    f=urllib.request.urlopen(url_str,timeout=10)
except urllib.error.HTTPError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)
