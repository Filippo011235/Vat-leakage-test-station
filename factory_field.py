from vat import Vat


class FactoryField:
    """ Kokos
    Kokos kokos
    """

    def __init__(self, field_name="Bufor") -> None:
        """
        A class used to represent an Animal

        ...

        Attributes
        ----------
        says_str : str
            a formatted string to print out what the animal says
        name : str
            the name of the animal
        sound : str
            the sound that the animal makes
        num_legs : int
            the number of legs the animal has (default 4)

        Methods
        -------
        says(sound=None)
            Prints the animals name and what sound it makes
        """
        self.name_ = field_name
        self.current_vat = None
    
    def receive_vat(self, new_vat: Vat):
        """Assign a new_vat to an empty FactoryField

        Parameters:
        new_vat -- new Vat class object to fill this Field

        Return:
        bool -- True, if assigned correctly, False if Field is taken
        """

        if self.current_vat is None:
            self.current_vat = new_vat
            print(f"Field {self.name_} received {new_vat.get_barcode()}")
            return True
        else:
            print(f"Field {self.name_} is already taken by \
                    {self.current_vat.get_barcode()}! Take it back first!")
            return False

    def get_vat(self):
        """If Field has a Vat, return a copy of it, otherwise None."""
        if self.current_vat is not None:
            return self.current_vat
        else:
            print(f"Field {self.name_} has no vat inside")
            return None

    def delete_vat(self):
        """Delete Vat. If doable return True, otherwise False."""
        if self.current_vat is not None:
            self.current_vat = None
            return True
        else:
            print(f"Field {self.name_} has no vat inside!")
            return False