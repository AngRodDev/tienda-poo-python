from tienda.models.producto_fisico import ProductoFisico


def test_precio_final_producto_fisico():
    """
    Verifica que el precio final incluya costo de envío.
    """
    producto = ProductoFisico("Laptop", 1000, 5, 50)

    assert producto.calcular_precio_final() == 1050

    