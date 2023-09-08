"""Module containing class that simulates whole factory.

Classes:
    Factory
"""

from text_data import INPUT_ID, CORRECTION_ID, TEST_FIXTURE_ID, OUTPUT_ID, \
                      INPUT_VAT_DISTINGUISHER, OUTPUT_VAT_DISTINGUISHER, \
                      TRANSFER_VAT_DISTINGUISHER
from vat import Vat, VAT_MODELS
from factory_field import FactoryField
from test_fixture import TestFixture



class Factory:
    """Simulate whole factory, contain FactoryFields and Vats.

    To Do 

    Attributes:
        # name_ (str): Name of the field.
        # current_vat (class Vat): Current vat that is being stored(or not).
    """

    def __init__(self, menu_options: dict, factory_fields_names=["Bufor"]) -> None:
        """Initiate a factory with a list of names for factory fields.
        
        Args:
            menu_options : Shared dictionary, on which method mapping is based.
            factory_fields_names : List of str names for Factory fields.
        """
        # Mapping menu_options numeration to methods
        self.methods_mapping = {}
        # To Do - verify is menu_options a correct dict?
        for k, v in menu_options.items():
            # Focus on menu options(int keys), not section dividers(str keys).
            if isinstance(k, int): 
                # If menu option description matches a Distinguisher, connect \
                # this option numeric value with the method of Factory class
                if INPUT_VAT_DISTINGUISHER in v:
                    self.methods_mapping[k] = self.add_vat_to_input

                if OUTPUT_VAT_DISTINGUISHER in v:
                    self.methods_mapping[k] = self.remove_vat_from_output

                if TRANSFER_VAT_DISTINGUISHER in v:
                    self.methods_mapping[k] = self.transfer_vat_between_fields
        
        # Factory fields init, by analysing strings in list of names.
        self.factory_fields = [TestFixture(x) if x.startswith(TEST_FIXTURE_ID)
                            else FactoryField(x) for x in factory_fields_names]


    def add_vat_to_input(self):
        """

        Return:
            
        """
        # Look for a free input buffer...
        for field in self.factory_fields:
            # Avoiding nested if's with "not" and "continue"
            if not field.get_name().startswith(INPUT_ID):
                continue
            if field.get_vat() is not None:
                continue

            # ... Yay, now ask about new Vat, and verify.
            vat_model_min, *_, vat_model_max = list(VAT_MODELS.keys())
            input_text = f"Please enter model ({vat_model_min}" \
                         + f" - {vat_model_max}) of the new Vat: "
            while True:
                try: # check for correct input type
                    new_model = int(input(input_text))
                except (ValueError, KeyboardInterrupt):
                    print("Enter correct model, silly!")
                    continue

                # check for correct value of the model
                if vat_model_min <= new_model <= vat_model_max:
                    break # all good, break while loop
                else:
                    print("Enter correct model, silly!")

            field.set_vat(Vat(new_model))
            return f"Vat was correctly assigned to {field.get_name()}"

        # If no free buffer has been found, operation has failed
        return "\n Sorry! No available Input buffers :( \n"



    def remove_vat_from_output(self):
        """

        Args:
            

        Return:
            
        """
        # Look for a taken output buffer...
        for field in self.factory_fields:
            # Avoiding nested if's with "not" and "continue"
            if not field.get_name().startswith(OUTPUT_ID):
                continue
            if field.get_vat() is None:
                continue

            # ... Yay, now ask for confirmation.
            vat_ID = field.current_vat.barcode()
            f_name = field.get_name()
            input_text = f"Do you want to remove {vat_ID} from {f_name}(y/n)?"

            while True:
                decision = input(input_text)

                # Check for correct string.
                if decision == "y":
                    field.delete_vat()
                    return f"Vat {vat_ID} was pushed out from {f_name}"
                elif decision == "n":
                    print(f"Ok, I'm leaving {vat_ID} alone.")
                    break # all good, break while loop
                else:
                    print("Enter correct input (y/n), silly!")

        # Every field was analysed and no Vat was pushed out
        return f"No Vat has been harmed during making of this operation."


    def transfer_vat_between_fields(self):
        """

        Args:
            

        Return:
            
        """
        print("koko")
        
    def get_factory_status(self):
        """

        Return:
            
        """
        factory_status = []

        for field in self.factory_fields:
            f_name = field.get_name()

            if field.get_vat():
                f_status = field.get_vat().get_barcode()

                vat_test_res = field.get_vat().get_test_result()
                if vat_test_res:
                    f_vat_test_results = "Pos"
                elif vat_test_res is False:
                    f_vat_test_results = "Neg"
                else: # None
                    f_vat_test_results = "---"

            else: # Field without Vat(None)
                f_status = "Empty"
                f_vat_test_results = "---"

            factory_status.append((f_name, f_status, f_vat_test_results))

        return tuple(factory_status)

    def print_enum_fields(self):
        """

        Args:
            

        Return:
            
        """
        print("koko")

    def execute_user_input(self, users_wish):
        """Based on user input, and method mapping, execute according method"""
        return self.methods_mapping[int(users_wish)]()