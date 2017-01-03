
from selenium import webdriver

# URL
url = 'http://vnexpress.net/tin-tuc/thoi-su/cong-ngan-trieu-bung-nap-o-sai-gon-co-dau-hieu-bi-cay-pha-3522886.html'
element_id = '19822386'  # Get second element of same id group
like_count = 3

# ACTION

for _ in range(like_count):
    driver = webdriver.Chrome()
    driver.get(url)
    element = driver. element = driver.find_elements_by_id(element_id)[1]
    element.click()
    driver.quit()
