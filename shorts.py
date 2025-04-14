from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
import time

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_argument("--log-level=3")

driver=webdriver.Chrome(options=chrome_options)
url_shorts=input("Write yours youtube url-short: ")
driver.get(f"{url_shorts}")

driver.find_element(By.XPATH,value='//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button/span').click()


while(1):
    try:

        if driver.find_element(By.XPATH,value='//*[@id="shorts-player"]').get_attribute("class").split(" ")[-3]=="ad-created":
            driver.find_element(By.XPATH,value='//*[@id="navigation-button-down"]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()
        else:
            time.sleep(0.009)
            width_time=driver.find_element(By.XPATH,value='//*[@id="scrubber"]/desktop-shorts-player-controls/div/yt-progress-bar/div/div/yt-progress-bar-line/div/div[4]').get_attribute("style").split(" ")[-1]
            width_time=float(width_time[:-2])
            print(width_time)
            if width_time>=97:
                driver.find_element(By.XPATH,value='//*[@id="navigation-button-down"]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()
                width_time=width_time=driver.find_element(By.XPATH,value='//*[@id="scrubber"]/desktop-shorts-player-controls/div/yt-progress-bar/div/div/yt-progress-bar-line/div/div[4]').get_attribute("style").split(" ")[-1]
    except StaleElementReferenceException:
        continue
    except NoSuchElementException:
        continue
        
        
