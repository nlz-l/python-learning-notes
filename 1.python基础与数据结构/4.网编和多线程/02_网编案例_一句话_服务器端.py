
"""
1.创建服务器端Socket对象
2.绑定IP地址和端口号
3.设置最大监听数
4.等待客户端申请建立连接
5.给客户端发消息
6.接收客户端的信息并打印
7.释放资源
客户端和服务器是通过 字节流(bytes) 的形式实现的
"""

import socket
# 1.创建服务器端Socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.绑定IP地址和端口号
server_socket.bind(('192.168.1.200',10086))
# 3.设置最大监听数
server_socket.listen(5)
# 4.等待客户端申请建立连接
accept_server,client_info = server_socket.accept()
# 5.给客户端发消息
# accept_server.send(b'Welcome To Socket!')
accept_server.send('欢迎来到NLZ'.encode('utf-8'))
# 6.接收客户端的信息并打印
data = accept_server.recv(1024).decode('utf-8')
print(f'服务器端收到 来自({client_info} 的信息: {data}')
# 7.释放资源
accept_server.close()
# server_socket.close() #服务器端一般不关闭

#扩展:设置端口号重用(释放端口)
# 参1 当前套接字对象 参2 选项名 参3 该选项的值
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)