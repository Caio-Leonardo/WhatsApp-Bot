# import biblioteca 
from selenium import webdriver 
import time 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# navegação web 
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(9)

# contatos e grupos 
contatos = ['Democrito']
mensagem = 'Atenção, chamando todos os cornos, chamando todos os cornos. Isso não é um teste, atenção'

# buscar cont/gp
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contatos)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click() 
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)  

for contato in contatos: 
    buscar_contato(contato)
    enviar_mensagem(mensagem)

