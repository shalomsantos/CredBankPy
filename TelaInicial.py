from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from Banco import ConexaoDB
import Cadastro
import Principal

banco = ConexaoDB("test.db")

def windowLogin():
    
    def chamaCadastro():
        telaInicialWindow.destroy()
        Cadastro.Cadastro()

    def logar():
        usuario = in_nome.get()
        senha = in_Senha.get()
        id_usuario = banco.valida_login(usuario, senha)

        if id_usuario == None:
            messagebox.showinfo("Usuário inexistente!", f"Usuário ou Senha incorreto! para: {usuario} pass: {senha}")
        else:
            telaInicialWindow.destroy()
            messagebox.showinfo("Parabéns", f"Usuário {usuario} Logado com sucesso!!!!")
            Principal.Principal()
    
    # cores -----------------
    preta = "#f0f3f5"
    branco = "#ffffff"
    cinza = "#787878"
    valor = "#38576b"

    # Criando janela --------------------
    telaInicialWindow = Tk()   
    telaInicialWindow.title("CredBanckPy")
    telaInicialWindow.iconbitmap('./icons/Icone-menu.ico')
    telaInicialWindow.geometry("610x300")
    telaInicialWindow.configure(background=branco)
    # telaInicialWindow.resizable(False, False)
    # telaInicialWindow.eval('tk::PlacetelaInicialWindow . center')
    # telaInicialWindow.state('zoomed')

    # --- DIVIDINDO TELA ---
    topo_frame = Frame(telaInicialWindow, width=300, height=50, bg=branco, relief='flat')
    topo_frame.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

    meio_frame = Frame(telaInicialWindow, width=300, height=250, bg=branco, relief='flat')
    meio_frame.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    lateral_frame = Frame(telaInicialWindow, width=300, height=256, bg=branco, relief='flat')
    lateral_frame.grid(row=1, column=1, pady=1, padx=0, sticky=NSEW)

    # configurando frame de cima da tela ----------
    l_nome = Label(topo_frame, text='Login', anchor=NE, font=('System 25'), bg=branco, fg=cinza)
    l_nome.place(x=5, y=5)

    l_linha = Label(topo_frame, text='', width=31, anchor=NW, font=('System'), bg=cinza, fg=cinza)
    l_linha.place(x=10, y=48)

    img = PhotoImage(file="icons/bank.png")
    Label(lateral_frame, image=img, bg=branco).place(x=25, y=0)

    # configurando frame do meio datela ----------
    l_nome = Label(meio_frame, text='Usuário: *', anchor=NW, font=('System 10'), bg=branco, fg=cinza)
    l_nome.place(x=10, y=20)

    in_nome = Entry(meio_frame, width=25, justify='left', border=0, font=("", 12), highlightthickness=1, relief='solid')
    in_nome.place(x=10, y=45)

    l_Senha = Label(meio_frame, text='Senha: *', anchor=NW, font=('System 10'), bg=branco, fg=cinza)
    l_Senha.place(x=10, y=90)

    in_Senha = Entry(meio_frame, width=25, justify='left', show='*', border=0, font=("", 12), highlightthickness=1, relief='solid')
    in_Senha.place(x=10, y=115)

    b_Entrar = Button(meio_frame, width=15, height=1, command=logar, text='Entrar', font=("System 8 bold"), bg=cinza, fg=branco, relief=RAISED, overrelief=RIDGE)
    b_Entrar.place(x=10, y=170)

    b_cadastrar = Button(meio_frame, width=15, height=1, command=chamaCadastro, text='Cadastrar', font=("System 8 bold"), bg=cinza, fg=branco, relief=RAISED, overrelief=RIDGE)
    b_cadastrar.place(x=175, y=170)
        
    telaInicialWindow.mainloop()

windowLogin()