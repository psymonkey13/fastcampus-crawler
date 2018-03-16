from selenium import webdriver

driver = webdriver.Chrome('./driver/chromedriver.exe')
driver.get('https://mbasic.facebook.com/login')

driver.find_element_by_css_selector('#m_login_email').send_keys('psymonkey13@naver.com')
driver.find_element_by_css_selector('input[name="pass"').send_keys('mong&4176')
driver.find_element_by_css_selector('form').submit()

driver.get('https://mbasic.facebook.com/groups/pythonwebcrawling/')
for _ in range(10):
    posts = driver.find_elements_by_css_selector('div[role="article"]')
    for post in posts:
        title = post.find_element_by_css_selector('h3')
        contents = post.find_elements_by_css_selector('div > span > p')
        content = ''

        for con in contents:
            content += con.text.strip()

        if not content:
            continue

        print('제목 : ', title.text)
        print('내용 : ', content.strip())

    try:
        driver.find_element_by_css_selector('#m_group_stories_container > div:nth-child(2) > a').click()
    except Exception as e:
        break

    print('============' * 10)


driver.quit()

# a.href[]

