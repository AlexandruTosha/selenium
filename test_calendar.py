import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By




from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

# Handle pop up calendar in forms


def test_case1():
    driver.get("https://demoqa.com/automation-practice-form")
    time.sleep(6)
    driver.find_element(By.XPATH, "//input[@id='dateOfBirthInput']").click()
    time.sleep(3)
    #driver.find_element(By.XPATH, "//div[contains(text(),'17')]").click()
    #time.sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(),'Previous Month')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(text(),'Previous Month')]").click()
    time.sleep(3)


