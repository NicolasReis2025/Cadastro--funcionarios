def mostrar_menu():
    print(
    "\n[1] Cadastrar funcionário" 
    "\n[2] Atualizar salário de um funcionário" 
    "\n[3] Remover funcionário" 
    "\n[4] Listar todos os funcionários" 
    "\n[5] Mostrar estatísticas" 
    "\n[6] Exportar para csv" 
    "\n[7] Buscar funcionário" 
    "\n[8] Sair"
    )
    
def cadastrar_funcionario(dicionario):
    try:
        matricula = int(input("Digite a matricula do funcionario: "))
        if matricula <= 0:
            print("ERRO: matrícula deve ser positiva.")
            return
    except ValueError:
        print("ERRO: a matricula precisa ser um numero positivo. Tente novamente!")
        return

    if matricula not in dicionario:
        try:
            nome = str(input("Digite o nome do(a) funcionário(a): ")).title()
            cargo = str(input(f"Digite o cargo do(a) {nome}: "))
            while True:
                salario = float(input(f"Digite o salário do(a) {nome}: [R$] "))
                if salario < 0:
                    print("ERRO: O salário não deve ser um valor negativo. Tente novamente!")
                else:
                    break
        except ValueError:
            print("Erro no valor de entrada inserido. Tente novamente!")
            return

        dicionario[matricula] = {
            "Nome": nome,
            "Cargo": cargo,
            "Salario": round(salario, 2)
            }
        
        print(f"'{nome}' cadastrado(a) com sucesso")
    else:
        print("Matricula já está cadastrada no sistema. Tente novamente!")

def atualizar_salario(matricula, dicionario):
    try:
        salario_novo = float(input("Digite o salário novo: "))
        if salario_novo < 0:
            print("ERRO: o salário deve ser um valor positivo!")
            return  
    except ValueError:
        print("ERRO: o salário precisa ser um valor válido. Tente novamente!")
        return
    
    dicionario[matricula]["Salario"] = round(salario_novo, 2)
    print("Salário atualizado com sucesso!")
    
def mostrar_funcionarios(dicionario):
    print("===== Funcionários cadastrados no sistema =====\n")
    for matricula, dados in dicionario.items():
        print(f"Matricula: {matricula} - {dados['Nome']} | {dados['Cargo']} | R${dados['Salario']}")

def remover_funcionario(dicionario):
    try:
        buscar_matricula = int(input("Digite a matricula: "))

        if buscar_matricula not in dicionario:
            print("Matricula não está cadastrada no sistema")
        else:
            resp = str(input("Tem certeza que deseja remover esse funcionário do sistema? [S/ N] ")).lower()
            if resp in ['s', 'sim']:
                del dicionario[buscar_matricula]
                print(f"Matricula '{buscar_matricula}' removida com sucesso!")
            return
    except ValueError:
            print("ERRO: a matricula deve ser um numero. Tente novamente!")
            return

def exportar_csv(dicionario):
    with open("arquivo.csv", "w") as arquivo:
        arquivo.write("Matricula, Nome, Cargo, salario\n")
        for matricula, dados in dicionario.items():
            linha = f"{matricula}, {dados['Nome']}, {dados['Cargo']}, {dados['Salario']}\n"
            arquivo.write(linha)
    
def buscar_funcionario(dicionario):
    if dicionario:
        try:
            buscar_matricula = int(input("Digite a matricula do funcionário: "))
            if buscar_matricula not in dicionario:
                print(f"A matricula '{buscar_matricula}' não está cadastrada no sistema")

            else:
                for matricula, dados in dicionario.items():
                    if buscar_matricula == matricula:
                        print(f"{matricula} - {dados['Nome']} | {dados['Cargo']} | R${dados['Salario']}") 

        except ValueError:
            print("ERRO: a matricula deve ser um numero. Tente novamente!")
            return
    else:
        print("Nenhum funcionário foi cadastrado no sistema!")
    
funcionarios = {}

while True:
    mostrar_menu()
    while True:
        try:
            opcao = int(input("Digite uma opção: "))
            if opcao not in [1, 2, 3, 4, 5, 6, 7, 8]:
                print("Opção inválida. Digite novamente!")
                continue
            break
        except ValueError:
            print("ERRO: a opção precisa ser um numero positivo. Tente novamente!")
    if opcao == 8:
        print("Programa encerrado!")
        break
    else:
        if opcao == 1:
            cadastrar_funcionario(funcionarios)
        
        elif opcao == 2:
            buscar_matricula = int(input("Digite a matricula: "))
            if buscar_matricula not in funcionarios:
                print("Matricula não está cadastrada no sistema")
            else:
                atualizar_salario(buscar_matricula, funcionarios)
        
        elif opcao == 3:
            remover_funcionario(funcionarios)
           
        elif opcao == 4:
            mostrar_funcionarios(funcionarios)
        
        elif opcao == 5:
            if not funcionarios:
                print("Não há funcionários cadastrados no sistema!")
            else:
                print("\n===== Análise de dados =====")
                max_salario = max(funcionarios.items(), key = lambda x: x[1]['Salario'])
                min_salario = min(funcionarios.items(), key = lambda x: x[1]['Salario'])

                media_salarial = round(sum(dados['Salario'] for dados in funcionarios.values()) / len(funcionarios), 2)

                acima_media_salarial = len([dados['Salario'] for dados in funcionarios.values() if dados['Salario'] > media_salarial])
                percentual_acima_media = round(acima_media_salarial / len(funcionarios) * 100, 2)

                cargos = {}

                
                for dados in funcionarios.values():
                    cargo = dados['Cargo']
                    if cargo in cargos:
                        cargos[cargo] += 1
                    else:
                        cargos[cargo] = 1


                print(f"Maior salário: {max_salario[1]['Nome']} | R${max_salario[1]['Salario']}")
                print(f"Menor salário: {min_salario[1]['Nome']} | R${min_salario[1]['Salario']}")
                print(f"Média salarial dos funcionários: R${media_salarial}")
                print(f"Total de funcionários com salários acima da média: {acima_media_salarial} -> {percentual_acima_media}% sobre o total ")
                print(f"\nQuantidade de funcionários por cargo:")
                for nome_cargo, total in cargos.items():
                    print(f"{nome_cargo}: {total}")
        
        elif opcao == 6:
            exportar_csv(funcionarios)
            print("Arquivo csv exportado com sucesso!")
        
        elif opcao == 7:
            buscar_funcionario(funcionarios)

                        




                



            
