# coding=utf-8
import os.path
from selenium import webdriver
import collections

StudentInfo = collections.namedtuple(
    'StudentInfo', 
    [
        'schoolName',
        'myName',
        'citizenNum'
    ]
)
MY_PATH = os.path.abspath(os.path.dirname(__file__))


def SearchSite(school, my, citizen):
    # url에 접근한다.
    if first != True:
        driver.execute_script('window.open("about:blank", "_blank");')
        driver.switch_to_window(driver.window_handles[-1])
    driver.get(site)

    #3초쯤 그냥 기다려 주자.
    driver.implicitly_wait(3)

    driver.find_element_by_xpath('//*[@title="학생정보 입력"]/div').click()

    #3초쯤 그냥 기다려 주자.
    driver.implicitly_wait(3)

    driver.find_element_by_xpath('//*[@id="btnSrchSchul"]').click()

    while len(driver.window_handles) == 1:
        driver.implicitly_wait(1)
    driver.switch_to_window(driver.window_handles[-1])
    driver.find_element_by_xpath('//*[@id="schulNm"]').send_keys(school)
    driver.find_element_by_xpath('//*[@id="infoForm"]/div[1]/p/span[3]/button').click()
    driver.find_element_by_xpath('//*[@id="infoForm"]/div[2]/table/tbody/tr/td[1]/a').click()

    driver.switch_to_window(driver.window_handles[-1])
    driver.find_element_by_name('pName').send_keys(' ' + my)
    driver.find_element_by_name('frnoRidno').send_keys(citizen)
    driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()

    #3초쯤 그냥 기다려 주자.
    driver.implicitly_wait(3)

    driver.find_element_by_xpath('//*[@id="infoForm"]/div/div/table[1]/tbody/tr[2]/td/span/label[1]').click()
    driver.find_element_by_xpath('//*[@id="infoForm"]/div/div/table[2]/tbody/tr[2]/td/span/label[1]').click()
    driver.find_element_by_xpath('//*[@id="infoForm"]/div/div/table[3]/tbody/tr[2]/td/span/label[1]').click()
    driver.find_element_by_xpath('//*[@id="infoForm"]/div/div/table[4]/tbody/tr[2]/td/span/label[1]').click()
    driver.find_element_by_xpath('//*[@id="infoForm"]/div/div/table[5]/tbody/tr[2]/td/span/label[1]').click()


def RemoveEnter(str):
    if(str[-1] == '\n'):
        return str[:-1]

path = os.path.join(MY_PATH, 'config.txt')
configfile = open(path,'r',encoding='UTF-8')
originalconfigs = [RemoveEnter(x) for x in configfile.readlines()]

site = originalconfigs[0]
webroute = originalconfigs[1]
browser = originalconfigs[2]
Students = []
for x in originalconfigs[3:]:
    y = x.split()
    Students.append(StudentInfo(schoolName = y[0], myName = y[1], citizenNum = y[2]))

if browser == "chrome":
    driver = webdriver.Chrome(webroute)
elif browser =="edge":
    driver = webdriver.Edge(webroute)
elif browser =="firefox":
    driver = webdriver.Firefox(executable_path=webroute)
elif browser =="safari":
    driver = webdriver.Safari(webroute)
first = True
for x in Students:
    SearchSite(x.schoolName, x.myName, x.citizenNum)
    first = False

x = input("작동이 끝났습니다. 끝내려면 Enter 키를 눌러주세요...")
