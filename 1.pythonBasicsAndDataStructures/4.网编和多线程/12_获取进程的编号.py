import os

"""
getpid
getppid

main 进程的父进程是pycharm
"""
import multiprocessing
import time

"""
方式一 : args : 位置参数
方式二 : kwargs : 关键字参数
"""

def coding(name,num):
    for i in range(1,num+1):
        time.sleep(0.1)
        print(f" {name} 正在敲第 {i} 行")
    print(f'p1的进程pid:{os.getpid()},{multiprocessing.current_process().pid},父进程id(ppid):{os.getppid()}')
def music(name,count):
    for i in range(1,count+1):
        time.sleep(0.1)
        print(f' {name} 正在听第 {i} 遍音乐....')
    print(f'p2的进程pid:{os.getpid()},{multiprocessing.current_process().pid},父进程id(ppid):{os.getppid()}')
if __name__ == '__main__':
    p1 = multiprocessing.Process(target = coding,args = ("m",10))
    p2 = multiprocessing.Process(target = music,kwargs={'count' : 20,'name' : 'mm'})

    p1.start()
    p2.start()
    time.sleep(5)
    print(f'nain的进程pid:{os.getpid()},{multiprocessing.current_process().pid},父进程id(ppid):{os.getppid()}')
