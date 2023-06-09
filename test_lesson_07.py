import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def test_open_page(driver):
    assert 'openweathermap' in driver.current_url
    print(driver.current_url)


def test_check_page_title(driver):
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


def test_fill_search_city_field(driver):
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_city_field.send_keys('New York')
    time.sleep(10)
    search_button = driver.find_element(By.CSS_SELECTOR, "button[class ='button-round dark']")
    search_button.click()
    driver.implicitly_wait(10)
    search_option = driver.find_element(By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')
    search_option.click()
    time.sleep(5)
    expected_city = 'New York City, US'
    displayed_city = driver.find_element(By.CSS_SELECTOR, '.grid-container.grid-4-5 h2')
    displayed_city_text = displayed_city.text
    print(displayed_city_text)
    assert displayed_city_text == expected_city
