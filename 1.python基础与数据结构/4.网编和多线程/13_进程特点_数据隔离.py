#1.进程之间不共享全局变量
#2.主进程会等待所有的子进程执行结束在结束
import multiprocessing
import time

my_list = []

def write_data():
    for i in range(1,6):
        my_list.append(i)
        print(f'添加数据:{i}')

    print(f'write_data函数:{my_list}')

def read_data():
    time.sleep(3)
    print(f'read_data函数:{my_list}')
print("main外资源")
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=write_data)
    p2 = multiprocessing.Process(target=read_data)
    p1.start()
    p2.start()
    print("main内资源")