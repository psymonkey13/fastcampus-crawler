from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')

driver = webdriver.Chrome('./driver/chromedriver.exe', chrome_options=options)
driver.get('http://www.naver.com')
driver.save_screenshot('naver.png')
driver.quit()