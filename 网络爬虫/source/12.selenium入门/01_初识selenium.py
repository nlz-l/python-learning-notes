from selenium.webdriver import Chrome,Edge
web = Edge()
url = "http://www.baidu.com"
web.get(url)
print(web.title)
