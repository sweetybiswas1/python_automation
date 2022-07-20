import selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

PATH = "/home/cbnits/Desktop/chromedriver_linux64/chromedriver"

driver = webdriver.Chrome(PATH)
driver.get('http://www.flipkart.com/')
# print(driver.title) #title of the page

# log_in = driver.find_element_by_class_name("_1_3w1Nc")
# log_in.click()
# driver.find_element(By.CLASS_NAME, " _1_3w1Nc")
driver.find_element(By.XPATH,)
email = driver.find_element(By.XPATH,"")
email.send_keys("6290445177")
    
password = driver.find_element(By.XPATH,)
password.send_keys("Sayan#7278")
logged = driver.find_element(By.XPATH,)
logged.submit()



# driver.fin

# search.send_keys("mobile")
# search.send_keys(Keys.RETURN)
# log_in.click()
time.sleep(30)

