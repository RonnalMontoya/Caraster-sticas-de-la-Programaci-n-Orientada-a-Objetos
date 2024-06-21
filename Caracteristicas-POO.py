class Cliente:
    def __init__(self, nombre, correo):
        """
        Inicializa un objeto Cliente con nombre y correo.
        """
        self.nombre = nombre
        self.correo = correo

    def __str__(self):
        """
        Devuelve una representación en cadena del cliente.
        """
        return f"Cliente: {self.nombre}, Correo: {self.correo}"


class Habitacion:
    def __init__(self, numero, tipo, costo):
        """
        Inicializa una habitación con un número, tipo y costo.
        """
        self.numero = numero
        self.tipo = tipo
        self.costo = costo
        self.esta_disponible = True

    def __str__(self):
        """
        Devuelve una representación en cadena de la habitación.
        """
        return f"Habitación {self.numero}: {self.tipo} - ${self.costo} por noche"


class Reserva:
    def __init__(self, cliente, habitacion, fecha_inicio, fecha_fin):
        """
        Inicializa una reserva con un cliente, habitación, fecha de inicio y fecha de fin.
        """
        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def __str__(self):
        """
        Devuelve una representación en cadena de la reserva.
        """
        return (f"Reserva para {self.cliente.nombre} en la {self.habitacion.tipo} "
                f"(Habitación {self.habitacion.numero}) desde {self.fecha_inicio} hasta {self.fecha_fin}")


class Hotel:
    def __init__(self, nombre):
        """
        Inicializa un objeto Hotel con un nombre y listas vacías de habitaciones y reservas.
        """
        self.nombre = nombre
        self.habitaciones = []
        self.reservas = []

    def agregar_habitacion(self, habitacion):
        """
        Agrega una habitación a la lista de habitaciones del hotel.
        """
        self.habitaciones.append(habitacion)

    def hacer_reserva(self, cliente, numero_habitacion, fecha_inicio, fecha_fin):
        """
        Realiza una reserva para un cliente si la habitación está disponible.
        """
        habitacion = next((h for h in self.habitaciones if h.numero == numero_habitacion and h.esta_disponible), None)
        if habitacion:
            nueva_reserva = Reserva(cliente, habitacion, fecha_inicio, fecha_fin)
            self.reservas.append(nueva_reserva)
            habitacion.esta_disponible = False
            return nueva_reserva
        else:
            raise ValueError("La habitación no está disponible")

    def __str__(self):
        """
        Devuelve una representación en cadena del hotel, incluyendo sus habitaciones y reservas.
        """
        habitaciones_str = "\n".join(str(h) for h in self.habitaciones)
        reservas_str = "\n".join(str(r) for r in self.reservas)
        return f"Hotel {self.nombre}\n\nHabitaciones:\n{habitaciones_str}\n\nReservas:\n{reservas_str}"


# Ejemplo de uso del sistema de reservas de hotel
cliente1 = Cliente("Ronnal Montoya", "ronnal.montoya@example.com")
cliente2 = Cliente("Patricia Barzola", "patricia.barzola@example.com")

habitacion1 = Habitacion(101, "Individual", 30)
habitacion2 = Habitacion(102, "Doble", 50)

hotel = Hotel("Hotel Cielo")

hotel.agregar_habitacion(habitacion1)
hotel.agregar_habitacion(habitacion2)

print(hotel)

# Hacer una reserva
reserva1 = hotel.hacer_reserva(cliente1, 101, "2024-07-01", "2024-07-05")
print("\nReserva realizada:\n", reserva1)

print("\nEstado del hotel después de la reserva:\n")
print(hotel)

