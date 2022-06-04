from tkinter import *
from tkinter import Tk

def Cadastro():
    
    def voltar():
        cadastroWindow.destroy()
        import TelaInicial
    
    # cores -----------------------------
    preta = "#f0f3f5"
    branco = "#ffffff"
    cinza = "#787878"
    valor = "#38576b"

    cadastroWindow = Tk()
    cadastroWindow.title("CredBanckPy")
    cadastroWindow.iconbitmap('./icons/Icone-menu.ico')
    cadastroWindow.geometry("700x400")
    cadastroWindow.configure(background=branco)
    # --- DIVIDINDO TELA ---
    topo_frame = Frame(cadastroWindow, width=300, height=50, bg=branco, relief='flat')
    topo_frame.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

    topo_lateral_frame = Frame(cadastroWindow, width=300, height=50, bg=branco, relief='flat')
    topo_lateral_frame.grid(row=0, column=1, pady=1, padx=0, sticky=NSEW)

    meio_frame = Frame(cadastroWindow, width=300, height=350, bg=branco, relief='flat')
    meio_frame.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    meio_lateral_frame = Frame(cadastroWindow, width=300, height=350, bg=branco, relief='flat')
    meio_lateral_frame.grid(row=1, column=1, pady=1, padx=0, sticky=NSEW)

    # configurando frame de cima da tela ----------
    l_nome = Label(topo_frame, text='Crie sua conta', anchor=NE, font=('System 25'), bg=branco, fg=cinza)
    l_nome.place(x=5, y=5)

    b_voltar = Button(topo_lateral_frame, width=5, command=voltar, height=1, text='Voltar', font=("System 8 bold"), bg=cinza, fg=branco, relief=RAISED, overrelief=RIDGE)
    b_voltar.place(x=250, y=0)
    
    l_linha = Label(topo_frame, text='', width=61, anchor=NW, font=('System'), bg=cinza, fg=cinza)
    l_linha.place(x=10, y=48)

    # configurando frame do meio datela ----------
    l_nome = Label(meio_frame, text='Usuario: *', anchor=NW, font=('System 10'), bg=branco, fg=cinza)
    l_nome.place(x=10, y=20)

    in_nome = Entry(meio_frame, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
    in_nome.place(x=10, y=45)

    l_Senha = Label(meio_frame, text='Senha: *', anchor=NW, font=('System 10'), bg=branco, fg=cinza)
    l_Senha.place(x=10, y=90)

    in_Senha = Entry(meio_frame, width=25, justify='left', show='*', font=("", 15), highlightthickness=1, relief='solid')
    in_Senha.place(x=10, y=115)

    l_Email = Label(meio_lateral_frame, text='E-mail: *', anchor=NW, font=('System 10'), bg=branco, fg=cinza)
    l_Email.place(x=10, y=20)

    in_Email = Entry(meio_lateral_frame, width=25, justify='left', show='*', font=("", 15), highlightthickness=1, relief='solid')
    in_Email.place(x=10, y=45)

    l_ReSenha = Label(meio_lateral_frame, text='Reescreva a Senha: *', anchor=NW, font=('System 10'), bg=branco, fg=cinza)
    l_ReSenha.place(x=10, y=90)

    in_ReSenha = Entry(meio_lateral_frame, width=25, justify='left', show='*', font=("", 15), highlightthickness=1, relief='solid')
    in_ReSenha.place(x=10, y=115)

    b_Entrar = Button(meio_frame, width=15, height=1, text='...', font=("System 8 bold"), bg=cinza, fg=branco, relief=RAISED, overrelief=RIDGE)
    b_Entrar.place(x=10, y=170)

    b_cadastrar = Button(meio_frame, width=15, height=1, text='...', font=("System 8 bold"), bg=cinza, fg=branco, relief=RAISED, overrelief=RIDGE)
    b_cadastrar.place(x=175, y=170)

    cadastroWindow.mainloop()