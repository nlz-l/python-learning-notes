#1.进程之间不共享全局变量
#2.主进程会等待所有的子进程执行结束在结束

import multiprocessing
import time

def work():
    for i in range(10):
        print(f'hello {i}')
        time.sleep(0.2)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=work)  #进程默认命名 Process-编号 (从1开始)
    p1.daemon = True  # 守护进程
    p1.start()
    time.sleep(1)
    """
    强制关闭子进程
    p1.terminate 僵尸进程 (不建议使用)
    """
    print("main进程结束了!")
