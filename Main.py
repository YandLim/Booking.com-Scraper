#Importing Module
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import re


def main_function(user_input):
    #Starting the program
    try:
        #Openning the Browser
        PATH = r"C:\Program Files (x86)\chromedriver.exe"
        service = Service(PATH)
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.booking.com/index.id.html?label=gen173nr-1BCAEoggI46AdIM1gEaGiIAQGYARK4ARfIAQzYAQHoAQGIAgGoAgO4AtCx8boGwAIB0gIkOTY1NDgxZTMtZTMzOC00YWRhLWI1ZTgtN2VlMzNiMWU0MWU42AIF4AIB&sid=f39d648b0983480e3b2cd7f0f8eefbbf&keep_landing=1&sb_price_type=total&")

        #Find the search box
        search = driver.find_element(By.CLASS_NAME, "eb46370fe1")

        #Dismiss the login page
        wait = WebDriverWait(driver, 20)
        try:
            close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Tutup informasi login.']")))
            close_button.click()
            time.sleep(10)
            
        except Exception as e:
            print(f"An error occurred: {e}")


        #Entering user input into search box without error
        element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "eb46370fe1")))
        element.send_keys(user_input)
        time.sleep(5)
        element.send_keys(Keys.RETURN)

        items_found = []

        #Dismiss the login page
        try:
            close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Tutup informasi login.']")))
            close_button.click()
            time.sleep(10)
            
        except Exception as e:
            print(f"An error occurred: {e}")


        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "d4924c9e74")))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".a3b8729ab1.d86cee9b25")))


        #Collecting the data
        while True:
            main_page = driver.find_elements(By.CSS_SELECTOR, "[role='listitem']")
            for hotel in main_page:
                linked = hotel.find_element(By.CLASS_NAME, "aab71f8e4e")
                anchor = linked.find_element(By.TAG_NAME, "a")
                link = anchor.get_attribute("href")
                name = hotel.find_element(By.CSS_SELECTOR, "[class*='f6431b446c']").text

                try:
                    rate_num = hotel.find_element(By.CSS_SELECTOR, ".a3b8729ab1.d86cee9b25").text[5:8]
                    rate_amount = hotel.find_element(By.CSS_SELECTOR, "[class*='f45d8e4c32']").text.rstrip()

                    rate_amount = re.search(r'[\d.]+', rate_amount)
                    if rate_amount:
                        rate_amount = rate_amount.group()

                    rate = f"{rate_num}({rate_amount})"

                except Exception as e:
                    rate = "Not Found"


                if link not in items_found:
                    items_found.append({
                        "Name": name,
                        "Rate": rate,
                        "Link": link
                    })
            break

        #store data to csv
        df = pd.DataFrame(items_found)
        df.to_csv(f"Booking.com {user_input} List.csv", index=False)

        driver.quit()

        output = ("The Scraping done without an error")
        saved = f"The scraping has been save with the name Booking.com {user_input}.csv\n"
        if output == None:
            output = f"Something is wrong \nwith {user_input} Scraping Procces"
            saved = ""
        return output, saved

    except Exception as e:
        output = print(f"An error occurred: {e}\n-----------------------------------------\nAn error occurred")
        saved = ""
        print(e)
        return output, saved

    if __name__ == "__main__":
        pass

