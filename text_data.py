TEST_FIXTURE_DISTINGUISHER = "T"
"""Constant to distinguish between regular FactoryField and TestFixture."""
INPUT_VAT_DISTINGUISHER = "(-> In)"
"""Constant to distinguish adding Vat to Input menu option"""
OUTPUT_VAT_DISTINGUISHER = "(Out ->)"
"""Constant to distinguish removing Vat from Output menu option"""
TRANSFER_VAT_DISTINGUISHER = "(<->)"
"""Constant to distinguish transfer Vat between Fields menu option"""


# Factory buffer fields names.
# To Do - .startswidth("T") for TestFixture
FACTORY_FIELDS_NAMES = ["In",
                        "Corr",
                        TEST_FIXTURE_DISTINGUISHER + "1",
                        TEST_FIXTURE_DISTINGUISHER + "2",
                        "Out",
                        ]

# Dictionary containing menu options and sections dividers.
# To Do - rules - str dividers, int options, "(X <-> Y)" for Factory Field, 
TEXT_MENU = {
    "Mov": "---------- Vat logistics ----------",
    1: INPUT_VAT_DISTINGUISHER + " Input new Vat to In",
    2: INPUT_VAT_DISTINGUISHER + " Move OK Vat from Out",
    3: TRANSFER_VAT_DISTINGUISHER + " Transfer Vat between Fields",

    "End": "---------- Finish program ----------",
    0: "Finish productive work shift :)",
    }
