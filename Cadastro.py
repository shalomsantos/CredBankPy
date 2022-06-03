from tkinter import *
from tkinter import Tk
from tkinter import messagebox

import TelaInicial

def Cadastro():
    cadastroWindow = Tk()
    # cores -----------------------------
    preta = "#f0f3f5"
    branco = "#ffffff"
    cinza = "#787878"
    valor = "#38576b"

    cadastroWindow.title("CredBanckPy")
    cadastroWindow.iconbitmap('./icons/Icone-menu.ico')
    cadastroWindow.geometry("600x300")
    cadastroWindow.configure(background=branco)
    # --- DIVIDINDO TELA ---
    topo_frame = Frame(cadastroWindow, width=600, height=50, bg=branco, relief='flat')
    topo_frame.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

    meio_frame = Frame(cadastroWindow, width=600, height=250, bg=branco, relief='flat')
    meio_frame.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    # configurando frame de cima da tela ----------
    l_nome = Label(topo_frame, text='Cadastro', anchor=NE, font=('System 25'), bg=branco, fg=cinza)
    l_nome.place(x=5, y=5)

    b_voltar = Button(topo_frame, width=5, height=1, text='Voltar', font=("System 8 bold"), bg=cinza, fg=branco, relief=RAISED, overrelief=RIDGE)
    b_voltar.place(x=520, y=20)

    l_linha = Label(topo_frame, text='', width=31, anchor=NW, font=('System'), bg=cinza, fg=cinza)
    l_linha.place(x=10, y=48)

    # configurando frame do meio datela ----------
    l_nome = Label(meio_frame, text='fffff: *', anchor=NW, font=('System 10'), bg=branco, fg=cinza)
    l_nome.place(x=10, y=20)

    in_nome = Entry(meio_frame, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
    in_nome.place(x=10, y=45)

    l_Senha = Label(meio_frame, text='ffff: *', anchor=NW, font=('System 10'), bg=branco, fg=cinza)
    l_Senha.place(x=10, y=90)

    in_Senha = Entry(meio_frame, width=25, justify='left', show='*', font=("", 15), highlightthickness=1, relief='solid')
    in_Senha.place(x=10, y=115)

    b_Entrar = Button(meio_frame, width=15, height=1, text='sdfsdf', font=("System 8 bold"), bg=cinza, fg=branco, relief=RAISED, overrelief=RIDGE)
    b_Entrar.place(x=10, y=170)

    b_cadastrar = Button(meio_frame, width=15, height=1, text='sdfsdf', font=("System 8 bold"), bg=cinza, fg=branco, relief=RAISED, overrelief=RIDGE)
    b_cadastrar.place(x=175, y=170)

    cadastroWindow.mainloop()