from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

def crawl_comments(url, num=500):
    opt = webdriver.ChromeOptions()
    opt.add_argument("--headless")
    driver = webdriver.Chrome(options=opt)
    driver.get(url)
    time.sleep(2)
    
    comments = []
    while len(comments) < num:
        items = driver.find_elements(By.CSS_SELECTOR, ".comment-item")
        for item in items:
            if len(comments) >= num:
                break
            try:
                text = item.find_element(By.CSS_SELECTOR, ".comment-content").text
                comments.append({"评论": text})
            except:
                pass
        
        try:
            driver.find_element(By.CSS_SELECTOR, ".next").click()
            time.sleep(1)
        except:
            break
    
    driver.quit()
    pd.DataFrame(comments).to_excel("评论数据.xlsx", index=False)
    print(f"完成! 共{len(comments)}条评论")

if __name__ == "__main__":
    crawl_comments("https://book.douban.com/subject/1084336/comments/", 500)