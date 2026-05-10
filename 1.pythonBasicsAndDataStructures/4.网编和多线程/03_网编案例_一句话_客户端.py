import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('172.20.10.2', 10086))
data = client_socket.recv(1024).decode('utf-8')
print(f'客户端收到:{data}')
client_socket.send('NLZ很好玩'.encode('utf-8'))
client_socket.close()

