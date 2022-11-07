from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options
import sys
import os

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31m ERRO: Digite um valor valido. \033[m')
        if ok:
            break
    return (valor)


print('-' * 13)
print('Chamados GLPI')
print('-' * 13)

usuario = input('Usuario: ')
senha = input('Senha: ')
os.system('cls') or None
print(f'Logado como: {usuario}')

while True:
    print('=' * 20)
    print('Abertura de chamados')
    print('=' * 20)

    op1 = leiaInt('Qual chamado deseja abrir?\n'
                  '[ 1 ] Chamado Generico\n'
                  '[ 2 ] Cupom fiscal não impresso\n'
                  '[ 3 ] Forticliente não conecta\n'
                  '[ 4 ] PinPad não aparece Debito\n'
                  '[ 5 ] Erro de Transmissão\n'
                  '[ 6 ] Loja sem Internet\n'
                  '[ 7 ] Sistema Fora do AR\n'
                  'Sua Opção -> ')

    nav = leiaInt('Deseja ver o processo de abertura?\n'
                  '[ 1 ] Sim\n'
                  '[ 2 ] Não\n'
                  'Sua Opção ->')

    nome = str(input('Qual usuario do requerente? -> '))


    def usuarios():
        sleep(0.4)
        navegador.find_element(By.XPATH, '//*[@id="select2-chosen-6"]').click()
        sleep(0.4)
        navegador.find_element(By.XPATH, '//*[@id="s2id_autogen6_search"]').send_keys(nome)
        sleep(0.4)
        navegador.find_element(By.XPATH, '//*[@id="s2id_autogen6_search"]').send_keys(Keys.ENTER)
        sleep(0.4)
        navegador.find_element(By.XPATH, '//*[@id="select2-chosen-24"]').click
        print('=' * 20)
        print('Requerente Adicionado')


    def setor():
        navegador.find_element(By.XPATH, '//*[@id="select2-chosen-18"]').click()
        sleep(0.4)
        navegador.find_element(By.XPATH, '//*[@id="s2id_autogen18_search"]').send_keys('lojas south')
        sleep(0.4)
        navegador.find_element(By.XPATH, '//*[@id="s2id_autogen18_search"]').send_keys(Keys.ENTER)
        sleep(0.4)
        print('=' * 20)
        print('Setor Adicionado')

    if nav == 1:
        navegador = webdriver.Chrome()  # Abre o Navegador em primeiro plano
        navegador.maximize_window()
        print('=' * 20)
        print('Navegador Aberto')
    elif nav == 2:
        # abertura de chamado convencional
        chrome_options = Options()
        chrome_options.headless = True
        navegador = webdriver.Chrome(options=chrome_options)  # Abre o Navegador em segundo plano
        print('=' * 20)
        print('Navegador Aberto')
    else:
        print('Opção Invalida')
    navegador.get('http://glpi/glpi/front/ticket.php')  # Abre o GLPI
    navegador.find_element('xpath', '//*[@id="login_name"]').send_keys(usuario)  # Coloca usuario
    navegador.find_element('xpath', '//*[@id="login_password"]').send_keys(senha)  # Coloca senha
    navegador.find_element('xpath', '//*[@id="boxlogin"]/form/p[3]/input').send_keys(Keys.ENTER)  # Clica em enter para acessar
    navegador.find_element('xpath', '//*[@id="menu_all_button"]').send_keys(Keys.ENTER)  # Abre o Menu
    navegador.find_element('xpath', '//*[@id="show_all_menu"]/table[2]/tbody/tr[3]/td/a').send_keys(Keys.ENTER)  # Clica para abrir chamados
    print('=' * 20)
    print('GLPI Aberto')




    if op1 == 1:  # Chamado generico
        cat = str(input('Digite a categoria: '))
        setor = str(input('Digite o setor: '))
        titulo = str(input('Digite o titulo do Chamado: '))
        desc = str(input('Digite a descrição do Chamado: '))


        navegador.get('http://glpi/glpi/front/ticket.php')  # Abre o GLPI
        navegador.find_element('xpath', '//*[@id="login_name"]').send_keys(usuario)  # Coloca usuario
        navegador.find_element('xpath', '//*[@id="login_password"]').send_keys(senha)  # Coloca senha
        navegador.find_element('xpath', '//*[@id="boxlogin"]/form/p[3]/input').send_keys(
            Keys.ENTER)  # Clica em enter para acessar
        navegador.find_element('xpath', '//*[@id="menu_all_button"]').send_keys(Keys.ENTER)  # Abre o Menu
        navegador.find_element('xpath', '//*[@id="show_all_menu"]/table[2]/tbody/tr[3]/td/a').send_keys(
            Keys.ENTER)  # Clica para abrir chamados
        print('=' * 20)
        print('GLPI Aberto')

        usuarios()
        # Setor
        navegador.find_element(By.XPATH, '//*[@id="select2-chosen-18"]').click()
        sleep(0.3)
        navegador.find_element(By.XPATH, '//*[@id="s2id_autogen18_search"]').send_keys(setor)
        sleep(0.3)
        navegador.find_element(By.XPATH, '//*[@id="s2id_autogen18_search"]').send_keys(Keys.ENTER)
        sleep(0.8)
        print('=' * 20)
        print('Setor Adicionado')

        # Categoria
        navegador.find_element(By.XPATH, '//*[@id="select2-chosen-5"]').click()
        sleep(0.3)
        navegador.find_element(By.XPATH, '//*[@id="s2id_autogen5_search"]').send_keys(cat)
        sleep(0.3)
        navegador.find_element(By.XPATH, '//*[@id="s2id_autogen5_search"]').send_keys(Keys.ENTER)
        sleep(0.3)
        print('=' * 20)
        print('Categoria Adicionada')

        # Titulo
        navegador.find_element(By.XPATH, '//*[@id="mainformtable4"]/tbody/tr[1]/td/input').send_keys(Keys.CONTROL, 'a')
        sleep(0.3)
        navegador.find_element(By.XPATH, '//*[@id="mainformtable4"]/tbody/tr[1]/td/input').send_keys(titulo)
        sleep(0.6)
        print('=' * 20)
        print('Titulo Adicionado')

        # Descrição
        navegador.find_element(By.NAME, 'content').send_keys(Keys.CONTROL, 'a')
        sleep(0.3)
        navegador.find_element(By.NAME, 'content').send_keys(desc)
        print('=' * 20)
        print('Descrição Adicionada')

        # Enviar
        navegador.find_element(By.XPATH, '//*[@id="mainformtable4"]/tbody/tr[5]/td/input[1]').click()
        print('')
        print('-' * 14)
        print('Chamado aberto')
        print('-' * 14)
        sleep(1)

    elif op1 == 2:
        if nav == 1:
            navegador = webdriver.Chrome()  # Abre o Navegador
            navegador.maximize_window()
            print('=' * 20)
            print('Navegador Aberto')
        elif nav == 2:
            # abertura de chamado convencional
            chrome_options = Options()
            chrome_options.headless = True
            navegador = webdriver.Chrome(options=chrome_options)  # Abre o Navegador
            print('=' * 20)
            print('Navegador Aberto')
        else:
            print('Opção Invalida')

        navegador.get('http://glpi/glpi/front/ticket.php')  # Abre o GLPI
        navegador.find_element('xpath', '//*[@id="login_name"]').send_keys(usuario)  # Coloca usuario
        navegador.find_element('xpath', '//*[@id="login_password"]').send_keys(senha)  # Coloca senha
        navegador.find_element('xpath', '//*[@id="boxlogin"]/form/p[3]/input').send_keys(Keys.ENTER)  # Clica em enter para acessar
        navegador.find_element('xpath', '//*[@id="menu_all_button"]').send_keys(Keys.ENTER)  # Abre o Menu
        navegador.find_element('xpath', '//*[@id="show_all_menu"]/table[2]/tbody/tr[3]/td/a').send_keys(Keys.ENTER)  # Clica para abrir chamados
        print('=' * 20)
        print('GLPI Aberto')

        usuarios()
        # Setor
        navegador.find_element(By.XPATH, '//*[@id="select2-chosen-18"]').click()
        sleep(0.3)
        navegador.find_element(By.XPATH, '//*[@id="s2id_autogen18_search"]').send_keys(setor)
        sleep(0.3)
        navegador.find_element(By.XPATH, '//*[@id="s2id_autogen18_search"]').send_keys(Keys.ENTER)
        sleep(0.8)
        print('=' * 20)
        print('Setor Adicionado')

        # Categoria
        navegador.find_element(By.XPATH, '//*[@id="select2-chosen-5"]').click()
        sleep(0.3)
        navegador.find_element(By.XPATH, '//*[@id="s2id_autogen5_search"]').send_keys( if op1)
        sleep(0.3)
        navegador.find_element(By.XPATH, '//*[@id="s2id_autogen5_search"]').send_keys(Keys.ENTER)
        sleep(0.3)
        print('=' * 20)
        print('Categoria Adicionada')

        # Titulo
        navegador.find_element(By.XPATH, '//*[@id="mainformtable4"]/tbody/tr[1]/td/input').send_keys(Keys.CONTROL, 'a')
        sleep(0.3)
        navegador.find_element(By.XPATH, '//*[@id="mainformtable4"]/tbody/tr[1]/td/input').send_keys(titulo)
        sleep(0.6)
        print('=' * 20)
        print('Titulo Adicionado')

        # Descrição
        navegador.find_element(By.NAME, 'content').send_keys(Keys.CONTROL, 'a')
        sleep(0.3)
        navegador.find_element(By.NAME, 'content').send_keys(desc)
        print('=' * 20)
        print('Descrição Adicionada')

        # Enviar
        navegador.find_element(By.XPATH, '//*[@id="mainformtable4"]/tbody/tr[5]/td/input[1]').click()
        print('')
        print('-' * 14)
        print('Chamado aberto')
        print('-' * 14)
        sleep(1)


    op2 = int(input('Deseja Abrir outro Chamado?\n'
                    '[ 1 ] Sim\n'
                    '[ 2 ] Não\n'
                    'Sua Opção -> '))
    os.system('cls') or None
    if op2 == 2:
        print('Finalizando')
        sleep(0.8)
        print('.')
        sleep(0.8)
        print('.')
        sleep(0.8)
        print('.')
        sleep(0.8)
        break
