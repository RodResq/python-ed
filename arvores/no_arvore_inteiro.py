from arvores import no_arvore

class NoArvoreInteriro(no_arvore.NoArvore):
    def __init__(self, valor):
        super().__init__(valor)

    def peso(self):
        return self.valor
