###使用 post函数向网站发送请求
import requests
url = 'https://www.ptpress.com.cn/login'
login = {'username': '******',
         'password': '*****'
         }      ## 将需要提交的表单数据放进 dict
r = requests.post(url, login)  #发送请求
print(r.status_code)

##使用session对象发送请求
##1、创建一个session对象
##2、让session发送get或post请求
##3、再使用session对象访问网站
# import requests
# url = 'https://www.ptpress.com.cn/login'
# login = {'username': '18671077707',
#          'password': 'yangfeng820703@'
#          }      ## 将需要提交的表单数据放进 dict
# s = requests.Session()
# r = s.post(url, login)  #发送请求
# print(r.status_code)
# ##需要注意，返回状态码是200并不能证明登录成功，200只表明表单数据被成功发送出去。

#
# import requests
# url = 'https://movie.douban.com/subject/34949767/comments?status=P'
# ua = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) Chrome/65.0.3325.181'
# headers = {'User-Agent':ua}
# session=requests.session() #创建session对象
# r=session.get(url,headers=headers) #使用session对象发送get请求，就能获取服务端设置的session对象
#


# ###表单登录方法模拟登录网站“ https://www.ptpress.com.cn/login ”
# ###方法一，使用requests与pillow库
# import requests
# from PIL import Image
#
# s = requests.Session()     # 创建会话对象 Session
# login_url = 'https://www.ptpress.com.cn/login'    # 提交入口
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) Chrome/65.0.3325.181'}  # 请求头的 User-Agent
#
# # 识别验证码函数
# def get_captcha():
#     captcha_url = 'https://www.ptpress.com.cn/kaptcha.jpg?v=0.7097504522264793'    # 验证码图片生成地址
#     r = s.get(captcha_url, headers=headers)    # 向验证码地址发送请求，获取图片
#     print(r.status_code)
#     with open('captcha1.gif', 'wb') as f:      # 将图片保存到本地
#         f.write(r.content)
#     im = Image.open('captcha1.gif')    # 创建 Image 对象
#     im.show()  # 调用本机图片查看程序打开图片
#     captcha = input(' 请输入输入验证码： ')   # 输入验证码图片上的字符，然后按 enter 键
#     return captcha
#
# login_data = {'username': '******', 'password': '*****', 'captcha': get_captcha()}    # 构建需要提交的表单数据 dict
# r = s.post(login_url, data=login_data, headers=headers)   # 提交表单数据，使用 POST 请求方法向提交入口发送请求
# # 测试是否成功登陆
# print(r.status_code)
# print(' 发送请求后返回的网址为： ', r.url)




###表单登录方法模拟登录网站“ https://www.ptpress.com.cn/login ”
###方法二，使用requests与matplotlib库
# import requests
# import matplotlib.pyplot as plt
#
# s = requests.Session()  #创建会话对象
# url = 'https://www.ptpress.com.cn/login'
# def get_captcha():
#     captcha_url = 'https://www.ptpress.com.cn/kaptcha.jpg?v=0.7097504522264793'
#     res1 = s.get(captcha_url)
#     print(res1.status_code)
#     with open('captcha3.jpg', 'wb') as f:
#         f.write(res1.content)
#     pic = plt.imread('captcha3.jpg')
#     plt.imshow(pic)
#     plt.show()
#     captcha = input('请输入验证码：')
#     return captcha
#
# login = {'username': '*****',
#          'password': '*******',
#          'captcha': get_captcha()}
# res2 = s.post(url, data=login)
# print(res2.status_code)
# print(res2.url)
#
#


