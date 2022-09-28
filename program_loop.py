__all__ = ['app']

from cgi import test
import Hotel

def __show_menu():
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

def __execute_option(option: str, data: Hotel) -> bool:
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
        data.print_all_rooms()
        return False
    elif option == "2":
        data.print_empty_rooms()
        return False
    elif option == "3":
        data.print_full_rooms()
        return False
    elif option == "4":
        data.check_in()
        return False
    elif option == "5":
        data.check_out()
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
    hotel_file = Hotel.Hotel("Vendredi")
    hotel_file.open_hotel_data("rooms.csv")
    while(not should_exit):
        __show_menu()
        option = input("Input option: ")
        should_exit = __execute_option(option, hotel_file)