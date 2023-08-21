from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

@pytest.fixture()
def test_setup(self):
    global driver
    driver.get("https://demoqa.com/elements")
    time.sleep(4)
    yield
    #driver.close()
    #driver.quit()


def test_elements1():
    driver.get("https://demoqa.com/elements")
    time.sleep(5)


def test_elements2():
    driver.get("https://demoqa.com/text-box")
    time.sleep(5)
    driver.find_element(By.XPATH, "//input[@id='userName']").send_keys("Bandit Papito")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("papito@gmail.com")
    time.sleep(2)
    driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys("1840 Huntington Blvd., Chicago, IL")
    time.sleep(2)
    driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys("Same as current")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, window.scrollY + 400)")
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[@id='submit']").click()
    time.sleep(5)


def test_elements3():
    driver.get("https://demoqa.com/checkbox")
    time.sleep(3)
    driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/button[1]/*[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/ol[1]/li[1]/ol[1]/li[1]/span[1]/button[1]/*[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/ol[1]/li[1]/ol[1]/li[2]/ol[1]/li[1]/span[1]/label[1]/span[1]/*[1]").click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, window.scrollY + 400)")
    time.sleep(5)
    driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/ol[1]/li[1]/ol[1]/li[3]/span[1]/label[1]/span[1]/*[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/ol[1]/li[1]/ol[1]/li[3]/span[1]/button[1]/*[1]").click()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, window.scrollY - 400)")
    time.sleep(5)
    driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/ol[1]/li[1]/span[1]/button[1]/*[1]").click()
    time.sleep(3)


def test_elements4():
    driver.get("https://demoqa.com/radio-button")
    time.sleep(3)
    driver.find_element(By.XPATH, "//label[contains(text(),'Yes')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//label[contains(text(),'Impressive')]").click()
    time.sleep(2)


def test_elements5():
    driver.get("https://demoqa.com/webtables")
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@id='addNewRecordButton']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("Bandit")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("Papito")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("papito@gmail.com")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='age']").send_keys("2")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='salary']").send_keys("25")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='department']").send_keys("Security")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@id='submit']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='searchBox']").send_keys("Bandit")
    time.sleep(2)


def test_elements6():
    # Double Click, Right Click
    driver.get("https://demoqa.com/buttons")
    time.sleep(3)

    doubleclick = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
    action = ActionChains(driver)
    action.double_click(on_element=doubleclick)
    action.perform()
    time.sleep(3)

    rightclick = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
    action = ActionChains(driver)
    action.context_click(on_element=rightclick)
    action.perform()
    time.sleep(3)

    #driver.find_element(By.XPATH, "//button[@id='W6HoP']").click()
    #time.sleep(3)

def test_elements7():
    driver.get("https://demoqa.com/links")
    time.sleep(3)

    parentwindow = driver.current_window_handle
    print("Parent window name", parentwindow)

    driver.find_element(By.XPATH, "//a[@id='simpleLink']").click()
    time.sleep(3)

    childwindow = driver.window_handles
    print("Type of windows", type(childwindow))

    for child in childwindow:
        print(child)
        if parentwindow != child:
            driver.switch_to.window(child)


# Expect to fail 1-2 ? :)


def test_elements8():
    driver.get("https://demoqa.com/upload-download")
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[@id='downloadButton']").click()
    time.sleep(3)


def test_elements9():
    driver.get("https://demoqa.com/automation-practice-form")
    time.sleep(4)
    driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
    time.sleep(4)
    driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("Bandit")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("Papito")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("papito@gmail.com")
    time.sleep(3)
    driver.find_element(By.XPATH, "//label[contains(text(),'Male')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='userNumber']").send_keys("123456789")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='dateOfBirthInput']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[5]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/select[1]").click()
    time.sleep(3)

    driver.close()
    driver.quit()









