from tienda.interfaces.pago_interface import MetodoPago


class PagoEfectivo(MetodoPago):
    """
    Implementación concreta del pago en efectivo.

    Aplica:
    - Herencia
    - Polimorfismo
    - LSP
    """

    # 🔹 Polimorfismo
    def procesar_pago(self, monto: float) -> str:
        return f"💵 Pago en efectivo recibido: ${monto}"
    
    