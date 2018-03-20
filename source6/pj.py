from selenium import webdriver

driver = webdriver.PhantomJS('./driver/phantomjs.exe')
driver.set_window_size(1920, 1080)
driver.get('http://www.naver.com')
driver.get_screenshot_as_file('naver.com_pj.png')
driver.quit()


