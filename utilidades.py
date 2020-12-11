def separar_por_linha():
    print('-'*82)


def vermelho(palavra):
    print(palavra)  


def verde(palavra):
    print(palavra)


def amarelo(palavra):
    print(palavra)


def azul(palavra):
    print(palavra)


def apresentar_programa():
    '''
    CORES ANSII
    vermelha \u001b[31m
    verde \u001b[32m
    amarela \u001b[33m
    azul \u001b[34m

    \u001b[0m'
    '''
    separar_por_linha()
    print('''
        ██ ███    ██ ██    ██ ██ ███████ ████████  █████        ███    ███ ███████ 
        ██ ████   ██ ██    ██ ██ ██         ██    ██   ██       ████  ████ ██       ___   ___ 
        ██ ██ ██  ██ ██    ██ ██ ███████    ██    ███████ █████ ██ ████ ██ █████   |_  | |   |
        ██ ██  ██ ██  ██  ██  ██      ██    ██    ██   ██       ██  ██  ██ ██      |  _|_| | |
        ██ ██  ██ ██  ██  ██  ██      ██    ██    ██   ██       ██  ██  ██ ██      |___|_|___|
        ██ ██   ████   ████   ██ ███████    ██    ██   ██       ██      ██ ███████''')
    print(' '*35 + 'Pronto para investir?')
    separar_por_linha()
