from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image # type: ignore

ICON_PATH = "rsc/logo.jpeg"
def cria_gui():
    interface = Tk()
    FONTE = Font(family="Helvetica", size=20)
    # Título, dimensões e ícone
    interface.title("NPSP")
    X = interface.winfo_screenwidth()
    interface.geometry("600x600+{}+50".format((X//2)-300))
    icone = ImageTk.PhotoImage(Image.open(ICON_PATH))
    interface.iconphoto(True, icone)

    frame_contatos = Frame(interface)
    frame_contatos.pack()
    frame_mensagem = Frame(interface)
    frame_mensagem.pack()
 
    
    # Caixas de entrada de texto (contatos e mensagem)
    label_nome_contatos = Label(frame_contatos, text="Contatos", font=FONTE, fg="#083F38", bg="#9BE1B6")
    label_nome_contatos.pack()
    
    contatos = Text(frame_contatos, height="17")
    contatos.pack()
    submeter_contatos = Button(frame_contatos, text="Enviar", command=lambda:escreve_texto(contatos.get(1.0, END), "contatos"))
    submeter_contatos.pack()

    label_nome_mensagem = Label(frame_contatos, text="Mensagem", font=FONTE, fg="#083F38", bg="#9BE1B6")
    mensagem = Text(frame_mensagem, height="17")
    mensagem.pack()
    label_nome_mensagem.pack()
    submeter_mensagem = Button(frame_mensagem, text="Enviar", command=lambda:escreve_texto(mensagem.get(1.0, END), "mensagem"))
    submeter_mensagem.pack()

    interface.mainloop()

def cria_gui_aviso():
    interface = Tk()
    interface.title("NPSP - Aviso")
    X = interface.winfo_screenwidth()
    interface.geometry("574x530+{}+50".format((X//2)-300))
    icone = ImageTk.PhotoImage(Image.open("rsc/logo.jpeg"))
    interface.iconphoto(True, icone)
    
    canvas = Canvas(interface, width=574, height=500)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open("rsc/aviso.png"))
    canvas.create_image(0, 0, anchor=NW, image=img)

    ok_button = Button(interface, text="Ok", font=("Arial",17), command=interface.destroy)
    ok_button.pack()
    interface.mainloop()

    cria_gui()

def escreve_texto(texto, tipo):
    with open(f"{tipo}.txt", "w+") as f:
        f.write(texto)

def main():
    cria_gui_aviso()

if __name__=="__main__":
    main()
