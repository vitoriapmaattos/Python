from abc import ABC, abstractclassmethod

class GeometricForm(ABC):
    """GeometricForm representa uma forma geométrica."""

    @abstractclassmethod
    def get_area(self) -> float:
        pass

    @abstractclassmethod
    def
