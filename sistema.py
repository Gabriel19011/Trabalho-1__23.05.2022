#Um programa para inserir o nome do aluno, cpf, sexo, idade, materia que cursa, nota dessa materia. 
# Podendo alterar o nome, cpf,  idade, sexo , materia que cursa, a nota dessa materia.

import json
from lib.interface import*
from time import sleep
limpaTerminal()
heard('Seja Bem Vindo')
sleep(2)

while True:
    limpaTerminal()
    resposta = menu(['Adicionar novos alunos', 'Quantidade de alunos cadastrados', 'Ver alunos cadastrados','Alterar alunos', 'Deletar alunos', 'Creditos', 'Sair'])
    if resposta == 1:
        # limpaTerminal()
        heard('Adicionar novos alunos')
        from lib.adicionar import inserir01 
        print(inserir01())
    elif resposta == 2:
        limpaTerminal()
        heard('Quantidade de alunos cadastrados')

        file = open("estudantes01.json", "r", encoding='utf-8')
        data = file.read()
        data = json.loads(data)

        print(f'Ao todo temos {len(data)} alunos cadastrados')
        print(linha())
    elif resposta == 3:
        limpaTerminal()
        heard('Ver alunos cadastrados')
        file = open("estudantes01.json", "r", encoding='utf-8')
        data = file.read()
        data = json.loads(data)
        dataedit=str(data).replace('[', '').replace(']', '').replace(', {', '').replace('}', '\n').replace('{','')
        print(dataedit)
        print(linha())
    elif resposta == 4:
        limpaTerminal()
        heard('Alterar alunos')
        from lib.atualiza import update
        print(update())
    elif resposta == 5:
        limpaTerminal()
        heard('Deletar alunos')
        from lib.deletar import delet
        print(delet())
        
    elif resposta == 6:
        limpaTerminal()
        heard('Creditos')
        from lib.creditos import baseDeEstudo
        print(baseDeEstudo())
    elif resposta == 7:
        limpaTerminal()
        heard('Saindo do Sistema')
        break
    else:
        limpaTerminal()
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(3)
    






