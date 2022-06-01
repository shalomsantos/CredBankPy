from tkinter import *
from tkinter import Tk, ttk

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
window.geometry("310x300")
window.eval('tk::PlaceWindow . center')
window.configure(background=branco)

# Dividindo janela --------------------
topo_frame = Frame(window, width=310, height=50, bg=branco, relief='flat')
topo_frame.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

meio_frame = Frame(window, width=310, height=250, bg=branco, relief='flat')
meio_frame.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# configurando frame de cima da tela ----------
l_nome = Label(topo_frame, text='Login', anchor=NE, font=('ivy 25'), bg=branco, fg=letra)
l_nome.place(x=5, y=5)

l_linha = Label(topo_frame, text='', width=25, anchor=NW, font=('ivy'), bg=verde, fg=letra)
l_linha.place(x=10, y=48)

# configurando frame de cima da tela ----------
l_nome = Label(meio_frame, text='Login', anchor=NE, font=('ivy 25'), bg=branco, fg=letra)
l_nome.place(x=5, y=5)

window.mainloop()