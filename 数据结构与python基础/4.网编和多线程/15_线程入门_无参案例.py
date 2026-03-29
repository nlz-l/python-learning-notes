import threading
import time
#进程更占用资源 更稳定  线程 反之


def coding():
    for i in range(1,11):
        time.sleep(0.1)
        print(f"正在敲第 {i} 遍代码!")

def music():
    for i in range(1,11):
        time.sleep(0.1)
        print(f'正在听第 {i} 遍音乐......')

if __name__ == '__main__':
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=music)
    for i in range(1,11):
        print("我是main")
    t1.start()
    t2.start()
