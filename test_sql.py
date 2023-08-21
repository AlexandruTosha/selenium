from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By



from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

@pytest.fixture()
def test_setup(self):
    global driver
    driver.get("https://www.w3schools.com/sql/default.asp")
    time.sleep(4)
    yield
    #driver.close()
    #driver.quit()

def test_sql1():
    driver.get("https://www.w3schools.com/sql/default.asp")
    time.sleep(4)

def test_sql2():
    driver.get("https://www.w3schools.com/sql/default.asp")
    time.sleep(3)

def test_sql3():
    driver.get("https://www.w3schools.com/sql/sql_intro.asp")
    time.sleep(4)

    driver.find_element(By.XPATH, "//body/div[@id='belowtopnav']/div[1]/div[1]/div[2]/a[2]").click()
    time.sleep(3)

def test_sql4():
    driver.get("https://www.w3schools.com/sql/sql_syntax.asp")
    time.sleep(4)

    driver.find_element(By.XPATH, "//a[contains(text(),'Try it Yourself »')]").click()
    time.sleep(3)

def test_sql5():
    driver.get("https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all")
    time.sleep(5)

    driver.find_element(By.XPATH, "//button[contains(text(),'Run SQL »')]").click()
    time.sleep(3)

    driver.close()
    driver.quit()

