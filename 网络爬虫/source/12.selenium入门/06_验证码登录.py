from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying_Client
import time
web = Edge()
web.get("https://www.chaojiying.com/user/login/")
png = web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
username = input("用户名:")
password = input("密码:")
chao = Chaojiying_Client(username, password, input("软件ID:"))
result = chao.PostPic(png,1902)
v_code = result["pic_str"]

web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(v_code)
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys(username)
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys(password)
time.sleep(2)
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()