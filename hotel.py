import csv
import Room


class Hotel:
    '''
    Class Hotel reads a csv file with all the data of
    the rooms that the hotel has.
    The csv file needs to use ',' as separator and have the
    following columns in the same order.
        -id
        -type
        -capacity
        -is empty
        -description
    
    Also it has the capacity to save the new csv.
    '''

    # CONSTANTS
    __ROOM_NUMBER_OF_ATTRIBUTES = 5

    # ATTRIBUTES
    __rooms = list()
    __hotel_name: str = None
    __data_dir: str = None

    # CONSTRUCTORS
    def __init__(self):
        self.__hotel_name = "No Name"

    def __init__(self, hotel_name: str):
        self.__hotel_name = hotel_name

    # PUBLIC FUNCTIONS
    def open_hotel_data(self, data_dir: str):
        '''
        @brief opens the file containing the hotel data
        and saves it in the hotel object.
        '''
        self.__data_dir = data_dir

        # file will be opened once during execution
        with open(data_dir) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            self.__rooms = []
            for row in csv_reader:
                # read csv row and save variables
                room_id = row[0]
                room_type = row[1] 
                capacity = row[2]
                is_empty = row[3] == "True" # Convert to boolean 
                description = row[4]

                # instantiate room in array
                self.__rooms.append(Room.Room(room_id, room_type, capacity, is_empty, description))

            # remove header of table
            del self.__rooms[0]

    def save_hotel_data(self):
        '''
        @brief saves current hotel data.
        '''
        with open(self.__data_dir, "w") as csv_file:
            csv_file.write("id,type,capacity,is empty,description\n")
            for row in self.__rooms:
                csv_file.write(
                    row.get_room_id() + "," +
                    row.get_room_type() + "," +
                    row.get_capacity() + "," +
                    ("True" if row.get_is_empty() else "False") + "," +
                    row.get_description() + "\n"
                    )

        
    def print_rooms(self):
        '''
        @brief prints all the rooms data of
        the hotel.
        '''
        print("id type   capacity is_empty\tdescription")
        print("------------------------------------------------")
        for row in self.__rooms:
            row.print_info()

    def print_empty_rooms(self):
        '''
        @brief prints all the empty rooms data
        of the hotel.
        '''
        print("id type   capacity is_empty\tdescription")
        print("------------------------------------------------")
        for row in self.__rooms:
            if row.get_is_empty():
                row.print_info()

    def print_full_rooms(self):
        '''
        @brief prints all the full rooms data
        of the hotel.
        '''
        print("id type   capacity is_empty\tdescription")
        print("------------------------------------------------")
        for row in self.__rooms:
            if not row.get_is_empty():
                row.print_info()
    


    def check_in(self, room_id: str):
        '''
        @brief Allows to check in the room.
        @param room_id: str Room to do the check in.
        '''
        if self.__room_exists(room_id):
            if self.__rooms[int(room_id)].get_is_empty():
                self.__rooms[int(room_id)].set_full()
                print("Room " + room_id + " checked in succesfully")
            else:
                print("Room is not empty.")

    def check_out(self, room_id: str):
        '''
        @brief Allows to check out the room.
        @param room_id: str Room to do the check out.
        '''
        if self.__room_exists(room_id):
            if not self.__rooms[int(room_id)].get_is_empty():
                self.__rooms[int(room_id)].set_empty()
                print("Room " + room_id + " checked out succesfully")
            else:
                print("Room is already empty.")

    # PRIVATE FUNCTIONS.
    def __room_exists(self, room_id: str) -> bool:
        '''
        @brief checks if the room_id exists in the
        hotel list, in case of not existing prints
        it in the console.
        @param room_id: str. id to search for.
        @return True if exists, False otherwise.
        '''
        room_id_as_number = -1
        try:
            room_id_as_number = int(room_id)
        except:
            print("Room doesn't exist Bad Format")
            return False
        
        if (room_id_as_number < 0 or room_id_as_number > len(self.__rooms)):
            return False
        
        return True