#7.1. Найдите кпопку c текстом "Gold". Попробуйте подобрать
# как минимум 2 разных XPATH и/или CSS-селекторов
#http://suninjuly.github.io/xpath_examples
#ctrl + f

# 1XPATH
#//*[contains(text(), 'Gold')] #find in whole text by word
# 2XPATH
#/html/body/div[2]/button[3]

#CSS
#body > div:nth-child(2) > button:nth-child(3)
#//button[text()='Gold']

#7.2. Найдите элемент с текстом "Fully charged cat". Чем больше разных XPATH и/или CSS-селекторов сможете подобрать, тем лучше
#http://suninjuly.github.io/cats.html

# 1XPATH
#//*[contains(text(), 'Fully charged cat')]

# 2XPATH


#CSS
#body > main > div > div > div > div:nth-child(5) > div > div > p

"""from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.by import By

URL = 'https://openweathermap.org/'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url


def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url


def test_fill_search_city_field():
    driver.get('https://openweathermap.org/')
    search_city_field = driver.find_element(By.XPATH, "//div[@id='weather-widget']//input")
    search_city_field.send_keys('New York')


def test_fill_search_city_field2():
    driver.get('https://openweathermap.org/')
    search_city_field2 = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_city_field2.send_keys('London')
    time.sleep(10)"""






