from email import message
from logging import PlaceHolder
from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from Banco import ConexaoDB

# cores -----------------------------
preta = "#f0f3f5"
branco = "#ffffff"
cinza = "#787878"
valor = "#38576b"
letra = "#403d3d"
# --- BRANCO DE DADOS ---
banco = ConexaoDB("test.db")

# Criando janela --------------------
window = Tk()
window.title("CredBanckPy")
window.iconbitmap('./icons/Icone-menu.ico')
window.geometry("600x300")
window.configure(background=branco)
# window.resizable(False, False)
# window.eval('tk::PlaceWindow . center')
# window.state('zoomed')

def windowCadastro():
    # configurando frame de cima da tela ----------
    l_nome = Label(topo_frame, text='Cadastro', anchor=NE, font=('System 25'), bg=branco, fg=letra)
    l_nome.place(x=5, y=5)

    l_linha = Label(topo_frame, text='', width=31, anchor=NW, font=('System'), bg=cinza, fg=letra)
    l_linha.place(x=10, y=48)

    # configurando frame do meio datela ----------
    l_nome = Label(meio_frame, text='fffff: *', anchor=NW, font=('System 10'), bg=branco, fg=letra)
    l_nome.place(x=10, y=20)

    in_nome = Entry(meio_frame, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
    in_nome.place(x=10, y=45)

    l_Senha = Label(meio_frame, text='ffff: *', anchor=NW, font=('System 10'), bg=branco, fg=letra)
    l_Senha.place(x=10, y=90)

    in_Senha = Entry(meio_frame, width=25, justify='left', show='*', font=("", 15), highlightthickness=1, relief='solid')
    in_Senha.place(x=10, y=115)

    b_Entrar = Button(meio_frame, width=15, height=1, command=Principal, text='sdfsdf', font=("System 8 bold"), bg=cinza, fg=banco, relief=RAISED, overrelief=RIDGE)
    b_Entrar.place(x=10, y=170)

    b_cadastrar = Button(meio_frame, width=15, height=1, command=Cadastro, text='sdfsdf', font=("System 8 bold"), bg=cinza, fg=branco, relief=RAISED, overrelief=RIDGE)
    b_cadastrar.place(x=175, y=170)

def windowPrincipal():
    # configurando frame de cima da tela ----------
    l_nome = Label(topo_frame, text='Seja bem vindo!', anchor=NE, font=('System 25'), bg=branco, fg=letra)
    l_nome.place(x=5, y=5)

    b_voltar = Button(topo_frame, width=5, height=1, command=windowLogin, text='Voltar', font=("System 8 bold"), bg=cinza, fg=branco, relief=RAISED, overrelief=RIDGE)
    b_voltar.place(x=520, y=20)

    l_linha = Label(topo_frame, text='', width=61, anchor=NW, font=('System'), bg=cinza, fg=letra)
    l_linha.place(x=10, y=48)

    # configurando frame do meio datela ----------
    l_Saldo = Label(meio_frame, text='Saldo: *', anchor=NW, font=('System 10'), bg=branco, fg=letra)
    l_Saldo.place(x=10, y=20)

    in_Saldo = Entry(meio_frame, width=10, justify='left', font=("", 15), highlightthickness=1, relief='solid')
    in_Saldo.place(x=55, y=20)
    
    check_Saldo = Checkbutton(meio_frame, text='Exibir saldo')
    check_Saldo.place(x=180, y=20)

    b_Transferir = Button(meio_frame, width=15, height=1, command=Principal, text='Transferir', font=("System 8 bold"), bg=cinza, fg=branco, relief=RAISED, overrelief=RIDGE)
    b_Transferir.place(x=300, y=25)

    b_Saque = Button(meio_frame, width=15, height=1, command=Cadastro, text='Saque', font=("System 8 bold"), bg=cinza, fg=branco, relief=RAISED, overrelief=RIDGE)
    b_Saque.place(x=450, y=25)

def windowLogin():
    for widget in topo_frame.winfo_children():
            widget.destroy()
    for widget in meio_frame.winfo_children():
        widget.destroy()
    
    # configurando frame de cima da tela ----------
    l_nome = Label(topo_frame, text='Login', anchor=NE, font=('System 25'), bg=branco, fg=letra)
    l_nome.place(x=5, y=5)

    l_linha = Label(topo_frame, text='', width=31, anchor=NW, font=('System'), bg=cinza, fg=letra)
    l_linha.place(x=10, y=48)

    # configurando frame do meio datela ----------
    l_nome = Label(meio_frame, text='Usuário: *', anchor=NW, font=('System 10'), bg=branco, fg=letra)
    l_nome.place(x=10, y=20)

    in_nome = Entry(meio_frame, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
    in_nome.place(x=10, y=45)

    l_Senha = Label(meio_frame, text='Senha: *', anchor=NW, font=('System 10'), bg=branco, fg=letra)
    l_Senha.place(x=10, y=90)

    in_Senha = Entry(meio_frame, width=25, justify='left', show='*', font=("", 15), highlightthickness=1, relief='solid')
    in_Senha.place(x=10, y=115)

    b_Entrar = Button(meio_frame, width=15, height=1, command=Principal, text='Entrar', font=("System 8 bold"), bg=cinza, fg=letra, relief=RAISED, overrelief=RIDGE)
    b_Entrar.place(x=10, y=170)

    b_cadastrar = Button(meio_frame, width=15, height=1, command=Cadastro, text='Cadastrar', font=("System 8 bold"), bg=cinza, fg=letra, relief=RAISED, overrelief=RIDGE)
    b_cadastrar.place(x=175, y=170)

def Cadastro():
    for widget in topo_frame.winfo_children():
        widget.destroy()
    for widget in meio_frame.winfo_children():
        widget.destroy()

    windowCadastro()

def Principal():
    usuario = in_nome.get()
    senha = in_Senha.get()
    id_usuario = banco.valida_login(usuario, senha)

    if id_usuario == None:
        messagebox.showinfo("Usuário inexistente!", f"Usuário ou Senha incorreto! para: {usuario} pass: {senha}")
        windowLogin()
    else:
        for widget in topo_frame.winfo_children():
            widget.destroy()
        for widget in meio_frame.winfo_children():
            widget.destroy()
        windowPrincipal()

# --- DIVIDINDO TELA ---
topo_frame = Frame(window, width=600, height=50, bg=branco, relief='flat')
topo_frame.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

meio_frame = Frame(window, width=600, height=250, bg=branco, relief='flat')
meio_frame.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# configurando frame de cima da tela ----------
l_nome = Label(topo_frame, text='Login', anchor=NE, font=('System 25'), bg=branco, fg=letra)
l_nome.place(x=5, y=5)

l_linha = Label(topo_frame, text='', width=31, anchor=NW, font=('System'), bg=cinza, fg=letra)
l_linha.place(x=10, y=48)

# configurando frame do meio datela ----------
l_nome = Label(meio_frame, text='Usuário: *', anchor=NW, font=('System 10'), bg=branco, fg=letra)
l_nome.place(x=10, y=20)

in_nome = Entry(meio_frame, width=25, justify='left', border=0, font=("", 12), highlightthickness=1, relief='solid')
in_nome.place(x=10, y=45)

l_Senha = Label(meio_frame, text='Senha: *', anchor=NW, font=('System 10'), bg=branco, fg=letra)
l_Senha.place(x=10, y=90)

in_Senha = Entry(meio_frame, width=25, justify='left', show='*', border=0, font=("", 12), highlightthickness=1, relief='solid')
in_Senha.place(x=10, y=115)

b_Entrar = Button(meio_frame, width=15, height=1, command=Principal, text='Entrar', font=("System 8 bold"), bg=cinza, fg=branco, relief=RAISED, overrelief=RIDGE)
b_Entrar.place(x=10, y=170)

b_cadastrar = Button(meio_frame, width=15, height=1, command=Cadastro, text='Cadastrar', font=("System 8 bold"), bg=cinza, fg=branco, relief=RAISED, overrelief=RIDGE)
b_cadastrar.place(x=175, y=170)

window.mainloop()