import time
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #键盘按钮

# 引入字体解码包
import requests
import re
import html
from io import BytesIO
from fontTools.ttLib import TTFont

def get_font_map(page_url):      #获取字体解码文件
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.get(page_url, headers=headers)
    res.encoding = "utf-8"
    page_html = res.text

    font_path = re.search(r"src:\s*url\((.*?)\)", page_html).group(1)

    if font_path.startswith("/"):
        font_url = "https://www.shixiseng.com" + font_path
    else:
        font_url = font_path

    font_res = requests.get(font_url, headers=headers)
    font = TTFont(BytesIO(font_res.content))

    cmap = font["cmap"].getBestCmap()

    font_map = {}
    for code, glyph_name in cmap.items():
        if glyph_name.startswith("uni"):
            fake_char = chr(code)
            real_char = chr(int(glyph_name[3:], 16))
            font_map[fake_char] = real_char

    return font_map
def decode_text(text, font_map):     #字体解码
    text = html.unescape(text)
    return "".join(font_map.get(ch, ch) for ch in text)


web = Edge()
web.get("https://www.shixiseng.com/")
time.sleep(2)
x_btn = web.find_element(By.XPATH,"/html/body/div[5]/div/img[1]")
time.sleep(1)
x_btn.click()
time.sleep(1)
# 这个网站回车无效
# web.find_element(By.XPATH,'//*[@id="__layout"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/input[1]').send_keys("python",Keys.ENTER)
web.find_element(By.XPATH,'//*[@id="__layout"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/input[1]').send_keys("python")
x_f = web.find_element(By.XPATH,'//*[@id="__layout"]/div/div[2]/div[2]/div/div/div[2]/div[3]/input[1]') #搜索
x_f.click() #点击搜索
time.sleep(3)
# 切换窗口
web.switch_to.window(web.window_handles[-1])
time.sleep(1)
# 动态执行js
web.execute_script("""
    var a = document.getElementsByClassName("footer-login--is-show")[0];
    a.parentNode.removeChild(a);
""")

a = web.find_elements(By.XPATH,'//*[@id="__layout"]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div')
# print(a.text) # 这里有字体反爬,暂时没办法
font_map = get_font_map("https://www.shixiseng.com/interns?keyword=python&city=%E5%85%A8%E5%9B%BD&type=intern") #字体解码
for i in a:
    try:
        h = i.find_element(By.XPATH, "./div[1]/div[1]/p[1]/a")
        # print(h.text) # 这里有字体反爬,暂时没办法
        # title = h.get_attribute("title")
        # title = decode_text(title, font_map)
        h.click()
        web.switch_to.window(web.window_handles[-1])
        con_job = web.find_element(By.XPATH,'//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]')
        con_txt = con_job.text
        print(f"公司简介:\n{con_txt}\n")
        job_detail = web.find_element(By.XPATH,'//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div')
        job_txt = job_detail.text
        print(f"{job_txt}\n")
        time.sleep(1)
        web.close()
        web.switch_to.window(web.window_handles[1])
    except:
        pass
