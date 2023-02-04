
# (1)导入seleniu
from importlib.resources import path
from selenium import webdriver

# (2)创建浏览器操作对象

path = 'chromedriver.exe'

browser = webdriver.Chrome(path)

# （3）访问网站
url = 'https://baidu.com'

import time


def openbrowser():
    driver_path = r"C:\Program Files\Python38\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get('https://www.baidu.com/')
    time.sleep()
    # driver.close()
if __name__ == '__main__':
    print('PyCharm')
    openbrowser()

browser.get(url)
