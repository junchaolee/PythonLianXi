#coding:utf-8
"""
Selenium 库里有个叫 WebDriver 的 API。WebDriver 有点儿像可以加载网站的浏览器，
但是它也可以像 BeautifulSoup 或者其他 Selector 对象一样用来查找页面元素，与页
面上的元素进行交互 (发送文本、点击等)，以及执行其他动作来运行网络爬虫
"""
from selenium import webdriver
#想要调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys

#如果没有在环境变量指定PhantomJS位置
driver=webdriver.PhantomJS(executable_path="./phantomjs")

driver.get("http://www.baidu.com")

# data=driver.find_element_by_id("wrapper").text

# print data

# print driver.title
#生成当前页面快照并保存
driver.save_screenshot("baidu.png")