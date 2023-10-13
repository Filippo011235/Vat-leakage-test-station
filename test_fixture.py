"""Module containing class that simulates a field with a testing device.

Classes:
    TestFixture
"""

from math import e
# from time import sleep
from random import random
import matplotlib.pyplot as plt
from os import path
from datetime import datetime
import csv

from vat import Vat
from factory_field import FactoryField
from text_data import RESULTS_SAVE_DIR, TEST_FILE_CODE, RESULTS_BUFFER_FILE

POS_RESULT_THRESHOLD = 0.95
"""Min. percentage of pressure to declare test as positive."""
INIT_CHANCE_FOR_LEAK = 0.005
"""Simulating process - chance that a leakage will occur during init curve."""
MAIN_CHANCE_FOR_LEAK = 0.005
"""Simulating process - chance that a leakage will occur during main part."""

class TestFixture(FactoryField):
    """Adds mechanism of testing Vats to the FactoryField class.

    Attributes:
        name_ (str): Name of the field.
        current_vat (class Vat): Current vat that is being stored(or not).
        pressure (float) : Pressure of air during the test.
    """

    def __init__(self, field_name="Bufor") -> None:
        """Initiate like a FactoryField, and additionaly set air pressure.

        Args:
            new_pressure (float) : Initial value of air pressure during tests.
        """
        FactoryField.__init__(self, field_name)

    # TODO remove or restore at the end of the project
    # def get_pressure(self):
    #     return self.pressure

    # def set_pressure(self, new_pressure: float):
    #     self.pressure = new_pressure

    def test_vat(self):
        """Simulate leakage test of a vat. Return True if OK, False if NOK."""
        if not isinstance(self.get_vat(), Vat):
            raise ValueError(f"{self.name_} has no correct Vat assigned!")

        # Get values for P, t, from current vat model data. 
        target_pressure, target_time = self.get_vat().get_values_for_test()
        # target_pressure is for reference; vat_pressure_cap for modifications.
        vat_pressure_cap = target_pressure

        # SOPHISTICATED TEST PROCEDURE
        X = [0.0]
        t = [0.0]
        time_interwal = 0.1 # in sec
        # TODO work out the a coefficient
        # a = self.get_vat().get_model()*1

        # Initial curve - S-curve
        while (X[-1] < vat_pressure_cap):
            
            # # For visual debug TODO delete later
            # print(X[-1], round(t[-1], 1))

            t.append(round(t[-1] + time_interwal, 1))
            # Sigmoid function - shifted to start from 0 and with "a" coeff.
            simulating_function = (1/(1 + e**(e**2 - t[-1])))
            X.append(round(vat_pressure_cap * simulating_function, 3))
            
            # Chance that a leakage will appear now, and prevent further
            # pressure build up. As pressure is closing to the target, 
            # this becomes more likely.
            if random() < INIT_CHANCE_FOR_LEAK * (X[-1]/vat_pressure_cap):
                vat_pressure_cap = X[-1] # Used in the main curve!
                break

        # Main curve - flat value (with possible drops)
        test_time = target_time + t[-1] # +t[-1] to compensate for init curve.
        while(t[-1] <= test_time):

            # # For visual debug. TODO delete later
            # print(X[-1], round(t[-1], 1))

            t.append(round(t[-1] + time_interwal, 1))
            X.append(X[-1])
            # Chance of leakage is propotional to elapsed time 
            # and inversely propotional to the already leaked pressure.
            if random() < (MAIN_CHANCE_FOR_LEAK * (t[-1]/test_time)
                           * 0.1*(X[-1]/target_pressure)):
                # Calculate random pressure drop, just don't cross half of cap.
                X_drop = random() * 0.5*vat_pressure_cap
                X[-1] = round(X[-1] - X_drop, 3)
                vat_pressure_cap = X[-1]

        # Return test results according to meeting pressure target.
        # For technical accuracy, base outcome on the mean of several samples.
        sample_X = X[-10:]
        if sum(sample_X)/len(sample_X) >= POS_RESULT_THRESHOLD * target_pressure:
            outcome = True
        else:
            outcome = False
        self.current_vat.set_test_result(outcome)

        # In real life, test fixture would be connected with the PLC and send
        # data packages to it. For simulation purposes, the data is being 
        # written into the buffer file, from which Test Data Handler parses it.
        test_timestamp = datetime.now().strftime("%d%m-%H%M%S")
        test_file_header = "_".join([TEST_FILE_CODE[0], 
                                   str(self.get_vat().get_barcode()),
                                   TEST_FILE_CODE[1],
                                   test_timestamp,
                                   TEST_FILE_CODE[2],
                                   self.current_vat.get_test_result(),
                                   TEST_FILE_CODE[3],
                                   str(self.current_vat.get_times_tested()),
                                   ])

        pressure_versus_time = zip(t, X)

        buffer_file_path = path.join(RESULTS_SAVE_DIR, RESULTS_BUFFER_FILE)
        with open(buffer_file_path, "w") as f:
            f.write(test_file_header + "\n")
            f.writelines([str(x)+"\n" for x in pressure_versus_time])

        return outcome


        # SIMPLEST POSSIBLE TEST PROCEDURE
        # test_time = 5
        # print(f"Building pressure, which'll take approx. {test_time} sec.")
        # sleep(test_time)

        # if random() <= 0.75:
        #     self.current_vat.set_test_result(True)
        #     return True
        # else:
        #     self.current_vat.set_test_result(False)
        #     return False
