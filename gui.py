from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image # type: ignore
from bot_module import *
import selenium
import time
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions

ICON_PATH = "rsc/logo.jpeg"

def cria_gui():
    '''
    Cria interface gráfica de entrada dos contatos e da mensagem. Essa função
    pode ser chamada separadamente sem ser dentro do escopo de criar_gui_aviso().
    '''
    interface = Tk()
    TITULO = "NPSP"
    # Título, dimensões e ícone
    interface.title(TITULO)
    X = interface.winfo_screenwidth()
    interface.geometry("650x650+{}+30".format((X//2)-300))
    icone = ImageTk.PhotoImage(Image.open(ICON_PATH))
    interface.iconphoto(True, icone)

    frame_contatos = Frame(interface)
    frame_contatos.pack()
    frame_mensagem = Frame(interface)
    frame_mensagem.pack()

    FONTE = Font(family="Helvetica", size=20)
    fg_cor = "#083F38"
    bg_cor = "#9BE1B6"
    label_nome_contatos = Label(frame_contatos, text="Contatos", 
                                font=FONTE, fg=fg_cor, bg=bg_cor)
    label_nome_contatos.pack()
    label_nome_mensagem = Label(frame_contatos, text="Mensagem", 
                                font=FONTE, fg=fg_cor, bg=bg_cor)
    
    text_area_height = "13"
    contatos = Text(frame_contatos, height=text_area_height)
    contatos.pack()
    submeter_contatos = Button(frame_contatos, text="Enviar", command=lambda:escreve_texto(contatos.get(1.0, END), "contatos"))
    submeter_contatos.pack()

    mensagem = Text(frame_mensagem, height=text_area_height)
    mensagem.pack()
    submeter_mensagem = Button(frame_mensagem, text="Enviar", command=lambda:escreve_texto(mensagem.get(1.0, END), "mensagem"))
    submeter_mensagem.pack()
    label_nome_mensagem.pack()

    finalizado = Button(interface, text="Finalizar", font=("Arial", 15),
                        command=acha_numero_envia_mensagem)
    finalizado.pack(side=RIGHT)

    interface.mainloop()

def cria_gui_aviso():
    '''
    Cria interface inicial com as orientações de uso do resto do programa,
    chamando dentro de seu escopo a função que cria a janela posterior. Ou seja,
    não é necessário chamar a função cria_gui().
    '''
    GUI_AVISO_TITULO = "NPSP - Aviso"
    DIMENSOES = (574, 530)

    # Cria instância de Tk, define o título, dimensões e o ícone do janela
    interface = Tk()
    interface.title(GUI_AVISO_TITULO)
    X = interface.winfo_screenwidth()
    interface.geometry("{}x{}+{}+50".format(DIMENSOES[0], DIMENSOES[1], (X//2)-300))
    icone = ImageTk.PhotoImage(Image.open(ICON_PATH))
    interface.iconphoto(True, icone)
    
    canvas = Canvas(interface, width=DIMENSOES[0], height=DIMENSOES[1]-30)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open("rsc/aviso.png"))
    canvas.create_image(0, 0, anchor=NW, image=img)

    ok_button = Button(interface, text="Ok", font=("Arial",17), command=interface.destroy)
    ok_button.pack()
    interface.mainloop()

    cria_gui()

def escreve_texto(texto, tipo):
    '''
    Escreve texto no arquivo de nome tipo.txt
    Parâmetros: str, str
    '''
    with open(f"{tipo}.txt", "w+", encoding="utf-8") as f:
        f.write(texto)

DRIVER_PATH = "chromedriver.exe"
TEMPO_DE_ESPERA = 300
contagem_clique_finalizar = 0
def pegar_contagem():
    global contagem_clique_finalizar
    contagem_clique_finalizar += 1
    return contagem_clique_finalizar


def acha_contato_envia_mensagem():
    '''
    Função que acha o contato e envia a mensagem
    '''
    contagem = pegar_contagem()
    contatos = le_arquivo("contatos")
    mensagem = le_arquivo("mensagem")
    if contagem == 1:
        global driver
        driver = iniciar_driver(DRIVER_PATH)
        driver.implicitly_wait(TEMPO_DE_ESPERA)
        no_remember_me(driver)
    for contato in contatos:
        barra_de_pesquisa(contato, driver)
        time.sleep(0.5)
        envia_mensagem(mensagem, driver)
        time.sleep(0.5)

def processa_numero(numero):
    # TODO: processa número para ficar no padrão adequado. Manipulação de strings
    # 9 números: número sem DD
    # 11 números: com DD
    # 13 números: com código 55
    numero = numero.replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
    if len(numero) < 11:
        return numero
    elif len(numero) == 11:
        return f"+55{numero}"
    elif len(numero) > 11:
        if numero[0] == "+":
            return numero
        else:
            return f"+{numero}"

def acha_numero_envia_mensagem():
    '''
    Função que usa a estrutura https://wa.me/phonenumber e envia a mensagem
    Número tem que estar no formato internacional
    '''
    contagem = pegar_contagem()
    numeros = le_arquivo("contatos")
    mensagem = le_arquivo("mensagem")
    if contagem == 1:
        global driver
        driver = iniciar_driver(DRIVER_PATH)
        #no_remember_me(driver)
    try:
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "_13NKt copyable-text selectable-text")))
        element.click()
    except:
        pass
    print(numeros)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    for i, numero in enumerate(numeros):
        driver.implicitly_wait(TEMPO_DE_ESPERA)
        numero = processa_numero(numero)
        print(numero)
        numero_entra_chat(numero, driver)
        envia_mensagem(mensagem, driver)
        #driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
        driver.execute_script('''window.open("http://google.com","_blank");''')
        window_name = driver.window_handles[-1]
        driver.switch_to.window(window_name=window_name)
    sys.exit(0)
