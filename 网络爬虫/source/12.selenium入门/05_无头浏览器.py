import time
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# 配置无头
from selenium.webdriver.edge.options import Options

opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")

web = Edge(options= opt)
web.get("https://www.rili.com.cn/wannianli/")

sel = web.find_element(By.XPATH,'//*[@id="wnl_nian_sel"]')
sel_new = Select(sel)
# print(sel_new.options) # 获取所有选项
for i in range(len(sel_new.options)):
    for j in range(12):
        time.sleep(2)
        web.find_element(By.XPATH,f'//*[@id="wnl_12yue"]/table/tbody/tr/td[{j+1}]').click()
        sel_new.select_by_index(i) # 通过索引
        day = web.find_element(By.XPATH,'//*[@id="wnl_body"]/div/table/tbody')
        print(f'{day.text}\n')
# sel_new.select_by_value()   # 通过value属性
# sel_new.select_by_visible_text() # 通过展示文本
"""
<select>
    <option value="2020年">2020</option>
    <option value="2021年">2021</option>
</select>
"""

# 获取页面代码 不是源代码
# page_source = web.page_source
# print(page_source)