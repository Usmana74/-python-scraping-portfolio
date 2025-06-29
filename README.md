🚀 python-scraping-portfolio
A collection of Python-based data extraction projects, including web scraping and PDF table extraction.
Built to demonstrate expertise in automating data collection, cleaning, and exporting to structured formats (CSV, JSON).

🔍 Projects in this portfolio
📚 books_scraper/
Scrapes book data (title, price, availability) from books.toscrape.com.

Outputs a clean books.csv file.

Tech stack: requests, BeautifulSoup, csv.

💼 jobs_scraper/
Extracts latest remote software job listings from remoteok.com.

Collects title, company, date posted, and link into jobs.json.

Tech stack: requests, BeautifulSoup, json.

🔍 google_search_scraper/
Uses SerpAPI to perform Google searches.

Collects top 10 organic results for a keyword and saves them in google_results.json.

Tech stack: requests, json, SerpAPI.

📝 pdf_grade_extractor/
Parses grade distribution tables from University of Wisconsin-Madison PDF reports.

Filters out:

Rows with "course totals" or "department totals"

Sections like “Summary by Level” or “University of Wisconsin-Madison”

Rows where Avg GPA = "***"

Outputs a structured grades.csv.

Tech stack: pdfplumber, pandas.
