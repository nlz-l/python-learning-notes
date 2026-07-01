import asyncio
import aiohttp

urls = [
    "https://w.wallhaven.cc/full/k8/wallhaven-k82d26.jpg",
    "https://w.wallhaven.cc/full/w5/wallhaven-w5m6yr.jpg",
    "https://w.wallhaven.cc/full/yq/wallhaven-yqg6r7.jpg",
]


async def download(url):
    name = url.rsplit("/",1)[1]
    # s = aiohttp.ClientSession() # == requests
    async with aiohttp.ClientSession(trust_env=True) as session: # trust_env=True 获取环境变量的代理
        async with session.get( url) as resp:
            with open(f'./img/{name}',mode="wb") as f:
                f.write(await resp.content.read())
    print(name,"下载完毕")



async def main():
    tasks =  []
    for url in urls:
        task = asyncio.create_task(download(url))
        tasks.append(task)

    await asyncio.wait(tasks)

if __name__ == "__main__":
    asyncio.run(main())

