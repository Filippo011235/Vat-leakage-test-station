"""Module containing class that simulates a field with a testing device.

Classes:
    TestFixture
"""

from math import e
from time import sleep
from random import random
import matplotlib.pyplot as plt

from vat import Vat, VAT_MODELS
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
        """Simulate leakage test of a vat. Return True if OK, False if NOK."""
        if not isinstance(self.get_vat(), Vat):
            raise ValueError(f"{self.name_} has no correct Vat assigned!")

        # SOPHISTICATED TEST PROCEDURE
        # "./Test results"
        X = [0.0]
        t = [0.0]
        time_interwal = 0.1 # in sec
        # a = self.get_vat().get_model()*1
        target_vessel_pressure = self.pressure

        # Initial curve - S-curve
        while (X[-1] < target_vessel_pressure):
            
            # For visual debug TODO delete later
            print(X[-1], round(t[-1], 1))

            t.append(t[-1] + time_interwal)
            # Sigmoid function - shifted to start from 0 and with "a" coeff.
            simulating_function = (1/(1 + e**(e**2 - t[-1])))
            X.append(round(target_vessel_pressure * simulating_function, 3))
            
            # Chance that a leakage will appear now, and prevent further
            # pressure build up. As pressure is closing to the target, 
            # this becomes more likely.
            # TODO HARDCODED VAR
            if random() < 0.005*(X[-1]/target_vessel_pressure):
                target_vessel_pressure = X[-1] # Used in the main curve!
                break

        # Main curve - flat value
        # TODO HARDCODED VAR
        test_time = 30 + 15 # 15 sec - S-curve approx. time
        while(t[-1] <= test_time):

            # For visual debug TODO delete later
            print(X[-1], round(t[-1], 1))

            t.append(t[-1] + time_interwal)
            X.append(X[-1])
            # Chance of leakage is propotional to elapsed time 
            # and inversely propotional to leaked pressure.
            # TODO HARDCODED VAR
            if random() < 0.005*(t[-1]/test_time)*0.1*(X[-1]/self.pressure):
                X_drop = random()*0.4*target_vessel_pressure
                X[-1] = round(X[-1] - X_drop, 3)
                target_vessel_pressure = X[-1]

        plt.plot(t, X)
        plt.savefig()


        # Return test result according to meeting pressure target.
        if X[-1] >= 0.95*self.get_pressure():
            return True
        else:
            return False

        # SIMPLE TEST PROCEDURE
        # test_time = 5
        # print(f"Building pressure, which'll take approx. {test_time} sec.")
        # sleep(test_time)

        # if random() <= 0.75:
        #     self.current_vat.set_test_result(True)
        #     return True
        # else:
        #     self.current_vat.set_test_result(False)
        #     return False
