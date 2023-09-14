"""Module containing Factory class, which serves as a scene for simulation.

Classes:
    Factory
"""

from text_data import FINISH_CONST, INPUT_ID, TEST_FIXTURE_ID, OUTPUT_ID, \
                      ADD_INPUT_VAT_ID, DEL_OUTPUT_VAT_ID, MOVE_VAT_ID, \
                      TEST_VAT_ID
from vat import Vat, VAT_MODELS
from factory_field import FactoryField
from test_fixture import TestFixture

from random import randint

class Factory:
    """Simulate whole factory, contain and operate on FactoryFields and Vats.

    Attributes:
        methods_mapping : Dict connecting Factory methods with menu options.
        factory_fields : List that stores buffer fields making the scene.
    """

    def __init__(self, menu_options: dict, factory_fields_names=["Bufor"]) -> None:
        """Init. a factory with a list of factory fields names and menu dict.

        Args:
            menu_options : Shared dictionary, on which method mapping is based.
            factory_fields_names : List of str names for Factory fields.
        """
        # Mapping menu_options numeration to methods
        self.methods_mapping = {}
        # To Do - verify is menu_options a correct dict? 1 In, 1 Out, 1 TF

        self.methods_mapping[FINISH_CONST] = self.finish_entered_do_nothing
        for k, v in menu_options.items():
            # Focus on menu options(int keys), not section dividers(str keys).
            if isinstance(k, int): 
                # If menu option description matches a Distinguisher, connect \
                # this option numeric value with the method of Factory class
                if ADD_INPUT_VAT_ID in v:
                    self.methods_mapping[k] = self.add_vat_to_input
                elif DEL_OUTPUT_VAT_ID in v:
                    self.methods_mapping[k] = self.remove_vat_from_output
                elif MOVE_VAT_ID in v:
                    self.methods_mapping[k] = self.transfer_vat_between_fields
                elif TEST_VAT_ID in v:
                    self.methods_mapping[k] = self.test_vat
                # elif AUTO_MODE_ID in v:
                #     self.methods_mapping[k] = self.test_vat
                else:
                    continue

        # Factory fields init, by analysing strings in list of names.
        self.factory_fields = [TestFixture(x) if x.startswith(TEST_FIXTURE_ID)
                            else FactoryField(x) for x in factory_fields_names]

    def add_vat_to_input(self):
        """Look for a free Field with input ID, and assign a new Vat to it.

        Return:
            str : Informing whether the operation was succesful or not.
        """
        # Look for a free input buffer...
        for field in self.factory_fields:
            # Avoiding nested if's with "not" and "continue"
            if not field.get_name().startswith(INPUT_ID):
                continue
            if field.get_vat() is not None:
                continue

            # OPTION 1 - ASKING USER FOR NEW VAT MODEL:
            # ... Yay, now ask about new Vat, and verify.
            # vat_model_min, *_, vat_model_max = list(VAT_MODELS.keys())
            # input_text = f"Please enter model ({vat_model_min}" \
            #              + f" - {vat_model_max}) of the new Vat: "
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
            vat_model_min, *_, vat_model_max = list(VAT_MODELS.keys())
            new_model = randint(vat_model_min, vat_model_max)

            field.set_vat(Vat(new_model))
            return f"Vat was correctly assigned to {field.get_name()}"

        # If no free buffer has been found, operation has failed
        return "\n Sorry! No available Input buffers :( \n"

    def remove_vat_from_output(self):
        """Look for a taken Output Field, and confirm before removing a Vat.

        Return:
            str : Informing whether the operation was succesful or not.
        """
        # Look for a taken output buffer...
        for field in self.factory_fields:
            # Avoiding nested if's with "continue".
            if not field.get_name().startswith(OUTPUT_ID):
                continue
            if field.get_vat() is None:
                continue

            # ... Yay, now ask for confirmation.
            vat_ID = field.get_vat().get_barcode()
            f_name = field.get_name()
            input_text = f"Do you want to take out " \
                            + f"{vat_ID} from {f_name} (y/n) ? "

            # To Do: weryfikacja czy Vat ma pozytywny test przed usunieciem

            while True:
                try:
                    decision = input(input_text)
                except (ValueError, KeyboardInterrupt, EOFError):
                    print("What was that? Try again.")
                    continue

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
        """Ask user for a busy Field, then an empty one, and move the Vat.

        Return:
            str : Informing whether the operation was succesful or not.
        """
        def print_enum_fields():
            """Print out all fields in the Factory."""
            for idx, field in enumerate(self.factory_fields):
                print(f"{idx}. {field.get_name()} - " \
                      + f"{field.get_vat()}")
            print()

        # Establish field for the source vat:
        print_enum_fields()
        source_text = "From which field would you like " \
                        + "to move the Vat? Enter int: "
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
                print("Enter field according to the table, silly!")
                continue

            if source_field.get_vat() is None:
                print("Selected Field has no Vat! Try again")
                continue

            vat_to_transfer = source_field.get_vat()
            break

        # Now, establish field for the destination vat:
        print_enum_fields()
        dest_text = "OK, now, where do you want to transfer it?" \
                            + " Enter int: "
        while True:
            # To Do: Function for check whether input is int
            try: # Check for correct input type.
                dest_field_no = int(input(dest_text))
            except (ValueError, KeyboardInterrupt, EOFError):
                print("What was that? Try again")
                continue

            # dest_field is gonna be used to get vat, and later to add it.
            try:
                dest_field = self.factory_fields[dest_field_no]
            except IndexError:
                print("Enter field according to the table, silly!")
                continue

            if dest_field.get_vat():
                print("Selected Field has a Vat! Try again")
                continue

            break
        dest_field.set_vat(vat_to_transfer)
        source_field.delete_vat()
            # break

        return f"{vat_to_transfer} was moved to {dest_field.get_name()}"

    def test_vat(self):
        """Look for a Vat on a Test Field and test it.

        Return:
            str : Informing whether the operation was succesful or not.
        """
        print("Which Test Fixture would you like to start? ")
        for idx, field in enumerate(self.factory_fields):
            if not field.get_name().startswith(TEST_FIXTURE_ID):
                continue
            if field.get_vat() is None:
                print(f"--. {field.get_name()} - has no Vat")
                continue
            # Print Test Fields, with a Vat inside.
            print(f"{idx}. {field.get_name()} - " \
                    + f"{field.get_vat()}")
        print("Enter 100, if you want to cancel this operation\n")
        
        # TO DO 100 - hardcoded var


    # to do NOTE Jak nie ma takich pol to co wtedy?


        while True:
            try: # Check for correct input type.
                tf_no = int(input("Enter index of the desired Test Fixture: "))
            except (ValueError, KeyboardInterrupt, EOFError):
                print("What was that? Try again")
                continue

            try:
                test_field = self.factory_fields[tf_no]
            except IndexError:
                if tf_no is 100:
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

    def get_factory_status(self):
        """

        Return:
            
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
        """Based on user input, and method mapping, execute according method"""
        return self.methods_mapping[int(users_wish)]()

    def finish_entered_do_nothing(self):
        """If user requested to end the program, do nothing"""
        return "Finishing work for today."