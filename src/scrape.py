from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import os

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")


# Path to your chromedriver
driver_path = r"C:\Users\bhaga\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

product_url = "https://www.flipkart.com/apple-ipad-10th-gen-64-gb-rom-10-9-inch-wi-fi-5g-silver/product-reviews/itmd486c16ac081f?pid=TABGJ6XU2NWAGKRH&lid=LSTTABGJ6XU2NWAGKRHJSNI3C&marketplace=FLIPKART"

driver.get(product_url)
time.sleep(5)

reviews_list = []
max_reviews = 110
page = 1

while len(reviews_list) < max_reviews:
    print(f"Fetching page {page} ...")

    try:
        review_blocks = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.cPHDOP.col-12-12"))
        )
    except:
        print("Timeout or no reviews loaded yet.")
        break

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    for block in review_blocks:
        try:
            reviewer_name = block.find_element(By.CSS_SELECTOR, "p._2NsDsF").text
        except:
            reviewer_name = ""
        try:
            rating = block.find_element(By.CSS_SELECTOR, "div.XQDdHH.Ga3i8K").text
        except:
            rating = ""
        try:
            review_text = block.find_element(By.CSS_SELECTOR, "div.ZmyHeo div").text
        except:
            review_text = ""
        try:
            date_location = block.find_element(By.CSS_SELECTOR, "p.MztJPv").text
        except:
            date_location = ""

        reviews_list.append({
            "Reviewer": reviewer_name,
            "Rating": rating,
            "Review": review_text,
            "Date/Location": date_location
        })

        if len(reviews_list) >= max_reviews:
            break

    try:
        next_btn = driver.find_element(By.CSS_SELECTOR, "a._1LKTO3")
        driver.execute_script("arguments[0].click();", next_btn)
        page += 1
        time.sleep(5) 
    except:
        print("No next page found → stopping")
        break

csv_file = r"C:\Users\bhaga\OneDrive\Desktop\flipkart_reviews.csv"
file_exists = os.path.isfile(csv_file)

keys = ["Reviewer", "Rating", "Review", "Date/Location"]

with open(csv_file, "a", newline="", encoding="utf-8") as f:
    dict_writer = csv.DictWriter(f, keys)
    if not file_exists:
        dict_writer.writeheader()
    dict_writer.writerows(reviews_list)

print(f"Done | Total reviews extracted this run: {len(reviews_list)}")
print(f"CSV updated at: {csv_file}")

driver.quit()
