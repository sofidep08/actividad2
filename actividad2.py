class Cliente:
    def __init__(self, nombre, telefono, correo):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__correo = correo
        self.__mascotas = []

    def agregar_mascota(self, mascota):
        self.__mascotas.append(mascota)

    def get_nombre(self):
        return self.__nombre

    def get_mascotas(self):
        return self.__mascotas

    def __str__(self):
        return f"{self.__nombre} | Tel: {self.__telefono} | Email: {self.__correo}"


class Mascota:
    def __init__(self, nombre, especie, raza, edad):
        self.__nombre = nombre
        self.__especie = especie
        self.__raza = raza
        self.__edad = edad
        self.__historial_citas = []

    def agregar_cita(self, cita):
        self.__historial_citas.append(cita)

    def get_nombre(self):
        return self.__nombre

    def get_historial(self):
        return self.__historial_citas

    def __str__(self):
        return f"{self.__nombre} | {self.__especie}, {self.__raza}, {self.__edad} años"
