from selenium import webdriver

browser = webdriver.Chrome()
# browser = webdriver.Firefox()

# URL
url = 'http://vnexpress.net/tin-tuc/thoi-su/cong-ngan-trieu-bung-nap-o-sai-gon-co-dau-hieu-bi-cay-pha-3522886.html'
browser.get(url)

# Get second element of same id group
element = browser.find_element_by_xpath('//*[@id="19822386"][2]')
element.click()

