import os
import json

estudantes = list()
aluno = dict()

def limpaTerminal():
    if os.name == "nt":
        return os.system("cls")
    else:
        return os.system("clear")

def update():
    while True:
        lista=[]
        # lista.clear()
        file = open("estudantes01.json", "r", encoding='utf-8')
        data = file.read()
        data = json.loads(data)
        
        print('-'*42)
        for index, item in enumerate(data):
            print(index, item)
            lista.append(index)
        print('-'*42)
        
        while True:
            opc02=int(input('Digite o indice: '))
            if opc02 in lista:
                break
            print('ERRO! Por favor, digite o indice que exista')
        aluno.clear()
        aluno['nome'] = str(input('Nome: '))
        while True:
            aluno['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
            if aluno['sexo'] in 'MF':
                break
            print('ERRO! Por favor, digite apenas M ou F.')
        aluno['idade'] = int(input('Idade: '))

        while True:
            aluno['cpf'] = str(input('CPF: [xxx.xxx.xxx-xx] '))
            if len(aluno['cpf'].replace('.','').replace('-',''))==11:
                break
            print('ERRO! Por favor, digite o CPF corretamente.')

        aluno['materia'] = str(input(f'Digite a materia do {aluno["nome"]}: '))
        aluno['nota'] = float(input(f'Digite a nota do {aluno["nome"]}: '))
        

        filename="estudantes01.json"
        file = open(filename, "r", encoding='utf-8')
        data = file.read()
        data = json.loads(data)
        del data[opc02]
        data.insert(opc02,aluno)
        
        
        filename="estudantes01.json"
        file = open(filename,"w+", encoding='utf-8')
        data = json.dumps(data)
        file.write(data)
        file.close()

        while True:
            resp = str(input('Quer continuar? [S/N] ')).upper()[0]
            # limpaTerminal()
            if resp in 'SN':
                limpaTerminal()
                break
            print('ERRO! Responda apenas S ou N.')
        if resp == 'N':
            print('-='*30)
            print('Saindo de atualizar alunos')
            break 
    return('-='*30)


# update()

