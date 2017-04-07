"""
__title__ = ''
__author__ = 'LCHOICEzz'
__mtime__ = '2017-3-15'
__email__ = ''
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
'''driver=webdriver.PhantomJS(executable_path='E:\\python开发\\bin\\phantomjs.exe')#建立phantomjs驱动)
driver.set_window_size(800, 600)
login_url="https://gwucs.org/mail/"
wait=ui.WebDriverWait(driver,10)
'''
useraccount=[
    'michaeldemmer@gwucs.org',
    'margaretgraham@gwucs.org',
    'vickimanuel@gwucs.org',
    'annahuttar@gwucs.org',
    'angelkennedy@gwucs.org',
    'randallmask@gwucs.org',
    'karenmoran@gwucs.org',
    'richardbyun@gwucs.org',
    'terrypieper@gwucs.org',
    'lindsayellington@gwucs.org',
    'clarencenorman@gwucs.org',
    'lesliearmstrong@gwucs.org',
    'stevenalexander@gwucs.org',
    'francesshambo@gwucs.org',
    'leroygrove@gwucs.org',
    'jeffreylicursi@gwucs.org',
    'lisaveitch@gwucs.org',
    'davidbryan@gwucs.org',
    'maryruscio@gwucs.org',
    'orlandosnyder@gwucs.org',
    'randyridenour@gwucs.org'
    ]
def LoginGEmail(user):#登陆到邮箱中
    driver.get(login_url)
    time.sleep(2)
    username= wait.until(EC.visibility_of_element_located((By.ID, 'rcmloginuser')))
    username.clear()
    username.send_keys(user)
    passwd = wait.until(EC.visibility_of_element_located((By.ID,'rcmloginpwd')))
    passwd.clear()
    passwd.send_keys(u'123456')
    passwd.send_keys(Keys.ENTER)

def findUnreadMessage():#定位unread message
    el3 = []
    el4 = []
    el3 = driver.find_elements_by_xpath("//*[@class='message unread']/td[2]/a")
    el4 = driver.find_elements_by_xpath("//*[@class='message unread focused']/td[2]/a")
    if not el3:
        print("message unread为空")
    else:
        for i in range(len(el3)):
            Transfer_url.append(el3[i].get_attribute('href'))
    if not el4:
        print("message unread focused为空")
    else:
        for i in range(len(el4)):
            Transfer_url.append(el4[i].get_attribute('href'))
    return Transfer_url#返回某个账户里全部需要转发邮件的页面

def Transmist(Transfer_url):#转发邮件
    for i,transfer_url in enumerate(Transfer_url):
        print('第'+str(i+1)+'个未读邮件地址为：'+transfer_url)
        driver.get(transfer_url)
        wait.until(lambda driver:driver.find_element_by_xpath(r'//*[@id="rcmbtn110"]'))
        print('第'+str(i+1)+'个未读邮件目前地址为'+driver.current_url)
        driver.find_element_by_xpath('//*[@id="rcmbtn110"]').click()
        wait.until(lambda driver:driver.find_element_by_xpath(r'//*[@id="rcmbtn118"]'))
        print('点击完转发按钮后目前的网页地址'+driver.current_url)
        try:
            RecAdd=wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='compose-headers']/tbody/tr[2]/td[2]/textarea")))
        except:
            driver.get_screenshot_as_file("C:\\Users\\zou\\Desktop\\ScreenShot.png")
        RecAdd.clear()
        RecAdd.send_keys(u'rufuslamb@gwucs.org')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="rcmbtn118"]').click()
        time.sleep(2)
        print('第'+str(i+1)+'个未读邮件已转发完毕')



if __name__ == '__main__':
    for i, user in enumerate(useraccount):
        print('这是第' + str(i) + '个账户')
        driver = webdriver.PhantomJS(executable_path='E:\\python开发\\bin\\phantomjs.exe')  # 建立phantomjs驱动)
        driver.set_window_size(1124, 850)
        login_url = "https://gwucs.org/mail/"
        wait = ui.WebDriverWait(driver, 10)
        LoginGEmail(user)
        print(user+"成功登录")
        Transfer_url = []
        Transfer_url = findUnreadMessage()
        if Transfer_url:
            Transmist(Transfer_url)
        else:
            print(user + '账户里面没有收到新邮件')
        driver.quit()
    print("全部账户中的转发工作结束")








