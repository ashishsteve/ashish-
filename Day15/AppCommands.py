from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver= webdriver.Edge(options=options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print(driver.title)
print(driver.current_url)

print(driver.page_source)
driver.quit()