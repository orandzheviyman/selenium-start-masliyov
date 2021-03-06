from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Firefox()
driver.get("https://dev2.revetinc.com/join-now")

#делаем явное ожидание кликабельности элемента
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.NAME,"form")))


FirstName = driver.find_element_by_name("FirstName")
FirstName.send_keys("FirstName_test")

LastName = driver.find_element_by_name("LastName")
LastName.send_keys("LastName_test")

UserName_Email = driver.find_element_by_name("UserName")
UserName_Email.send_keys("UserName_Email@test.com")

Password = driver.find_element_by_name("Password")
Password.send_keys("Test!test1")

driver.find_element_by_xpath("//div[contains(@class, 'form-group')]/button").click()

#делаем неявное ожидание, чтобы драйвер пробовал 10 секунд найти в DOM нужный элемент
driver.implicitly_wait(10)

#проверяем, виден ли элемент подтверждающий успешное действие
if driver.find_elements_by_xpath("//*[contains(text(), 'Success')]").is_displayed() :
  print ("PASS")
else :
  print ("FAIL")
  driver.get_screenshot_as_file("screenshot.png")

driver.implicitly_wait(0)

driver.close()
