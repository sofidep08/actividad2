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

class CitaMedica:
    def __init__(self, motivo, diagnostico):
        self.motivo = motivo
        self.diagnostico = diagnostico

    def __str__(self):
        return f"Motivo: {self.motivo} | Diagnóstico: {self.diagnostico}"


class Veterinaria:
    def __init__(self):
        self.clientes = []

    def registrar_cliente(self, nombre, telefono, correo):
        cliente = Cliente(nombre, telefono, correo)
        self.clientes.append(cliente)
        print("Cliente registrado con éxito.")

    def buscar_cliente(self, nombre):
        for cliente in self.clientes:
            if cliente.get_nombre().lower() == nombre.lower():
                return cliente
        return None

    def registrar_mascota(self, nombre_cliente, nombre, especie, raza, edad):
        cliente = self.buscar_cliente(nombre_cliente)
        if cliente:
            mascota = Mascota(nombre, especie, raza, edad)
            cliente.agregar_mascota(mascota)
            print("Mascota registrada con éxito.")
        else:
            print("Cliente no encontrado.")

    def agendar_cita(self, nombre_cliente, nombre_mascota, motivo, diagnostico):
        cliente = self.buscar_cliente(nombre_cliente)
        if cliente:
            for mascota in cliente.get_mascotas():
                if mascota.get_nombre().lower() == nombre_mascota.lower():
                    cita = CitaMedica(motivo, diagnostico)
                    mascota.agregar_cita(cita)
                    print("Cita registrada con éxito.")
                    return
            print("Mascota no encontrada.")
        else:
            print("Cliente no encontrado.")

    def mostrar_historial(self, nombre_cliente, nombre_mascota):
        cliente = self.buscar_cliente(nombre_cliente)
        if cliente:
            for mascota in cliente.get_mascotas():
                if mascota.get_nombre().lower() == nombre_mascota.lower():
                    print(f"Historial de {mascota.get_nombre()}:")
                    for cita in mascota.get_historial():
                        print("-", cita)
                    return
            print("Mascota no encontrada.")
        else:
            print("Cliente no encontrado.")

    def mostrar_clientes_y_mascotas(self):
        for cliente in self.clientes:
            print(cliente)
            for mascota in cliente.get_mascotas():
                print("  -", mascota)

def menu():
    vet = Veterinaria()
    opcion = 0
    while opcion!=6 :
        print("[1] Registrar nuevo cliente")
        print("[2] Registrar nueva mascota")
        print("[3] Agendar cita médica")
        print("[4] Ver historial de citas")
        print("[5] Ver clientes y mascotas")
        print("[6] Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del cliente: ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")
            vet.registrar_cliente(nombre, telefono, correo)

        elif opcion == "2":
            nombre_cliente = input("Nombre del cliente: ")
            nombre = input("Nombre de la mascota: ")
            especie = input("Especie: ")
            raza = input("Raza: ")
            edad = input("Edad: ")
            vet.registrar_mascota(nombre_cliente, nombre, especie, raza, edad)