import time

chamados = []
inicio_tempo = time.time()

def abertura_chamado() -> str:
    while True:
        try:
            id_chamado = input("Informe o ID do problema (8 dígitos): ").strip()
            if len(id_chamado) != 8 or not id_chamado.isdigit():
                print("Por favor, forneça um ID válido com exatamente 8 dígitos. Tente novamente!")
                continue

            ordem_prioridade = int(input("Qual a prioridade do chamado numa escala de 1 a 5?\n(1 = baixa prioridade, 5 = alta prioridade): ").strip())
            if ordem_prioridade not in range(1, 6):
                print("A prioridade deve estar entre 1 e 5. Tente novamente!")
                continue
            info_user = {"id": int(id_chamado), "prioridade": ordem_prioridade}
            chamados.append(info_user)
            return f"O chamado {id_chamado} foi registrado com sucesso!"

        except ValueError:
            print("Entrada inválida. Tente novamente!")

def buscar_chamado() -> dict:
    while True:
        try:
            pesquisar_chamado = int(input("Insira a ID do chamado que deseja buscar: ").strip())
            for info_user in chamados:
                if info_user["id"] == pesquisar_chamado:
                    print(f"O chamado {pesquisar_chamado} foi localizado com sucesso!")
                    return info_user
            print("Chamado não encontrado.")
            return None
        
        except ValueError:
            print("Erro: ID inválido.")
            return None

def remover_chamado():
    chamado_concluido = input("Deseja remover um chamado? (S/N): ").strip().upper()
    if chamado_concluido == "S":
        chamado_encontrado = buscar_chamado()
        if chamado_encontrado:
            chamados.remove(chamado_encontrado)
            print("Chamado removido com sucesso.")
        else:
            print("Não foi possível remover o chamado.")
    elif chamado_concluido == "N":
        print("Ok, chamado não excluído.")
    else:
        print("Resposta inválida! Tente novamente.")

def ordem_prioridade():
    if chamados:
        chamados.sort(key=lambda x: x["prioridade"], reverse=True)
        print("Chamados ordenados por prioridade:")
        for info_user in chamados:
            print(f"ID: {info_user['id']} | Prioridade: {info_user['prioridade']}")
    else:
        print("Não há chamados para ordenar.")

def ordem_reversa(): #é a mesma coisa do ordem_prioridade, só que sem o reverse
    if chamados:
        chamados.sort(key=lambda x: x["prioridade"])
        print("Chamados ordenados por imprioridade:")
        for info_user in chamados:
            print(f"ID: {info_user['id']} | Prioridade: {info_user['prioridade']}")
    else:
        print("Não há chamados para ordenar.")

def resolver_chamado():
    while True:
        user_request = input("Para o seu problema é necessário enviar técnicos para resolver?\n(S/N): ").strip().upper()

        if user_request == "S":
            print("Estamos enviando técnicos para seu ambiente de trabalho...")
            print("A caminho", end="", flush=True)
            for _ in range(3):
                time.sleep(1)
                print(".", end="", flush=True)
            print("\nConcluído!")
            break
        elif user_request == "N":
            print("Resolve sozinho então ser humano mortal efemero.")
            break
        else:
            print("Resposta inválida. Digite apenas 'S' ou 'N'.")

    fim_tempo = time.time()
    total_chamados = len(chamados)

    if total_chamados > 0:
        tempo_resolucao = round(fim_tempo - inicio_tempo, 2)
        return f"Total de chamados: {total_chamados}\nTempo de resolução: {tempo_resolucao} segundos."
    else:
        print("Nenhum chamado foi registrado até o momento.")

def limpar_reverter_chamados():
    opcao = input("Deseja limpar todos os chamados? (S/N): ").strip().upper()
    if opcao == "S":
        chamados.clear()
        print("Todos os chamados foram removidos.")
    else:
        print("Nenhuma alteração feita.")

def menu(): #o menu ta meio frufru mas ta bonitinho
    while True:
        try:
            print(f"""\nMenu de opções: 
*¨¨*¨¨*¨¨*¨¨*¨¨*¨¨*¨¨*¨¨*¨¨*¨¨*¨¨*¨¨*¨*
* 1 - Abrir chamado                   *
* 2 - Buscar chamado                  *    
* 3 - Remover chamado                 *    
* 4 - Ordenar chamados por prioridade * 
* 5 - Resolver chamado                *   
* 6 - Limpar todos os chamados        *       
* 7 - Reverter ordem dos chamados     *    
* 8 - Sair                            *
*¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨*""")
            opcao = input("Escolha uma opção: ").strip()
            if opcao == "1":
                abertura_chamado()
            elif opcao == "2":
                buscar_chamado()
            elif opcao == "3":
                remover_chamado()
            elif opcao == "4":
                ordem_prioridade()
            elif opcao == "5":
                resolver_chamado()
            elif opcao == "6":
                limpar_reverter_chamados()
            elif opcao == "7":
                ordem_reversa()
            elif opcao == "8":
                print("Adeus.")
                break
            else:
                print("Escolha um número APENAS de 1 a 7.")
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente!")
menu()