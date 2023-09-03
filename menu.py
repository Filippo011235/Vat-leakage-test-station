from os import system


# Dictionary containing menu options.
menu = {}
menu['0'] = "(-> In) Input new Vessel to In"
menu['1'] = "(Out ->) Move OK Vessel from Out"

menu['T1'] = "---------- Tester 1 functions ----------"
menu['2'] = "(In -> T1) Move Vessel In to Tester 1"
menu['5'] = "(Corr -> T1) Move corrected Vessel to Tester 1"
menu['8'] = "(T1 -> Out/Corr) Move tested Vessel out of Tester 1"

menu['T2'] = "---------- Tester 2 functions ----------"
menu['3'] = "(In -> T2) Move Vessel In to Tester 2"
menu['6'] = "(Corr -> T2) Move corrected Vessel to Tester 2"
menu['9'] = "(T2 -> Out/Corr) Move tested Vessel out of Tester 2"

menu['End'] = "---------- Finish program ----------"
menu['10'] = "Finish productive work shift :)"

# Factory buffer fields names.
factory_fields = ["In",
                  "Corr",
                  "T1",
                  "T2",
                  "Out",
                  ]


def clear(): system('cls')

def draw_factory_floor():

    # Main information line, to which information will be added, 
    # and whole frame will be based upon.
    main_line = "*\t"
    for field in factory_fields:
        main_line = "".join([main_line,field,"\t"])

    line_with_vessels = "*\t"
    for index, field in enumerate(factory_fields):
        if index % 2:
            line_with_vessels = "".join([line_with_vessels,
                                         "Vessel","\t"])
        else:
            line_with_vessels = "".join([line_with_vessels,
                                         "Empty","\t"])

    horizontal_bar = "*" * (3*len(main_line))
    empty_line = "*"
    missing_length = len(horizontal_bar) - len(empty_line) - 1
    empty_line = ''.join([empty_line, " " * missing_length, "*"])

    print(horizontal_bar)
    print(empty_line)
    print(main_line)
    print(empty_line)
    print(line_with_vessels)
    print(empty_line)
    print(horizontal_bar)



def display_menu():

    # is_int is used to verify and edit menu options printing.
    def is_int(val):
        try:
            x = int(val)
            return True
        except ValueError:
            return False
        
    clear()
    draw_factory_floor()
    # print(f"Obecny Anzahl Tool: \t{VarFile.ANZAHL_TOOL}")
    # print(f"Obecny Eingang List: \t{VarFile.EingangList}")
    # print(f"Obecny Load Data: \t{VarFile.LOAD_DATA}")
    menu_lines = list(menu.keys())
    print("Opcje menu:")
    for position in menu_lines:
        if is_int(position):
            print("\t".expandtabs(2), position, "\t", menu[position])
        else:
            print()
            print("\t".expandtabs(2), position, "\t", menu[position])


def Change_Tool():
    # print(f"Obecny {VarFile.ANZAHL_TOOL}")
    try:
        # VarFile.ANZAHL_TOOL = int(input("Podaj nowy Anzahl_Tool(int): "))
        # print(f"Nowa wartość Anzahl Tool: {VarFile.ANZAHL_TOOL}")
        print("Kokos")
    except ValueError as NotIntErr:
        print("Numer Anzahl Tool musi być int!", NotIntErr)
    
    ConfirmMechanism()


def Change_Eingang():

    def IsInt(val):
        try:
            x = int(val)
            return True
        except ValueError:
            return False
        
    # print(f"Obecny {VarFile.EingangList}")
    InputData = input("Podaj nową Eingang List, jako ciąg 0/1: ")
    # Filter out eventuall not-ints and convert the rest to to int
    InputData = list(filter(IsInt,InputData))
    New_EL = [int(x) for x in InputData]
    
    # Check correct bit values
    if min(New_EL)>=0 and max(New_EL)<=1:
        # VarFile.EingangList.clear()
        # VarFile.EingangList = [bool(x) for x in New_EL]
        # print(f"Nowa wartość Eingang List: {VarFile.EingangList}")
        print("kokos")
    else:
        ################### TO DO #################
        print("Eingang List miało być jedynkami i zerami!")
        ConfirmMechanism
        raise ValueError("Eingang List miało być jedynkami i zerami!")
    
    ConfirmMechanism()


def Update_Load_Data():
    k = 0
    # for LoadDataLine in VarFile.LOAD_DATA[0:VarFile.ANZAHL_TOOL]:
    #     LoadDataLine = 1
    #     for i in range(0,VarFile.ANZAHL_TOOL):
    #         LoadDataLine += int(VarFile.EingangList[i]) * (2**i)
    #     VarFile.LOAD_DATA[k] = LoadDataLine
    #     k += 1

    # print(VarFile.LOAD_DATA)
    # ConfirmMechanism()


def finish_work_shift():
    print("Finishing work shift")
    # VarFile.Finishmenu = True
    
    ConfirmMechanism()


def IncorretData():
    print("\n Incorrect data was inputted! \n")
    
    ConfirmMechanism()


menuOptions = {
    1: Change_Tool,
    2: Change_Eingang,
    3: Update_Load_Data,
    4: finish_work_shift
}


def ExecuteOption(OptionChoice):
    Funkcja = menuOptions.get(OptionChoice, IncorretData) 
    clear()
    return Funkcja()


def ConfirmMechanism():
    input("Confirm with Entern key")