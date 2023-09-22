"""Module containing text menu related functions.

Functions:
    clear - Auxiliary function for clearing terminal screen.
    confirm_mechanism - Auxiliary function for giving user time after action.
    draw_factory_floor - Based on the status of Factory, draw visualisation.
    display_menu - Handles displaying menu and asking user for input/option.
"""

from os import system

def clear(): system('cls')

def confirm_mechanism():
    """After choosing an option/doing an action, stop menu_display loop."""
    input("Confirm with Entern key")

def draw_factory_floor(factory_status):
    """Visualize all FactoryFields and Vats information.

    Args:
        factory_status (list of FactoryField obj) : List with information
                                                for drawing the factory floor.
    """

    # Main information line, to which information will be added,
    # and whole frame will be based upon.
    main_line = "Fields:\t"
    # Line holding information about Vats in Factoryfields
    line_with_vats = "Vats:\t"
    # Line holding information about Vats' test results
    line_with_results = "Test:\t"

    # factory_status contains tuples with info:
    # [0] FactoryField name, 
    # [1] (if any) Vat code, 
    # [2] (if any) test result
    for field_stats in factory_status:
        main_line = "".join([main_line,field_stats[0], "\t"])
        line_with_vats = "".join([line_with_vats, str(field_stats[1]), "\t"])
        line_with_results = "".join([line_with_results, field_stats[2], "\t"])

    horizontal_bar = "*" * (2*len(main_line))
    empty_line = "*"
    missing_length = len(horizontal_bar) - len(empty_line) - 1
    empty_line = ''.join([empty_line, " " * missing_length, "*"])

    factory_outline = (horizontal_bar,
                       empty_line,
                       main_line,
                       empty_line,
                       line_with_vats,
                       empty_line,
                       line_with_results,
                       empty_line,
                       horizontal_bar,
                       )
    for line in factory_outline:
        print(line)

def display_menu(menu_options, factory_status):
    """Display factory visualization and all menu options.
    
    Args:
        menu_options (dict) : Dictionary with int keys as options numbers and
                            str keys for section dividers. 
                            Values are options/sections description.
        factory_status (list of FactoryField obj) : List with information
                                                for drawing the factory floor.
    Return:
        user_input (int) : number representing one of the menu options keys.
    """

    clear()
    draw_factory_floor(factory_status)
    print("Menu options:")
    for position in menu_options.keys():
        # Section titles are str, thus making section dividers easy to put.
        if isinstance(position, str):
            print()
        print("\t".expandtabs(2), position, "\t", menu_options[position])

    while True:
        try:
            user_input = int(input("What would you like to do? Enter int: "))
        except (ValueError, KeyboardInterrupt, EOFError):
            print("What was that? Try again with an int!")
            continue
        if user_input in menu_options.keys():
            return user_input
        else:
            print("Incorrect option, try again!")
