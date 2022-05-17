

O programa de simulação de um controle de estoque foi feito pelo Aluno Guilherme Dos Santos Modesto Teixeira do curso de Sistemas de Informações da Universidade do Estado da Bahia (UNEB), utilizando conceitos básicos (if,listas,função time e upper) em linguagem python


import time #FUNÇÃO TEMPO

produton=["A","B",] #LISTA DOS FUNCIONÁRIOS CADASTRADOS PARA O ACESSO 

func=["GUI","ROBERTO","MARIA"]#LISTA DOS PRODUTOS DISPONÍVEIS PARA RETIRADA
time.sleep(1)
print("|=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=|")
time.sleep(1.2)
print("|                                     |")
time.sleep(1.2)
print("|  BEM VINDO AO CONTROLE DE ESTOQUE   |")
time.sleep(1.2)
print("|                                     |")
time.sleep(1.2)
print("|=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=|")
time.sleep(1)
print("\n\n\n============================================================================================================================================================================================================================================================================================================================================================================")
time.sleep(1.5)
print("SIGA AS INSTRUÇÕES ABAIXO: ") #INSTRUÇÕES DE USO E "SEGURANÇA", A ÚLTIMA FEITA COM IF JUSTAMENTE PARA EVITAR CONSULTA DE MAIS DE UM PRODUTO POR VEZ 
time.sleep(3)
print("\n1)POR QUESTÕES DE SEGURANÇA VOCÊ SÓ PODE CONSULTAR UM PRODUTO POR VEZ\n2)O PROGRAMA SERA REINICIADO SE O CAMPO DE SELEÇÃO DO PRODUTO, NOME DO FUNCIONARIO OU A QUANTIDADE DE PRODUTOS FOR INCOMPATÍVEL COM A LISTA DE CONSULTA DO FUNCIONARIO FOREM FEITOS DE FORMA ERRADA APÓS A PRIMEIRA TENTATIVA\n")
time.sleep(1.5)
print("============================================================================================================================================================================================================================================================================================================================================================================")
time.sleep(4.5)
print("DIGÍTE SEU NOME PARA CADASTRO ABAIXO ")
time.sleep(1.5)

x=str(input("NOME: ")).upper() #USO DA FUNÇÃO UPPER AFIM DE FACILITAR O ACESSO 
if(x not in func):
    time.sleep(1)
    print("PROCESSANDO.........\n")
    time.sleep(1.5)
    print("###CADASTRO INVÁLIDO### \n\n")
    time.sleep(1.5)
    x=str(input("NOME: ")).upper() #USO DA FUNÇÃO UPPER AFIM DE FACILITAR O ACESSO
else:
    print("PROCESSANDO.........\n")
    time.sleep(1.5)
    print("\nCADASTRO VALIDADO\n")
    time.sleep(1.5)



produto=str(input("QUAL PRODUTO VOCÊ DESEJA CONSULTAR: ")).upper() #USO DA FUNÇÃO UPPER AFIM DE FACILITAR O ACESSO

if(produto in produton or produto==a or produto==b): #USO DO IF DE FORMA SIMULTÂNEA,SIMULANDO PRODUTOS DIFERENTES COM MESMA QUANTIDADE
    print("PROCURANDO......\n")
    time.sleep(3)
    print("=======================================================================================")
    time.sleep(1.5)
    print("VOCÊ SELECIONOU O PRODUTO INDICADO ABAIXO...")
    time.sleep(1.5)
    print(produto)
    time.sleep(1.5)
    print("O PRODUTO APRESENTA 100 UNIDADES EM ESTOQUE ")
    time.sleep(1.5)
    print("=======================================================================================")
    time.sleep(1)
    retirada=int(input(("DIGÍTE A QUANTIDADE QUE DESEJA RETIRAR: ")))
if(retirada>100): #USO DO IF PARA QUE NÃO SEJA POSSÍVEL RETIRAR UM NÚMERO MAIOR QUE A QUANTIDADE DISPONÍVEL DO PRODUTO
    print("#### INVALIDO ####")
    input()
else: #QUANDO A "RETIRADA" FOR POSSÍVEL
    ret=100-retirada
    time.sleep(1.5)
    print("PEGANDO A CALCULADORA.....\n\n")
    time.sleep(2.5)
    print("SOBRARAM EM ESTOQUE: ")
    time.sleep(1.5)
    print(ret)
    time.sleep(1.5)
    print("======================================================================================")
if(ret<50): #QUANDO A QUANTIDADE RETIRADA FOR MUITA É AVISADO QUE HÁ POUCOS PRODUTOS NO ESTOQUE 
    print("POUCAS QUANTIDADES EM ESTOQUE, FAVOR TRATAR COM O SETOR DE FORNECIMENTO")
    time.sleep(1.5)
    print("======================================================================================")
time.sleep(10)

input()
