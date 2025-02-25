from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver= webdriver.Edge(options=options)
# Initialize the WebDriver (ensure chromedriver is in PATH)
driver = webdriver.Chrome()

# Open the target URL
driver.get("https://thriveptks.openviowebsites.com/")

# Get all anchor tags
links = driver.find_elements(By.TAG_NAME, "a")

broken_links = []

for link in links:
    url = link.get_attribute("href")
    if url is None or url.strip() == "":
        continue  # Skip if href is empty
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        if response.status_code >= 400:
            print(f"Broken link: {url} - Status Code: {response.status_code}")
            broken_links.append((url, response.status_code))
        else:
            print(f"Valid link: {url} - Status Code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error checking link: {url} - Exception: {e}")
        broken_links.append((url, str(e)))

print("\nSummary of broken links:")
for url, status in broken_links:
    print(f"{url} returned {status}")

# Clean up: close the browser
driver.quit()
