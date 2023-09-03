import random

class Vessel:
    """ Kokos
    Kokos kokos
    """

    def __init__(self, initial_size) -> None:
        self.size_ = initial_size
        self.barcode = random.randint(1, 1000)
        self.tests_list = []
    
    def add_test(self, time_date):
        self.tests_list.append(time_date)

    def get_barcode(self):
        return self.size_
    
    def get_barcode(self):
        return self.barcode
    
    def get_tests_list(self):
        return self.tests_list
