from tkinter import *

janela = Tk()  # instancia um objeto da classe Tk()

#-----CRIANDO UM LABEL NA JANELA-----
lb1 = Label(janela, text="Label 1", bg="yellow")     # cria um widget do tipo Label atribuido ao container pai "janela"
lb2 = Label(janela, text="Label 2", bg="green")
lb3 = Label(janela, text="Label 3", bg="blue")
lb4 = Label(janela, text="Label 4", bg="red")

lb2.pack()        # atribui o gerenciador de layout "pack" ao widget "lb", posicionando o widget dentro do container pai
lb1.pack()      # por padão "side"=TOP
lb3.pack()
lb4.pack(side=RIGHT)    # o atributo "side" vincula uma extremidade a um widget


# ----------CONFIGURAÇÕES DA JANELA-------------------
janela.title("Janela principal")  # título da janela
janela["bg"] = "grey"  # altera o valor do índice do dicionário "janela"
janela.geometry("500x300+200+100")  # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
janela.mainloop()  # cria um laço de repetição enquanto a janela estiver aberta
# ----------------------------------------------------

