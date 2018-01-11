from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Firefox()
driver.get("https://vk.com/")

#делаем явное ожидание появления элемента
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.NAME,"email")))

driver.find_element_by_id("index_email").send_keys("|||EMAIL|||")
driver.find_element_by_id("index_pass").send_keys("|||PASS|||")
driver.find_element_by_id("index_login_button").click()

#делаем явное ожидание появления элемента
wait.until(EC.presence_of_element_located((By.ID,"l_msg")))
driver.find_element_by_id("l_msg").click()

#делаем явное ожидание появления элемента
wait.until(EC.presence_of_element_located((By.ID,"im_dialogs_search")))
driver.find_element_by_id("im_dialogs_search").send_keys("Игорь Посталенко")

#делаем явное ожидание появления элемента
wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='im_dialogs']/div[1]/div[1]/div/div[1]/li[1]/div/button")))
driver.find_element_by_class_name("nim-dialog--name").click()

#делаем явное ожидание появления элемента
wait.until(EC.presence_of_element_located((By.ID,"im_editable0")))
driver.find_element_by_id("im_editable0").send_keys("секси")


driver.find_element_by_xpath("//*[@id='content']/div/div/div[3]/div[3]/div[4]/div[3]/div[3]/div[1]/button").click()

elem = None

#ждём пока снова отобразиться кнопка отличная от кнопки отправки
while elem != None :
	elem = driver.find_element_by_xpath("//*[@id='content']/div/div/div[3]/div[3]/div[4]/div[3]/div[3]/div[1]/button")

driver.close()
