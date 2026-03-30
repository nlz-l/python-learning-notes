"""
1.线程执行具有随机性
2.默认情况下 主线程会等待所有的子线程执行结束在结束
3.(同一个进程) 数据共享
4.多线程共享数据 可能会出现安全问题 用互斥锁解决
"""

import threading,time

def work():
    for i in range(11):
        time.sleep(0.2)
        print("工作中...")


if __name__ == '__main__':

    t = threading.Thread(target=work,daemon=True)
    #t.daemon = True
    t.start()
    time.sleep(1)

    print("主线程结束了")