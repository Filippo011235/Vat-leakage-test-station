"""Module containing text menu related functions and data."""

from os import system

def clear(): system('cls')

def draw_factory_floor(factory_status):
    """Visualize all FactoryFields and Vats information.

    Args:
        factory_status (list of FactoryField obj) : List with information
                                                for drawing the factory floor
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

    factory_outline = [horizontal_bar,
                       empty_line,
                       main_line,
                       empty_line,
                       line_with_vats,
                       empty_line,
                       line_with_results,
                       empty_line,
                       horizontal_bar,
                       ]
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


# def Change_Tool():
#     # print(f"Obecny {VarFile.ANZAHL_TOOL}")
#     try:
#         # VarFile.ANZAHL_TOOL = int(input("Podaj nowy Anzahl_Tool(int): "))
#         # print(f"Nowa wartość Anzahl Tool: {VarFile.ANZAHL_TOOL}")
#         print("Kokos")
#     except ValueError as NotIntErr:
#         print("Numer Anzahl Tool musi być int!", NotIntErr)
    
#     confirm_mechanism()


# def Change_Eingang():

#     def IsInt(val):
#         try:
#             x = int(val)
#             return True
#         except ValueError:
#             return False
        
#     # print(f"Obecny {VarFile.EingangList}")
#     InputData = input("Podaj nową Eingang List, jako ciąg 0/1: ")
#     # Filter out eventuall not-ints and convert the rest to to int
#     InputData = list(filter(IsInt,InputData))
#     New_EL = [int(x) for x in InputData]
    
#     # Check correct bit values
#     if min(New_EL)>=0 and max(New_EL)<=1:
#         # VarFile.EingangList.clear()
#         # VarFile.EingangList = [bool(x) for x in New_EL]
#         # print(f"Nowa wartość Eingang List: {VarFile.EingangList}")
#         print("kokos")
#     else:
#         ################### TO DO #################
#         print("Eingang List miało być jedynkami i zerami!")
#         confirm_mechanism()
#         raise ValueError("Eingang List miało być jedynkami i zerami!")
    
#     confirm_mechanism()


# def Update_Load_Data():
#     k = 0
#     # for LoadDataLine in VarFile.LOAD_DATA[0:VarFile.ANZAHL_TOOL]:
#     #     LoadDataLine = 1
#     #     for i in range(0,VarFile.ANZAHL_TOOL):
#     #         LoadDataLine += int(VarFile.EingangList[i]) * (2**i)
#     #     VarFile.LOAD_DATA[k] = LoadDataLine
#     #     k += 1

#     # print(VarFile.LOAD_DATA)
#     # confirm_mechanism()


def finish_work_shift():
    """Break out of the menu loop."""
    print("Finishing work shift")
    # VarFile.Finishmenu = True

    confirm_mechanism()


def incorrect_option():
    """Inform that incorrect option was chosen."""
    print("\n Incorrect data was inputted! \n")
    
    confirm_mechanism()


menuOptions = {
    # 1: Change_Tool,
    # 2: Change_Eingang,
    # 3: Update_Load_Data,
    4: finish_work_shift
}


def execute_option(OptionChoice):
    Funkcja = menuOptions.get(OptionChoice, incorrect_option) 
    clear()
    return Funkcja()


def confirm_mechanism():
    """After choosing an option/doing an action, stop menu_display loop."""
    input("Confirm with Entern key")