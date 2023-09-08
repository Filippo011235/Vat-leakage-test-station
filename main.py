from text_data import TEXT_MENU, FACTORY_FIELDS_NAMES
from vat import Vat
from factory_field import FactoryField
from test_fixture import TestFixture
from factory import Factory
from text_menu import display_menu



if __name__ == "__main__":

    vat_test_station = Factory(TEXT_MENU, FACTORY_FIELDS_NAMES)
    # Preliminary simulation of Vats states.
    # for index, field in enumerate(factory_fields):
    #     field.set_vat(Vat(2))
        
    #     if index is not 0:
    #         if index % 2:
    #             field.get_vat().set_test_result(False)
    #         else:
    #             field.get_vat().set_test_result(True)

    # factory_fields[3].delete_vat()

    display_menu(TEXT_MENU, vat_test_station.get_factory_status())


