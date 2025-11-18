# test_turma.py
import unittest
import aluno as a
import turma as t


class TestTurma(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Dados de entrada com alguns valores inválidos para garantir que sejam ignorados
        cls.candidatos = [
            ("Fabio", "Teixeira", 11),    # inválido (nota > 10)
            ("Fabiano", "Teixeira", 7),
            ("Melissa", "Teixeira", 8),
            ("Rafael", "Teixeira", 9),
            ("Angela", "Teixeira", 6),
            ("Joao", "Silva", -1),        # inválido (nota < 0)
        ]

    def setUp(self):
        # cria objetos Aluno e instancia Turma antes de cada teste
        self.alunos = []
        for nome, sobrenome, nota in self.candidatos:
            try:
                self.alunos.append(a.Aluno(nome, sobrenome, nota))
            except (TypeError, ValueError):
                # Alunos com notas inválidas serão ignorados na lista inicial
                pass

        self.turma = t.Turma()
        self.turma.cadastrar_alunos(self.alunos)

    def test_quantidade_alunos_valida(self):
        # apenas 4 alunos válidos na lista acima (11 e -1 inválidos)
        esperados_validos = 4
        self.assertEqual(
            esperados_validos,
            len(self.turma.alunos),
            f"Esperado {esperados_validos} alunos válidos, encontrado {len(self.turma.alunos)}",
        )

    def test_maior_nota(self):
        maior = self.turma.maior_nota
        self.assertIsNotNone(maior, "maior_nota não deve ser None quando há alunos")
        self.assertEqual(9.0, maior.nota, "Erro ao identificar maior nota")

    def test_menor_nota(self):
        menor = self.turma.menor_nota
        self.assertIsNotNone(menor, "menor_nota não deve ser None quando há alunos")
        self.assertEqual(6.0, menor.nota, "Erro ao identificar menor nota")

    def test_intervalo_notas_validas(self):
        menor = self.turma.menor_nota
        maior = self.turma.maior_nota
        self.assertTrue(
            0.0 <= menor.nota <= 10.0 and 0.0 <= maior.nota <= 10.0,
            "Notas devem estar no intervalo de 0.0 a 10.0",
        )


if __name__ == "__main__":
    unittest.main()
