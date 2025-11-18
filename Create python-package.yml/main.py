# main.py
from typing import List
import aluno as a
import turma as t


def montar_alunos() -> List[a.Aluno]:
    candidatos = [
        ("Fabio", "Teixeira", 11),
        ("Fabiano", "Teixeira", 7),
        ("Melissa", "Teixeira", 8),
        ("Rafael", "Teixeira", 9),
        ("Angela", "Teixeira", 6),
    ]

    alunos: List[a.Aluno] = []
    for nome, sobrenome, nota in candidatos:
        try:
            alunos.append(a.Aluno(nome, sobrenome, nota))
        except (TypeError, ValueError) as exc:
            # Ignora/altera alunos inválidos e informa no console
            print(f"Atenção: não foi possível criar Aluno({nome} {sobrenome}, {nota}): {exc}")
    return alunos


def imprimir_resultados(turma_obj: t.Turma) -> None:
    print("=" * 40)
    print("Lista de alunos:")
    turma_obj.mostrar_alunos()

    print("\n" + "-" * 40)
    menor = turma_obj.menor_nota
    maior = turma_obj.maior_nota

    if menor:
        print("Aluno com menor nota:", menor.mostrar_aluno())
    else:
        print("Nenhum aluno encontrado para menor nota")

    if maior:
        print("Aluno com maior nota:", maior.mostrar_aluno())
    else:
        print("Nenhum aluno encontrado para maior nota")


if __name__ == "__main__":
    alunos = montar_alunos()
    turma_obj = t.Turma()
    turma_obj.cadastrar_alunos(alunos)
    imprimir_resultados(turma_obj)
