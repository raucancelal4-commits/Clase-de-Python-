class AnalizadorNumeros:

    def __init__(self):
        pass

    def es_par(self, numero):
        if numero % 2 == 0:
            return True
        else:
            return False

    def separar_numeros(self, *numeros):
        resultado = {
            "pares": [],
            "impares": []
        }
        for numero in numeros:
            if self.es_par(numero): resultado["pares"].append(numero)
            else: resultado["impares"].append(numero)
        return resultado
    
an = AnalizadorNumeros()
print(an.es_par(10))
print(an.separar_numeros(1, 2, 3, 4, 5))