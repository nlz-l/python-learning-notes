import requests
import json
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

url = "https://pdapis.pdnews.cn/api/rmrb-bff-display-zh/display/zh/c/compInfo"

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh",
    "User-Agent": "PeopleDailyChinese/14757.3.36 (iPhone; iOS 26.0.1; Scale/3.00)",
    "Cookie": "RMRB-X-TOKEN=eyJhbGciOiJIUzI1NiIsImtpZCI6ImN1UEpSQjRiOGt1NThkeEJld1dIrQWtOUjMwVHIQWdHRSdktabmFBQ190a3cifQ.eyJpc3MiOiJZW9wbGVzLWRhaWxhaW5XaWcvXJhiwic3ViIjoicGxicGVvcGxl",
    "adcode": "420602",
    "build_version": "202604231032",
    "channel": "AppStore",
    "city": "%E8%A5%84%E9%98%B3%E5%B8%82",
    "citycode": "0710",
    "device_id": "6A8083CC-BD2E-4D4A-98F0-92CACEDF55DB",
    "EagleEye-TraceID": "A6E8DC02A66F45E4A33B0F5252F3F9D7",
    "imei": "6A8083CC-BD2E-4D4A-98F0-92CACEDF55DB",
    "mpaasid": "ahk6k8c1EygDAOpIlHo/nHy",
    "os_version": "26.0.1",
    "plat": "Phone",
    "resolution": "390*844",
    "RMRB-X-TOKEN": "eyJhbGciOiJIUzI1NiIsImtpZCI6ImN1UEpSQjRiOGt1NThkeEJld1lrQWtOUjMwVHlQcHRSdktabmFBQ190a3cifQ.eyJpc3MiOiJwZW9wbGVzLWRhaWx5LWZvdXJhIiwic3ViIjoicGVvcGxlcy1kYWlseS1mb3VyYSIsImV4cCI6MTc4MDEyNDc2MCwidXNlcklkIjoxMTM5MTM1Mjc1NjkzNjQ3LCJ1c2VyVmVyc2lvbiI6IjExMzkxMzUyNzU2OTM2NDdfMCIsInVzZXJOYW1lIjoiJUU0JUJBJUJBJUU2JUIwJTkxJUU2JTk3JUE1JUU2JThBJUE1JUU3JUJEJTkxJUU1JThGJThCZ3RDQXlkIiwidXNlclR5cGUiOjEsImNyZWF0b3JJZCI6bnVsbCwidXNlcklkWmgiOm51bGx9.v560WCPHWlFFzw9UhluF6Ytmx79u8p5b1tdAcSB9Uxg",
    "system": "Ios",
    "timestamp": "1780045244000",
    "userId": "1139135275693647",
    "userType": "1",
    "version_name": "7.4.2.4",
    "versionCode": "7424",
    "X-Ca-Stage": "RELEASE",
    "Authorization": "APPCODE 48e210817e2d47328d2c47f42d7ef778",
    "Connection": "keep-alive",
    "Host": "pdapis.pdnews.cn"
}

params = {
    "channelId": "",
    "channelStrategy": 2,
    "cityCode": "420600",
    "districtCode": "420602",
    "groupId": 44088,
    "loadStrategy": "first_load",
    "pageId": 30595,
    "pageNum": 1,
    "pageSize": 20,
    "provinceCode": "420000",
    "refreshTime": 1780045244000,
    "topicId": 10000011113,
    "topicType": 21
}

def timestamp_to_time(ts):
    if not ts:
        return ""
    return datetime.fromtimestamp(int(ts)/1000).strftime("%Y-%m-%d %H:%M:%S")

def scrape_news():
    all_news = []
    res = requests.get(url, headers=headers, params=params, verify=False, timeout=15)
    data = res.json()
    comp_list = data.get("data", {}).get("compList", [])

    for comp in comp_list:
        for news in comp.get("operDataList", []):
            item = {
                "标题": news.get("newsTitle", ""),
                "发布时间": timestamp_to_time(news.get("publishTime", "")),
                "来源": news.get("source", ""),
                "新闻ID": news.get("objectId", ""),
                "图片链接": news.get("coverUrl", "")
            }
            all_news.append(item)

    # 保存文件
    with open("人民日报新闻.json", "w", encoding="utf-8") as f:
        json.dump(all_news, f, ensure_ascii=False, indent=2)
    print(f"爬取完成，共 {len(all_news)} 条新闻，已保存")

if __name__ == "__main__":
    scrape_news()