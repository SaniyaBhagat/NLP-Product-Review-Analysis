# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import csv

# # ----------------------------
# # Setup Chrome
# # ----------------------------
# chrome_options = Options()


# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--disable-notifications")

# driver_path = "C:\\Users\\bhaga\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
# driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

# # ----------------------------
# # Flipkart product review URL
# # ----------------------------
# url = "https://www.flipkart.com/apple-ipad-10th-gen-64-gb-rom-10-9-inch-wi-fi-5g-silver/product-reviews/itmd486c16ac081f?pid=TABGJ6XU2NWAGKRH&lid=LSTTABGJ6XU2NWAGKRHJSNI3C&marketplace=FLIPKART"
# driver.get(url)

# # Close login popup if exists
# try:
#     close_login = WebDriverWait(driver, 5).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'✕')]"))
#     )
#     close_login.click()
# except:
#     pass

# # ----------------------------
# # Scrape reviews
# # ----------------------------
# reviews_list = []
# max_reviews = 105
# wait = WebDriverWait(driver, 10)

# while len(reviews_list) < max_reviews:
#     # Scroll down to load reviews
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)

#     try:
#         review_blocks = wait.until(
#             EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.col._2wzgFH"))
#         )
#     except:
#         print("Timeout or no reviews loaded yet, retrying...")
#         time.sleep(2)
#         continue

#     for review in review_blocks:
#         try:
#             rating = review.find_element(By.CSS_SELECTOR, "div._3LWZlK").text
#         except:
#             rating = ""
#         try:
#             title = review.find_element(By.CSS_SELECTOR, "p._2-N8zT").text
#         except:
#             title = ""
#         try:
#             comment = review.find_element(By.CSS_SELECTOR, "div.t-ZTKy div").text
#         except:
#             comment = ""
#         try:
#             user = review.find_element(By.CSS_SELECTOR, "p._2sc7ZR").text
#         except:
#             user = ""
#         try:
#             date = review.find_element(By.CSS_SELECTOR, "p._2sc7ZR ~ p").text
#         except:
#             date = ""

#         review_data = {
#             "User": user,
#             "Rating": rating,
#             "Title": title,
#             "Comment": comment,
#             "Date": date
#         }
#         if review_data not in reviews_list:
#             reviews_list.append(review_data)

#         if len(reviews_list) >= max_reviews:
#             break

#     # Click next page if exists
#     try:
#         next_button = driver.find_element(By.CSS_SELECTOR, "a._1LKTO3")
#         driver.execute_script("arguments[0].click();", next_button)
#         time.sleep(2)
#     except:
#         print("No next page found → stopping")
#         break

# # ----------------------------
# # Save CSV
# # ----------------------------
# csv_file = "C:\\Users\\bhaga\\OneDrive\\Desktop\\flipkart_reviews.csv"

# keys = reviews_list[0].keys() if reviews_list else ["User", "Rating", "Title", "Comment", "Date"]

# with open(csv_file, "w", newline="", encoding="utf-8") as f:
#     writer = csv.DictWriter(f, fieldnames=keys)
#     writer.writeheader()
#     writer.writerows(reviews_list)

# print(f"Done ✅ | Total reviews extracted: {len(reviews_list)}")
# print(f"CSV saved as: {csv_file}")

# driver.quit()

# # -----------------------------
# # Flipkart Review Scraper (Updated)
# # -----------------------------
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import csv

# # -----------------------------
# # Setup Chrome options
# # -----------------------------
# options = Options()
# options.add_argument("--start-maximized")
# options.add_argument("--disable-notifications")
# options.add_argument("--disable-infobars")
# options.add_argument("--disable-extensions")
# # options.add_argument("--headless=new")  # Keep visible to handle Flipkart popups

# # Path to your chromedriver
# driver_path = r"C:\Users\bhaga\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
# service = Service(driver_path)
# driver = webdriver.Chrome(service=service, options=options)

# # --------------------------
# # Flipkart product review URL
# # -----------------------------
# product_url = "https://www.flipkart.com/apple-ipad-10th-gen-64-gb-rom-10-9-inch-wi-fi-5g-silver/product-reviews/itmd486c16ac081f?pid=TABGJ6XU2NWAGKRH&lid=LSTTABGJ6XU2NWAGKRHJSNI3C&marketplace=FLIPKART"

# driver.get(product_url)
# time.sleep(5)  # wait for page to load completely

# reviews_list = []
# max_reviews = 110
# page = 1

# while len(reviews_list) < max_reviews:
#     print(f"Fetching page {page} ...")

#     try:
#         # Wait until review blocks are visible
#         review_blocks = WebDriverWait(driver, 10).until(
#             EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.cPHDOP.col-12-12"))
#         )
#     except:
#         print("Timeout or no reviews loaded yet.")
#         break

#     # Scroll to bottom to load lazy-loaded reviews
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)

#     for block in review_blocks:
#         try:
#             reviewer_name = block.find_element(By.CSS_SELECTOR, "p._2NsDsF").text
#         except:
#             reviewer_name = ""
#         try:
#             rating = block.find_element(By.CSS_SELECTOR, "div.XQDdHH.Ga3i8K").text
#         except:
#             rating = ""
#         try:
#             review_text = block.find_element(By.CSS_SELECTOR, "div.ZmyHeo div").text
#         except:
#             review_text = ""
#         try:
#             date_location = block.find_element(By.CSS_SELECTOR, "p.MztJPv").text
#         except:
#             date_location = ""

#         reviews_list.append({
#             "Reviewer": reviewer_name,
#             "Rating": rating,
#             "Review": review_text,
#             "Date/Location": date_location
#         })

#         if len(reviews_list) >= max_reviews:
#             break

#     # Try to go to next page
#     try:
#         next_btn = driver.find_element(By.CSS_SELECTOR, "a._1LKTO3")
#         driver.execute_script("arguments[0].click();", next_btn)
#         page += 1
#         time.sleep(5)  # wait for next page to load properly
#     except:
#         print("No next page found → stopping")
#         break

# # -----------------------------
# # Save reviews to CSV
# # -----------------------------
# csv_file = r"C:\Users\bhaga\OneDrive\Desktop\flipkart_reviews.csv"

# keys = reviews_list[0].keys() if reviews_list else ["Reviewer", "Rating", "Review", "Date/Location"]

# with open(csv_file, "w", newline="", encoding="utf-8") as f:
#     dict_writer = csv.DictWriter(f, keys)
#     dict_writer.writeheader()
#     dict_writer.writerows(reviews_list)

# print(f"Done ✅ | Total reviews extracted: {len(reviews_list)}")
# print(f"CSV saved as: {csv_file}")

# driver.quit()




# -----------------------------
# Flipkart Review Scraper (Append Mode)
# -----------------------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import os

# -----------------------------
# Setup Chrome options
# -----------------------------
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
# options.add_argument("--headless=new")  # Keep visible to handle Flipkart popups

# Path to your chromedriver
driver_path = r"C:\Users\bhaga\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

# -----------------------------
# Flipkart product review URL
# -----------------------------
product_url = "https://www.flipkart.com/apple-ipad-10th-gen-64-gb-rom-10-9-inch-wi-fi-5g-silver/product-reviews/itmd486c16ac081f?pid=TABGJ6XU2NWAGKRH&lid=LSTTABGJ6XU2NWAGKRHJSNI3C&marketplace=FLIPKART"

driver.get(product_url)
time.sleep(5)  # wait for page to load completely

reviews_list = []
max_reviews = 110
page = 1

while len(reviews_list) < max_reviews:
    print(f"Fetching page {page} ...")

    try:
        # Wait until review blocks are visible
        review_blocks = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.cPHDOP.col-12-12"))
        )
    except:
        print("Timeout or no reviews loaded yet.")
        break

    # Scroll to bottom to load lazy-loaded reviews
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

    # Try to go to next page
    try:
        next_btn = driver.find_element(By.CSS_SELECTOR, "a._1LKTO3")
        driver.execute_script("arguments[0].click();", next_btn)
        page += 1
        time.sleep(5)  # wait for next page to load properly
    except:
        print("No next page found → stopping")
        break

# -----------------------------
# Save reviews to CSV (Append if exists)
# -----------------------------
csv_file = r"C:\Users\bhaga\OneDrive\Desktop\flipkart_reviews.csv"
file_exists = os.path.isfile(csv_file)

keys = ["Reviewer", "Rating", "Review", "Date/Location"]

with open(csv_file, "a", newline="", encoding="utf-8") as f:
    dict_writer = csv.DictWriter(f, keys)
    if not file_exists:
        dict_writer.writeheader()
    dict_writer.writerows(reviews_list)

print(f"Done ✅ | Total reviews extracted this run: {len(reviews_list)}")
print(f"CSV updated at: {csv_file}")

driver.quit()
