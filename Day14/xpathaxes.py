from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.devtools.v130.fed_cm import click_dialog_button

options = Options()
options.add_experimental_option("detach", True)
driver= webdriver.Edge(options=options)

driver.get("https://www.google.com/")
driver.maximize_window()

searchbox=driver.find_element(By.NAME,'q')

searchbox.send_keys("Selenium")
searchbox.submit()

driver.find_element(By.XPATH,'//h3[normalize-space()='Selenium']')