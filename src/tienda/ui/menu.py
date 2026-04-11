from tienda.models.producto_fisico import ProductoFisico
from tienda.models.producto_digital import ProductoDigital
from tienda.payments.pago_tarjeta import PagoTarjeta
from tienda.services.tienda_service import TiendaService

def mostrar_menu():
    """
    Menú principal de la tienda.

    Aplica:
    - UX en consola
    - integración de servicios
    """
    print("\n🛍️ Bienvenido a la Tienda POO")
    print("1. Comprar laptop")
    print("2. Comprar curso digital")
    print("3. Salir")


def ejecutar():
    # Controla la interacción con el usuario.
    metodo_pago = PagoTarjeta()
    tienda = TiendaService(metodo_pago)

    while True:
        mostrar_menu()
        opcion = input("👉 Selecciona una opción: ")

        if opcion == "1":
            producto = ProductoFisico("Laptop", 1000, 5, 50)
            tienda.agregar_producto(producto, 1)
            print(tienda.procesar_compra())

        elif opcion == "2":
            producto = ProductoDigital("Curso Python", 100, 10)
            tienda.agregar_producto(producto, 1)
            print(tienda.procesar_compra())

        elif opcion == "3":
            print("👋 Gracias por visitar la tienda")
            break

        else:
            print("⚠️ Opción no válida")

