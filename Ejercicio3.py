class AnalizadorTexto:

    def __init__(self):
        self.palabras = set()
        self.lista = []

    def agregar_palabra(self, palabra):
        self.palabras.add(palabra)
        self.lista.append(palabra)

    def contar_palabras(self):
        return len(self.palabras)
    
    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)

at = AnalizadorTexto()
at.agregar_multiples("hola", "mundo", "hola", "bebe", "estudiante", "madre")
print(at.contar_palabras())

    