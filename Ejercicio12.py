class ContadorFrecuencia:

    def __init__(self):
        self.frecuencia={}
        pass

    def agregar_elemento(self, elemento):
        if elemento in self.frecuencia: self.frecuencia[elemento] += 1
        else : self.frecuencia[elemento] = 1 

    def elemento_mas_frecuente(self):
        if not self.frecuencia: return None
        mas_frecuencia = None
        max_conteo = -1
        for elem, conteo in self.frecuencia.items():
            if conteo > max_conteo:
                max_conteo = conteo
                mas_frecuente = elem
        return mas_frecuente
    
    def frecuencia_elemento(self, elemento):
        if elemento in self.frecuencia: return self.frecuencia[elemento]
        else: return 0

cf = ContadorFrecuencia()
cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("b")
print(cf.elemento_mas_frecuente())
print(cf.frecuencia_elemento("a"))