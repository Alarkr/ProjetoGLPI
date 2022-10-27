from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from time import sleep
'''chrome_options = Options()
chrome_options.headless = True
driver = webdriver.Chrome(options=chrome_options)'''

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://10.16.51.65/sws/index.html')
sleep(2)
driver.find_element(By.XPATH, '//*[@id="ext-gen249"]').click()
sleep(2)
driver.find_element(By.XPATH, '//*[@id="ext-gen150"]/div/li/ul/li[3]/div/a/span').click()
modelo = driver.find_element(By.XPATH, '//*[@id="ext-gen1053"]')
contador = driver.find_element(By.XPATH, '//*[@id="ext-gen1075"]/div[3]/table/tbody/tr/td[6]/div')

print(f'Modelo {modelo}\n'
      f'Contador {contador}')





