"""
1.线程执行具有随机性
2.默认情况下 主线程会等待所有的子线程执行结束在结束
3.(同一个进程) 数据共享
4.多线程共享数据 可能会出现安全问题 用互斥锁解决
"""

import threading,time

my_list = []

def write_data():
    for i in range(1,6):
        my_list.append(i)
        print('写入数据',i)
    print(f'write_data函数: {my_list}')

def read_data():
    time.sleep(2)
    print(f'read_data函数: {my_list}')


if __name__ == '__main__':
    t1 = threading.Thread(target=write_data)
    t2 = threading.Thread(target=read_data)
    t2.start()
    t1.start()
