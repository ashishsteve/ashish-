from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.devtools.v130.fed_cm import click_dialog_button

options = Options()
options.add_experimental_option("detach", True)
driver= webdriver.Edge(options=options)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
alllinks=driver.find_element(By.TAG_NAME,'a')
count=0

for link in alllinks:
    url=link.get_attribute('href')
    res= requests.head(url)
    if_res.status_code>=400:
       print(url,"is broken link")
       count+=1
