class Equipo:

    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)
    
    def equipo_mayor_integrantes(self):
        if not self.equipos:
            return None
        equipo_mayor = None
        max_jugadores = -1
        for equipo, jugadores in self.equipos.items():
            if len(jugadores) > max_jugadores:
                max_jugadores = len(jugadores)
                equipo_mayor = equipo
                
        return equipo_mayor
    
eq = Equipo()
eq.crear_equipo("A")
eq.agregar_jugador("A","Juan")
eq.agregar_jugador("A","Pedro")