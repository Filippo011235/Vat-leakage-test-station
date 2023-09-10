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
    1: "900  x 900  x 600",
    2: "1200 x 1500 x 900",
    3: "1600 x 2000 x 1200",
    4: "2000 x 2400 x 1600",
}
"""VAT_MODELS contains example model sizes of the vats."""

BARCODE_MIN = 1
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

    def __init__(self, declared_model = 1, init_test_result = None) -> None:
        """Initiate with a given model, test result and random barcode.

        Args:
            declared_model (int) : Codes model/size of the vat, has to be 
                                    in range  of keys of the dictionary.
            init_test_result (float) : Initial value of air pressure during tests.
        """
        self.model = VAT_MODELS.get(declared_model, 1)

        self.barcode = random.randint(BARCODE_MIN, BARCODE_MAX)
        self.test_result = init_test_result

    def __str__(self):
        """Return str with vat barcode ID and test result"""
        return f"Vat: {self.get_barcode()} with {self.get_test_result()} test"

    def get_model(self):
        return self.model

    def get_barcode(self):
        return self.barcode

    def get_test_result(self):
        """Based on test_result(None, False, True), return according str."""
        match self.test_result:
            case None:
                return "---"
            case True:
                return "Pos"
            case False:
                return "Neg"

    def set_test_result(self, vat_test_result: bool):
        self.test_result = vat_test_result


