from bot_module import *
import time
from gui import cria_gui, cria_gui_aviso

PATH = "chromedriver.exe"

def entrada_contatos():
    contatos = []
    with open("contatos.txt", "r") as f:
        contatos = f.read().splitlines() 
    return contatos 

def entrada_mensagem():
    mensagem = ""
    with open("mensagem.txt", "r") as f:
        mensagem = f.read()
    return mensagem

def main():
    cria_gui_aviso()
    contatos = entrada_contatos()
    mensagem = entrada_mensagem()
    driver = iniciar_driver(PATH)
    no_remember_me(driver)
    for contato in contatos:
        acha_contato(contato, driver)
        envia_mensagem(mensagem, driver)
    
    time.sleep(8)
    driver.quit()
    

if __name__ == '__main__':
    main()