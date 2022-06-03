# from tkinter import *

# import fornecedores
# import produtos
# import saldoEstoque

# def telaInicio():

#     import clientes
#     def listarClientes():
        
#         janela2.destroy()
#         clientes.listarClientes()

#     def listarFonecedores():
#         janela2.destroy()
#         fornecedores.listarFonecedores()

#     def listarProdutos():
#         janela2.destroy()
#         produtos.listarProdutos()

#     def listarSaldo():
#         janela2.destroy()
#         saldoEstoque.listarSaldos()
#     def listarVendas():
#         ...


#     janela2 = Tk()
#     janela2.state("zoomed")
#     janela2.title("Tela inicial")
#     janela2.configure(background='white')

#     # variaveis de ajuste de tela
#     altMonitor = janela2.winfo_screenheight()
#     largMonitor = janela2.winfo_screenwidth()
#     altMenu = int((altMonitor - (altMonitor * 0.99)))
#     largMenu = altMenu
#     nEspaco = altMenu * 6

#     # Menus Cadastro
#     textUsu = Label(janela2, text="Menus do Sistema", font="Arial 20 bold", bg="#FFFFFF")
#     textUsu.place(x=largMenu, y=altMenu)

#     altMenu += nEspaco

#     menu = Button(janela2, text="Cadastro de Clientes", font="Arial 14 bold", bg="#FFFFFF", command=listarClientes)
#     menu.place(x=largMenu, y=altMenu)

#     altMenu += nEspaco

#     menu = Button(janela2, text="Cadastro de Fornecedores", font="Arial 14 bold", bg="#FFFFFF", command=listarFonecedores)
#     menu.place(x=largMenu, y=altMenu)

#     altMenu += nEspaco

#     menu = Button(janela2, text="Cadastro de Produtos", font="Arial 14 bold", bg="#FFFFFF", command=listarProdutos)
#     menu.place(x=largMenu, y=altMenu)

#     altMenu += nEspaco

#     menu = Button(janela2, text="Saldo em estoque", font="Arial 14 bold", bg="#FFFFFF", command=listarSaldo)
#     menu.place(x=largMenu, y=altMenu)

#     altMenu += nEspaco

#     menu = Button(janela2, text="Vendas", font="Arial 14 bold", bg="#FFFFFF", command=listarVendas)
#     menu.place(x=largMenu, y=altMenu)

#     janela2.mainloop()