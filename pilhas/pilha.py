from listas import lista_duplamente_ligada

class Pilha():
    def __init__(self):
        self.elementos = lista_duplamente_ligada.ListaDuplamenteLigada()

    def empilhar(self, elemento):
        self.elementos.inserir(elemento)

    def esta_vazia(self):
        return self.elementos.esta_vazia()

    def desempilhar(self):
        if self.esta_vazia():
            return None
        resultado = self.elementos.recuperar_elemento_no(self.elementos.tamanho -1)
        self.elementos.remover_posicao(self.elementos.tamanho -1)
        return  resultado
