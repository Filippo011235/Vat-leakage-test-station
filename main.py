from vat import Vat
from factory_field import FactoryField
from test_fixture import TestFixture
from text_menu import display_menu

# Factory buffer fields names.
factory_fields_names = ["In",
                        "Corr",
                        "T1",
                        "T2",
                        "Out",
                        ]

# Dictionary containing menu options and sections dividers.
text_menu = {
    0: "(-> In) Input new Vat to In",
    1: "(Out ->) Move OK Vat from Out",

    "T1": "---------- Tester 1 functions ----------",
    2: "(In -> T1) Move Vat In to Tester 1",
    5: "(Corr -> T1) Move corrected Vat to Tester 1",
    8: "(T1 -> Out/Corr) Move tested Vat out of Tester 1",

    "T2": "---------- Tester 2 functions ----------",
    3: "(In -> T2) Move Vat In to Tester 2",
    6: "(Corr -> T2) Move corrected Vat to Tester 2",
    9: "(T2 -> Out/Corr) Move tested Vat out of Tester 2",

    "End": "---------- Finish program ----------",
    10: "Finish productive work shift :)",
    }


if __name__ == "__main__":

    # Factory fields init
    factory_fields = [FactoryField(x) if not x.startswith("T")
                      else TestFixture(x) for x in factory_fields_names]

    # Preliminary simulation of Vats states.
    # for index, field in enumerate(factory_fields):
    #     field.set_vat(Vat(2))
        
    #     if index is not 0:
    #         if index % 2:
    #             field.get_vat().set_test_result(False)
    #         else:
    #             field.get_vat().set_test_result(True)

    # factory_fields[3].delete_vat()

    display_menu(text_menu, factory_fields)


