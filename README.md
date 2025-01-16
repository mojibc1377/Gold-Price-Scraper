
# Gold Price Scraper

This project is a Python-based web scraper built using **Selenium** to extract historical 24K gold price data from [tgju.org](https://www.tgju.org). The script automates the process of navigating through 103 pages of gold price history and saves the scraped data into a CSV file.

---

## Features

- **Automated Scraping**: Extracts historical 24K gold price data page by page.
- **Handles Pagination**: Automatically navigates through all 103 pages.
- **Error Handling**: Robust error handling ensures the script doesn't fail unexpectedly.
- **Dynamic Content Support**: Uses Selenium to interact with JavaScript-driven content.
- **CSV Output**: Saves scraped data into a CSV file for further analysis.

---

## Prerequisites

### 1. Python
Ensure you have Python 3.6 or later installed. You can verify your Python version with:
```bash
python --version
```

### 2. Selenium
Install the Selenium library:
```bash
pip install selenium
```

### 3. Google Chrome and ChromeDriver
- Install the latest version of **Google Chrome**.
- Download the matching version of **ChromeDriver** for your Chrome browser from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads).
- Place the `chromedriver` executable in the project directory or a location in your system's PATH.

### 4. Install Additional Dependencies
You can install all dependencies at once using:
```bash
pip install -r requirements.txt
```

(If you want, create a `requirements.txt` file with `selenium` listed.)

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/gold-price-scraper.git
cd gold-price-scraper
```

2. Create a Python virtual environment (optional but recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

3. Install dependencies:
```bash
pip install selenium
```

4. Place the `chromedriver` executable in the project directory or ensure it’s accessible via the system PATH.

---

## Usage

1. **Run the Scraper**:
   Execute the script using:
   ```bash
   python scraper.py
   ```

2. **Output**:
   - The script will navigate through all 103 pages of historical gold prices.
   - The extracted data will be saved into a file named `gold_prices.csv` in the same directory.

3. **CSV File Format**:
   The resulting CSV file will contain rows of data scraped from the table, with each row corresponding to a price record.

---

## Code Overview

### Key Components
- **`scrape_page()`**:
  - Scrapes data from the current page by locating the gold price table and extracting text from rows and columns.
- **`scrape_all_pages()`**:
  - Handles navigation across all pages using the "Next" button and manages the scraping process for each page.
- **`save_to_csv()`**:
  - Saves the scraped data into a CSV file with customizable headers.

### Highlights
- **Dynamic Content Handling**:
  - The script uses `WebDriverWait` to ensure that elements like tables and buttons are fully loaded before interacting with them.
- **Pagination**:
  - Handles the "Next" button dynamically and avoids stale element reference errors by re-locating elements on each page.
- **Error Handling**:
  - Gracefully handles timeouts, missing elements, or navigation failures.

---

## Project Structure

```
gold-price-scraper/
├── scraper.py           # Main script to scrape data
├── gold_prices.csv      # Output file with scraped data (created after running the script)
├── requirements.txt     # Optional: Dependency list for easy setup
└── README.md            # Project documentation
```

---

## Sample Output

Here’s a sample of what the `gold_prices.csv` file might look like:

| Date       | Price     | Other Columns |
|------------|-----------|---------------|
| 2025-01-01 | 1,293,563 | ...           |
| 2025-01-02 | 1,285,453 | ...           |

---

## Troubleshooting

### Common Issues
1. **ChromeDriver Version Mismatch**:
   Ensure the ChromeDriver version matches your installed Chrome browser version. Check your Chrome version at `chrome://settings/help` and download the correct ChromeDriver.

2. **Element Click Intercepted**:
   This issue occurs when another element overlaps the "Next" button. The script handles this by scrolling the button into view and clicking it via JavaScript.

3. **Stale Element Reference**:
   The script re-locates elements on each page load to avoid this error.

### Debugging Tips
- Run the script without headless mode to visually debug:
  ```python
  # Comment out this line in the script:
  # options.add_argument("--headless")
  ```

- Print the page source to inspect the table or button:
  ```python
  print(driver.page_source)
  ```

---

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request for:
- Adding new features.
- Fixing bugs.
- Improving documentation.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgements

- **Selenium**: For enabling interaction with dynamic web content.
- **tgju.org**: For providing the gold price data used in this project.
