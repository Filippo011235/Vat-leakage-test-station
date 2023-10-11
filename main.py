from text_data import (TEXT_MENU, FACTORY_FIELDS_NAMES, 
                        FINISH_CONST, RESULTS_SAVE_DIR)
from factory import Factory
from test_data_handler import TestDataHandler
from text_menu import display_menu, clear, confirm_mechanism

if __name__ == "__main__":
    # Initiate Factory as a stage with all the objects.
    vat_test_station = Factory(TEXT_MENU, FACTORY_FIELDS_NAMES)
    test_results_handler = TestDataHandler(RESULTS_SAVE_DIR)

    user_input = None
    clear()
    while user_input is not FINISH_CONST:
        # Display menu with current Factory status and get user input.
        user_input = display_menu(TEXT_MENU, 
                                  vat_test_station.get_factory_status())
        clear()

        # Do operations based on the user input, or skip it and finish loop.
        # Operations return string - their result, to be printed.
        print(vat_test_station.execute_user_input(user_input))
        # if user_input == test vat ID: update test librarian
        confirm_mechanism()

    # After finishing, clean directory with test results.
    test_results_handler.clear_dir()
