import asyncio
import time




# async def func():
#     print("你好,我叫周杰伦")
#
#
# if __name__ =="__main__":
#     g = func()
#     asyncio.run(g)

# async def func1():
#     print("你好,我叫周杰伦")
#     await asyncio.sleep(3)
#     print("你好,我叫周杰伦")
#
# async def func2():
#     print("你好,我叫王建国")
#     await asyncio.sleep(2)
#     print("你好,我叫王建国")
#
# async def func3():
#     print("你好,我叫李雪琴")
#     await asyncio.sleep(4)
#     print("你好,我叫李雪琴")
#
# async def main():
#     tasks = [
#         asyncio.create_task(func1()),
#         asyncio.create_task(func2()),
#         asyncio.create_task(func3()),
#     ]
#
#     await asyncio.wait(tasks)
# if __name__ =="__main__":
#     t1 = time.time()
#     asyncio.run(main())
#     t2 = time.time()
#     print(t2 - t1)

async def download(url):
    print("准备开始下载")
    await asyncio.sleep(2)
    print('下载完成')

async def main():
    urls = [
        "http://www.baidu.com",
        "http://www.bilibili.com",
        "http://www.163.com"
    ]
    tasks = []
    for url in urls:
        d =asyncio.create_task(download(url))
        tasks.append(d)
    await asyncio.wait(tasks)
if __name__ == "__main__":
    asyncio.run(main())
