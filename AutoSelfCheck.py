# coding=utf-8
from selenium import webdriver

chromedriver = '/home/hyuck/chromedriver' # 리눅스
driver = webdriver.Chrome(chromedriver)


# url에 접근한다.
driver.get('https://eduro.ice.go.kr/hcheck/index.jsp')

#3초쯤 그냥 기다려 주자.
driver.implicitly_wait(3)

driver.find_element_by_xpath('//*[@title="학생정보 입력"]/div').click()

#3초쯤 그냥 기다려 주자.
driver.implicitly_wait(3)

driver.find_element_by_name('schulNm').send_keys('선인' + 'ㄱ')

while len(driver.window_handles) == 1:
    driver.implicitly_wait(1)
print(driver.window_handles)
driver.switch_to_window(driver.window_handles[1])
driver.find_element_by_xpath("//*[contains(text(), '선인고등학교')]").click()

driver.switch_to_window(driver.window_handles[0])
driver.find_element_by_name('pName').send_keys(' 홍길동')
driver.find_element_by_name('frnoRidno').send_keys('123456')
driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()

#3초쯤 그냥 기다려 주자.
driver.implicitly_wait(3)

driver.find_element_by_xpath('//*[@id="infoForm"]/div/div/table[1]/tbody/tr[2]/td/span/label[1]').click()
driver.find_element_by_xpath('//*[@id="infoForm"]/div/div/table[2]/tbody/tr[2]/td/span/label[1]').click()
driver.find_element_by_xpath('//*[@id="infoForm"]/div/div/table[3]/tbody/tr[2]/td/span/label[1]').click()
driver.find_element_by_xpath('//*[@id="infoForm"]/div/div/table[4]/tbody/tr[2]/td/span/label[1]').click()
driver.find_element_by_xpath('//*[@id="infoForm"]/div/div/table[5]/tbody/tr[2]/td/span/label[1]').click()
