from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from Banco import ConexaoDB

banco = ConexaoDB("test.db")

def Cadastro():
    
    def voltar():
        cadastroWindow.destroy()
        import TelaInicial
    

    def cadastrarUsuario():

        #cpf, nome, datanasc, email, telefone, usuario, senha
        cpf = in_cpf.get()
        nome = in_nomeComplet.get()
        DtNasc = in_DtNascimento.get()
        email = in_email.get()
        tel = ""
        usuario = in_nome.get()
        senha = in_senha.get()

        banco.criar_usuario(cpf, nome, DtNasc, email, tel, usuario, senha)


    def limparTela():
        print()
    

    # cores -----------------------------
    preta = "#050505"
    branco = "#ffffff"
    cinza = "#787878"
    valor = "#38576b"

    cadastroWindow = Tk()
    cadastroWindow.title("CredBanckPy")
    cadastroWindow.iconbitmap('./icons/Icone-menu.ico')
    cadastroWindow.geometry("610x360")
    cadastroWindow.configure(background=branco)
    # --- DIVIDINDO TELA ---
    topo_frame = Frame(cadastroWindow, width=300, height=50, bg=branco, relief='flat')
    topo_frame.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

    topo_lateral_frame = Frame(cadastroWindow, width=300, height=50, bg=branco, relief='flat')
    topo_lateral_frame.grid(row=0, column=1, pady=1, padx=0, sticky=NSEW)

    meio_frame = Frame(cadastroWindow, width=300, height=450, bg=branco, relief='flat')
    meio_frame.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    meio_lateral_frame = Frame(cadastroWindow, width=300, height=250, bg=branco, relief='flat')
    meio_lateral_frame.grid(row=1, column=1, pady=1, padx=0, sticky=NSEW)

    meio_lateral1_frame = Frame(cadastroWindow, width=300, height=250, bg=branco, relief='flat')
    meio_lateral1_frame.grid(row=1, column=2, pady=1, padx=0, sticky=NSEW)

    # configurando frame de cima da tela ----------
    l_titulo = Label(topo_frame, text='Crie sua conta', anchor=NE, font=('System 25'), bg=branco, fg=preta)
    l_titulo.place(x=5, y=5)

    b_voltar = Button(topo_lateral_frame, width=5, command=voltar, height=1, text='Voltar', font=("System 8 bold"), bg=cinza, fg=branco, relief=RAISED, overrelief=RIDGE)
    b_voltar.place(x=240, y=15)
    
    l_linha = Label(topo_frame, text='', width=300, anchor=NW, font=('System'), bg=cinza, fg=cinza)
    l_linha.place(x=10, y=48)

    img = PhotoImage(file="icons/cadIcon.png")
    Label(topo_frame, width=40, height=40, image=img, bg=branco).place(x=220, y=0)

    # configurando frame do meio datela ----------
    l_nomeComplet = Label(meio_frame, text='Nome Completo: *', anchor=NW, font=('System 10'), bg=branco, fg=cinza)
    l_nomeComplet.place(x=10, y=20)

    in_nomeComplet = Entry(meio_frame, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
    in_nomeComplet.place(x=10, y=45)

    l_cpf = Label(meio_frame, text='CPF: *', anchor=NW, font=('System 10'), bg=branco, fg=cinza)
    l_cpf.place(x=10, y=90)

    in_cpf = Entry(meio_frame, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
    in_cpf.place(x=10, y=115)

    l_email = Label(meio_frame, text='E-mail: *', anchor=NW, font=('System 10'), bg=branco, fg=cinza)
    l_email.place(x=10, y=160)

    in_email = Entry(meio_frame, width=25, justify='left',  font=("", 15), highlightthickness=1, relief='solid')
    in_email.place(x=10, y=185)

    l_DtNascimento = Label(meio_frame, text='Data de nascimento: *', anchor=NW, font=('System 10'), bg=branco, fg=cinza)
    l_DtNascimento.place(x=10, y=230)

    in_DtNascimento = Entry(meio_frame, width=10, justify='left', font=("", 15), highlightthickness=1, relief='solid')
    in_DtNascimento.place(x=10, y=255)

    l_nome = Label(meio_lateral_frame, text='Usuário: *', anchor=NW, font=('System 10'), bg=branco, fg=cinza)
    l_nome.place(x=10, y=20)

    in_nome = Entry(meio_lateral_frame, width=25, justify='left',  font=("", 15), highlightthickness=1, relief='solid')
    in_nome.place(x=10, y=45)

    l_ReSenha = Label(meio_lateral_frame, text='Reescreva a Senha: *', anchor=NW, font=('System 10'), bg=branco, fg=cinza)
    l_ReSenha.place(x=10, y=90)

    in_ReSenha = Entry(meio_lateral_frame, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
    in_ReSenha.place(x=10, y=115)

    l_Senha = Label(meio_lateral_frame, text='Senha: *', anchor=NW, font=('System 10'), bg=branco, fg=cinza)
    l_Senha.place(x=10, y=160)
    
    in_senha = Entry(meio_lateral_frame, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
    in_senha.place(x=10, y=185)

    b_cadastrar = Button(meio_lateral_frame, width=15, height=1, command=cadastrarUsuario, text='Cadastrar', font=("System 8 bold"), bg=cinza, fg=branco, relief=RAISED, overrelief=RIDGE)
    b_cadastrar.place(x=10, y=255)

    b_Limpar = Button(meio_lateral_frame, width=15, height=1, command=limparTela, text='Limpar', font=("System 8 bold"), bg=cinza, fg=branco, relief=RAISED, overrelief=RIDGE)
    b_Limpar.place(x=175, y=255)

    cadastroWindow.mainloop()