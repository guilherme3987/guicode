import time
# ______________IMPORTAR BIBLIOTECA TKINTER_______________
from tkinter import *

# ------------------------------------------MOSTRAR A JANELAS-----------------------------------------------------------
tela = Tk()  # MOSTRAR TELA DO PROGRAMA(fundo branco)

tela.title("CALCULADORA")  # NOME DO PROGRAMA

visor = Entry(tela, bg="light blue")  # TELA DO VISOR DAS OPERAÇÕES
visor.place(x=70, y=70)  # DIMENSÕES DO VISOR

tela.resizable(False, False)  # O USÚARIO NÃO HABILITA O TAMANHO DA TELA

tela.geometry("300x450")


# -----------------------------------------FUNÇÕES-----------------------------------------------------------------------

# ---FUNÇÃO PARA CLICAR E MOSTRAR O NÚMERO NO VISOR---------------------
def clicarbotao(numero):
    atual = visor.get()  # pega o que ta mostrando (nada)
    time.sleep(0.3)
    visor.insert(END, str(atual) + str(numero))  # indexa a str (nome dado ao botão) e o número no visor




def deletandovisor():
    visor.delete(0, END)  # deleta o que estava mostrando antes

# ----------------------------------------FUNÇÕES PARA AS OPERÇÕES------------------------------------------------------

def clicandoemsoma():
    numero_natela=visor.get()
    global p_numero #variaveis auxiliares
    global operacao_matematica #variaveis auxiliares
    operacao_matematica= 'soma'
    p_numero= float(numero_natela)
    visor.delete(0, END)

def clicandoemmultiplicar():
    numero_natela=visor.get()
    global p_numero
    global operacao_matematica
    operacao_matematica = 'multiplicar'
    p_numero= float(numero_natela)
    visor.delete(0,END)

def clicandoemsubtracao():
    numero_natela=visor.get()
    global p_numero
    global operacao_matematica
    operacao_matematica= 'subtracao'
    p_numero=float(numero_natela)
    visor.delete(0,END)

def clicandoemdivisao():
    numero_natela=visor.get()
    global p_numero
    global opercaomatematica
    operacaomatematica= 'divisao'
    p_numero=float(numero_natela)
    visor.delete(0,END)

# -----------------------------------------FUNÇÃO PARA O RESULTADO------------------------------------------------------
def resultado():
    segundo_numero = visor.get()
    visor.delete(0,END)
    if (operacao_matematica == 'soma'):
        visor.insert(0, p_numero + float(segundo_numero))
    if (operacao_matematica == 'multiplicar'):
        visor.insert(0, p_numero * float(segundo_numero))
    if (operacao_matematica == 'subtracao'):
        visor.insert(0, p_numero - float(segundo_numero))
    if (operacao_matematica == 'divisao'):
        visor.insert(0, p_numero / float(segundo_numero))



# ------------------------------BOTÕES PARA OS NÚMEROS E SUAS DIMENSÕES-------------------------------------------------

# botão para o  número 7
botao7 = Button(tela, text="7", bg="lightblue", pady=16, padx=16, bd=5, command=lambda: clicarbotao(
    7))  # usando o comando lambda para retornar a função para o respectivo número
botao7.place(x=10, y=100,)  # COORDENADAS DO BOTÃO NOS EIXOS X E Y

# botão para o número 4
botao4 = Button(tela, text="4", bg="lightblue", pady=16, padx=16, bd=5,
                command=lambda: clicarbotao(4))  # usando o comando lambda para retornar a função para o
botao4.place(x=10, y=158)

# botão para o número 1
botao1 = Button(tela, text="1", bg="lightblue", pady=16, padx=16, bd=5,
                command=lambda: clicarbotao(1))  # usando o comando lambda para retornar a função para o
botao1.place(x=10, y=216)

# botão para o número 0
botao0 = Button(tela, text="0", bg="lightblue", pady=16, padx=90, bd=8,
                command=lambda: clicarbotao(0))  # usando o comando lambda para retornar a função para o
botao0.place(x=10, y=280)

# botão para o número 8
botao8 = Button(tela, text="8", bg="lightblue", pady=15, padx=15, bd=4.5,
                command=lambda: clicarbotao(8))  # usando o comando lambda para retornar a função para o
botao8.place(x=64, y=100)

# botão para o número 5
botao5 = Button(tela, text="5", bg="lightblue", pady=15, padx=15, bd=5,
                command=lambda: clicarbotao(5))  # usando o comando lambda para retornar a função para o
botao5.place(x=65, y=160)

# botão para o número 2
botao2 = Button(tela, text="2", bg="lightblue", pady=16, padx=16, bd=4.5,
                command=lambda: clicarbotao(2))  # usando o comando lambda para retornar a função para o
botao2.place(x=65, y=216)

# botão para o número 9
botao9 = Button(tela, text="9", bg="lightblue", pady=15, padx=15, bd=5,
                command=lambda: clicarbotao(9))  # usando o comando lambda para retornar a função para o
botao9.place(x=116, y=100)

# botão para o número 6
botao6 = Button(tela, text="6", bg="lightblue", pady=15, padx=15, bd=5,
                command=lambda: clicarbotao(6))  # usando o comando lambda para retornar a função para o
botao6.place(x=116.5, y=160)

# botão para o número 3
botao3 = Button(tela, text="3", bg="lightblue", pady=15, padx=15, bd=5,
                command=lambda: clicarbotao(3))  # usando o comando lambda para retornar a função para o
botao3.place(x=117, y=218)

# _______________________________________BOTÕES DAS OPERAÇÕES E SUAS DIMENSÕES__________________________________________

# botão para soma
botaosoma = Button(tela, text="+", bg="lightblue", padx=15, pady=15, bd=5,command=clicandoemsoma )
botaosoma.place(x=165, y=99)

# botão para subtração
botaosubt = Button(tela, text="-", bg="lightblue", padx=15, pady=15, bd=5,command=clicandoemsubtracao)
botaosubt.place(x=167, y=161)

# botão para multiplicação
botaomult = Button(tela, text="x", bg="lightblue", padx=15, pady=15, bd=5, command=clicandoemmultiplicar)
botaomult.place(x=168, y=219)

# botão divisão
botaodivi = Button(tela, text="/", bg="lightblue", padx=15, pady=15, bd=5,command=clicandoemdivisao)
botaodivi.place(x=218, y=159)

# botao CE
botaoce = Button(tela, text="CE", bg="lightblue", padx=11.5, pady=13.5, bd=5,
                 command=deletandovisor)  # comando para retornar a função do CE
botaoce.place(x=215, y=100)

# botão enter

botaoenter = Button(tela, text="ENTER", bg="lightblue", padx=0, pady=48, bd=5, command=resultado)
botaoenter.place(x=219, y=220)

tela.mainloop()
