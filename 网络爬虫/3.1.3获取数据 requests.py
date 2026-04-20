# #1.机器学习概述、使用 Requests 库生成 HTTP 请求
import requests
url = 'https://www.xiachufang.com/explore/'
# 生成 GET 请求
r = requests.get(url)   #第一步，获取数据
print('响应码：', r.status_code)  # 查看状态码
# print('编码：', r.encoding)   # 查看编码,为utf-8,
# print(r.apparent_encoding)  # Windows-1254,虽然与encoding查看不一样，可以综合chardet.detect()共同查验最终的编码形式
# print('请求头：', r.headers)  # 查看请求头
# print('实体：', r.text)   # 查看网页内容
# print('实体：', r.content)

# print('网页内容：', rqq.text[:40])  # 把响应对象转换为字符串数据
# print('网页内容：', rqq.content[:40]) #把响应对象转换为二进制数据


##2、发送GET请求并手动指定编码
# import requests
# url = 'https://www.baidu.com/'
# rqq = requests.get(url)
# print('编码：',rqq.encoding)
# rqq.encoding = 'utf-8'  #将编码手动指定为 utf-8
# print('修改后的编码：',rqq.encoding)


#3、使用apparent_encoding方法检测编码并手动修改编码
# import requests
# url = 'https://www.baidu.com/'
# r = requests.get(url)
# print(r.encoding)  #查看的编码为ISO-8859-1.机器学习概述
#
# print(r.apparent_encoding)  # utf-8,虽然与encoding查看不一样，可以综合chardet.detect()共同查验最终的编码形式
# # r.apparent_encoding是从内容中分析出响应内容编码，大多数情况下比encoding更加准确，但是一般先调用encoding方法，不存在的话再查看apparent_encoding
# r.encoding = r.apparent_encoding  #手动修改编码，但是apparent_encoding分析编码比较耗时
# print(r.encoding)

##选讲
# #4、使用 chardet库中的detect 方法检测编码并指定编码
# import requests
# import chardet  #python内置库
# url = 'https://www.baidu.com/'
# r = requests.get(url)
# print(r.encoding)  #查看的编码为ISO-8859-1.机器学习概述
# print(type(r.content))
#
# type = chardet.detect(r.content)  #detect方法检测编码并指定编码
# print('detect方法检测结果：',type)  #{'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
##综合apparent_encoding与chardet.detect()两种查验编码的方法，显示百度网页的实际编码格式为utf-8
# r.encoding = chardet.detect(r.content)['encoding']  # 将检测到的编码赋值给 r.encoding
# print(' 改变后的编码： ', r.encoding)  # 查看改变后的编码


##chardet.detent方法举例
# from chardet import detect
# data = '对酒当歌，人生几何'.encode('utf-8')  #输入的诗歌进行utf-8编码
# print(detect(data))#再用detect方法检测data的编码方法


##5、使用 Requests 库处理请求头与响应头，使用 Requests 库设置超时
# import requests
# # url = 'https://www.xiachufang.com/explore/'
# url = 'https://www.xiachufang.com/recipe/104507074/'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# r = requests.get(url, headers=headers, timeout=2.0)
# print(r.status_code)
# r.headers  ## 查看响应头


##6、生成完整 HTTP 请求
# import requests
# import chardet
# url = 'https://www.xiachufang.com/explore/'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# r = requests.get(url, headers=headers, timeout=2.0)
# # r.encoding = 'utf-8'
# r.encoding = chardet.detect(r.content)['encoding']
# r.text
#
# f = open("下厨房源代码request.html",'w',encoding='utf-8')
# f.write(rqq.text)
# f.close()




