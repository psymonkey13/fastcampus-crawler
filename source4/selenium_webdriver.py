from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./driver/chromedriver.exe')
driver.get('http://www.naver.com')

# html = driver.page_source
# driver.quit()
#
# soup = BeautifulSoup(html, 'lxml')
# words = soup.select('span.ah_k')
#
# for item in words:
#     print(item.text)
#

# first_word = driver.find_element_by_css_selector('span.ah_k')
# print(first_word)
# driver.quit()

new_word = driver.find_elements_by_css_selector('span.an_txt')
for word in new_word:
    print(word.text)

driver.quit()
