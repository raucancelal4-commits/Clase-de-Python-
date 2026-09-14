class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)

    def minima(self):
        return min(self.temperaturas) if self.temperaturas else None

    def maxima(self):
        return max(self.temperaturas) if self.temperaturas else None

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas) if self.temperaturas else 0
gt = GestorTemperatura()
gt.registrar_multiples(20, 25, 18, 30)
print(gt.promedio())  
print(gt.minima())    
print(gt.maxima()) 