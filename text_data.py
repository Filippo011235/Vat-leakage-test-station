"""Contains constants and shared data, like menu options, fields names."""

# Constants to avoid magic numbers in code
# For Factory fields names:
INPUT_ID = "In"
"""Represents Input field, used to receive new Vats."""
OUTPUT_ID = "Out"
"""Represents Output field, used to push out checked Vats."""
CORRECTION_ID = "Corr"
"""Represents Correction field, where Vats are repaired."""
TEST_FIXTURE_ID = "T"
"""Represents Test Fixture field, where Vats are being tested."""


# For menu options:
FINISH_CONST = 0
"""Integer used to break out of the menu loop and quit the program"""
INPUT_VAT_DISTINGUISHER = "(-> In)"
"""Distinguishes "add Vat to Input" menu option"""
OUTPUT_VAT_DISTINGUISHER = "(Out ->)"
"""Distinguishes "remove Vat from Output" menu option"""
TRANSFER_VAT_DISTINGUISHER = "(<->)"
"""Distinguishes "transfer Vat between Fields" menu option"""

# Factory buffer fields names.
# To Do - .startswidth("T") for TestFixture
FACTORY_FIELDS_NAMES = [INPUT_ID,
                        CORRECTION_ID,
                        TEST_FIXTURE_ID + "1",
                        TEST_FIXTURE_ID + "2",
                        OUTPUT_ID,
                        ]

# Dictionary containing menu options and sections dividers.
# To Do - rules - str dividers, int options, "(X <-> Y)" for Factory Field, 
TEXT_MENU = {
    "Mov": "---------- Vat logistics ----------",
    1: INPUT_VAT_DISTINGUISHER + " Input new Vat to In",
    2: INPUT_VAT_DISTINGUISHER + " Move OK Vat from Out",
    3: TRANSFER_VAT_DISTINGUISHER + " Transfer Vat between Fields",

    "End": "---------- Finish program ----------",
    FINISH_CONST: "Finish productive work shift :)",
    }
