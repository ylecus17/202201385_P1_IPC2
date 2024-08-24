

class Compra:
    _id_counter = 1  # Variable de clase para contar las compras y asignar IDs únicos

    def __init__(self, cliente,autos,total):
        self.id = Compra._id_counter  # Asignar el ID único a esta compra
        Compra._id_counter += 1  # Incrementar el contador para la próxima compra
        self.cliente = cliente
        self.autos = autos
        self.total = total

    