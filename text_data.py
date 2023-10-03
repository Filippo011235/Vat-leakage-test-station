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
"""Integer used to break out of the menu loop and quit the program."""
CANCEL_OPERATION = 100
"""Int. for input to cancel operations, such as transfer or test Vat."""
ADD_INPUT_VAT_ID = "(-> In)"
"""Distinguishes "add Vat to Input" menu option."""
DEL_OUTPUT_VAT_ID = "(Out ->)"
"""Distinguishes "remove Vat from Output" menu option."""
MOVE_VAT_ID = "(<->)"
"""Distinguishes "transfer Vat between Fields" menu option."""
TEST_VAT_ID = "Test"
"""Distinguishes "test Vat on Test Fixtures" menu option."""
AUTO_MODE_ID = "Auto"
"""Menu option for automatically doing basic operations(handles In, Out)"""


# Factory buffer fields names.
# To Do - .startswidth("T") for TestFixture
FACTORY_FIELDS_NAMES = (INPUT_ID,
                        CORRECTION_ID,
                        TEST_FIXTURE_ID + "1",
                        TEST_FIXTURE_ID + "2",
                        OUTPUT_ID,
                        )

# Dictionary containing menu options and sections dividers.
# To Do - rules - str dividers, int options, "(X <-> Y)" for Factory Field, 
TEXT_MENU = {
    "No.": "---------- Vat operations ----------",
    1: ADD_INPUT_VAT_ID + " Input new Vat to In",
    2: DEL_OUTPUT_VAT_ID + " Move OK Vat from Out",
    3: MOVE_VAT_ID + " Transfer Vat between Fields",
    4: TEST_VAT_ID + " Vat on a Test Fixture Field",
    5: AUTO_MODE_ID + " mode (handle In and Out fields)",

    "End": "---------- Finish program ----------",
    FINISH_CONST: "Finish productive work shift :)",
    }
