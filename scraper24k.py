from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
from selenium.webdriver.chrome.service import Service

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Run browser in headless mode
service = Service("/Users/mojtaba/Desktop/scrapershooli/chromedriver-mac-arm64/chromedriver")  # Update this path
driver = webdriver.Chrome(service=service, options=options)

# URL of the table
URL = "https://www.tgju.org/profile/geram24/history"

# Output CSV file
OUTPUT_FILE = "gold_prices.csv"

# Function to scrape a single page
def scrape_page():
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "table-list"))
    )  # Wait for the table body to load
    rows = table.find_elements(By.TAG_NAME, "tr")  # Find all rows in the table body

    data = []
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")  # Get all columns in the row
        data.append([col.text.strip() if col.text.strip() else "N/A" for col in cols])  # Extract text
    print(f"Scraped {len(data)} rows from the current page.")
    return data

# Main function to scrape all pages
def scrape_all_pages():
    driver.get(URL)
    all_data = []

    for page in range(1, 104):  # Scrape from page 1 to 103
        print(f"Scraping page {page}...")
        try:
            time.sleep(10)

            # Wait for the table to load on each page
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "table-list"))
            )
            
            # Scrape data from the current page
            page_data = scrape_page()
            all_data.extend(page_data)

            # Wait for 5 seconds to allow the page and "Next" button to load
            time.sleep(10)

            # Handle the "Next" button
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.paginate_button.next"))
            )
            # Scroll into view and click the "Next" button using JavaScript
            driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
            time.sleep(2)  # Allow scrolling
            driver.execute_script("arguments[0].click();", next_button)
            print(f"Clicked 'Next' button for page {page}.")
        except Exception as e:
            print(f"Error on page {page}: {e}")
            break

    return all_data

# Save data to CSV
def save_to_csv(data):
    with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Add headers based on the table columns
        writer.writerow(["Column1", "Column2", "Column3", "..."])  # Adjust as needed
        writer.writerows(data)

# Run the script
if __name__ == "__main__":
    try:
        print("Starting the scraping process...")
        scraped_data = scrape_all_pages()
        print(f"Scraped {len(scraped_data)} rows. Saving to CSV...")
        save_to_csv(scraped_data)
        print(f"Data saved to {OUTPUT_FILE}")
    finally:
        # driver.quit()
        print("done")
