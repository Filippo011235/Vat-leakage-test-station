"""Module containing text menu related functions and data."""

from os import system

def clear(): system('cls')

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

    for field in factory_status:
        main_line = "".join([main_line,field[0], "\t"])
        line_with_vats = "".join([line_with_vats, str(field[1]), "\t"])
        line_with_results = "".join([line_with_results, field[2], "\t"])

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
                                                for drawing the factory floor
    """

    clear()
    draw_factory_floor(factory_status)
    print("Menu options:")
    for position in menu_options.keys():
        # Section titles are str keys, thus making section dividers easy to put
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

# To Do usun to
# def incorrect_option():
#     """Inform that incorrect option was chosen."""
#     print("\n Incorrect data was inputted! \n")
    
#     confirm_mechanism()

def confirm_mechanism():
    """After choosing an option/doing an action, stop menu_display loop."""
    input("Confirm with Entern key")