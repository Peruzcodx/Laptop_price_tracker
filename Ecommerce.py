# Competitor Price Monitoring System
# Scrapes laptop listings (title, price, rating, reviews) from a public
# e-commerce test site, paginated, and saves results to a dated Excel file.

from playwright.sync_api import sync_playwright
import openpyxl
import os
from datetime import date

BASE_URL = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

wb = openpyxl.Workbook()
ws = wb.active
ws.append(["Title", "Price", "Rating (out of 5)", "Reviews"])

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page_num = 1
    while True:
        url = f"{BASE_URL}?page={page_num}" if page_num > 1 else BASE_URL
        page.goto(url)
        page.wait_for_selector(".product-wrapper")

        products = page.locator(".product-wrapper").all()
        if len(products) == 0:
            print("No more products. Done.")
            break

        for product in products:
            try:
                title = product.locator("a.title").get_attribute("title")
                price = product.locator("h4.price").inner_text()
                rating = product.locator("[data-rating]").get_attribute("data-rating")
                reviews = product.locator("p.review-count").inner_text()

                ws.append([title, price, rating, reviews])
                print(f"Saved: {title}")
            except Exception as e:
                print(f"Error on one product: {e}")

        page.wait_for_timeout(1000)  # polite delay between pages
        page_num += 1

        if page_num > 10:  # safety cap, this category has limited pages
            break

    browser.close()

today = date.today().isoformat()
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", f"laptop_prices_{today}.xlsx")
wb.save(desktop_path)
print(f"Saved to: {desktop_path}")