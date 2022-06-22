import base64
import hashlib

def change2base64(url):
    url = url.replace('=','').replace('/','_')
    hash = hashlib.md5(url.encode())
    return base64.b64encode(hash.digest())