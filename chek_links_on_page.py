from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Firefox()
driver.get("http://vsevolodustinov.ru/blog/")

#делаем явное ожидание появления элемента
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.NAME,"query")))

#находим все элементы-ссылки
id = driver.find_elements_by_xpath("//body//a")
links = []

n = 0

#проходим по списку
while n < len(id):
	#получаем URL ссылки из элемента
	links[n] = id[n].get_attribute("href")
	print (links[n], sep = "\n")
	#открываем ссылку
	driver.get(links[n])
	n = n + 1
	#делаем явное ожидание появления элемента
	wait.until(EC.presence_of_element_located((By.NAME,"query")))

driver.close()
