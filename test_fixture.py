INIT_PRESSURE = 0.15

import vessel
import factory_field

class TestFixture(factory_field):
    """ Kokos
    Kokos kokos
    """

    def __init__(self) -> None:
        self.pressure = INIT_PRESSURE
        
