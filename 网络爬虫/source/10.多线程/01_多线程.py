
# def func():
#     for i in range(10):
#         print("func",i)
#
#
# if __name__ == "__main__":
#     func()
#     for i in range(10):
#         print("main",i)

from threading import Thread
#
# def func():
#     for i in range(1000):
#         print("func",i)
#
# if __name__ == "__main__":
#     t = Thread(target=func)
#     t.start()
#     for i in range(1000):
#         print("main",i)

# class MyThread(Thread):
#     def run(self):
#         for i in range(1000):
#             print("子线程",i)
#
# if __name__ == "__main__":
#     t = MyThread()
#     t.start()
#     for i in range(1000):
#         print("主线程",i)

from threading import Thread


def func(name):
    for i in range(1000):
        print(name, i)


if __name__ == "__main__":
    t1 = Thread(target=func,args=("周杰伦",))
    t1.start()

    t2 = Thread(target=func,args=("王力宏",))
    t2.start()