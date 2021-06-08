from tkinter import *
from PIL import ImageTk, Image # type: ignore

ICON_PATH = "rsc/logo.jpeg"

def cria_gui():
    interface = Tk()
    # Título, dimensões e ícone
    interface.title("NPSP")
    interface.geometry("600x600")
    icone = ImageTk.PhotoImage(Image.open(ICON_PATH))
    interface.iconphoto(True, icone)
    # interface.config(bd="light blue")

    label_contatos = Frame(interface)
    label_contatos.pack()
    label_mensagem = Frame(interface)
    label_mensagem.pack()

    # Caixas de entrada de texto (contatos e mensagem)
    contatos = Text(label_contatos)
    contatos.pack()
    submeter_contatos = Button(label_contatos, text="Enviar")
    submeter_contatos.pack()

    mensagem = Text(label_mensagem)
    mensagem.pack()
    submeter_mensagem = Button(label_mensagem, text="Enviar")
    submeter_mensagem.pack()

    interface.mainloop()

def main():
    cria_gui()


if __name__=="__main__":
    main()
