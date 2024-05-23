from conectar_db import *
from conta import *


def alterar(conta):
    sql = "update conta set saldo = %s where id = %s;"
    connection_string = conectar()
    cursor = connection_string.cursor()
    try:
        cursor.execute(sql, (conta.id, conta.id))
        connection_string.commit()
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
        desconectar(connection_string)


def excluir(conta):
    sql = "delete from conta where id = %s;"
    connection_string = conectar()
    cursor = connection_string.cursor()
    try:
        cursor.execute(sql, (conta.id,))
        connection_string.commit()
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
        desconectar(connection_string)



def incluir(conta):
    sql = "insert into conta (nome, saldo) values (%s, %s);"
    connection_string = conectar()
    cursor = connection_string.cursor()
    try:
        cursor.execute(sql, (conta.nome, conta.saldo))
        connection_string.commit()
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
        desconectar(connection_string)


def consultar_conta_id(id):
    sql = "select * from conta where id = %s;"
    connection_string = conectar()
    cursor = connection_string.cursor()
    conta = None
    try:
        cursor.execute(sql, (id,))
        registro = cursor.fetchall()
        if (registro):
            conta = Conta(registro[0][0], registro[0][1], registro[0][2])

    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
        desconectar(connection_string)
    return conta



def consultar_contas():
    sql = "select * from conta;"
    connection_string = conectar()
    cursor = connection_string.cursor()
    contas = []
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            conta = Conta(registro[0], registro[1], registro[2])
            contas.append(conta)
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
        desconectar(connection_string)
    return contas