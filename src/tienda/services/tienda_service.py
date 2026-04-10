from tienda.models.pedido import Pedido
from tienda.interfaces.pago_interface import MetodoPago
from tienda.interfaces.descuento_interface import Descuento

class TiendaService:
    """
    Servicio principal de la tienda.

    Aplica:
    - SRP, DIP, Composición
    - Lógica de negocio
    """
    # 🔹 Constructor
    # 🔹 Dependency Injection
    def __init__(self, metodo_pago: MetodoPago, descuento: Descuento) -> None:
        # Atributos
        self._pedido = Pedido()
        # 🔹 DIP
        self._metodo_pago = metodo_pago
        self._descuento = descuento


    # 🔹 Composición
    def agregar_producto(self, producto, cantidad):
        self._pedido.agregar_producto(producto, cantidad)

    # 🔹 Lógica de negocio
    def procesar_compra(self):
        # Calculamos el total
        total = self._pedido.calcular_total()

        # 🔹 Polimorfismo
        # Si hay descuento lo aplica
        if self._descuento:
            total = self._descuento.aplicar_descuento(total)
        
        # Procesa el pago
        resultado_pago = self._metodo_pago.procesar_pago(total)

        return resultado_pago
    
    




    


