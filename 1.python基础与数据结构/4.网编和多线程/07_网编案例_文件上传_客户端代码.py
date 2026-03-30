import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.1.200', 10086))

with open('D:/bc/python/python_jg/4.网编和多线程/1.txt','rb') as src_f:
    while True:
        data = src_f.read(8192)
        client_socket.send(data)
        if len(data) == 0:
            break
#print(f'客户端收到:{client_socket.recv(8192).decode("utf-8")}')
client_socket.close()







