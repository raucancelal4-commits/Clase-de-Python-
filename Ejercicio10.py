class AnalizadorString:

    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return letra.lower() in "aeiou"

    def contar_por_tipo(self, texto):
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto
        conj = {'vocales': 0, 'consonantes': 0, 'digitos': 0}
        for letra in texto:
            if letra.isdigit():conj['digitos'] += 1
            elif letra.isalpha():
                if self.solo_vocales(letra): conj['vocales'] += 1
                else: conj['consonantes'] += 1
        return conj

astr = AnalizadorString()
print(astr.contar_por_tipo("Rpal, Mi familia, 593"))
print(astr.texto_mas_largo)
