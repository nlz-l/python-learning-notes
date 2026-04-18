#1、使用 urllib 3 库生成 HTTP 请求
import urllib3  #导入第三方库urllib3

## 使用Python3 requests发送HTTPS请求，已经关闭认证（verify=False移除SSL认证）情况下，控制台会输出以下错误：
##InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised.
## urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

http = urllib3.PoolManager()  # 创建 PoolManager 实例
rq = http.request('GET', url='https://www.baidu.com/')   # 通过 request 函数创建请求，此处使用 GET 方法
print('服务器响应码：', rq.status)  # 查看服务器响应码
# print('响应实体：', rq.data)  # 查看响应实体



# # # #2、使用 urllib 3 库处理请求头
# import urllib3
# http = urllib3.PoolManager()
# headers = {'User-Agent': 'Windows NT 6.1; Win64; x64'}
# # #发送带 headers 参数的 GET 请求
# rq = http.request('GET', url='https://www.xiachufang.com/explore/', headers=headers)
# print('服务器响应码：', rq.status)
# print('响应实体：', rq.data)



# #3、使用 urllib 3 库设置超时
# import urllib3
# http = urllib3.PoolManager()
# headers = {'User-Agent': 'Windows NT 6.1; Win64; x64'}
# #发送带 timeout 参数的 GET 请求
#
# #方法一、直接在 url 参数之后添加统一的 timeout 参数
# rq = http.request('GET', url='https://www.xiachufang.com/explore/', headers=headers, timeout=3.0)
# print('服务器响应码：', rq.status)
# print('响应实体：', rq.data)
#
# #方法二、分别设置连接与读取的 timeout 参数
# import urllib3
# http = urllib3.PoolManager()
# headers = {'User-Agent': 'Windows NT 6.1; Win64; x64'}
# rq = http.request('GET',url='https://www.xiachufang.com/explore/',headers=headers,timeout=urllib3.Timeout(connect=1.0,read=3.0))
# #指定超时时间或分别指定连接和读取的超时时间
# print('服务器响应码：', rq.status)
# print('响应实体：', rq.data)

# #方法三、在 PoolManager 实例中设置 timeout 参数
# import urllib3
# headers = {'User-Agent': 'Windows NT 6.1; Win64; x64'}
# http = urllib3.PoolManager(timeout=4.0)
# # http = urllib3.PoolManager(timeout=urllib3.Timeout(connect=1.0,read=3.0))
# rq = http.request('GET',url='https://www.xiachufang.com/explore/',headers=headers)
# print('服务器响应码：', rq.status)
# print('响应实体：', rq.data)


# #4、使用 urllib 3 库设置请求重试
#方法一、# 在 PoolManager 实例中设置 retries 参数参数
# import urllib3
# http = urllib3.PoolManager(timeout=4.0, retries=10)  #直接在 PoolManager 实例中定义请求重试次数
# head = {'User-Agent': 'Windows NT 6.1; Win64; x64'}
# rq = http.request('GET', url='https://www.xiachufang.com/explore/', headers=head)
# print('服务器响应码：', rq.status)
# print('响应实体：', rq.data)

# #方法二、直接在 url 之后添加 retries
# import urllib3
# http = urllib3.PoolManager(timeout=4.0)
# head = {'User-Agent': 'Windows NT 6.1; Win64; x64'}
# rq = http.request('GET', url='https://www.xiachufang.com/explore/', headers=head, retries=10)
# #向网站发送请求重试次数为 10 的 GET 请求
# print('服务器响应码：', rq.status)
# print('响应实体：', rq.data)

# #方法三、分别设置 5 次请求重试次数与 4 次重定向的 retries 参数
# import urllib3
# # 发送请求实例
# http = urllib3.PoolManager()
# # 网址
# url='https://www.xiachufang.com/explore/'
# # 请求头
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# # 超时时间
# tm = urllib3.Timeout(connect=1.0, read=3.0)
# # 重试次数和重定向次数设置并生成请求
# #发送请求重试次数为 5 与重定向次数为 4 的 GET 请求，发送同时关闭请求重试与重定向的 GET 请求
# rq = http.request('GET', url=url, headers=headers, timeout=tm, retries=5, redirect=4)
#
# # 同时关闭请求重试与重定向
# #rq = http.request('GET',url, retries = False)
# # 仅关闭重定向
# # rq = http.request('GET',url, redirect = False)
#
# print('服务器响应码：', rq.status)
# print('响应实体：', rq.data.decode('utf-8'))
#


# # #5、生成完整 HTTP 请求，该请求应当包含链接、请求头、超时时间和重试次数设置
# # # 创建 PoolManager 实例
# http = urllib3.PoolManager()
# # 目标 url
# url='https://www.xiachufang.com/explore/'
# # 设置请求头，
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# # 设置超时时间
# tm = urllib3.Timeout(connect = 1.0 , read = 3.0)
# # 设置重试次数并生成请求
# rq = http.request('GET',url, headers = headers,timeout = tm, retries = 5 , redirect = 4)
# # 查看服务器响应码
# print(' 服务器响应码： ', rq.status)
# # 查看获取的内容
# print(' 获取的内容： ', rq.data.decode('utf-8'))


