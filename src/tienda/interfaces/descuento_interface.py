from abc import ABC, abstractmethod


class Descuento(ABC):
    """
    Clase abstracta para aplicar descuentos.

    Aplica:
    - Clase Abstracta
    - Polimorfismo
    - OCP (Open/Closed Principle)
    """

    # 🔹 Clase Abstracta
    @abstractmethod
    def aplicar_descuento(self, monto: float) -> float:
        """
        Aplica descuento al monto.

        Args:
            monto (float): total del pedido

        Returns:
            float: monto con descuento aplicado
        """
        pass

    