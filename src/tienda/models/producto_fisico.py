from tienda.models.producto import Producto


class ProductoFisico(Producto):
    """
    Producto físico con costo de envío.

    Aplica:
    - Herencia
    - Polimorfismo
    - OCP
    """

    def __init__(self, nombre: str, precio: float, stock: int, costo_envio: float):
        super().__init__(nombre, precio, stock)
        self._costo_envio = costo_envio

    def calcular_precio_final(self) -> float:
        return self._precio + self._costo_envio
    
    
