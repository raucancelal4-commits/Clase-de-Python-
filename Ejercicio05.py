class InversorSecuencia:

    def __init__(self):
        pass
    
    def invertir_lista(self, lista):
        ordena = []
        for i in range(len(lista) - 1, -1, -1):
            ordena.append(lista[i])
        return ordena

    def invertir_multiples(self, *listas):
        resultado = {}
        for lista in listas:
            resultado[tuple(lista)] = self.invertir_lista(lista)
        return resultado

inv = InversorSecuencia()
print(inv.invertir_lista([1, 2, 3, 4]))
