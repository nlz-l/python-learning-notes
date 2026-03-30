"""
1.线程执行具有随机性
2.默认情况下 主线程会等待所有的子线程执行结束在结束
3.(同一个进程) 数据共享
4.多线程共享数据 可能会出现安全问题 用互斥锁解决
"""

import threading

global_num = 0
mutex = threading.Lock()
def target_fun1():
    mutex.acquire()
    global global_num
    for i in range(1000000):
        global_num += 1
    print(f'global_fun1函数结果: {global_num}' )
    mutex.release()

def target_fun2():
    mutex.acquire()
    global global_num
    for i in range(1000000):
        global_num += 1
    print(f'global_fun2函数结果: {global_num}' )
    mutex.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=target_fun1)
    t2 = threading.Thread(target=target_fun2)
    t1.start()
    t2.start()