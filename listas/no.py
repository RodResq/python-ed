
class No():
    def __init__(self, elemento, proximo = None):
        self.elemento = elemento
        self.proximo = proximo

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
