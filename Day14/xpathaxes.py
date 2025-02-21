from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver= webdriver.Edge(options=options)


driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

driver.find_element(By.XPATH,"//a[normalize-space()='Godrej Industries Lt']").click()