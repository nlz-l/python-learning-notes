import requests

session = requests.Session()
url = "https://passport.17k.com/ck/user/login"
data = {
    "loginName": "19738382651",
    "password": "123456789ll",
    }
session.post(url,data=data)
# print(resp.text)
# print(resp.cookies)
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0",
    "Cookie":"GUID=af781ef2-9249-480d-9ae9-8482922bf10b; BAIDU_SSP_lcr=https://cn.bing.com/; sajssdk_2015_cross_new_user=1; Hm_lvt_9793f42b498361373512340937deb2a0=1780385927; HMACCOUNT=560A886192ECA999; _c_WBKFRo=4CNJqqdScGZGknvv4Tr8yT73RcVGjDi4zwGbswZR; _nb_ioWEgULi=; c_channel=0; c_csc=web; acw_sc__v2=6a1e93dc55aa9d88b52fbae5e7aeeddd51ad2c53; ssxmod_itna=1-eqfx0D9DgGp4nD4kADpx0xCuwGDRiQDBP01aD_xQ5DODLxn_5GdDuYNC63tm1OiL00D3NRiie=8MD0HxrDnqD8XDQeDveZShX1YR7YWAIzRA7eNqOFR00Rq6sGAZlIsaj/TZnL5BOgCrt4GLDY=DCwKNSbeD4R3Dt4DIDAYDDxDWj4DLDYoDY_TKxGp3yluiLl23D0YDzqDgD7j3feDEDG3D0fR5b0G3wQ4DGqDS8aBWxD3Df4TqDDNqm9DNUGrqDYp3Zm0HLYF_E2uhfeDMbxGXYDZsPtZc=GWNPsYjHS2FkPGuDG=8gni2bK7RWG_r7qo/or_0D_A8xfonD5iB5YBxMixeixQ0qNixO75VGDNG5Kg4MGhAjhodiwBm3bxNesMusa4G4WevCD0gNUgNYoqzit1iq3Dpl05DrYziAO7e8mxPxe3fhz0AtexdoteA8kQL=l_wAhKZP_ph4D; ssxmod_itna2=1-eqfx0D9DgGp4nD4kADpx0xCuwGDRiQDBP01aD_xQ5DODLxn_5GdDuYNC63tm1OiL00D3NRiie=8_DDPbqYyD7pde_buDD/Qe1Gcd7sc109_GPs2f5uCr7p9S4ExVGkcmGZecUSHnMbwNz_8dDxwKSYmNNWY3NArNPsehf4xXQ8nUX4L6VK0j5oQLHfSp93lPn_oXM_of7Qa66_h2MRdItcRaMzuFTZmtW63dkrLiGd/6W5TtkEMh5R=X4nlDURA6zButyDL6asLXK64SHDc3NqqBV4nlTgWUb63f5iVbMRDjfC9uU9RqqWuDRqhlWk4TwD4FKGxHP40_RYBq1cDze=lmRjTx1P6WTfAw5z0kU_LUWhYGSYAYWDxW0tlyReBpFE4W7HlDQZ0pUDV9_4FvsDx/KbWlO8AucWBFKqj/Y5foHbGrcqNLq8RE=M2TvFwRiHWiK9xNQDneAYlGYzRTKxNlxie_5lD4S38EMqeh1=GDD; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F18%252F78%252F19%252F104531978.jpg-88x88%253Fv%253D1780389263000%26id%3D104531978%26nickname%3Dimll61%26e%3D1795942122%26s%3D5c03c1e06100c2bd; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22104531978%22%2C%22%24device_id%22%3A%2219e87454e41d71-0326f7e114a0658-4c657b58-1638720-19e87454e422669%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fgraph.qq.com%2F%22%2C%22%24latest_referrer_host%22%3A%22graph.qq.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%22af781ef2-9249-480d-9ae9-8482922bf10b%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1780390224",
}
resp = session.get("https://user.17k.com/ck/user/myInfo/104531978?bindInfo=1&appKey=2406394919",headers=headers)
print(resp.json())