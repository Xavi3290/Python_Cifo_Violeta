from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

#para probarlo tendras que poner un email y una contraseña

driver = webdriver.Chrome()

driver.get('https://www.linkedin.com/login')

driver.implicitly_wait(3)  # Espera 5 segundos para que la página cargue completamente

email_input = driver.find_element(by = By.ID, value = "username")
email_input.send_keys("tu_email")
password_input = driver.find_element(by = By.ID, value = "password")
password_input.send_keys("tu_password")

password_input.send_keys(Keys.RETURN)

#vigila que al probarlo varias veces te salta la verificacion

driver.implicitly_wait(3)  # Espera 5 segundos para que la página cargue completamente

#driver.get('https://www.linkedin.com/jobs/')

driver.implicitly_wait(3)  # Espera 5 segundos para que la página cargue completamente

search_box = driver.find_element(by = By.ID, value ='jobs-search-box-keyword-id-ember24')
search_box.send_keys('machine learning')
search_box = driver.find_element(by = By.ID, value ='jobs-search-box-location-id-ember24')
search_box.send_keys('Barcelona')
search_box.click()
search_box.submit()
search_box.send_keys(Keys.ENTER)