# Import dependencies
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

#  Depending on your enviroment you may need to Accept cookies etc.
#  Here is a simple demonstration on how to deal with cookies window.
# cookies_button = driver.find_element(by=By.XPATH, value='//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button/span')
# cookies_button.click()

# Search for a particular location
location_search = driver.find_element(by=By.ID, value='searchboxinput')
location_search.send_keys('Národní park Šumava', Keys.ENTER)
time.sleep(5)


# Search for reviews
reviews_button = driver.find_element(by=By.XPATH, value='//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div/div/button[2]')
reviews_button.click()
time.sleep(5)


# SCROLLING DOWN THE REVIEWS CONTAINER AND SCRAPE THE REVIEWS
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

all_reviews = []
run = True
while run:
    # Find 'Další' buttons and click on them ('Další' means 'Next')
    more_buttons = driver.find_elements(by=By.CSS_SELECTOR, value="button.w8nwRe.kyuRq[aria-label='Zobrazit další']")
    for button in more_buttons:
        button.click()
    time.sleep(3) #3

    # Find reviews elements and loop through each review
    reviews = driver.find_elements(by=By.CLASS_NAME, value='wiI7pd')
    dates = driver.find_elements(by=By.CLASS_NAME, value='rsqaWe')
    stars = driver.find_elements(by=By.CSS_SELECTOR, value="span.kvMYJc[role='img']")
    for review, date, star in zip(reviews, dates, stars):
        #print(review.text, end='\n\n')
        review_item = [review.text.replace('\n', ' '), date.text, star.get_attribute("aria-label")]
        #all_reviews.append(review_item)
        if review_item not in all_reviews:
            all_reviews.append(review_item)

    time.sleep(3) #3

    # Scroll down to bottom
    element = driver.find_element(by=By.XPATH, value='//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]')
    driver.execute_script('arguments[0].scrollBy(0, 10000);', element)
    # Wait to load page
    time.sleep(5) #5

    print(f'Num. of reviews {len(all_reviews)}')

    print(f'Number of reviews {len(all_reviews)}')
    if len(all_reviews) > 5000:
        run = False

print(all_reviews)
print(len(all_reviews))
