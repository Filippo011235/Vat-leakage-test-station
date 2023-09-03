import vessel


class FactoryField:
    """ Kokos
    Kokos kokos
    """

    def __init__(self, field_name="Bufor") -> None:
        self.name_ = field_name
        self.current_vessel = None
    
    def receive_vessel(self, new_vessel):
        # TO DO - check whether new_vessel is of Vessel class?
        if self.current_vessel is None:
            self.current_vessel = new_vessel
            print(f"Field {self.name_} received {new_vessel}")
            return True
        else:
            print(f"Field {self.name_} is already taken by \
                    {self.current_vessel}! Take it back first!")
            return False

    def get_vessel(self):
        if self.current_vessel is not None:
            return self.current_vessel
        else:
            print(f"Field {self.name_} has no vessel inside")
            return None
            
self.current_vessel = None



    def get_vessel(self):
        return self.size_
    
    def get_barcode(self):
        return self.barcode
    
    def get_tests_list(self):
        return self.tests_list
    