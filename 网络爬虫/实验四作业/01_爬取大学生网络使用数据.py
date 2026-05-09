from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

url = "https://raw.githubusercontent.com/dinamohsin/Students-Social-Media-Addiction-Analysis/main/data/Students%20Social%20Media%20Addiction.csv"
driver.get(url)
time.sleep(2)

csv_text = driver.find_element(By.TAG_NAME, "pre").text
driver.quit()

with open("_temp.csv", "w", encoding="utf-8") as f:
    f.write(csv_text)

df = pd.read_csv("_temp.csv")
df.columns = ["编号", "年龄", "性别", "学历", "国家", "日均上网时长(小时)",
              "最常用平台", "是否影响学业", "日均睡眠(小时)", "心理健康评分",
              "感情状况", "社交媒体冲突次数", "网络成瘾评分"]
df.to_excel("大学生网络使用数据.xlsx", index=False)
print(f"已爬取 {len(df)} 条真实大学生网络使用数据，保存到 大学生网络使用数据.xlsx")
print(df.head(10))
