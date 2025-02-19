from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver= webdriver.Edge(options=options)

driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"inputtext").send_keys("abc@gmail.com")



# Close the browser
#driver.quit()
