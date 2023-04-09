import time

from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://suninjuly.github.io/xpath_examples')
time.sleep(3)
# driver.find_element(By.XPATH, '//div[2]/button[3]').click()
# time.sleep(3)

# driver.find_element(By.XPATH, '/div[2]/button[@class="btn"][3]').click()
# time.sleep(3)
# driver.find_element(By.XPATH, '//div[2]/button[text()="Gold"]').click()
# time.sleep(3)
# driver.find_element(By.XPATH, "html/body/div/button[text()='Gold']").click()
# time.sleep(3)
# driver.close()



# 2.
# http://suninjuly.github.io/cats.html
# //p[contains(text(),'Fully charged cat')]
