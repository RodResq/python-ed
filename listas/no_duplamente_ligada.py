
class NoDuplamenteLigada():
    def __init__(self, elemento, proximo = None, anterior = None):
        self.elemento = elemento
        self.proximo = proximo
        self.anterior = anterior

        @property
        def elemento(self):
            return self.elemento

        @elemento.setter
        def elemento(self, elemento):
            self.elemento = elemento

        @property
        def proximo(self):
            return self.proximo

        @proximo.setter
        def proximo(self, proximo):
            self.proximo = proximo

        @property
        def anterior(self):
            return self.anterior

        @proximo.setter
        def anterior(self, anterior):
            self.anterior = anterior
