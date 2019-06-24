#coding=utf-8
import requests
import time
from selenium import webdriver
# 设置请求头部信息
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
               'Accept': '*/*',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'gzip',
               'Connection': 'close',
               'Referer': 'http://www.baidu.com/link?url=_andhfsjjjKRgEWkj7i9cFmYYGsisrnm2A-TN3XZDQXxvGsM9k9ZZSnikW2Yds4s&amp;amp;wd=&amp;amp;eqid=c3435a7d00006bd600000003582bfd1f'
               }


def getToken(url):
    data = {'action': 'loginIn', 'name': '6g0pjqsiqCx6z', 'password': 'g13289508910'}
    r = requests.get(url, headers=headers, data=data)
    return r.text[2:]


def getPhone():
    url = 'http://api.duomi01.com/api'
    # phoneType=CMCC，CMCC是指移动，UNICOM是指联通，TELECOM是指电信
    # vno=1 表示指定只取虚拟运营商， vno=0 表示排除过滤虚拟运营商
    data = {'action': 'getPhone', 'sid': '11210', 'token': token, 'vno': 0}
    r = requests.get(url, headers=headers, data=data)
    time.sleep(3)
    print("手机号为："+ r.text[2:13])
    return r.text[2:13]


def getMa(token, phone):
    i = 1
    while(i > 0):
        url = 'http://api.duomi01.com/api'
        data = {'action': 'getMessage', 'sid': '11210', 'phone': phone, 'token': token}
        r = requests.get(url, headers=headers, data=data)
        if (r.text[2:].__len__() < 30):
            time.sleep(3)
        else:
            print(r.text)
            print("验证码为：" + r.text[32:38])
            i = 0
            return r.text[32:38]


def wandaLogin(token, phone):
    # 火狐浏览器
    # driver = webdriver.Firefox()
    pass


if __name__ == '__main__':
    token = getToken('http://api.duomi01.com/api/')
    phone = getPhone()
    # driver = webdriver.Chrome()
    driver = webdriver.Firefox()
    driver.get(r'https://m.wandacinemas.com/login')
    username = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[3]/div[2]/div[1]/input')
    username.send_keys(phone)
    click = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[3]/div[2]/div[2]/div/a')
    click.click()
    yzm1 = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[3]/div[2]/div[2]/input')
    yzm = getMa(token, phone)
    yzm1.send_keys(yzm)
    login = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[3]/a')
    login.click()

    time.sleep(6)

    city = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[3]/div[2]/div[1]/div[2]/div')
    city.click()

    time.sleep(3)

    wode = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[4]/div[4]/div[1]')
    wode.click()
    time.sleep(3)
    driver.execute_script("window.scrollBy(0,100)", "")  # 向下滚动200px
    qianbao = driver.find_elements_by_css_selector('#app > div > div._bpy8R > div._2M9B0 > div:nth-child(2) > div:nth-child(3) > div')
    qianbao.click()
    time.sleep(10)
    div = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[5]')
    print("大小"+div.size)