import multiprocessing
import time
def coding():
    for i in range(1,11):
        time.sleep(0.1)
        print(f"正在敲第 {i} 遍代码!")

def music():
    for i in range(1,11):
        time.sleep(0.1)
        print(f'正在听第 {i} 遍音乐......')
#单任务
# coding()
# music()
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=coding)
    p2 = multiprocessing.Process(target=music)

    p1.start()
    p2.start()
