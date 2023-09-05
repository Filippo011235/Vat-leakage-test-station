from vat import Vat
from factory_field import FactoryField

INIT_PRESSURE = 0.15

class TestFixture(FactoryField):
    """ Kokos
    Kokos kokos
    """

    def __init__(self, new_pressure = INIT_PRESSURE) -> None:
        self.pressure = new_pressure

    def test_vat(self):
        print("todo")
