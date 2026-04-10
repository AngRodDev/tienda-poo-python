from typing import List
from tienda.models.producto import Producto


class Pedido:
    """
    Representa un pedido.

    Aplica:
    - Composición
    - Encapsulamiento
    - SRP
    """

    def __init__(self):
        self._productos: List[Producto] = []

    def agregar_producto(self, producto: Producto, cantidad: int):
        print(f"\n🛒 Agregando {cantidad} x {producto.nombre}")

        if cantidad <= 0:
            raise ValueError("❌ Cantidad inválida")

        if producto.stock < cantidad:
            raise RuntimeError("❌ Stock insuficiente")

        producto.reducir_stock(cantidad)

        for _ in range(cantidad):
            self._productos.append(producto)

        print("✅ Producto agregado correctamente")

    def calcular_total(self) -> float:
        total = sum(p.calcular_precio_final() for p in self._productos)
        return total

    def mostrar_pedido(self):
        print("\n📦 Pedido actual:")
        for producto in self._productos:
            print(producto)

    def __str__(self):
        return f"🛒 Pedido con {len(self._productos)} productos"

    def __repr__(self):
        return f"Pedido(productos={self._productos})"