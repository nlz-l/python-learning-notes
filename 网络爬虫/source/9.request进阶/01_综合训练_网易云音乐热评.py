from Crypto.Cipher import AES
from base64 import b64encode
import requests
import json

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_108640",
    "threadId": "R_SO_4_108640",
}
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g = '0CoJUm6Qyw8W8jud'
e = '010001'
i = 'qQLowsrv6vikwEUq'
def get_encSeckey():
    return "afffc70d2f50530ff9c00fc5af819789a3d7ef43539cd4fa5e5ba1d245c17b6e734cf206345d550d3e55b2009b113d72409c3caa454a79e76c8ae3fab3bb49c092007d50f43ced3627fa3d42a5da1a800f6d3ef9ec2af65c6ad927f3402f8b3968b742be07bb415005b1ba3dc9a0c00a885157614a5195aa1bebf15dfdb18048"

def get_params(data):  # 默认收到的是字符串
    first = enc_params(data,g)
    second = enc_params(first,i)
    return second
def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return  data


def enc_params(data,key):
    data = to_16(data)
    iv = "0102030405060708"
    aes = AES.new(key=key.encode("utf-8"),IV=iv.encode("utf-8"),mode=AES.MODE_CBC,)
    bs = aes.encrypt(data.encode("utf-8")) # 加密
    return str(b64encode(bs),"utf-8") #转换成字符串返回
"""
    function a(a) { #随机的16位字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)  # 循环16次
            e = Math.random() * b.length, # 随机数
            e = Math.floor(e), # 取整
            c += b.charAt(e);  # 去XXX 取b
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) { d: 数据 ,e:'010001',
        var h = {}
          , i = a(16); # 16位的随机值
        return h.encText = b(d, g),
        h.encText = b(h.encText, i), # params
        h.encSecKey = c(i, e, f),    # encSecKey
        h
    }
"""

resp = requests.post(url,data={
    "params":get_params(json.dumps(data)),
    "encSecKey":get_encSeckey(),
})
print(resp.text)