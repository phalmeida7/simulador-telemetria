from colorama import init, Fore, Back, Style
init(autoreset=True)

def menu():
    print("Gerenciador de Tarefas:")
    print("\n1. Adicionar tarefa")
    print("2. Listar tarefa")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Sair")

def executar():
    tarefas = []

    while True:
        menu()
        opcao = input("\nEscolha uma opção (1-5): ")

        if opcao == "1":
            descricao = input("Digite a descrição da tarefa: ").strip()

            if descricao:
                tarefa1 = {"descricao": descricao, "concluida": False}
                tarefas.append(tarefa1)
                print(f"Tarefa {descricao} adicionada com sucesso!")

            else:
                print(Style.BRIGHT + Fore.RED + "A descrição não pode estar vazia!")

        elif opcao == "2":
            if not tarefas:
                print(Style.BRIGHT + Fore.RED + "Ainda não há tarefas!")
            else:
                print("\n Suas tarefas:")
                for i, tarefa in enumerate(tarefas, start=1):
                    status = "✅" if tarefa["concluida"] else "❌"
                    print (f"{i}. [{status}] {tarefa['descricao']}")

        elif opcao == "3":
            if not tarefas:
                print("Ainda não existem tarefas para concluir.")
                
            else:
                for i, tarefa in enumerate(tarefas, start=1):
                    status = "✅" if tarefa["concluida"] else "❌"
                    print (f"{i}. [{status}] {tarefa['descricao']}")
                try: 
                    escolha = int(input("\nDigite o número da tarefa concluída: "))

                    if 1 <= escolha <= len(tarefas):
                        indice_real = escolha - 1
                    
                        tarefas[indice_real]["concluida"] = True
                        print (f"\nTarefa '{tarefas[indice_real]['descricao']}' marcada como concluída")

                    else:
                        print(Style.BRIGHT + Fore.RED + "\n Número inválido! Essa tarefa não existe")
                
                except ValueError:
                    print("\nEntrada inválida!")
            
        elif opcao == "4":
            if not tarefas:
                print("Ainda não existem tarefas para remover.")
            
            else:
                for i, tarefa in enumerate(tarefas, start=1):
                    status = "✅" if tarefa["concluida"] else "❌"
                    print (f"{i}. [{status}] {tarefa['descricao']}")
                try:
                    escolha = int(input("\nDigite o número da tarefa que deseja remover: "))
                
                    if 1 <= escolha <= len(tarefas):
                        indice_real = escolha - 1 
                        tarefa_removida = tarefas.pop(indice_real)
                        print(f"\nTarefa '{tarefa_removida['descricao']}' removida com sucesso!")
                    else:
                        print(Style.BRIGHT + Fore.RED + "\n Número inválido: essa tarefa não existe." )

                except ValueError:
                    print(Style.BRIGHT + Fore.RED +  "Entrada inválida!")       

        elif opcao == "5":
            print(Style.BRIGHT + "Saindo do programa...")
            break
        else:
            print("Opção inválida! Somente números de 1 a 5.")

executar()


