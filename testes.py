from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options
import sys
import os


navegador = webdriver.Chrome()  # Abre o Navegador
navegador.maximize_window()
navegador.get('http://glpi/glpi/front/ticket.php')  # Abre o GLPI
navegador.find_element('xpath', '//*[@id="login_name"]').send_keys('paulo.alarcao')  # Coloca usuario
navegador.find_element('xpath', '//*[@id="login_password"]').send_keys('Paulo@123452w')  # Coloca senha
navegador.find_element('xpath', '//*[@id="boxlogin"]/form/p[3]/input').send_keys(Keys.ENTER)  # Clica em enter para acessar

navegador.get('http://glpi/glpi/front/ticket.form.php?id=96216')
navegador.find_element(By.XPATH, '//*[@id="ui-id-5"]').click()
sleep(1)
navegador.find_element(By.XPATH, '//*[@id="ui-tabs-2"]/div/div[1]/ul/li[4]').click()
sleep(1)
navegador.find_element(By.XPATH, '//*[@id="mainformtable"]/tbody/tr[2]/td[3]/a').click()
sleep(1)
navegador.find_element(By.NAME, 'contains').send_keys(Keys.CONTROL, 'A')
sleep(1)
navegador.find_element(By.NAME, 'contains').send_keys('Fechamento de chamado padrão')
sleep(1)
navegador.find_element(By.XPATH, '//*[@id="ui-tabs-1"]/div[1]/form/table/tbody/tr/td[2]/input').click()
sleep(1)
navegador.find_element(By.XPATH, '//*[@id="ui-tabs-1"]/div[3]/table/tbody/tr[4]/td[3]/a').click()
sleep(1)
navegador.find_element(By.XPATH, '//*[@id="mainformtable"]/tbody/tr[7]/td/input[1]').click()

teste
