"""Module containing Vat class which simulates a vat during quality control.

Classes:
    Vat

Constants:
    VAT_MODELS : dictionary coding vats models. Keys(int) represent names, and
                values(str) store models dimensions. Used during leak tests.
    BARCODE_MIN and _MAX : define range of int values possible for barcodes.
"""

import random

# Vat models - keys must be integers!
VAT_MODELS = {
    1: [0.15, 10],
    2: [0.25, 15],
    3: [0.35, 20],
    4: [0.45, 25],
}
"""Holds all models and their values for pressure and time during tests."""

BARCODE_MIN = 1
"""Range for possible barcode values."""
BARCODE_MAX = 1000
"""Range for possible barcode values."""

class Vat:
    """Simulate a physical vat that is being tested.

    Attributes:
        model (int) : Model size of the Vat, coded with an int, and a dict.
        barcode (int) : Random number representing barcode of the vat.
        test_result (bool) : Result of the leakage test. Initially None.
                                True for positive result, False for negative.
    """

    def __init__(self, declared_model: int=1, init_test_result = None, no_of_times_tested: int=0) -> None:
        """Initiate with a given model, test result and random barcode.

        Args:
            declared_model (int) : Codes model/size of the vat, has to be 
                                    in range  of keys of the dictionary.
            init_test_result (float) : Initial value of air pressure during tests.
        """
        if declared_model in VAT_MODELS.keys():
            self.model = declared_model
        else:
            raise ValueError("Incorrect Vat model!")

        self.barcode = random.randint(BARCODE_MIN, BARCODE_MAX)
        self.test_result = init_test_result
        self.times_tested = no_of_times_tested

    def __str__(self):
        """Return str with vat barcode ID and test result"""
        return f"Vat: {self.get_barcode()} with {self.get_test_result()} test"

    def get_model(self):
        return self.model

    def get_barcode(self):
        return self.barcode

    def get_times_tested(self):
        return self.times_tested

    def get_test_result(self):
        """Based on test_result return str ("---", "Pos", "Neg")."""
        match self.test_result:
            case None:
                return "---"
            case True:
                return "Pos"
            case False:
                return "Neg"

    def get_values_for_test(self):
        return VAT_MODELS[self.get_model()]

    def set_test_result(self, vat_test_result: bool):
        self.times_tested += 1
        self.test_result = vat_test_result
