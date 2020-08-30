from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    # 需要安装chrome driver, 和浏览器版本保持一致
    # http://chromedriver.storage.googleapis.com/index.html

    browser.get('https://shimo.im/login?from=home')
    time.sleep(1)
    btm1 = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]')

    btm1.click()
    print(btm1)
    time.sleep(5)

    browser.find_element_by_xpath('//div[@class="input"]/input[@type="text"]').send_keys('15050211878')
    browser.find_element_by_xpath('//div[@class="input"]/input[@name="password"]').send_keys('001122aa')
    #li/a[@class="text-link"]
    time.sleep(1)
    browser.find_element_by_xpath('//button[@type="black"]').click()

    cookies = browser.get_cookies()  # 获取cookies
    print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)
finally:
    browser.close()
    