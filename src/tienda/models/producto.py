from abc import ABC, abstractmethod


class Producto(ABC):
    """
    Clase abstracta base para todos los productos.

    Aplica:
    - Encapsulamiento
    - Herencia
    - Polimorfismo
    - Clase abstracta
    - SRP
    """

    # Constructor
    def __init__(self, nombre: str, precio: float, stock: int):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    # Encapsulamiento
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor.strip():
            raise ValueError("❌ El nombre no puede estar vacío")
        self._nombre = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor <= 0:
            raise ValueError("❌ El precio debe ser mayor a 0")
        self._precio = valor

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise ValueError("❌ El stock no puede ser negativo")
        self._stock = valor

    # Método de negocio
    def reducir_stock(self, cantidad: int):
        if cantidad > self._stock:
            raise RuntimeError("❌ Stock insuficiente")
        self._stock -= cantidad

    # Polimorfismo
    @abstractmethod
    def calcular_precio_final(self) -> float:
        pass

    # Métodos especiales
    def __str__(self):
        return f"📦 {self._nombre} | 💰 ${self._precio} | 📊 Stock: {self._stock}"

    def __repr__(self):
        return f"Producto(nombre={self._nombre}, precio={self._precio}, stock={self._stock})"
    
    