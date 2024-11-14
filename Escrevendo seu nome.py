from tkinter import *

def mostrarNome():
    nome = textbox_1.get()
    label_final = Label(root, text="O teu nome é "+nome, font=("Arial", 15, "bold"), bg="lightcyan", fg="saddlebrown")
    label_final.grid()


# Interface Gráfica
root = Tk()
root.title("Escreva seu nome")
root.geometry("400x400")
root.configure(bg="lightcyan")  

# Onde o nome é escrito
label_1 = Label(root,text="Escreve o teu nome: ", font=("Arial", 15), bg="lightcyan", fg="indigo")
textbox_1 = Entry(root, font=("Arial", 15))
button_1 = Button(root, text="Executar", command=mostrarNome, font=("Arial", 15, "bold"), bg="darkviolet", fg="seashell")

label_1.grid()
textbox_1.grid()
button_1.grid()

root.mainloop()
