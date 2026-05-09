import requests, os, time

os.makedirs("music", exist_ok=True)
headers = {"User-Agent": "Mozilla/5.0", "Referer": "https://y.qq.com"}

singer = "王菲"
saved = 0

for page in range(1, 15):
    if saved >= 20:
        break

    # 1. 逆向搜索API - 获取歌曲列表
    try:
        r = requests.get("https://c.y.qq.com/soso/fcgi-bin/client_search_cp",
            params={"w": singer, "format": "json", "p": page, "n": 30}, headers=headers, timeout=10)
        songs = r.json()["data"]["song"]["list"]
    except:
        continue

    # 2. 逆向vkey接口 - 获取每首歌的下载链接
    mids = [s["songmid"] for s in songs]
    vk_data = {"req_0": {"module": "vkey.GetVkeyServer", "method": "CgiGetVkey",
        "param": {"guid": "10000", "songmid": mids, "songtype": [0]*len(mids), "uin": "0", "loginflag": 1, "platform": "20"}}}
    r2 = requests.post("https://u.y.qq.com/cgi-bin/musicu.fcg", json=vk_data, headers=headers, timeout=10)
    infos = r2.json()["req_0"]["data"]["midurlinfo"]
    sip = r2.json()["req_0"]["data"]["sip"]

    for s, info in zip(songs, infos):
        if saved >= 20:
            break
        purl = info.get("purl", "")
        if not purl:
            continue

        song_name = s["songname"].replace("/", "_")
        singer_name = s["singer"][0]["name"]

        # 3. 下载歌曲
        dl_url = sip[0] + purl
        audio = requests.get(dl_url, headers=headers, timeout=20)
        if audio.status_code == 200 and len(audio.content) > 500000:
            saved += 1
            filepath = f"music/{saved:02d}_{song_name}-{singer_name}.mp3"
            with open(filepath, "wb") as f:
                f.write(audio.content)
            print(f"[{saved}/20] {song_name} - {singer_name} | {len(audio.content)//1024}KB")

    time.sleep(0.5)

print(f"\n共下载 {saved} 首歌曲，保存在 music/ 目录")
