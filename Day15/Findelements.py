from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver= webdriver.Edge(options=options)
# Open the webpage
driver.get("https://demo.nopcommerce.com/login")  # Replace with your target website
emailbox=driver.find_element(By.XPATH,"//input[@id='Email']")
emailbox.clear()


