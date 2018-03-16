from selenium import webdriver
import time

driver = webdriver.Chrome('./driver/chromedriver.exe')
# driver.get('https://nid.naver.com/nidlogin.login')
# driver.find_element_by_css_selector('#id').send_keys('psymonkey13')
# driver.find_element_by_css_selector('#pw').send_keys('mong&4176')
# time.sleep(3)
# driver.find_element_by_css_selector('#frmNIDLogin').submit()

driver.get('https://section.cafe.naver.com/')
while True:
    try:
        driver.find_element_by_css_selector('a.btn_view').click()
    except Exception as e:
        break

cafe_list = driver.find_elements_by_css_selector('div.list_content > p.tit > a')
for cafe in cafe_list:
    print(cafe.text)

driver.quit()


