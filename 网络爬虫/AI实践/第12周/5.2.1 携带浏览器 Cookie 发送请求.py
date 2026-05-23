


# ##https://www.ptpress.com.cn/login
# ##https://www.ptpress.com.cn/kaptcha.jpg?v=0.7097504522264793
#
# import requests
# login_url = 'https://www.ptpress.com.cn/'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
#
# ##从浏览器登录后复制 Cookie
# cookie_str = '__guid=66323496.1626990540758681900.1637202188460.828; gr_user_id=a1d3dfe0-f8d0-4e19-9aaa-485589d56ff4; acw_tc=2760823f16379285662513312ebb912cdfe08c7f9dae78ccfd8aa4e31a0d0d; JSESSIONID=323115AAEA9D81212177B2F4DE89E4CF; gr_session_id_9311c428042bb76e=d701659c-fe8a-4b1c-9346-deba489adb43; gr_session_id_9311c428042bb76e_d701659c-fe8a-4b1c-9346-deba489adb43=true; monitor_count=47'
# #
# ##把 Cookie字符串处理成 dict，以便接下来使用
# cookies = {}
# for line in cookie_str.split('; '):   #根据分号切片
#     key, value = line.split('=', 1)    #以'='切割，1为切割1次，中间以逗号分割
#     cookies[key] = value  #遍历并切片存入字典cookies
# print(cookies)
# #
# r = requests.get(login_url, cookies=cookies, headers=headers)     # 携带 Cookie 发送请求
# print(' 发送请求后返回的网址为： ', r.url)     # 测试是否成功登陆
#


# ##携带cookie登录豆瓣
# import requests
# login_url = 'https://www.douban.com/'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
#
# ##从浏览器登录后复制 Cookie
# cookie_str = 'gr_user_id=0f69b84b-4361-4d06-9e51-39339a01c638; douban-fav-remind=1; _ga=GA1.1.980877420.1634178722; __utmv=30149280.139; bid=gmzBWl5gN4Q; __gads=ID=63174ae421f5cae7-228c3af573d800fa:T=1668689513:RT=1668689513:S=ALNI_MbIVVhPNQaR3AI0v9DeK9V_mTQZ3A; ll="118256"; viewed="36184694"; __utmz=30149280.1681897442.13.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; push_noty_num=0; push_doumail_num=0; dbcl2="1390951:bm2GVZ5p8js"; _ga_RXNMP372GL=GS1.1.1683427975.2.1.1683428698.36.0.0; ck=A9_Z; ap_v=0,6.0; __utma=30149280.980877420.1634178722.1683427296.1684049283.15; __utmc=30149280; __utmt=1; frodotk_db="b352c96a6cae750f19f85c3f460b5f2d"; __utmt_douban=1; __utmb=30149280.3.10.1684049283; __gpi=UID=000009e99051a335:T=1664334930:RT=1684049324:S=ALNI_MafN3XJiLGIIZg_sp0Xg553pFh36Q'
#
# ##把 Cookie字符串处理成 dict，以便接下来使用
# cookies = {}
# for line in cookie_str.split('; '):   #根据分号切片
#     key, value = line.split('=', 1)    #以'='切割，1为切割1次，中间以逗号分割
#     cookies[key] = value  #遍历并切片存入字典cookies
# print(cookies)
#
# r = requests.get(login_url, cookies=cookies, headers=headers)     # 携带 Cookie 发送请求
# print(' 发送请求后返回的网址为： ', r.url)     # 测试是否成功登陆
# print(r.status_code)





