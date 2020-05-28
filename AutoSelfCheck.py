# coding=utf-8
from selenium import webdriver

chromedriver = '/home/hyuck/chromedriver' # 리눅스
driver = webdriver.Chrome(chromedriver)

schoolName = '선인고등학교'
myName = '홍길동'
citizenNum = '123456'

# url에 접근한다.
driver.get('https://eduro.ice.go.kr/hcheck/index.jsp')

#3초쯤 그냥 기다려 주자.
driver.implicitly_wait(3)

driver.find_element_by_xpath('//*[@title="학생정보 입력"]/div').click()

#3초쯤 그냥 기다려 주자.
driver.implicitly_wait(3)

driver.find_element_by_xpath('//*[@id="btnSrchSchul"]').click()

while len(driver.window_handles) == 1:
    driver.implicitly_wait(1)
print(driver.window_handles)
driver.switch_to_window(driver.window_handles[1])
driver.find_element_by_xpath('//*[@id="schulNm"]').send_keys(schoolName)
driver.find_element_by_xpath('//*[@id="infoForm"]/div[1]/p/span[3]/button').click()
driver.find_element_by_xpath('//*[@id="infoForm"]/div[2]/table/tbody/tr/td[1]/a').click()

driver.switch_to_window(driver.window_handles[0])
driver.find_element_by_name('pName').send_keys(' ' + myName)
driver.find_element_by_name('frnoRidno').send_keys(citizenNum)
driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()

#3초쯤 그냥 기다려 주자.
driver.implicitly_wait(3)

driver.find_element_by_xpath('//*[@id="infoForm"]/div/div/table[1]/tbody/tr[2]/td/span/label[1]').click()
driver.find_element_by_xpath('//*[@id="infoForm"]/div/div/table[2]/tbody/tr[2]/td/span/label[1]').click()
driver.find_element_by_xpath('//*[@id="infoForm"]/div/div/table[3]/tbody/tr[2]/td/span/label[1]').click()
driver.find_element_by_xpath('//*[@id="infoForm"]/div/div/table[4]/tbody/tr[2]/td/span/label[1]').click()
driver.find_element_by_xpath('//*[@id="infoForm"]/div/div/table[5]/tbody/tr[2]/td/span/label[1]').click()
