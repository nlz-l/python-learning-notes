import requests

url = "https://www.pearvideo.com/video_1806108"
contid = url.split("_")[1]
videoStatus = f"https://www.pearvideo.com/videoStatus.jsp?contId=1806108&mrd=0.819035493952894"
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0",
    "referer":url
}
resp = requests.get(videoStatus,headers= headers)
dic = resp.json()
srcUrl = dic["videoInfo"]["videos"]["srcUrl"]
systemTime = dic["systemTime"]
srcUrl = srcUrl.replace(systemTime,f"cont-{contid}")

# 下载视频

with open("mp4/a.mp4","wb") as f:
    f.write(requests.get(srcUrl).content)