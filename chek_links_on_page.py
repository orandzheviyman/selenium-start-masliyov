from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Firefox()
driver.get("http://vsevolodustinov.ru/blog/all/")

#делаем явное ожидание появления элемента
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.NAME,"query")))

#находим количество ссылок
id = driver.find_elements_by_xpath("//body//div[contains(@class, 'e2-note-list e2-text')]//a")
n = 0

#проходим по списку
while n < len(id):
	#получаем URL ссылки из элемента
	id = driver.find_elements_by_xpath("//body//a")
	links = id[n].get_attribute("href")
	#выводим URL в консоль
	print (id[n].get_attribute("href"))
	#открываем ссылку
	driver.get(links)
	n = n + 1
	driver.back()
print ("Проверили", len(id), "ссылок")

driver.close()
