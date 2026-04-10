from tienda.models.producto import Producto


class ProductoDigital(Producto):
    """
    Producto digital sin costo de envío.

    Aplica:
    - Herencia
    - Polimorfismo
    """

    def calcular_precio_final(self) -> float:
        return self._precio
    
