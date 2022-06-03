from tkinter import *
from tkinter import messagebox

from TelaInicial import *

def Principal():
    principalWindow = Tk()
    # cores -----------------------------
    preta = "#f0f3f5"
    branco = "#ffffff"
    cinza = "#787878"
    valor = "#38576b"

    principalWindow.title("CredBanckPy")
    principalWindow.iconbitmap('./icons/Icone-menu.ico')
    principalWindow.geometry("600x300")
    principalWindow.configure(background=branco)

    # --- DIVIDINDO TELA ---
    topo_frame = Frame(principalWindow, width=600, height=50, bg=branco, relief='flat')
    topo_frame.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

    meio_frame = Frame(principalWindow, width=600, height=250, bg=branco, relief='flat')
    meio_frame.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)
    # configurando frame de cima da tela ----------
    l_nome = Label(topo_frame, text='Seja bem vindo!', anchor=NE, font=('System 25'), bg=branco, fg=cinza)
    l_nome.place(x=5, y=5)

    b_voltar = Button(topo_frame, width=5, height=1, text='Voltar', font=("System 8 bold"), bg=cinza, fg=branco, relief=RAISED, overrelief=RIDGE)
    b_voltar.place(x=520, y=20)

    l_linha = Label(topo_frame, text='', width=61, anchor=NW, font=('System'), bg=cinza, fg=cinza)
    l_linha.place(x=10, y=48)

    # configurando frame do meio datela ----------
    l_Saldo = Label(meio_frame, text='Saldo: *', anchor=NW, font=('System 10'), bg=branco, fg=cinza)
    l_Saldo.place(x=10, y=20)

    in_Saldo = Entry(meio_frame, width=10, justify='left', font=("", 15), highlightthickness=1, relief='solid')
    in_Saldo.place(x=55, y=20)
        
    check_Saldo = Checkbutton(meio_frame, text='Exibir saldo')
    check_Saldo.place(x=180, y=20)

    b_Transferir = Button(meio_frame, width=15, height=1, text='Transferir', font=("System 8 bold"), bg=cinza, fg=branco, relief=RAISED, overrelief=RIDGE)
    b_Transferir.place(x=300, y=25)

    b_Saque = Button(meio_frame, width=15, height=1, text='Saque', font=("System 8 bold"), bg=cinza, fg=branco, relief=RAISED, overrelief=RIDGE)
    b_Saque.place(x=450, y=25)

    principalWindow.mainloop()