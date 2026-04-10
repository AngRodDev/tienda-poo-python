from abc import ABC, abstractmethod


class MetodoPago(ABC):
    """
    Clase abstracta que define el contrato para métodos de pago.

    Aplica:
    - Clase Abstracta
    - Polimorfismo
    - DIP (Dependency Inversion Principle)
    - ISP (Interface Segregation Principle)
    """

    # 🔹 Clase Abstracta
    # 🔹 Contrato obligatorio para las clases hijas
    @abstractmethod
    def procesar_pago(self, monto: float) -> str:
        """
        Procesa el pago del monto indicado.

        Args:
            monto (float): monto a pagar

        Returns:
            str: mensaje de confirmación
        """
        pass

    