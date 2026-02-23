def dicionario_aluno():

  nome = input()
  matricula = int(input())
  nota1 = float(input())
  nota2 = float(input())
  nota3 = float(input())

  media = (nota1 + nota2 + nota3) / 3

  aluno ={
    "Nome": nome,
    "Matrícula": matricula,
    "Média": media
  }

  return aluno

aluno = dicionario_aluno()
print(f"Nome: {aluno['Nome']}")
print(f"Matrícula: {aluno['Matrícula']}")
print(f"Média: {aluno['Média']:.2f}")