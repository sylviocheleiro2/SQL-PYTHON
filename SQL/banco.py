from crud import *
from menu import *

FIM = 6
opcao = entrar_opcao()

while (opcao != FIM):
    match (opcao):
        case 1:
            incluir_conta()
        case 2:
            alterar_conta()
        case 3:
            excluir_conta()
        case 4:
            consultar_conta()
        case 5:
            consultar_todas()
        case 6:
            print("Saindo...")
        case other:
            print("Opção invalida")
    opcao = entrar_opcao()
# consultar_todas()
# consultar_conta()

# excluir_conta()


 