from dataclasses import dataclass, field
from typing import Any
import functools

@functools.total_ordering
@dataclass
class Aluno:
    nome: str
    sobrenome: str
    nota: float = field(default=0.0)

    def __post_init__(self) -> None:
        # Normaliza strings
        if not isinstance(self.nome, str) or not isinstance(self.sobrenome, str):
            raise TypeError("nome e sobrenome devem ser strings")
        self.nome = self.nome.strip()
        self.sobrenome = self.sobrenome.strip()

        # Valida nota e converte para float
        try:
            self.nota = float(self.nota)
        except (TypeError, ValueError):
            raise TypeError("nota deve ser um número (int ou float)")

        if not (0.0 <= self.nota <= 10.0):
            raise ValueError("nota deve estar entre 0.0 e 10.0")

    def __str__(self) -> str:
        return f"Aluno: {self.nome} {self.sobrenome} - Nota: {self.nota:.2f}"

    def __repr__(self) -> str:
        return f"Aluno(nome={self.nome!r}, sobrenome={self.sobrenome!r}, nota={self.nota!r})"

    def mostrar_aluno(self) -> str:
        return str(self)

    # Implementa comparação por nota (maior nota => maior)
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Aluno):
            return NotImplemented
        return self.nota == other.nota

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, Aluno):
            return NotImplemented
        return self.nota < other.nota
