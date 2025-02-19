from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver= webdriver.Edge(options=options)

driver.get("http://www.automationpractice.pl/index.php")
driver.maximize_window()
driver.find_element(By.XPATH,'/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]').send_keys('T-shirts')
driver.find_element(By.XPATH,'//*[@id="searchbox"]/button').click()

