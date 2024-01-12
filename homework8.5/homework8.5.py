# 导入bs4和requests库
from bs4 import BeautifulSoup
import requests

# 定义北邮管网的网址
url = "http://www.bupt.edu.cn/yxjg1.htm"

# 发送HTTP请求，获取网页内容
response = requests.get(url)

# print(response.encoding)

# 解析HTML文档，创建BeautifulSoup对象
bupt_soup = BeautifulSoup(response.text.encode("ISO-8859-1").decode("utf-8"), "html.parser")

# 使用find方法，根据id属性，查找党委名称列表所在的ul元素
ul = bupt_soup.find("ul", class_="linkPageList")

# 使用find_all方法，查找ul元素下的第一个li元素下的div元素下的ul元素下的所有li元素
print("使用find方法实现：")
li_list = ul.find("li").find("div").find("ul").find_all("li")

# 遍历li元素列表，提取并打印党委名称
for li in li_list:
    name = li.getText()
    print(name)

print()
# 使用select方法，根据CSS选择器，查找党委名称列表所在的ul元素下的所有li元素
print("使用select方法实现：")
li_list = bupt_soup.select('ul[class="linkPageList"] > li:nth-child(1) > div > ul > li > a')

# 遍历li元素列表，提取并打印党委名称
for li in li_list:
    name = li.getText()
    print(name)