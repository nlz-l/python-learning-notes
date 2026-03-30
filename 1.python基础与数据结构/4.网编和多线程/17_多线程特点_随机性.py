"""
1.线程执行具有随机性
2.默认情况下 主线程会等待所有的子线程执行结束在结束
3.(同一个进程) 数据共享
4.多线程共享数据 可能会出现安全问题 用互斥锁解决
"""

import threading
import time

def print_info():
    time.sleep(0.2)
    current_thread = threading.current_thread()
    print(current_thread.name)

if __name__ == '__main__':
    for i in range(1,11):
        t = threading.Thread(target=print_info)
        t.start()