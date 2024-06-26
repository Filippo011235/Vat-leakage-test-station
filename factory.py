"""Module containing Factory class, which serves as a scene for simulation.

Classes:
    Factory
"""

from text_data import (FINISH_CONST, INPUT_ID, TEST_FIXTURE_ID, OUTPUT_ID,
                      ADD_INPUT_VAT_ID, DEL_OUTPUT_VAT_ID, MOVE_VAT_ID,
                      TEST_VAT_ID, CANCEL_OPERATION, AUTO_MODE_ID)
from vat import Vat, VAT_MODELS
from factory_field import FactoryField
from test_fixture import TestFixture

from random import randint
from types import NoneType

class Factory:
    """Simulate whole factory, contain and operate on FactoryFields and Vats.

    Attributes:
        methods_mapping : Dict connecting Factory methods with menu options.
        factory_fields : List that stores buffer fields making the scene.
    """

    def __init__(self, menu_options: dict, factory_fields_names: list=["Bufor"]) -> None:
        """Init. a factory with a list of factory fields names and menu dict.

        Args:
            menu_options : Shared dictionary, on which method mapping is based.
            factory_fields_names : List of str names for Factory fields.
        """
        # Check whether menu has all non-empty values(keys descriptions).
        if not any(menu_options.values()):
            raise ValueError("\nmenu_options haven't been properly declared!\n")

        # Mapping menu_options numeration to methods
        self.methods_mapping = {}
        # TODO - verify whther menu_options a correct dict? 1 In, 1 Out, 1 TF?

        self.methods_mapping[FINISH_CONST] = self.finish_entered_do_nothing
        for k, v in menu_options.items():
            # Focus on menu options(int keys), not section dividers(str keys).
            if isinstance(k, int): 
                # If menu option description matches a Distinguisher, connect
                # this option numeric value with the method of Factory class.
                if ADD_INPUT_VAT_ID in v:
                    self.methods_mapping[k] = self.add_vat_to_input
                elif DEL_OUTPUT_VAT_ID in v:
                    self.methods_mapping[k] = self.remove_vat_from_output
                elif MOVE_VAT_ID in v:
                    self.methods_mapping[k] = self.transfer_vat_between_fields
                elif TEST_VAT_ID in v:
                    self.methods_mapping[k] = self.test_vat
                elif AUTO_MODE_ID in v:
                    self.methods_mapping[k] = self.auto_mode_step
                else:
                    continue

        # Factory fields init, by analysing strings in list of names.
        self.factory_fields = [TestFixture(x) if x.startswith(TEST_FIXTURE_ID)
                            else FactoryField(x) for x in factory_fields_names]

    def provide_fields_for_methods(self, field_ID: str="", 
                                   check_for_full: bool=False):
        """ 
        TODO poprawic docstring
        Yield Field which matches criteria, or print info about it.

        Arguments:
            field_ID : str which will filter Fields, based on their name.
            check_for_full : boolean for filtering Fields with(out) a Vat.
        Yield:
            field : FactoryField matching filters.
            None : when there is nothing more to yield.
        """
        if check_for_full:
            desired_state = Vat
        else:
            desired_state = NoneType

        for idx, field in enumerate(self.factory_fields):
            # Avoiding nested if with negation and continue.
            # Filter Fields with different name.
            if not field.get_name().startswith(field_ID):
                continue

            # Filter Fields with undesired Vat occupancy.
            # If field_ID is "", then don't filter according to Vat state.
            if not isinstance(field.get_vat(), desired_state) and field_ID != "":
                # For test Vat operation, inform that there is an empty Field.
                if field_ID is TEST_FIXTURE_ID:
                    print(f"--. {field.get_name()} - has no Vat to test.")
                continue

            # For test and transfer operations, print the Fields.
            if TEST_FIXTURE_ID in field_ID or field_ID == "":
                print(f"{idx}. {field.get_name()} - {field.get_vat()}")
            # Input, output operations - return index of desired Field.
            else:
                return field

        # After last element, additionally print cancelation option.
        # But not for Input and Output operations!
        if not (field_ID == INPUT_ID or field_ID == OUTPUT_ID):
            print(f"Enter {CANCEL_OPERATION}, if you want to",
                            "cancel this operation\n")

        # For test, transfer - all info has been printed.
        # For input, output - no Field has satisfied criteria.
        return None

    def add_vat_to_input(self):
        """Look for a free Field with input ID, and assign a new Vat to it.

        Return:
            str : Informing whether the operation was succesful or not.
        """
        input_field = self.provide_fields_for_methods(INPUT_ID)
        if input_field:
            # OPTION 1 - ASKING USER FOR NEW VAT MODEL:
            # ... Yay, now ask about new Vat, and verify.
            # vat_model_min, *_, vat_model_max = list(VAT_MODELS.keys())
            # input_text = (f"Please enter model ({vat_model_min}"
            #              + f" - {vat_model_max}) of the new Vat: ")
            # while True:
            #     try: # check for correct input type
            #         new_model = int(input(input_text))
            #     except (ValueError, KeyboardInterrupt, EOFError):
            #         print("Enter correct model, silly!")
            #         continue

            #     # check for correct value of the model
            #     if vat_model_min <= new_model <= vat_model_max:
            #         break # all good, break while loop
            #     else:
            #         print("Enter correct model, silly!")

            # OPTION 2 - MAKING NEW VAT WITH A RAND MODEL:
            vat_model_min, *_, vat_model_max = VAT_MODELS.keys()
            new_model = randint(vat_model_min, vat_model_max)

            input_field.set_vat(Vat(new_model))
            dest_field_name = input_field.get_name()

            return f"\nVat was correctly assigned to {dest_field_name}.\n"

        # If no free buffer has been found, operation has failed
        else:
            return "\n Sorry! No available Input buffers :( \n"

    def remove_vat_from_output(self):
        """Look for a taken Output Field, and confirm before removing a Vat.

        Return:
            str : Informing whether the operation was succesful or not.
        """
        # Look for a taken output buffer...
        output_field = self.provide_fields_for_methods(OUTPUT_ID, True)
        if output_field:
            # ... Yay, now ask for confirmation.
            vat_ID = output_field.get_vat().get_barcode()
            f_name = output_field.get_name()
            input_text = ("Do you really want to take out "
                            f"{vat_ID} from {f_name} (\"y\"/\"n\")? ")
            while True:
                try:
                    decision = input(input_text)
                except (ValueError, KeyboardInterrupt, EOFError):
                    print("What was that? Try again.")
                    continue

                # Check for correct string.
                if decision.lower() == "y":
                    output_field.delete_vat()
                    return f"\nVat {vat_ID} was pushed out from {f_name}\n"
                elif decision.lower() == "n":
                    print(f"\nOk, I'm leaving {vat_ID} alone.\n")
                    break # all good, break while loop
                else:
                    print("Enter correct input (y/n), silly!")
        else:
            print("\n No taken Output Field was found.\n")
        
        # Every field was analysed and no Vat was pushed out
        return "\tNo Vat has been harmed during this operation.\n"

    def transfer_vat_between_fields(self):
        """Ask user for a busy Field, then an empty one, and move the Vat.

        Return:
            str : Informing whether the operation was succesful or not.
        """
        # Establish field for the source vat:
        self.provide_fields_for_methods()
        source_text = ("From which field would you like "
                        "to move the Vat? Enter int: ")
        while True:
            try: # Check for correct input type.
                source_field_no = int(input(source_text))
            except (ValueError, KeyboardInterrupt, EOFError):
                print("What was that? Try again")
                continue

            # source_field is gonna be used to get vat, and later to delete it.
            try:
                source_field = self.factory_fields[source_field_no]
            except IndexError:
                if source_field_no is CANCEL_OPERATION:
                    return("Canceling this operation")
                print("Enter field according to the table, silly!")
                continue

            if source_field.get_vat() is None:
                print("Selected Field has no Vat! Try again")
                continue

            vat_to_transfer = source_field.get_vat()
            break

        # Now, establish field for the destination vat:
        print()
        self.provide_fields_for_methods()
        dest_text = ("OK, now, where do you want to transfer it?"
                     " Enter int: ")
        while True:
            # TODO: Function for check whether input is int
            try: # Check for correct input type.
                dest_field_no = int(input(dest_text))
            except (ValueError, KeyboardInterrupt, EOFError):
                print("What was that? Try again")
                continue

            # dest_field is gonna be used to get vat, and later to add it.
            try:
                dest_field = self.factory_fields[dest_field_no]
            except IndexError:
                if dest_field_no is CANCEL_OPERATION:
                    return("Canceling this operation")
                print("Enter field according to the table, silly!")
                continue

            if dest_field.get_vat():
                print("Selected Field has a Vat! Try again")
                continue

            break

        dest_field.set_vat(vat_to_transfer)
        source_field.delete_vat()

        return f"\n {vat_to_transfer} was moved to {dest_field.get_name()}\n"

    def test_vat(self):
        """Look for a Vat on a Test Field and test it.

        Return:
            str : Informing whether the operation was succesful or not.
        """
        print("Which Test Fixture would you like to start? ")
        self.provide_fields_for_methods(TEST_FIXTURE_ID, True)

        while True:
            try: # Check for correct input type.
                tf_no = int(input("Enter index of the desired Test Fixture: "))
            except (ValueError, KeyboardInterrupt, EOFError):
                print("What was that? Try again")
                continue

            try:
                test_field = self.factory_fields[tf_no]
            except IndexError:
                if tf_no is CANCEL_OPERATION:
                    return("Canceling this operation")
                print("Enter field according to the table, silly!")
                continue

            if test_field.get_vat() is None:
                print("Selected Field has no Vat! Try again")
                continue

            if test_field.test_vat():
                return "Vat has passed The Great Trial!"
            else:
                return "Vat has failed and has to be corrected!"

    def auto_mode_step(self):
        # Input fields:
        while True:
            empty_In_field = self.provide_fields_for_methods("In", False)
            if empty_In_field:
                self.add_vat_to_input()
            else:
                break
        
        # Output fields:
        while True:
            full_Out_field = self.provide_fields_for_methods("Out", True)
            if full_Out_field:
                self.remove_vat_from_output()
            else:
                break

    def get_factory_status(self):
        """Return tuples with info. about Fields, Vats and tests, for display.

        Return:
            factory_status : tuple containing tuples with info. for each Field.
                             (Field name, Vat barcode, Vat test result)
        """
        factory_status = []
        for field in self.factory_fields:
            f_name = field.get_name()

            try:
                f_status = field.get_vat().get_barcode()
                f_vat_test_results = field.get_vat().get_test_result()
            except AttributeError: # Field without Vat(None)
                f_status = "Empty"
                f_vat_test_results = ""

            factory_status.append((f_name, f_status, f_vat_test_results))

        return tuple(factory_status)

    def execute_user_input(self, users_wish):
        """Based on user input, and methods mapping, execute method."""
        # Input verification was conducted in function from menu module.
        return self.methods_mapping[int(users_wish)]()

    def finish_entered_do_nothing(self):
        """If user requested to end the program, do nothing"""
        return "\n Finishing work for today.\n"
