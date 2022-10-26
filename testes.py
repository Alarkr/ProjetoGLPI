import unittest
import pyautogui
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


def usuarios():
    sleep(0.4)
    navegador.find_element(By.XPATH, '//*[@id="select2-chosen-6"]').click()
    sleep(0.4)
    navegador.find_element(By.XPATH, '//*[@id="s2id_autogen6_search"]').send_keys('carlos.sousa')
    sleep(0.4)
    navegador.find_element(By.XPATH, '//*[@id="s2id_autogen6_search"]').send_keys(Keys.ENTER)
    sleep(0.4)
    navegador.find_element(By.XPATH, '//*[@id="select2-chosen-24"]').click()
    print('=' * 20)
    print('Requerente Adicionado')


navegador = webdriver.Chrome()  # Abre o Navegador
navegador.get('http://glpi/glpi/front/ticket.php')  # Abre o GLPI
navegador.find_element('xpath', '//*[@id="login_name"]').send_keys('paulo.alarcao')  # Coloca usuario
navegador.find_element('xpath', '//*[@id="login_password"]').send_keys('Paulo@123452w')  # Coloca senha
navegador.find_element('xpath', '//*[@id="boxlogin"]/form/p[3]/input').send_keys(Keys.ENTER)  # Clica em enter para acessar
navegador.find_element('xpath', '//*[@id="menu_all_button"]').send_keys(Keys.ENTER)  # Abre o Menu
navegador.find_element('xpath', '//*[@id="show_all_menu"]/table[2]/tbody/tr[3]/td/a').send_keys(Keys.ENTER)  # Clica para abrir chamados
sleep(0.4)
navegador.find_element(By.XPATH, '//*[@id="select2-chosen-6"]').click()
sleep(0.4)
navegador.find_element(By.XPATH, '//*[@id="s2id_autogen6_search"]').send_keys('carlos.sousa')
sleep(0.4)
navegador.find_element(By.XPATH, '//*[@id="s2id_autogen6_search"]').send_keys(Keys.ENTER)
sleep(0.4)
navegador.find_element(By.CLASS_NAME, 'select2-hidden-accessible').click()






'''navegador = webdriver.Chrome()  # Abre o Navegador
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
sleep(10)'''