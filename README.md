# Competitor Price Monitoring System — Playwright + OpenPyXL

A Python web scraper that tracks product prices, ratings, and reviews across paginated e-commerce listings, exporting results to a dated Excel file — built for competitor price monitoring use cases.

## What it does

- Scrapes a paginated product listing page (laptops category on a public e-commerce test site)
- Extracts for each product: **Title, Price, Rating (out of 5), Number of Reviews**
- Automatically moves through all pages of listings until no more products are found
- Saves results into an Excel file named with today's date (e.g. `laptop_prices_2026-07-27.xlsx`) — running the script again on a different day produces a new dated file, making it easy to compare prices over time
- Handles errors gracefully — if one product fails to load correctly, the script logs it and continues instead of crashing
- Includes a polite delay between page requests to avoid overloading the target site

## Tech stack

- [Playwright](https://playwright.dev/python/) — browser automation
- [OpenPyXL](https://openpyxl.readthedocs.io/) — Excel file generation

## How to run it

1. Clone this repo
2. Install dependencies:
3. Run the script:
4. The output file (`laptop_prices_<date>.xlsx`) will be saved to your Desktop.

## Sample Output

![Sample output](Output.png)

## Notes

This project was built against a public site designed for scraping practice. The same approach — paginated extraction, structured data, dated exports — applies directly to real-world competitor price monitoring, stock tracking, or catalog auditing for e-commerce businesses.
