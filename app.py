from utilidades import apresentar_programa, verde, vermelho, azul, amarelo, separar_por_linha
import json
from pathlib import Path
from playsound import playsound
from tabulate import TableFormat, tabulate

def criar_investimentos_inciais():
    lista_de_investimentos = [
        {
            "id": 1,
            "nome": "celular",
            "valor": 1500
        },
        {
            "id": 2,
            "nome": "geladeira",
            "valor": 1300
        },
        {
            "id": 3,
            "nome": "notebook",
            "valor": 3500
        },
        {
            "id": 4,
            "nome": "IPhone",
            "valor": 7000
        },
        {
            "id": 5,
            "nome": "Placa de Video",
            "valor": 1200
        },
        {
            "id": 6,
            "nome": "PS5",
            "valor": 4999
        }

    ]
    investimentos_json = json.dumps(lista_de_investimentos)
    Path('investimentos.json').write_text(investimentos_json)


def ler_investimentos_existentes():
    investimentos_json = Path('investimentos.json').read_text()
    investimentos = json.loads(investimentos_json)
    return investimentos


def exibir_investimento_total():
    investimentos = ler_investimentos_existentes()
    total = 0
    for investimento in investimentos:
        total = investimento['valor'] + total

    verde(f'O total investido até o momento foi de: R${total:.2f}')


def listar_investimentos(exibir_todos=False):
    
    investimentos = ler_investimentos_existentes()
    lista_de_investimentos = []
    if exibir_todos == False:
        for investimento in investimentos[0:5]:
            lista_de_investimentos.append(
                [investimento['id'], investimento['nome'], investimento['valor']])
        print(tabulate(lista_de_investimentos,
                       headers=['id', 'nome', 'valor'],tablefmt='_'))
    else:
        for investimento in investimentos:
            lista_de_investimentos.append(
                [investimento['id'], investimento['nome'], f'{investimento["valor"]:.2f}'])
        print(tabulate(lista_de_investimentos,
                       headers=['id', 'nome', 'valor']))

def listar_investimentos_em_ordem(ordem=True):
    from operator import itemgetter
    investimentos = ler_investimentos_existentes()
    lista_de_investimentos = []
    dict_de_investimentos_ids = dict()
    dict_de_investimentos_somente_valores = dict()
   
    for investimento in investimentos:
            # armazena todos os ids em um dict suas chaves sao seus respectivos nomes
            dict_de_investimentos_ids[investimento['nome']] = investimento['id'] 
            
            # armazena todos os preços em um dict suas chaves sao seus respectivos nomes
            dict_de_investimentos_somente_valores[investimento['nome']] = investimento['valor'] 

                                                                    # o itemgetter 1 coloca em ordem os valores, se fosse 0 colocaria as chaves
    ranking = sorted(dict_de_investimentos_somente_valores.items(), key=itemgetter(1), reverse=ordem) # ordena em ordem
   
    #passa os valores para o lista
    for i, value in enumerate(ranking):   
        lista_de_investimentos.append(
                    [dict_de_investimentos_ids[value[0]], value[0], f'{value[1]:.2f}'])
                                # valor do id              # nome    # preço
    print(tabulate(lista_de_investimentos,
            headers=['id', 'nome', 'valor']))
   

def apresentar_menu():
    separar_por_linha()
    verde('1 - Listar todos investimentos')
    amarelo('2 - Editar investimento existente')
    vermelho('3 - Excluir um investimento')
    verde('4 - Criar investimento')
    amarelo('5 - Listar investimentos Maior-Menor')
    vermelho('6 - Listar investimentos Menor-Maior')
    verde('7 - Limpar tela')
    opcao = input('Digite uma opção: ')
    separar_por_linha()
    return opcao


def salvar_alteracoes(investimentos):
    investimento_json = json.dumps(investimentos)
    Path('investimentos.json').write_text(investimento_json)


def editar_investimento_existente(investimento_id):
    investimentos = ler_investimentos_existentes()
    nome = input('Digite o novo nome: ')
    valor = float(input('Digite o novo valor: '))
    for investimento in investimentos:
        if investimento['id'] == investimento_id:
            if nome != '':
                investimento.update({'nome': nome})
            if valor != '':
                investimento.update({'valor': valor})
            salvar_alteracoes(investimentos)
            print(investimento)


def excluir_investimento(investimento_id):
    investimentos = ler_investimentos_existentes()
    for indice, item in enumerate(investimentos):
        if item['id'] == int(investimento_id):
            print(f'O investimento {item} foi excluído com sucesso!')
            del investimentos[indice]
            salvar_alteracoes(investimentos)


def obter_ultimo_id(investimentos):
    # descobrir qual foi o útlimo investimento criado
    # 1 - ler o útlimo investimento
    ultimo_investimento = investimentos[-1:]
    # 2 - Extrair a propriedade id
    ultimo_id = ultimo_investimento[0]['id']
    # 3 - Adicionar 1 ao último id
    ultimo_id += 1
    return ultimo_id


def criar_novo_investimento(nome, valor):
    # saber quais são os investimentos existentes
    investimentos = ler_investimentos_existentes()
    ultimo_id = obter_ultimo_id(investimentos)
    novo_investimento = {'id': ultimo_id, 'nome': nome, 'valor': valor}
    investimentos.append(novo_investimento)
    salvar_alteracoes(investimentos)
    verde(f'o {novo_investimento} acaba de ser criado')


    # Criar um novo investimento, usando um novo ID

if __name__ == '__main__':
    # playsound('1. Ghost Town.wav', block=False)
    apresentar_programa()
    exibir_investimento_total()
    listar_investimentos()
    # Listar todos, editar, excluir e criar
    while True:
        opcao = apresentar_menu()
        if opcao == '1':
            listar_investimentos(exibir_todos=True)
        if opcao == '2':
            investimento_id = input('Qual investimento deseja alterar:')
            editar_investimento_existente(investimento_id)
        if opcao == '3':
            investimento_id = input('Digite o id do investimento a excluir: ')
            excluir_investimento(investimento_id)
        if opcao == '4':
            nome = input('Nome do investimento: ')
            valor = float(input('Valor do investimento: '))
            criar_novo_investimento(nome, valor)
        
        if opcao == '5':
            listar_investimentos_em_ordem(True)
        
        if opcao == '6':
            listar_investimentos_em_ordem(False)
        
        if opcao == '7':
            from os import system
            system('cls')
            apresentar_programa()
            exibir_investimento_total()
            listar_investimentos()
            
