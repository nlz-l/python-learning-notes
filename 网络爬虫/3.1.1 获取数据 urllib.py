
import urllib.request  #导入Python内置的HTTP请求库urllib的request模块
# from urllib import request

url = 'https://www.xiachufang.com/recipe/107078178/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}

request = urllib.request.Request(url,headers=headers)
# print(request)
responses = urllib.request.urlopen(request)
print(responses.status)

# url = 'https://music.163.com/'
# url ='https://www.baidu.com/?tn=85070231_9_hao_pg'
# url = 'https://weibo.com/newlogin?tabtype=weibo&gid=102803&openLoginLayer=0&url=https%3A%2F%2Fweibo.com%2F'
# response = urllib.request.urlopen(url)
# print(response.status)

# #1、用request模块抓取Python官网
# response1 = urllib.request.urlopen('https://www.python.org')   #抓取Python官网
# print(response1.status)  #输出响应状态码
# print(response1)  #输出为<http.client.HTTPResponse object at 0x00000213324550C8>，我们需要的信息包含在这个对象里

#
# #不调用read（）方法，编码方法，也可以，上面的操作是为了避免出现乱码
#
#
# #2、查看响应的类型
# print(type)  #输出结果：<http.client.HTTPResponse object at 0x0000000002DFA0C8>  <class 'type'>
# # #输出一个HTTPResponse类型的对象，包含多种方法：read(),getheader(name),getheaders()
# print(response1.getheaders())  #调用getheaders(),获取响应头信息
# print(response1.getheader('Server'))  #调用getheader()方法，并传递一个参数Server,获取响应头中的server值，意思是服务器用nginx搭建的。
# print(response1.read()) #调用read()方法是指，读取响应内容，就是网页内容
#
# # #3、抓取百度首页，并存储
# response2 = urllib.request.urlopen('https://www.baidu.com')
# print(response2.status)  #输出响应状态码
# print(response2.read().decode('utf-8'))  #调用read()方法，输出编码为‘utf-8’的网页内容
# print(response2)  #不调用read（）方法，编码方法，也可以，上面的操作是为了避免出现乱码
# n = response2.read().decode('utf-8')
# #存储百度首页源代码
# page = open('百度网页源代码.html','w')
# page.write(n)
# page.close()

#
# # 4、添加可选参数data，
# #这里我们传递了一个参数word,值是hello,它需要被转码成bytes(字节流)类型，使用bytes()方法，该方法的第一个参数需要为str（字符串）类型，用urllib.parse模块中的urlencode()方法将参数字典转化为字符串；第二个参数指定编码格式为utf-8
# import urllib.parse
# import urllib.request
# #
# # response3 = urllib.request.urlopen('http://httpbin.org/get')
# data = bytes(urllib.parse.urlencode({'word':'hello77777777777777'}),encoding='utf-8')  #使用bytes()方法将参数转化为字节流编码格式的内容，即bytes类型
# response3 = urllib.request.urlopen('http://httpbin.org/get',data=data)
# # #请求的站点是httpbin.org,是一个提供HTTP请求测试的网站，我们的链接是用来测试post请求的，因此最终输出一下信息，包含我们传递的data参数
# print(response3.read())
# #输出结果显示传递的参数出现在了form字段中，表明是模拟了表单提交的方式，以POST方式传输数据。



# # #5、timeout参数的用法,设置超时时间，单位为秒
# response4 = urllib.request.urlopen('http://httpbin.org/get',timeout=0.02)
# print(response4.read())
# #timeout表明如果请求超过0.01秒，没有得到服务器的响应，就会抛出异常，输出结果为urllib.error.URLError: <urlopen error timed out>
# #报错，URLError异常属于，urllib.error模块，错误原因为超时







# #6、用timeout控制时间，跳过超时的网页抓取
# import socket #调用socket库中的socket.timeout,为异常的原因
# import urllib.request
# import urllib.error
#
# #用try...except语句来说实现异常处理
# try:
#     response5 = urllib.request.urlopen('http://httpbin.org/get',timeout=0.01)
# except urllib.error.URLError as e:  #except语句后面指定了要处理的异常类型
#     if isinstance(e.reason,socket.timeout): #判断错误是否为已知的异常类型，isinstance(object,classinfo),object是实例对象，classinfo类型名
#         print('TIME OUT!')
# #请求链接，设置超时时间为0.01秒，捕获了URLError异常，判断异常是socket.timeout类型（即超时异常），输出TIME OUT!
# #发生超时，从而引发socket.timeout异常


#7、更完整的发送请求的方法urllib.request.Request
# import urllib.request
# request1 = urllib.request.Request('https://www.baidu.com')
# response6 = urllib.request.urlopen(request1)
# print(response6.read().decode('utf-8'))

#
# # # # 8、传入多个参数构建请求的例子
# from urllib import request,parse
# # #
# # # import urllib.request
# # import urllib.parse  # 第二个参数data,必须传bytes字节流类型，如果是字典，需要用urllib.parse模块里的urlencod
# # #
# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/4.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
#     'Host': 'httpbin.org'
# }
#
# dict = {
#     'name': 'Germey'
# }
# data = bytes(parse.urlencode(dict), encoding='utf-8')  # 使用bytes()方法将参数转化为字节流编码格式的内容，即bytes类型
# req = request.Request(url=url, data=data, headers=headers, method='POST')  # 带参数请求
# response = request.urlopen(req)  # 获取响应
# print(response.read().decode('utf-8'))
# # 这里加入了4个参数构造了更强大请求，，指定了请求方式为POST
# # 观察输出结果，我们成功设置了data,headers和method

