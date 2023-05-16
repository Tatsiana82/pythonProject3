import time

from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

URL = 'https://openweathermap.org/'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


"""def test_open_page():
    driver.get('https://openweathermap.org/')
    assert 'openweathermap' in driver.current_url
    print(driver.current_url)


def test_open_page2(): #check word guide in url my test
    driver.get('https://openweathermap.org/guide')
    assert 'guide' in driver.current_url
    print(driver.current_url)"""



def test_fill_search_city_field():
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder = 'Search city']")
    search_city_field.send_keys('New York')
    time.sleep(10)
    search_button = driver.find_element(By.CSS_SELECTOR, "button[class = 'button-round dark']")
    search_button.click()
    search_option = driver.find_element(By.CSS_SELECTOR, "ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)")


#def test_check_title_guide():
#   assert driver.title_guide == 'OpenWeatherMap API guide - OpenWeatherMap'"""


#def test_check_title():
 #   assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'

"""import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

URL = 'https://openweathermap.org/'"""

"""def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url


def test_search_Dashboard(driver):
    driver.get('https://openweathermap.org/')
    time.sleep(5)

    search_field = driver.find_element(By.XPATH, "//*[contains(text(), 'Dashboard')]")
    print(search_field.text)


def test_open_page2(driver):
    driver.get('https://openweathermap.org/guide')
    time.sleep(5)
    assert 'guide' in driver.current_url
    print(driver.current_url)"""

"""def test_fill_search_city_field(driver):
    driver.get('https://openweathermap.org/')
    search_city_field = driver.find_element(By.XPATH, "//div[@id='weather-widget']//input")
    search_city_field.send_keys('New York')
    search_button = driver.find_element(By.CSS_SELECTOR, "button[class = 'button-round dark']")
    search_button.click()
    search_option = driver.find_element(By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')
    search_option.click()
    time.sleep(5)
    expected_city = 'New York'
    displayed_city = driver.find_element(By.CSS_SELECTOR, '.grid-container.grid-4-5 h2')
    displayed_city_text = displayed_city.text
    assert displayed_city_text == expected_city"""

