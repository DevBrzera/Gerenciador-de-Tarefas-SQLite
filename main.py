import os
import database
from datetime import datetime

os.system('cls')

system = True

print('============================')
print('GERENCIADOR DE TAREFAS')
print('============================')

database.Create_Table()

name = input("Digite o nome para criar a Tabela: ")
nameTabela = " ".join(name.split())
database.Insert_Table(name)

os.system('cls')

def Menu():
    global system
    while system:
        print('============================')
        print('GERENCIADOR DE TAREFAS')
        print('============================')

        print(f'TABELA: {nameTabela}')

        op = int( input('1) Inserir Tarefa\n2) Listar Tarefas\n3) Remover Tarefa\n4) Editar Tarefa\n5) Sair\n--> ') )

        if op == 1:
            database.Insert_Task(
                description = input('Digite o nome da tarefa: '),
                date = datetime.now(),
                tableId = 1
            )
            print('Tarefa criada com sucesso!')

        elif op == 2:
            database.Select_Task()

        elif op == 3:
            database.Delete_Task(
                id = int(input('Digite o ID da tarefa para remover: '))
            )
            print('Tarefa deletada com sucesso!')

        elif op == 4:
            database.Update_Task(
                id = int(input('Digite o ID da tarefa para editar: ')),
                    description = input('Digite a nova descrição da tarefa: '),
                )
            print('Tarefa editada com sucesso!')

        elif op == 5:
            print('Saindo...')
            system = False
            exit()

        else:
            print('Opção inválida!')
            Menu()

Menu()
    

    


