# Um professor quer sortear um de quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o do escolhido.
from random import choice
alunos = ("José", "Marcelo", "Pedro", "Marcos")
print(f"O aluno escolhido foi {choice(alunos)}")
