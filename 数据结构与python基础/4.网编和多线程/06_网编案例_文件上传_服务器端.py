
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.1.200',10086))
server_socket.listen(5)
accept_socket,client_info = server_socket.accept()
with open('./data/my.txt','wb') as dest_f:
    while True:
        bys = accept_socket.recv(8192)

        #无数据,结束即可
        if len(bys) == 0:
            break
        dest_f.write(bys)
#accept_socket.send("文件上传成功".encode("utf-8"))

accept_socket.close()
