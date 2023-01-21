from selenium import webdriver

driver = webdriver.Chrome(r"chromedriver")
websiteName="https://github.com/"
driver.get(websiteName)
print(driver.title)
driver.close()
