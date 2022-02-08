import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By




from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

def test_case1():
    driver.get("https://www.w3schools.com/sql/exercise.asp?filename=exercise_select1")
    time.sleep(3)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[1]").send_keys("Select")
    time.sleep(1)

    driver.find_element(By.XPATH, "//button[@id='answerbutton']").click()
    time.sleep(2)

def test_case2():
    driver.get("https://www.w3schools.com/sql/exercise.asp?filename=exercise_select2")
    time.sleep(3)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[1]").send_keys("Select")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[2]").send_keys("City")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[3]").send_keys("From")
    time.sleep(1)

    driver.find_element(By.XPATH, "//button[@id='answerbutton']").click()
    time.sleep(2)


def test_case3():
    driver.get("https://www.w3schools.com/sql/exercise.asp?filename=exercise_select3")
    time.sleep(3)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[1]").send_keys("Select")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[2]").send_keys("Distinct")
    time.sleep(1)

    driver.find_element(By.XPATH, "//button[@id='answerbutton']").click()
    time.sleep(2)


def test_case4():
    driver.get("https://www.w3schools.com/sql/exercise.asp?filename=exercise_where1")
    time.sleep(3)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[1]").send_keys("Where")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[2]").send_keys("City")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[3]").send_keys("'Berlin'")
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[@id='answerbutton']").click()
    time.sleep(2)


def test_case5():
    driver.get("https://www.w3schools.com/sql/exercise.asp?filename=exercise_where2")
    time.sleep(3)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[1]").send_keys("Where NOT City")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[2]").send_keys("Berlin")
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[@id='answerbutton']").click()
    time.sleep(2)


def test_case6():
    driver.get("https://www.w3schools.com/sql/exercise.asp?filename=exercise_where3")
    time.sleep(3)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[1]").send_keys("Where")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[2]").send_keys("=")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[3]").send_keys("32")
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[@id='answerbutton']").click()
    time.sleep(3)


def test_case7():
    driver.get("https://www.w3schools.com/sql/exercise.asp?filename=exercise_where4")
    time.sleep(3)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[1]").send_keys("Select")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[2]").send_keys("Where")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[3]").send_keys("And")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[4]").send_keys("Papito")
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[@id='answerbutton']").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "//u[contains(text(),'here')]").click()
    time.sleep(3)

    driver.refresh()
    time.sleep(2)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[1]").send_keys("Select")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[2]").send_keys("Where")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[3]").send_keys("And")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[4]").send_keys("PostalCode")
    time.sleep(1)

    driver.find_element(By.XPATH, "//button[@id='answerbutton']").click()
    time.sleep(3)


def test_case8():
    driver.get("https://www.w3schools.com/sql/exercise.asp?filename=exercise_where5")
    time.sleep(3)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[1]").send_keys("Select")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[2]").send_keys("Where")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[3]").send_keys("Or")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[4]").send_keys("City")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[5]").send_keys("London")
    time.sleep(1)

    driver.find_element(By.XPATH, "//button[@id='answerbutton']").click()
    time.sleep(2)


def test_case9():
    driver.get("https://www.w3schools.com/sql/exercise.asp?filename=exercise_orderby1")
    time.sleep(3)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[1]").send_keys("Order By")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[2]").send_keys("City")
    time.sleep(1)

    driver.find_element(By.XPATH, "//button[@id='answerbutton']").click()
    time.sleep(2)


def test_case10():
    driver.get("https://www.w3schools.com/sql/exercise.asp?filename=exercise_orderby2")
    time.sleep(3)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[1]").send_keys("Order By")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[2]").send_keys("City")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[3]").send_keys("Desc")
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[@id='answerbutton']").click()
    time.sleep(3)


def test_case11():
    driver.get("https://www.w3schools.com/sql/exercise.asp?filename=exercise_orderby3")
    time.sleep(3)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[1]").send_keys("Order By")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[2]").send_keys("Country,")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[3]").send_keys("City")
    time.sleep(1)

    driver.find_element(By.XPATH, "//button[@id='answerbutton']").click()
    time.sleep(3)


def test_case12():
    driver.get("https://www.w3schools.com/sql/exercise.asp?filename=exercise_insert1")
    time.sleep(3)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[1]").send_keys("Insert Into")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[2]").send_keys("(")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[3]").send_keys(")")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[4]").send_keys("Values")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[5]").send_keys("(")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[6]").send_keys(")")
    time.sleep(2)

    driver.execute_script("window.scrollTo(0, window.scrollY + 400)")
    time.sleep(3)

    driver.find_element(By.XPATH, "//button[@id='answerbutton']").click()
    time.sleep(2)


def test_case13():
    driver.get("https://www.w3schools.com/sql/exercise.asp?filename=exercise_null1")
    time.sleep(3)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[1]").send_keys("PostalCode")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[2]").send_keys("IS")
    time.sleep(1)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/pre[1]/input[3]").send_keys("NULL")
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[@id='answerbutton']").click()
    time.sleep(2)


def test_case14():
    driver.get("https://www.w3schools.com/sql/exercise.asp?filename=exercise_null2")
    time.sleep(3)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/button[1]").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[4]/div[5]/button[2]").click()
    time.sleep(3)




def test_case15():
    driver.get("https://www.w3schools.com/sql/sql_groupby.asp")
    time.sleep(3)

    parentwindow = driver.current_window_handle
    print("Parent window name", parentwindow)

    driver.execute_script("window.scrollTo(0, window.scrollY + 500)")
    time.sleep(3)

    driver.execute_script("window.scrollTo(0, window.scrollY + 500)")
    time.sleep(3)

    driver.execute_script("window.scrollTo(0, window.scrollY + 500)")
    time.sleep(3)

    driver.execute_script("window.scrollTo(0, window.scrollY + 400)")
    time.sleep(5)

    driver.find_element(By.XPATH, "//body/div[@id='belowtopnav']/div[1]/div[1]/form[1]/div[1]/div[1]/pre[1]/input[1]").send_keys("COUNT")
    time.sleep(3)

    driver.find_element(By.XPATH, "//body/div[@id='belowtopnav']/div[1]/div[1]/form[1]/div[1]/div[1]/pre[1]/input[2]").send_keys("Group By Country")
    time.sleep(3)

    driver.find_element(By.XPATH, "//button[contains(text(),'Submit Answer »')]").click()
    time.sleep(5)

    childwindow = driver.window_handles
    print("Type of windows", type(childwindow))

    for child in childwindow:
        print(child)
        if parentwindow != child:
            driver.switch_to.window(child)
            driver.find_element(By.XPATH, "//button[@id='answerbutton']").click()
            time.sleep(5)


def test_case16():
    driver.get("https://www.w3schools.com/sql/sql_exam.asp")
    time.sleep(5)

    driver.execute_script("window.scrollTo(0, window.scrollY + 300)")
    time.sleep(3)

    driver.execute_script("window.scrollTo(0, window.scrollY + 300)")
    time.sleep(3)

    driver.execute_script("window.scrollTo(0, window.scrollY + 300)")
    time.sleep(5)



def test_case17():
    driver.get("https://courses.w3schools.com/browse/certifications/courses/sql-certification-exam")
    time.sleep(5)

    driver.close()
    driver.quit()





















