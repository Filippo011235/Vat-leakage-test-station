"""Module containing class that simulates a field with a testing device.

Classes:
    TestFixture
"""

from time import sleep
from random import randint

from vat import Vat
from factory_field import FactoryField

INIT_PRESSURE = 0.15
"""Initial pressure of air during the test."""

class TestFixture(FactoryField):
    """Adds mechanism of testing Vats to the FactoryField class.

    Attributes:
        name_ (str): Name of the field.
        current_vat (class Vat): Current vat that is being stored(or not).
        pressure (float) : Pressure of air during the test.
    """

    def __init__(self, field_name="Bufor", 
                 new_pressure = INIT_PRESSURE) -> None:
        """Initiate like a FactoryField, and additionaly set air pressure.

        Args:
            new_pressure (float) : Initial value of air pressure during tests.
        """
        FactoryField.__init__(self, field_name)
        self.pressure = new_pressure
        
    def get_pressure(self):
        return self.pressure

    def set_pressure(self, new_pressure: float):
        self.pressure = new_pressure

    def test_vat(self):
        """Simulate leakage test of a vat. Return True if OK, False if NOK"""
        if not isinstance(self.current_vat, Vat):
            print(f"{self.name_} has no correct Vat assigned!")
            return False

        sleep(15)

        result = randint(1,100)
        if result <= 75:
            self.current_vat.set_test_result(True)
        else:
            self.current_vat.set_test_result(False)
        



