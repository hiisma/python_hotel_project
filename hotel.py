import csv
import room

__ROOM_NUMBER_OF_ATTRIBUTES = 5

class Hotel:
    __rooms: room = []
    __hotel_name: str = None
    __data_dir: str = None

    def __init__(self):
        pass

    def __init__(self, hotel_name: str):
        self.__hotel_name = hotel_name
        pass

    def open_hotel_data(data_dir: str):
        #TODO: Finish function
        with open(data_dir) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            i = 0
            for row in csv_reader:
                for j in range(__ROOM_NUMBER_OF_ATTRIBUTES):
                    room[i] = row[j]
                
                i += 1