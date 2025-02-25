from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver= webdriver.Edge(options=options)

from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver (Change path to your WebDriver)
driver = webdriver.Chrome()

# Open the website
url = "https://www.mohawkinsurance.com/about"  # Replace with the target website
driver.get(url)

# Get the entire page source
page_source = driver.page_source

# Word to search for
word = " Spencer Shepperly "

# Check if the word exists in the page source
if word in page_source:
    print(f"'{Spencer Shepperly }' found on the webpage!")
else:
    print(f"'{Spencer Shepperly }' NOT found on the webpage!")

# Close the browser
driver.quit()
