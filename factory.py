"""Module containing class that simulates whole factory.

Classes:
    Factory
"""

# NOTE: Does importing from main create a cross reference, 
#       which should be avoided?
from text_data import TEST_FIXTURE_DISTINGUISHER, INPUT_VAT_DISTINGUISHER, \
                    OUTPUT_VAT_DISTINGUISHER, TRANSFER_VAT_DISTINGUISHER
from vat import Vat
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
        self.factory_fields = [TestFixture(x) if
                                    x.startswith(TEST_FIXTURE_DISTINGUISHER)
                                        else FactoryField(x) for
                                            x in factory_fields_names]


    def add_vat_to_input(self, new_vat : Vat):
        """

        Args:
            

        Return:
            
        """
        
    def remove_vat_from_output(self):
        """

        Args:
            

        Return:
            
        """
        
    def transfer_vat_between_fields(self):
        """

        Args:
            

        Return:
            
        """
        
    def get_factory_status(self):
        """

        Return:
            
        """
        factory_status = []

        for field in self.factory_fields:
            f_name = field.get_name()

            if field.get_vat():
                f_status = field.get_vat().get_barcode()

                if field.get_vat().get_test_result():
                    f_vat_test_results = "Pos"
                else:
                    f_vat_test_results = "Neg"

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
        print("kok")

    def execute_user_input(self, users_wish):
        """Based on user input, and method mapping, execute according method"""
        return self.methods_mapping[users_wish]()