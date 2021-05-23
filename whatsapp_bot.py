from bot_module import *
import time

def entrada_contatos():
    contatos = []
    with open("contatos.txt", "r+") as f:
        contatos = f.read().splitlines() 
    return contatos 

def main():
    contatos = entrada_contatos()
    mensagem = "WebDriver drives a browser natively"
    driver = iniciar_driver()
    no_remember_me(driver)
    for contato in contatos:
        acha_contato(contato, driver)
        envia_mensagem(mensagem, driver)
    
    time.sleep(1)
    driver.quit()
    

if __name__ == '__main__':
    main()