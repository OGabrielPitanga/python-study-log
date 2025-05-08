class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
    
    def atualizar_curso(self, novo_curso):
        self.curso = novo_curso

    def __str__(self):
        return f"{self.nome} | Matrícula {self.matricula} | Curso: {self.curso}"
    
class SistemaCadastro:
    def __init__(self):
        self.alunos = []
    
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    
    def listar_alunos(self):
        for aluno in self.alunos:
            print(aluno)
    
    def atualizar_curso_aluno(self, matricula, novo_curso):
            for aluno in self.alunos:
                if aluno.matricula == matricula:
                    aluno.atualizar_curso(novo_curso)
                    print("Curso atualizado.")
                    return
                print("Aluno não encontrado")