from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

WPP_URL = "https://web.whatsapp.com/"

def le_arquivo(nome_arquivo):
    '''
    Função que lê o arquivo e retorna seu conteúdo na estrutura de dados adequada

    Parâmetro: 
    nome_arquivo : str
            
    Retorna: list | None
    '''
    if nome_arquivo == "contatos":
        contatos = list()
        with open(f"{nome_arquivo}.txt", "r") as f:
            contatos = f.read().rstrip().splitlines()
        return contatos
    elif nome_arquivo == "mensagem":
        mensagem = str()
        with open(f"{nome_arquivo}.txt", "r") as f:
            mensagem = f.read().rstrip().splitlines()
        return mensagem
    else:
        return None

def iniciar_driver(path):
    '''
    Inicia o ChromeDriver, abre o navegador e retorna uma instância do
    ChromeDriver.  

    Parâmetro: 
    path : str
    '''
    driver = webdriver.Chrome(path)
    driver.get(WPP_URL)
    return driver

def no_remember_me(driver):
    '''
    Aperta o botão de "rememberMe" para evitar o log-in a longo prazo
    Parâmetro: WebDriver object
    '''
    botao = driver.find_element(By.NAME, "rememberMe")
    botao.click()

def acha_contato(contato, driver):
    '''
    Acha a caixa de texto para pesquisar o contato e o pesquisa

    Parâmetros: 
    contato : str
    driver : WebDriver object
    '''
    try:
        campo_pesquisa = driver.find_element_by_xpath("//div[contains(@class, 'copyable-text selectable-text')]")
        campo_pesquisa.click()
        campo_pesquisa.send_keys(contato)
        campo_pesquisa.send_keys(Keys.ENTER)
    except NoSuchElementException:
        driver.quit()

def envia_mensagem(mensagem, driver):
    '''
    Envia a mensagem ao contato

    Parâmetros: 
    mensagem : list 
    driver : WebDriver object
    '''
    try:
        campo_mensagem = driver.find_elements_by_xpath("//div[contains(@class, 'copyable-text selectable-text')]")
        campo_mensagem[1].click()
        for linha in mensagem:
            campo_mensagem[1].send_keys(linha)
            campo_mensagem[1].send_keys(Keys.SHIFT, Keys.ENTER)
        campo_mensagem[1].send_keys(Keys.ENTER)
    except NoSuchElementException:
        return