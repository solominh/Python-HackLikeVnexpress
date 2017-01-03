from selenium import webdriver

# BROWSER

# browser = webdriver.Firefox()

# URL
url = 'http://vnexpress.net/tin-tuc/thoi-su/cong-ngan-trieu-bung-nap-o-sai-gon-co-dau-hieu-bi-cay-pha-3522886.html'
element_id='//*[@id="19822386"][2]'  # Get second element of same id group
like_count=3

# ACTION

for _ in range(like_count):
    driver = webdriver.Chrome()
    driver.get(url)
    element = driver.find_element_by_xpath(element_id)
    element.click()
    driver.quit()

