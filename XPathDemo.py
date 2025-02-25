from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import difflib

# Define website URLs
DEMO_URL = "http://demo.transcriptioncertificationinstitute.org/general-transcription-course"
LIVE_URL = "https://www.transcriptioncertificationinstitute.org/general-transcription-course"

# Setup Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run without opening browser
driver = webdriver.Chrome(options=options)

def get_page_content(url):
    """Fetch and return full page text, including FAQ dropdowns."""
    driver.get(url)
    time.sleep(3)  # Allow page to load

    # Click on FAQ sections (Assuming they have a common class 'faq-question')
    faq_buttons = driver.find_elements(By.CLASS_NAME, "faq-question")
    for btn in faq_buttons:
        try:
            btn.click()  # Expand FAQ
            time.sleep(1)  # Allow content to load
        except:
            pass  # If already expanded or error occurs, continue

    # Extract all visible text from the body
    page_text = driver.find_element(By.TAG_NAME, "body").text
    return page_text

# Get content from both websites
demo_content = get_page_content(DEMO_URL)
live_content = get_page_content(LIVE_URL)

# Close the WebDriver
driver.quit()

# Compare content line by line
diff = list(difflib.unified_diff(demo_content.splitlines(), live_content.splitlines(),
                                 fromfile="Demo", tofile="Live", lineterm=""))

# Prepare data for Excel report
comparison_data = []
demo_lines = demo_content.splitlines()
live_lines = live_content.splitlines()
max_len = max(len(demo_lines), len(live_lines))

for i in range(max_len):
    demo_text = demo_lines[i] if i < len(demo_lines) else ""
    live_text = live_lines[i] if i < len(live_lines) else ""
    status = "MATCH" if demo_text == live_text else "DIFFERENT"

    comparison_data.append([i+1, demo_text, live_text, status])

# Create a DataFrame
df = pd.DataFrame(comparison_data, columns=["Line No.", "Demo Content", "Live Content", "Status"])

# Save report to Excel
excel_filename = "website_comparison_report.xlsx"
df.to_excel(excel_filename, index=False)

print(f"Comparison report saved as: {excel_filename}")
