from tkinter import *
from tkinter import Tk, ttk
from turtle import heading

# cores -----------------------------
preta = "#f0f3f5"
branco = "#feffff"
verde = "#3fb5a3"
valor = "#38576b"
letra = "#403d3d" 

# Criando janela --------------------
window = Tk()
window.title("CredBanckPy")
window.iconbitmap('./icons/Icone-menu.ico')
window.geometry("310x280")
# window.eval('tk::PlaceWindow . center')
window.resizable(False, False)
window.configure(background=branco)


def windowCadastro():
    window.geometry("700x500")
    topo_frame = Frame(window, width=310, height=50, bg=branco, relief='flat')
    topo_frame.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

    meio_frame = Frame(window, width=310, height=250, bg=branco, relief='flat')
    meio_frame.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    # configurando frame de cima da tela ----------
    l_nome = Label(topo_frame, text='Cadastro', anchor=NE, font=('ivy 25'), bg=branco, fg=letra)
    l_nome.place(x=5, y=5)

    l_linha = Label(topo_frame, text='', width=31, anchor=NW, font=('ivy'), bg=verde, fg=letra)
    l_linha.place(x=10, y=48)

    # configurando frame do meio datela ----------
    l_nome = Label(meio_frame, text='fffff: *', anchor=NW, font=('ivy 10'), bg=branco, fg=letra)
    l_nome.place(x=10, y=20)

    in_nome = Entry(meio_frame, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
    in_nome.place(x=10, y=45)

    l_Senha = Label(meio_frame, text='ffff: *', anchor=NW, font=('ivy 10'), bg=branco, fg=letra)
    l_Senha.place(x=10, y=90)

    in_Senha = Entry(meio_frame, width=25, justify='left', show='*', font=("", 15), highlightthickness=1, relief='solid')
    in_Senha.place(x=10, y=115)

    b_Entrar = Button(meio_frame, width=15, height=1, command=Principal, text='sdfsdf', font=("Ivy 8 bold"), bg=verde, fg=letra, relief=RAISED, overrelief=RIDGE)
    b_Entrar.place(x=10, y=170)

    b_cadastrar = Button(meio_frame, width=15, height=1, command=Cadastro, text='sdfsdf', font=("Ivy 8 bold"), bg=verde, fg=letra, relief=RAISED, overrelief=RIDGE)
    b_cadastrar.place(x=175, y=170)

def windowPrincipal():
    window.geometry("700x500")

    topo_frame = Frame(window, width=600, height=50, bg=branco, relief='flat')
    topo_frame.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

    meio_frame = Frame(window, width=600, height=250, bg=branco, relief='flat')
    meio_frame.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    # configurando frame de cima da tela ----------
    l_nome = Label(topo_frame, text='Seja bem vindo!', anchor=NE, font=('ivy 25'), bg=branco, fg=letra)
    l_nome.place(x=5, y=5)

    b_voltar = Button(topo_frame, width=5, height=1, command=Login, text='Voltar', font=("Ivy 8 bold"), bg=verde, fg=branco, relief=RAISED, overrelief=RIDGE)
    b_voltar.place(x=520, y=20)

    l_linha = Label(topo_frame, text='', width=61, anchor=NW, font=('ivy'), bg=verde, fg=letra)
    l_linha.place(x=10, y=48)

    # configurando frame do meio datela ----------
    l_Saldo = Label(meio_frame, text='Saldo: *', anchor=NW, font=('ivy 10'), bg=branco, fg=letra)
    l_Saldo.place(x=10, y=20)

    in_Saldo = Entry(meio_frame, width=10, justify='left', font=("", 15), highlightthickness=1, relief='solid')
    in_Saldo.place(x=55, y=20)
    
    check_Saldo = Checkbutton(meio_frame, text='Exibir saldo')
    check_Saldo.place(x=180, y=20)

    b_Transferir = Button(meio_frame, width=15, height=1, command=Principal, text='Transferir', font=("Ivy 8 bold"), bg=verde, fg=branco, relief=RAISED, overrelief=RIDGE)
    b_Transferir.place(x=300, y=25)

    b_Saque = Button(meio_frame, width=15, height=1, command=Cadastro, text='Saque', font=("Ivy 8 bold"), bg=verde, fg=branco, relief=RAISED, overrelief=RIDGE)
    b_Saque.place(x=450, y=25)

def Login():
    #============================  LOGIN  ===========================================
    # Dividindo janela --------------------
    topo_frame = Frame(window, width=310, height=50, bg=branco, relief='flat')
    topo_frame.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

    meio_frame = Frame(window, width=310, height=250, bg=branco, relief='flat')
    meio_frame.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    # configurando frame de cima da tela ----------
    l_nome = Label(topo_frame, text='Login', anchor=NE, font=('ivy 25'), bg=branco, fg=letra)
    l_nome.place(x=5, y=5)

    l_linha = Label(topo_frame, text='', width=31, anchor=NW, font=('ivy'), bg=verde, fg=letra)
    l_linha.place(x=10, y=48)

    # configurando frame do meio datela ----------
    l_nome = Label(meio_frame, text='Usuário: *', anchor=NW, font=('ivy 10'), bg=branco, fg=letra)
    l_nome.place(x=10, y=20)

    in_nome = Entry(meio_frame, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
    in_nome.place(x=10, y=45)

    l_Senha = Label(meio_frame, text='Senha: *', anchor=NW, font=('ivy 10'), bg=branco, fg=letra)
    l_Senha.place(x=10, y=90)

    in_Senha = Entry(meio_frame, width=25, justify='left', show='*', font=("", 15), highlightthickness=1, relief='solid')
    in_Senha.place(x=10, y=115)

    b_Entrar = Button(meio_frame, width=15, height=1, command=Principal, text='Entrar', font=("Ivy 8 bold"), bg=verde, fg=letra, relief=RAISED, overrelief=RIDGE)
    b_Entrar.place(x=10, y=170)

    b_cadastrar = Button(meio_frame, width=15, height=1, command=Cadastro, text='Cadastrar', font=("Ivy 8 bold"), bg=verde, fg=letra, relief=RAISED, overrelief=RIDGE)
    b_cadastrar.place(x=175, y=170)

def Cadastro():
    for widget in topo_frame.winfo_children():
        widget.destroy()
    for widget in meio_frame.winfo_children():
        widget.destroy()

    windowCadastro()

def Principal():
    for widget in topo_frame.winfo_children():
        widget.destroy()
    for widget in meio_frame.winfo_children():
        widget.destroy()

    windowPrincipal()

#============================  LOGIN  ===========================================
# Dividindo janela --------------------
topo_frame = Frame(window, width=310, height=50, bg=branco, relief='flat')
topo_frame.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

meio_frame = Frame(window, width=310, height=250, bg=branco, relief='flat')
meio_frame.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# configurando frame de cima da tela ----------
l_nome = Label(topo_frame, text='Login', anchor=NE, font=('ivy 25'), bg=branco, fg=letra)
l_nome.place(x=5, y=5)

l_linha = Label(topo_frame, text='', width=31, anchor=NW, font=('ivy'), bg=verde, fg=letra)
l_linha.place(x=10, y=48)

# configurando frame do meio datela ----------
l_nome = Label(meio_frame, text='Usuário: *', anchor=NW, font=('ivy 10'), bg=branco, fg=letra)
l_nome.place(x=10, y=20)

in_nome = Entry(meio_frame, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
in_nome.place(x=10, y=45)

l_Senha = Label(meio_frame, text='Senha: *', anchor=NW, font=('ivy 10'), bg=branco, fg=letra)
l_Senha.place(x=10, y=90)

in_Senha = Entry(meio_frame, width=25, justify='left', show='*', font=("", 15), highlightthickness=1, relief='solid')
in_Senha.place(x=10, y=115)

b_Entrar = Button(meio_frame, width=15, height=1, command=Principal, text='Entrar', font=("Ivy 8 bold"), bg=verde, fg=letra, relief=RAISED, overrelief=RIDGE)
b_Entrar.place(x=10, y=170)

b_cadastrar = Button(meio_frame, width=15, height=1, command=Cadastro, text='Cadastrar', font=("Ivy 8 bold"), bg=verde, fg=letra, relief=RAISED, overrelief=RIDGE)
b_cadastrar.place(x=175, y=170)

window.mainloop()