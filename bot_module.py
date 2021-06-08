from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys, os

def iniciar_driver(path):
    '''
    Iniciar o Chrome Driver e abre o navegador
    Parâmetros:
    Retorna: WebDriver object
    '''
    driver = webdriver.Chrome(path)
    whatsapp_link = "https://web.whatsapp.com/"
    driver.get(whatsapp_link)
    driver.implicitly_wait(30)
    return driver

def no_remember_me(driver):
    '''
    Aperta o botão de "rememberMe" para evitar o log-in a longo prazo
    Parâmetros: WebDriver object
    Retorna:
    '''
    botao = driver.find_element(By.NAME, "rememberMe")
    botao.click()


def acha_contato(contato, driver):
    '''
    Acha a caixa de texto para pesquisar o contato e o pesquisa
    Parâmetro: string e WebDriver object
    Retorna:
    '''
    try:
        campo_pesquisa = driver.find_element_by_xpath("//div[contains(@class, 'copyable-text selectable-text')]")
        campo_pesquisa.click()
        campo_pesquisa.send_keys(contato)
        campo_pesquisa.send_keys(Keys.ENTER)
        driver.implicitly_wait(0.5)
    except:
        driver.quit()
        sys.exit()


def envia_mensagem(mensagem, driver):
    '''
    Envia a mensagem ao contato
    Parâmetros: string e WebDriver object
    Retorna:
    '''
    campo_mensagem = driver.find_elements_by_xpath("//div[contains(@class, 'copyable-text selectable-text')]")
    campo_mensagem[1].click()
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)
