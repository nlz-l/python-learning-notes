# 所有章节内容
# https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}
# 章节内部内容
# https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}

import requests
import asyncio
import aiohttp
import aiofiles
import json


async def aiodownload(cid,b_id,title,a):
    if a == 9:
        a = 0
    if a > 9:
        a = a - 1
    data = {
        "book_id":b_id,
        "cid":f'{b_id}|{cid}',
        "need_bookinfo":1
    }
    data = json.dumps(data)
    url = f'https://dushu.baidu.com/api/pc/getChapterContent?data={data}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()
            async with aiofiles.open(f'./西游记全集/{a}.{title}.txt',mode="w",encoding="utf-8") as f:
                await f.write(dic["data"]["novel"]["content"])

async def getCatalog(url):
    resp = requests.get(url)
    dic = resp.json()
    tasks = []
    a = 0
    for i in dic["data"]["novel"]["items"]:
        a += 1
        title = i["title"]
        cid = i["cid"]
        task = asyncio.create_task(aiodownload(cid,b_id,title,a))
        tasks.append(task)
    await asyncio.wait(tasks)

if __name__ == '__main__':
    b_id = '4306063500'
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"'+ b_id +'"}'
    asyncio.run(getCatalog(url))