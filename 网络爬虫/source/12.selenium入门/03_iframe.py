from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
import requests
import time

web = Edge()
web.get("https://www.xinpianyugao.com/play_218554_73680.html")
iframe = web.find_element(By.XPATH,'//*[@id="playerFrame"]')
web.switch_to.frame(iframe)
time.sleep(1)
a1 = web.find_element(By.XPATH,'//*[@id="my-video"]/div[1]/picture/img')
src = a1.get_property("src")
with open(f"./img/封面.png",mode="wb") as f:
    f.write(requests.get(src).content)

# 跳出frame
web.switch_to.default_content()

a2 = web.find_element(By.XPATH,'//*[@id="page-content"]/div[1]/div/ul/li[2]/a')
print(a2.text)