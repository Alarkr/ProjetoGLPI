import pyautogui
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

navegador = webdriver.Chrome()  # Abre o Navegador
navegador.get('http://glpi/glpi/front/ticket.php')  # Abre o GLPI
sleep(1)
navegador.find_element('xpath', '//*[@id="login_name"]').send_keys('paulo.alarcao')  # Coloca usuario
sleep(1)
navegador.find_element('xpath', '//*[@id="login_password"]').send_keys('Paulo@123452w', Keys.ENTER)  # Coloca senha
sleep(1)
navegador.get('http://glpi/glpi/front/ticket.form.php?id=95517')
sleep(1)
navegador.find_element(By.XPATH, '//*[@id="ui-id-5"]').click()
sleep(1)
navegador.find_element(By.XPATH, '//*[@id="ui-tabs-2"]/div/div[1]/ul/li[4]').click()
sleep(1)
navegador.find_element(By.ID, '//*[@id="tinymce"]').click()
navegador.find_element(By.XPATH, 'http://glpi/glpi/front/ticket.form.php?id=95517').send_keys('teste')
sleep(10)