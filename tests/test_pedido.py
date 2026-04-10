from tienda.models.producto_digital import ProductoDigital
from tienda.models.pedido import Pedido


def test_total_pedido():
    """
    Verifica cálculo total del pedido.
    """
    pedido = Pedido()
    producto = ProductoDigital("Curso", 100, 10)

    pedido.agregar_producto(producto, 2)

    assert pedido.calcular_total() == 200

