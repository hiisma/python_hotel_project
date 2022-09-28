import csv
import Room


class Hotel:
    # CONSTANTS
    __ROOM_NUMBER_OF_ATTRIBUTES = 5

    # ATTRIBUTES
    __rooms = list()
    __hotel_name: str = None
    __data_dir: str = None

    # CONSTRUCTORS
    def __init__(self):
        self.__hotel_name = "No Name"
        pass

    def __init__(self, hotel_name: str):
        self.__hotel_name = hotel_name
        pass

    # FUNCTIONS
    def open_hotel_data(self, data_dir: str):
        '''
        @brief opens the file containing the hotel data
        and saves it in the hotel object.
        '''

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
        
    def print_rooms(self):
        print("id type   capacity is_empty\tdescription")
        print("------------------------------------------------")
        for row in self.__rooms:
            row.print_info()

    def print_empty_rooms(self):
        print("id type   capacity is_empty\tdescription")
        print("------------------------------------------------")
        for row in self.__rooms:
            if row.get_is_empty():
                row.print_info()

    def print_full_rooms(self):
        print("id type   capacity is_empty\tdescription")
        print("------------------------------------------------")
        for row in self.__rooms:
            if not row.get_is_empty():
                row.print_info()
    
    def check_in(self, room_id):
        pass

    def check_out(self, room_id):