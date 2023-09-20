"""Module containing class that simulates a field, buffer, in a factory.

Classes:
    FactoryField
"""

from vat import Vat

class FactoryField:
    """Simulate a physical place on which Vats are being stored/processed.

    Initial example of usage include "In", and "Out" buffors, tester stations
    (which are a subclass in separate module and handle testing simulation)
    and vat "Correction" station. 

    Attributes:
        name_ (str): Name of the field.
        current_vat (class Vat): Current vat that is being stored(or not).
    """

    def __init__(self, field_name="Bufor") -> None:
        """Initiate a field with a given name and empty slot for a Vat.
        
        Args:
            field_name : str which will become name of the Field.
        """
        self.name_ = field_name
        self.current_vat = None

    def set_vat(self, new_vat: Vat):
        """Assign a new_vat to an empty FactoryField.

        Args:
            new_vat : new Vat class object to fill this Field.

        Return:
            bool : True, if assigned correctly, False if Field is taken.
        """
        if self.current_vat is None:
            self.current_vat = new_vat
            # print(f"Field {self.name_} received {new_vat.get_barcode()}")
            return True
        else:
            print(f"Field {self.name_} is already taken by"
                    f"{self.current_vat.get_barcode()}! Take it back first!")
            return False

    def get_vat(self):
        """If Field has a Vat, return a copy of it, otherwise None."""
        if self.current_vat is not None:
            return self.current_vat
        else:
            # print(f"Field {self.name_} has no vat inside")
            return None

    def delete_vat(self):
        """Delete Vat. If doable return True, otherwise False."""
        if self.current_vat is not None:
            self.current_vat = None
            return True
        else:
            print(f"Field {self.name_} has no vat inside!")
            return False

    def get_name(self):
        return self.name_
