import random

class Vat:
    """ Kokos
    Kokos kokos
    """

    def __init__(self, initial_size, init_test_result = None) -> None:
        self.size_ = initial_size
        self.barcode = random.randint(1, 1000)
        self.test_result = init_test_result

    def get_size(self):
        return self.size_

    def get_barcode(self):
        return self.barcode

    def set_test_result(self, vat_test_result):
        if isinstance(vat_test_result, bool):
            self.test_result = vat_test_result
        else:
            raise TypeError("Only bool result is allowed!")

    def get_test_result(self):
        return self.test_result

