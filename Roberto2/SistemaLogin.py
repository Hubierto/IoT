from tkinter import *
from tkinter import messagebox
import banco

#Funções

def cancelar():
    resposta = messagebox.askyesno('Sair', 'Deseja realmente sair?')
    if resposta == True:
        menu_principal.destroy()
    else:
        messagebox.showinfo('Voltar', 'Você voltou para o sistema!')


def entrar():
    nome = txtUsuario.get()
    senha = txtSenha.get()

    print(nome, senha) # Para depuração, pode ser removido depois
    banco.salvar(nome, senha)
#def entrar():
#    usuario = txtUsuario.get()
#   senha = txtSenha.get()
#    
#    if usuario == 'admin' and senha == '1234':
#       messagebox.showinfo('Login', 'Login realizado com sucesso!')
#        # Aqui você pode adicionar a lógica para abrir a próxima janela ou funcionalidade
#    else:
#        messagebox.showerror('Erro', 'Usuário ou senha incorretos!')



menu_principal = Tk()
menu_principal.title('login')
menu_principal.geometry('520x300+120+170')

menu_principal.resizable(False, False)

Label1 = Label(menu_principal, text='Usuário', font= "Arial 16 bold")
Label1.grid(row=0, column=0, padx=0, pady=0 )

Label2 = Label(menu_principal, text='Senha', fg='red',  font= "Arial 16 bold")
Label2.grid(row=1, column=0, padx=27, pady=0, sticky= W)

#caixas de texto
txtUsuario = Entry(menu_principal, font= "Arial 16")
txtUsuario.grid(row=0, column=1, padx=0, pady=10, sticky=W)

txtSenha = Entry(menu_principal, font= "Arial 16", show ='*')
txtSenha.grid(row=1, column=1, padx=0, pady=10, sticky=W)

#botões
btnLogin = Button(menu_principal, text='Entrar', font= "Arial 10 bold", width=10, height=2, command=entrar)
btnLogin.grid(row=2, column=1, padx=0, pady=10, sticky= W)

btncancelar = Button(menu_principal, text='Cancelar', font= "Arial 10 bold", width=10, height=2, command=cancelar)
btncancelar.grid(row=2, column=1, padx=0, pady=10, sticky= E)

btnAlterar = Button (menu_principal, text='Alterar', font= "Arial 10 bold", width=10, height=2)
btnAlterar.grid(row=3, column=1, padx=0, pady=10, sticky= W)
menu_principal.mainloop()