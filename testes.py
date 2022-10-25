import unittest
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
navegador.get('http://glpi/glpi/front/ticket.form.php?id=95429')
sleep(1)
navegador.find_element(By.XPATH, '//*[@id="ui-id-5"]').click()
sleep(1)
navegador.find_element(By.XPATH, '//*[@id="ui-tabs-2"]/div/div[1]/ul/li[4]').click()
sleep(1)
navegador.find_element(By.ID, '//*[@id="tinymce"]').click()
navegador.find_element(By.XPATH, '//*[@id="tinymce"]').send_keys('teste')
sleep(10)

'''
# Fechando chamado
navegador.find_element(By.XPATH, '//*[@id="message_after_redirect_0"]/a[1]').click()  # Abrindo a pagina do chamado

navegador.find_element(By.XPATH, '//*[@id="ui-id-5"]').click()  # Processandoo chamado

navegador.find_element(By.CLASS_NAME, 'solution').click()  # Solução

navegador.find_element(By.ID, 'tinymce').send_keys('Resolvido!')

navegador.find_element(By.XPATH, '//*[@id="mainformtable"]/tbody/tr[7]/td/input[1]').click()'''