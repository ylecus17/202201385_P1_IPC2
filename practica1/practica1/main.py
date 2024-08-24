from Clientes import cliente
from Autos import autos 
from Compras import Compra
listAutos=[]
listClientes=[]
listCompra=[]
def menu():
    while True:
        print("------------ Menú ------------")
        print("1. Registrar Auto")
        print("2. Registrar Cliente")
        print("3. Realizar Compra")
        print("4. Reporte de Compras")
        print("5. Datos del Estudiante")
        print("6. Salir")
        eleccion = int(input("Escribe una opción (1-6): "))
        
        if eleccion==1:
            registrarAuto()
            
        elif eleccion==2:
            registrarCliente()
            
        elif eleccion==3:
            print('opcion1')
            realizarCompra()
        elif eleccion==4:
            
            reporteCompras()
        elif eleccion==5:
            print('Natalia Garrido')
            print('202201385')
        elif eleccion==6:
            print('saliendo')
            break
        else:
            print('opcion invalida ')
def registrarCliente():
    print("Registrar nuevo cliente")
    nombre=input('ingrese nombre del cliente:')
    correo= input("Ingrese correo del cliente: ")
    nit = input("Ingrese el NIT del cliente: ")
    
    clientes = cliente(nombre,correo,nit)
    listClientes.append(clientes)
    print("Cliente registrado exitosamente.")

def realizarCompra():

    clienteCompra=input('ingrese el nit del cliente que quiere comprar ')
    for cliente in listClientes:
        if(clienteCompra==cliente.nit):
            submenu(clienteCompra)
        else:
            print('cliente no esta registrado')




def registrarAuto():
    print("Registrar nuevo producto")
    placa=input('ingrese placa del auto:')
    marca = input("Ingrese la marca del auto: ")
    modelo = input("Ingrese el modelo del auto: ")
    descripcion = (input("Ingrese la descricion del auto: "))
    precioU = float(input("Ingrese el precio unitario del auto: "))
    auto = autos(placa, marca, modelo, descripcion, precioU)

    # Agregar el auto a la lista de autos
    listAutos.append(auto)

    print("Auto registrado exitosamente.")
def submenu(cliente):
    total = 0
    autosCompra = []
    while True:
        print("------------ Menú Compra ------------")
        print("1. Agregar Auto")
        print("2. Terminar compra y generar Factura")
        eleccion = input('Elija una opción: ')

        if eleccion == '1':
            autoEleccion = input('Ingrese la placa del vehículo: ')
            auto_encontrado = False

            for auto in listAutos:
                if autoEleccion == auto.placa:
                    total += auto.precioU
                    autosCompra.append(auto)  
                    auto_encontrado = True
                    print(f"Auto {auto.placa} agregado a la compra.")
                    break

            if not auto_encontrado:
                print('No se encontró un auto con esa placa.')

        elif eleccion == '2':
            if autosCompra: 
                seguro = input("¿Desea agregar seguro a los autos comprados? (SI/NO): ").strip().upper()
                
                if seguro == "SI":
                    total_con_seguro = total  
                    for auto in autosCompra:
                        total_con_seguro += auto.precioU * 0.15  
                    total = total_con_seguro
                    print(f"Se ha añadido el seguro al total. Nuevo total: Q{total:.2f}")
                else:
                    print(f"Total sin seguro: Q{total:.2f}")
                
               
                compra = Compra(cliente, autosCompra, total)
                listCompra.append(compra)

                print('------------------------')
                print('Total de factura')
                print(f'Q {total:.2f}')

                break 
            else:
                print("No se han agregado autos a la compra.")
        else:
            print('Opción no válida, por favor intente de nuevo.')

    

    
def reporteCompras():
    total=0
    for compra in listCompra:
        print('--------------------------')
        print('Datos del Cliente:')
        
        
        for cliente in listClientes:
            if compra.cliente== cliente.nit:
                print(f'Nombre del cliente: {cliente.nombre}')
                print(f'Correo del cliente: {cliente.correo}')
                print(f'NIT del cliente: {cliente.nit}')
                break

        print('--------------------------')
        print('Autos comprados:')
        
        
        for auto in compra.autos:
            print(f"- Placa: {auto.placa}, Marca: {auto.marca}, Modelo: {auto.modelo}, Precio: Q{auto.precioU:.2f}")
        
        print('--------------------------')
        print(f'Total a pagar: Q{compra.total:.2f}')
        print('--------------------------')
        total+=compra.total
    print(f'total general: {total}')

if __name__ == "__main__":
    menu()