from classes import Aluno, SistemaCadastro

sistema = SistemaCadastro()

while True:
    print("\n === Menu ===")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Atualizar curso")
    print("0 - Sair")
    opcao = input("Escolha uma Opção:")

    if opcao == "1":
        nome = input("Nome:")
        matricula = input("Matricula:")
        curso = input("Curso: ")
        aluno = Aluno(nome, matricula, curso)
        sistema.adicionar_aluno(aluno)
        print("aluno cadastado com sucesso!")

    elif opcao == "2":
        print("\nLista de alunos:")
        sistema.listar_alunos()

    elif opcao == "3":
        matricula = input("Informe a matrícula do aluno: ")
        novo_curso = input("Novo curso: ")
        sistema.atualizar_curso_aluno(matricula, novo_curso)

    elif opcao == "0":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")