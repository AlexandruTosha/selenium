from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By



from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

class TestSuite():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver.get("https://www.w3schools.com/")
        time.sleep(4)
        yield
        #driver.close()
        #driver.quit()

    def test_case1(self, test_setup):
        driver.get("https://www.w3schools.com/")
        time.sleep(4)

    def test_case2(self, test_setup):
        driver.get("https://www.w3schools.com/")
        time.sleep(4)

        driver.find_element(By.XPATH, "//input[@id='search2']").send_keys("python")
        time.sleep(1)

        driver.find_element(By.XPATH, "//button[@id='learntocode_searchbtn']").click()
        time.sleep(4)

    def test_case3(self, test_setup):
        driver.get("https://www.w3schools.com/")
        time.sleep(4)

        driver.find_element(By.XPATH, "//input[@id='search2']").send_keys("python")
        time.sleep(1)

        driver.find_element(By.XPATH, "//button[@id='learntocode_searchbtn']").click()
        time.sleep(4)

        driver.find_element(By.XPATH, "//a[contains(text(),'Start learning Python now »')]").click()
        time.sleep(4)

    def test_case4(self):
        driver.get("https://www.w3schools.com/python/python_intro.asp")
        time.sleep(4)

        driver.find_element(By.XPATH, "//body/div[@id='belowtopnav']/div[1]/div[1]/div[2]/a[2]").click()
        time.sleep(4)

    def test_case5(self):
        driver.get("https://www.w3schools.com/python/python_getstarted.asp")
        time.sleep(4)

        driver.find_element(By.XPATH, "//body/div[@id='belowtopnav']/div[1]/div[1]/div[2]/a[2]").click()
        time.sleep(4)

    def test_case6(self):
        driver.get("https://www.w3schools.com/python/python_syntax.asp")
        time.sleep(4)

        driver.find_element(By.XPATH, "//body/div[@id='belowtopnav']/div[1]/div[1]/div[2]/a[2]").click()
        time.sleep(4)



    def test_case7(self):
        driver.get("https://www.w3schools.com/python/python_variables.asp")
        time.sleep(4)

        driver.find_element(By.XPATH, "//body/div[@id='belowtopnav']/div[1]/div[1]/div[2]/a[2]").click()
        time.sleep(4)



    def test_case8(self):
        driver.get("https://www.w3schools.com/python/python_variables_names.asp")
        time.sleep(4)

        driver.find_element(By.XPATH, "//body/div[@id='belowtopnav']/div[1]/div[1]/div[2]/a[2]").click()


    def test_case9(self):
        driver.get("https://www.w3schools.com/python/python_variables_multiple.asp")
        time.sleep(4)

        driver.find_element(By.XPATH, "//body/div[@id='belowtopnav']/div[1]/div[1]/div[2]/a[2]").click()
        time.sleep(4)


    def test_case10(self):
        driver.get("https://www.w3schools.com/python/python_variables_output.asp")
        time.sleep(4)

        driver.find_element(By.XPATH, "//body/div[@id='belowtopnav']/div[1]/div[1]/div[3]/a[1]").click()
        time.sleep(4)

        driver.close()
        driver.quit()
