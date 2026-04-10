from tienda.interfaces.pago_interface import MetodoPago


class PagoTarjeta(MetodoPago):
    """
    Implementación concreta del pago con tarjeta.

    Aplica:
    - Herencia
    - Polimorfismo
    - LSP
    """

    # 🔹 Polimorfismo
    # Sobrescribe el método abstracto
    def procesar_pago(self, monto: float) -> str:
        return f"💳 Pago con tarjeta procesado por ${monto}"