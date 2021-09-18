from array import array
from vetores import vetores
from listas import lista_ligada, lista_duplamente_ligada
from pilhas import pilha
from filas import fila
from conjuntos import conjunto
from mapas import mapa
from arvores import arvore, no_arvore_inteiro


# vetor_inteiros = array('b', [1, 2, 3])
# print(vetor_inteiros)
# # 1 / 2 / 3 / 4
# vetor_inteiros.insert(3, 4)
# print(vetor_inteiros)
# print(vetor_inteiros.index(2))

print(30 * "-", "MENU", 30 * "-")
print("1. Vetores")
print("2. Listas Ligadas")
print("3. Listas Duplemente Ligadas")
print("4. Pilhas")
print("5. Filas")
print("6. Conjuntos")
print("7. Mapas")
print("8. Arvores")


menu = int(input("Digite a opcao desejada: "))

if menu == 1:
    vetor_teste = vetores.Vetor(0)
    vetor_teste.insirir_elemento_posicao(1, 0)
    vetor_teste.insirir_elemento_posicao(2, 1)
    vetor_teste.insirir_elemento_posicao(3, 2)
    vetor_teste.insirir_elemento_posicao(4, 2)
    vetor_teste.insirir_elemento_posicao(5, 2)
    vetor_teste.iniserir_elemento_final(1)
    # print(vetor_teste.contem(8))
    print(vetor_teste.indice(4))
    print(vetor_teste)
    vetor_teste.remover_elemento_indice(3)
    print(vetor_teste)
    vetor_teste.remover_elemento(5)
    print(vetor_teste)

elif menu == 2:
    lista_teste = lista_ligada.ListaLigada()
    lista_teste.inserir(1)
    lista_teste.inserir(4)
    lista_teste.inserir(5)
    lista_teste.inserir_posicao(2, 10)
    print(lista_teste)
    print(lista_teste.remover_elemento(4))
    print(lista_teste)
    # print(lista_teste.contem(5))
    # print(lista_teste.indice(55))
    # print(lista_teste.recuperar_elemento_no(0))

elif menu == 3:
    lista_teste = lista_duplamente_ligada.ListaDuplamenteLigada()
    lista_teste.inserir(1)
    lista_teste.inserir(4)
    lista_teste.inserir(5)
    lista_teste.inserir_posicao(2, 10)
    print(lista_teste)
    lista_teste.remover_posicao(1)
    print(lista_teste)
    # print(lista_teste.contem(5))
    # print(lista_teste.indice(55))
    # print(lista_teste.recuperar_elemento_no(0))

elif menu == 4:
    pilha_teste = pilha.Pilha()
    pilha_teste.empilhar(5)
    print(pilha_teste.desempilhar())

elif menu == 5:
    fila_teste = fila.Fila()
    fila_teste.enfilerar(1)
    fila_teste.enfilerar(2)
    fila_teste.enfilerar(3)
    fila_teste.enfilerar(4)
    print(fila_teste)
    print(fila_teste.desenfilerar())
    print(fila_teste)
    print(fila_teste.desenfilerar())
    print(fila_teste)
    fila_teste.enfilerar(6)
    print(fila_teste)

elif menu == 6:
    conjunto_teste = conjunto.Conjunto()
    conjunto_teste.inserir(1)
    conjunto_teste.inserir(2)
    conjunto_teste.inserir(3)
    print(conjunto_teste.inserir(3))
    # print(conjunto_teste.inserir_posicao(1,4))
    print(conjunto_teste)
    print(conjunto_teste.remover_elemento(3))
    print(conjunto_teste)
    print(conjunto_teste.inserir(3))
    print(conjunto_teste.inserir("Python"))
    print(conjunto_teste.inserir("TreinaWeb"))
    print(conjunto_teste.inserir(4))
    print(conjunto_teste)

elif menu == 7:
    mapa_teste = mapa.Mapa()
    print(mapa_teste)
    mapa_teste.adicionar('par', 10)
    print(mapa_teste)
    mapa_teste.adicionar("impar", 5)
    mapa_teste.adicionar("par", 2)
    print(mapa_teste)
    print(mapa_teste.contem_chave("par"))

elif menu == 8:
    arvore_test = arvore.Arvore()
    print(arvore_test)
    arvore_test.inserir_elemento(no_arvore_inteiro.NoArvoreInteriro(5))
    print(arvore_test)
    arvore_test.inserir_elemento(no_arvore_inteiro.NoArvoreInteriro(4))
    print(arvore_test)

else:
    print("Opcao Invalida!")
