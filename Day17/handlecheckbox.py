from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Setup WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed

# Define URLs
demo_url = "http://demo.transcriptioncertificationinstitute.org/general-transcription-course"
live_url = "https://www.transcriptioncertificationinstitute.org/general-transcription-course"

# Function to extract content
def extract_content(url):
    driver.get(url)
    content = {
        "Headings": [h.text for h in driver.find_elements(By.TAG_NAME, "h1")],
        "Paragraphs": [p.text for p in driver.find_elements(By.TAG_NAME, "p")],
        "Links": [a.get_attribute("href") for a in driver.find_elements(By.TAG_NAME, "a") if a.get_attribute("href")]
    }
    return content

# Extract content from both websites
demo_content = extract_content(demo_url)
live_content = extract_content(live_url)

# Close the browser
driver.quit()

# Convert to DataFrame for easy comparison
df = pd.DataFrame({
    "Demo_Headings": pd.Series(demo_content["Headings"]),
    "Live_Headings": pd.Series(live_content["Headings"]),
    "Demo_Paragraphs": pd.Series(demo_content["Paragraphs"]),
    "Live_Paragraphs": pd.Series(live_content["Paragraphs"]),
    "Demo_Links": pd.Series(demo_content["Links"]),
    "Live_Links": pd.Series(live_content["Links"]),
})

# Save to Excel
excel_file = "website_comparison.xlsx"
df.to_excel(excel_file, index=False)

print(f"Comparison saved in {excel_file}")