import bot_module
import gui

path = "contatos_extensao.txt"
numeros = list()
with open(path, "r") as f:
    numeros = f.read().strip().splitlines()
 

new_numeros = list()
for numero in numeros:
    new_numeros.append(gui.processa_numero(numero))

with open("contatos.txt", "w+") as f:
    for numero in new_numeros:
        f.write(f"https://web.whatsapp.com/send/?phone=%2B{numero[1:]}&text&app_absent=0{numero},\n")