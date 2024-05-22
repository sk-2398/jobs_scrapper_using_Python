# This project contains a Python script to scrape job listings from Working Nomads.

## Description

The script uses Selenium to scrape job listings, including job titles, company names, job locations, job types, salaries, and detailed job descriptions. It also extracts company details from the job description page.

## Installation

1. **Clone the Repository:**

   \`\`\`bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   \`\`\`

2. **Install Dependencies:**

   Make sure you have Python installed. Then install the required packages using pip:

   \`\`\`bash
   pip install selenium webdriver-manager
   \`\`\`

3. **Download ChromeDriver:**

   The script uses ChromeDriver for Selenium. It can be automatically managed by \`webdriver-manager\`.

## Usage

Run the script using Python:

\`\`\`bash
python job_scraper.py
\`\`\`

The script will print the scraped job listings in JSON format.

## Script Details

- \`get_job_listings(driver, url)\`: This function navigates to the job listings page and extracts job information.
- \`get_job_details(driver, url)\`: This function navigates to the job description page and extracts additional job and company details.
- \`main()\`: Sets up the WebDriver, calls \`get_job_listings\`, and prints the job listings.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details." > README.md
