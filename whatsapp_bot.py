from bot_module import *
import time
from gui import cria_gui_aviso

DRIVER_PATH = "chromedriver.exe"
TEMPO_DE_ESPERA = 300

def le_arquivo(nome_arquivo):
    '''
    Função que lê o arquivo e retorna seu conteúdo na estrutura de dados adequada

    Parâmetro: str
    Retorna: list | str | None
    '''
    if nome_arquivo == "contatos":
        contatos = []
        with open(f"{nome_arquivo}.txt", "r") as f:
            contatos = f.read().rstrip().splitlines()
        return contatos
    elif nome_arquivo == "mensagem":
        mensagem = ""
        with open(f"{nome_arquivo}.txt", "r") as f:
            mensagem = f.read()
        return mensagem
    else:
        return None

def main():
    cria_gui_aviso()
    contatos = le_arquivo("contatos")
    mensagem = le_arquivo("mensagem")
    driver = iniciar_driver(DRIVER_PATH)
    driver.implicitly_wait(TEMPO_DE_ESPERA)
    no_remember_me(driver)
    for contato in contatos:
        acha_contato(contato, driver)
        time.sleep(0.5)
        envia_mensagem(mensagem, driver)
        time.sleep(0.5)
    
    time.sleep(10)
    driver.quit()
    

if __name__ == '__main__':
    main()