#
# # #https://www.ptpress.com.cn/login   登录url
# # #https://www.ptpress.com.cn/kaptcha.jpg?v=0.7097504522264793   验证码链接

###因为http协议是无状态的，即每次请求都是独立的，“人生只如初见”，
###对服务器来说，每次的请求都是全新的，所以需要保持HTTP连接状态的cookie和session
###Cookie保存在浏览器中，而Session保存在服务器上。
###浏览器访问服务器的时候，服务器把客户端信息以某种形式记录在服务器上。这就是Session。
###浏览器再次访问时只需要从该Session中查找该用户的状态就可以了。

###1、创建session会话
###requests提供了一个一个叫做session的类，来实现客户端和服务端的会话保持。
###requests.Session让使用者能跨请求保持某些参数如cookie，而且能自动处理服务器发来的cookie
###使得同一个会话中的请求都带上最新的cookie，非常适合模拟登录。
###为了保持会话的连续，我们最好的办法是先创建一个session对象，用其打开一个url, 而不是直接使用requests.get方法打开一个url。
###每当我们使用这个session对象重新打开一个url时，请求头都会带上首次产生的cookie，实现了会话的延续。

###Session的作用，保持会话的连续性
# import requests
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) Chrome/65.0.3325.181",
# }
# r = requests.get('https://www.baidu.com/s?wd=python', headers=headers)
# # print(r.request.headers)
# print(r.cookies)
#
# # # 设置一个会话session对象s
# s = requests.session()
# r1 = s.get('https://www.baidu.com/s?wd=python', headers=headers)
# # # 打印请求头和cookies
# # print(r1.request.headers)
# print(r1.cookies)
# #
# # 利用s再访问一次
# r2 = s.get('https://www.baidu.com/s?wd=python', headers=headers)
# # 请求头已保持首次请求后产生的cookie
# # print(r2.request.headers)
# print(r2.cookies)

###① 由于session有20分钟的过期时间，所以，同一份cookie文件，只能20分钟内有效，可以反复登录。
###② requests库提供了会话对象（requests.Session()）让使用者能跨请求保持某些参数如cookie，
###而且能自动处理服务器发来的cookie，使得同一个会话中的请求都带上最新的cookie，非常适合模拟登录。



###2、将cookie保存在本地，然后再打开
# import requests
# from http import cookiejar    ###或者是import http.cookiejar
# #导入 cookiejar 模块，存储和加载Cookie需要用到http库的cookiejar模块，它提供可存储Cookie的对象
# ##https://docs.python.org/zh-cn/3.7/library/http.html
# ##http库是python的内置库
# s = requests.session()
# filename = 'cookies77.txt'
# s.cookies = cookiejar.LWPCookieJar(filename)
# print(s.cookies)
# url = 'https://www.baidu.com/'
# url1 = 'https://www.ptpress.com.cn/'
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) Chrome/65.0.3325.181'}
# r = s.post(url1,headers=headers)
# s.cookies.save(ignore_discard=True, ignore_expires=True)    ##必须要加save，不然cookies22无法保存
#
# # # ###用load方法加载cookie
# s.cookies.load(ignore_discard=True)   ##ignore_discard,表示即使Cookie不存在，也要加载，默认为False#     print(s.cookies)
# with open('cookies77.txt','r') as file:
#     c = file.read()
#     print(c)
#


###3、保存表单登录成功后的cookie，cookie保存在根目录
# import requests
# from PIL import Image
# from http import cookiejar
#
# #
# s = requests.Session()        #创建会话对象Session
# s.cookies = cookiejar.LWPCookieJar('cookie23')   #创建 LWPCookieJar对象，若 Cookie不存在建立 Cookie 文件，命名为 cookie
# ###直接保存在根目录下，名称为cookie23.txt
# # print(s.cookies)
# login_url = 'https://www.ptpress.com.cn/login'
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) Chrome/65.0.3325.181'}
# captcha_url = 'https://www.ptpress.com.cn/kaptcha.jpg?v=0.7097504522264793'
# response = s.get(captcha_url, headers=headers)   #向验证码地址发送请求，获取图片
# with open('captcha23.gif', 'wb') as f:   #将图片保存到本地,覆盖写入方式打开
#     f.write(response.content)
# im = Image.open('captcha23.gif')   #创建Image对象
# im.show()     #调用本机图片查看程序打开图片
# captcha = input(' 请输入验证码： ')    #输入验证码图片上的字符，然后按ENTER键
# #
# login_data = {'username': '******',
#               'password': '****@',
#               'captcha': captcha}    #构建需要提交的表单数据dict,要求为字典格式
# r = s.post(login_url, data=login_data, headers=headers)  #以参数方式提交表单数据，使用POST请求方法向提交入口发送请求
# print(r.status_code)   #200为请求成功，   Cookie失效则返回 500 。
# print(' 发送请求后返回的网址为： ', r.url)         #测试是否成功登陆
# s.cookies.save(ignore_discard=True, ignore_expires=True)         #保存 cookie，没有此操作，cookie不会被保存
# print(s.cookies)
# # # #ignore_discard,表示即使Cookie不存在，也要加载，默认为False
# # # #ignore_expires,表示覆盖原有Cookie,默认为True





##4、将cookie保存在本地，然后再打开
##判断保存的 Cookie文件是否存在，存在则加载
# import requests
# from http import cookiejar    ###或者是import http.cookiejar
# s = requests.session()
# filename = 'cookies22.txt'
# s.cookies = cookiejar.LWPCookieJar(filename)
#
# url = 'https://www.baidu.com/'
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) Chrome/65.0.3325.181'}
# r = s.post(url,headers=headers)
# s.cookies.save(ignore_discard=True, ignore_expires=True)    ##必须要加save，不然cookies22无法保存
# ###判断保存的 Cookie文件是否存在，存在则加载
# try:
#     s.cookies.load(ignore_discard=True)   ##ignore_discard,表示即使Cookie不存在，也要加载，默认为False
#     print(s.cookies)
#     # with open('cookies22.txt','r') as file:
#     #     c = file.read()
#     #     print(c)
# except:
#     print("load cookies failed")




