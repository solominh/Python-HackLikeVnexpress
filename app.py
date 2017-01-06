
from selenium import webdriver
import time
# URL
url = 'http://vnexpress.net/tin-tuc/thoi-su/giao-thong/nan-nhan-tren-cao-toc-long-thanh-nhieu-nguoi-bi-hat-tung-3523359.html'
element_id = '19832024'  # Get second element of same id group
like_count = 3

# ACTION

for _ in range(like_count):
    driver = webdriver.Chrome()
    driver.get(url)
    element = driver.find_elements_by_id(element_id)[1]

    # Scroll to element
    driver.execute_script("return arguments[0].scrollIntoView();", element)
    driver.execute_script("window.scrollBy(0, -150);")

    time.sleep(2)
    element.click()
    time.sleep(2)
    driver.quit()
