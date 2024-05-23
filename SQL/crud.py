from crud_db import *

def incluir_conta():
    nome = input("Entre com o nome: ")
    saldo = float(input("Entre com o saldo: "))
    conta = Conta(0, nome, saldo)
    incluir(conta)

def alterar_conta():
    id = input("Entre com o numero da conta: ")
    conta = consultar_conta_id(id)
    if (conta):
        oper = int(input(" [1] - Credito ou [2] - Debito"))
        valor = float(input("Entre com o valor: "))
        if (oper == 1):
            conta.creditar(valor)
        elif (oper == 2):
            conta.debitar(valor)
        else:
            print("operacao invalida")
        alterar(conta)
    else:
        print("Erro: Conta não existe")


def excluir_conta():
    id = input("Entre com o numero da conta: ")
    conta = consultar_conta_id(id)
    if (conta):
        excluir(conta)
    else:
        print("Erro: Conta não existe")


def consultar_todas():
    contas = consultar_contas()
    for conta in contas:
        print(conta)

def consultar_conta():
    id = input("Entre com o numero da conta: ")
    conta = consultar_conta_id(id)
    if (conta):
        print(conta)
    else:
        print("Erro: Conta não existe")