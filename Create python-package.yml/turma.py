from typing import List, Optional
from dataclasses import dataclass, field
import aluno as a


@dataclass
class Turma:
    alunos: List[a.Aluno] = field(default_factory=list)

    def cadastrar_alunos(self, novos: List[a.Aluno]) -> None:
        """Adiciona alunos válidos (nota entre 0 e 10) à turma e preserva ordem de inserção."""
        for aluno in novos:
            # aceita objetos Aluno e ignora entradas inválidas
            if not isinstance(aluno, a.Aluno):
                continue
            if 0.0 <= aluno.nota <= 10.0:
                self.alunos.append(aluno)

    @property
    def menor_nota(self) -> Optional[a.Aluno]:
        """Retorna o aluno com menor nota ou None se a turma estiver vazia."""
        if not self.alunos:
            return None
        return min(self.alunos, key=lambda s: s.nota)

    @property
    def maior_nota(self) -> Optional[a.Aluno]:
        """Retorna o aluno com maior nota ou None se a turma estiver vazia."""
        if not self.alunos:
            return None
        return max(self.alunos, key=lambda s: s.nota)

    def listar_alunos(self) -> List[str]:
        """Retorna lista com representações de cada aluno (usa Aluno.__str__)."""
        return [str(aluno) for aluno in self.alunos]

    def imprimir_alunos(self) -> None:
        """Imprime resumo e a lista de alunos."""
        print(f"Quantidade de alunos: {len(self.alunos)}")
        if not self.alunos:
            print("Nenhum aluno cadastrado.")
            return
        for aluno in self.alunos:
            print(str(aluno))
