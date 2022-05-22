import json
import os
def limpaTerminal():
    if os.name == "nt":
        return os.system("cls")
    else:
        return os.system("clear")


def delet():
    while True:
        lista01=[]
        # lista01.clear()
        filename="estudantes01.json"
        file = open(filename, "r", encoding='utf-8')
        data = file.read()
        data = json.loads(data)
        print('-='*30)
        for index, item in enumerate(data):
            print(index, item)
            lista01.append(index)
        print('-='*30)
        while True:
            opc01 = int(input('Digite o indice para qual elemento vc deseja remover: '))
            if opc01 in lista01:
                break
            print('ERRO! Por favor, digite o indice que exista')
        del data[opc01]
        # dataedit=str(data).replace('[', '').replace(']', '').replace(', {', '').replace('}', '\n').replace('{','')
        # print(dataedit)
        file = open(filename,"w+", encoding='utf-8')
        data = json.dumps(data)
        file.write(data)
        file.close()
        while True:
            resp = str(input('Quer continuar? [S/N] ')).upper()[0]
            if resp in 'SN':
                limpaTerminal()
                break
            print('ERRO! Responda apenas S ou N.')
        if resp == 'N':
            print('-='*30)
            print('Saindo de deletar alunos')
            break
    return('-='*30)

# delet()
        
    
