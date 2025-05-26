from tkinter import *
from tkinter import messagebox
menu_inicial = Tk()


#Tipos de messagebox = showinfo, askshowerror, askyesno
def executar():
    messagebox.showinfo("informação", "Função executar chamada")

def cancelar():
    messagebox.askokcancel("pergunta", "voçê quer cancelar?")


menu_inicial.title("Exemplo de interfaca")

menu_inicial.resizable(width= False, height=False)
menu_inicial.geometry("300x250+500+100")
menu_inicial.iconbitmap("icone.ico")

#colocar rótulos
#text muda o texto
#bg = background 
#fg = foreground
#font = fonte temanho título

label1 = Label(menu_inicial, text= "Primeiro rótulo", fg = "blue", font = "times 20 bold")
label1.pack()

botao1 = Button(menu_inicial, text = "executar", bg = "green", fg = "white", font = "times 20 normal", command= executar )
botao1.pack()

label2 = Label(menu_inicial, text= "segundo rótulo", font = "times 20 bold")
label2.pack()

botao2 = Button(menu_inicial, text = "Cancelar", bg = "red", font = "times 18 normal", command= cancelar)
botao2.pack()


menu_inicial.mainloop()