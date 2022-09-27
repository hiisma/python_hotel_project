__all__ = ['app']

def _show_menu():
    '''
    @brief Prints all the options that
    the user can choose.
    '''
    print("1. List all rooms")
    print("2. List empty rooms")
    print("3. List full rooms")
    print("4. Check In")
    print("5. Check Out")
    print("x. Exit program")

def _execute_option(option: str) -> bool:
    '''
    @brief executes one of the diferent options
    depending of the input.
    Option 1: List all rooms.
    Option 2: List empty rooms.
    Option 3: List full rooms.
    Option 4: Check In.
    Option 5: Check Out.
    @param option: option that should be executed
    @return True if option == 'x', else return False
    '''
    if option == "1":
        print("option 1")
        return False
    elif option == "2":
        print("option 2")
        return False
    elif option == "3":
        print("option 3")
        return False
    elif option == "4":
        print("option 4")
        return False
    elif option == "5":
        print("option 5")
        return False
    elif option == "x":
        return True
    else:
        print("option not valid")
        return False

def app():
    '''
    @brief Contains the main program.
    '''
    should_exit = False
    while(not should_exit):
        _show_menu()
        option = input("Input option: ")
        should_exit = _execute_option(option)