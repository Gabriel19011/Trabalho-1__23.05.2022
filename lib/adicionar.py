import json
import os

estudantes = list()
aluno = dict()


def limpaTerminal():
    if os.name == "nt":
        return os.system("cls")
    else:
        return os.system("clear")


def inserir01():
    while True:
        limpaTerminal()
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
        data.append(aluno)
        
        filename="estudantes01.json"
        file = open(filename,"w+", encoding='utf-8')
        data = json.dumps(data)
        file.write(data)
        file.close()

        while True:
            resp = str(input('Quer continuar? [S/N] ')).upper()[0]
            # limpaTerminal()
            if resp in 'SN':
                break
            print('ERRO! Responda apenas S ou N.')
        if resp == 'N':
            print('-='*30)
            print('Saindo do adicionar')
            break
    return('-='*30)


# inserir01()

