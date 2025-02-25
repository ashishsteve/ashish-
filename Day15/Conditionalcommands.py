from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver= webdriver.Edge(options=options)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
searchbox=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("Display status:",searchbox.is_displayed())
print("Enabled status:",searchbox.is_enabled())
rd_male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_female=driver.find_element(By.XPATH,"//input[@id='gender-female']")

print(rd_male.is_selected())
print(rd_female.is_selected())
