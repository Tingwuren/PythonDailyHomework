from selenium import webdriver
import time
import csv
from datetime import datetime, timedelta

yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d') # 获取昨天日期
csv_file_name = f'./BYR-JOB-{yesterday}.csv'
titles = []

byr_driver = webdriver.Firefox()
base_url = "https://bbs.byr.cn"
url = base_url + "/index"
byr_driver.get(url)

# 找到用户名输入框，并发送用户名信息
user_input = byr_driver.find_element('css selector', 'input[name="id"]')
user = input("请输入用户名：")
user_input.send_keys(user)
time.sleep(1) # 避免网页还在加载过程中，反应比较慢，保险起见，等待1秒

# 找到密码输入框，并发送口令信息
pw_input = byr_driver.find_element('css selector', 'input[name="passwd"]')
pw = input("请输入密码：")
pw_input.send_keys(pw)
time.sleep(1) # 保险起见，等待1秒

# 找到登录按钮，并登录
login_button = byr_driver.find_element('css selector', 'input[id="b_login"]')
login_button.submit()
time.sleep(10)

# 抓取第一页中日期是昨天的帖子的标题
url = base_url + "/board/JobInfo"
byr_driver.get(url)
time.sleep(5)
rows = byr_driver.find_elements('css selector', 'table.board-list.tiz tbody tr')
for row in rows:
        element = row.find_element('css selector', 'td.title_9')
        title = element.get_attribute('innerText')
        
        element = row.find_element('css selector', 'td.title_10')
        date = element.get_attribute('innerText')

        if date == yesterday:
            titles.append(title)

# 获取2-5页url地址
links = byr_driver.find_elements('css selector', 'ol.page-main li.page-normal a')
# 创建一个空列表
hrefs = []
# 遍历links中的1-4号元素
for link in links[0:4]:
    # 获取元素的href属性
    href = link.get_attribute("href")
    # 将href属性添加到列表中
    hrefs.append(href)

# 抓取2-5页日期是昨天的帖子的标题
for h in hrefs[0:4]:
    byr_driver.get(h)
    time.sleep(5)
    rows = byr_driver.find_elements('css selector', 'table.board-list.tiz tbody tr')
    for row in rows:
            element = row.find_element('css selector', 'td.title_9')
            title = element.get_attribute('innerText')
            
            element = row.find_element('css selector', 'td.title_10')
            date = element.get_attribute('innerText')

            if date == yesterday:
                titles.append(title)
    
byr_driver.close()

with open(csv_file_name, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['序号', '标题'])
    for i, title in enumerate(titles, start=1):
        writer.writerow([i, title])