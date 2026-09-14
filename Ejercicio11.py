class Tareas:

    def __init__(self):
        self.lista_tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        self.lista_tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        prioritarias = []
        for descripcion, prioridad in self.lista_tareas:
            if prioridad == "alta":
                prioritarias.append((descripcion, prioridad))
        return prioritarias

    def eliminar_completada(self, descripcion):
        tareas_restantes = []  
        for desc, prio in self.lista_tareas:
            if desc != descripcion:
                tareas_restantes.append((desc, prio))
        self.lista_tareas = tareas_restantes

t = Tareas()
t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
t.eliminar_completada("Estudiar")
t.agregar_tarea("Estudiar", "Muy baja")
print(t.lista_tareas)
