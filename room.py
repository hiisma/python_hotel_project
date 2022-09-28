class Room:
    '''
    @author Ismail A. O.
    @brief This class is a container of the room information.
    '''

    # ATTRIBUTES
    __room_id: str = None
    __room_type: str = None
    __capacity: int = None
    __is_empty: bool = None
    __description: str = None

    # CONSTRUCTORS
    def __init__(self,room_id: str, room_type: str, capacity: int, isEmpty: bool, description: str):
        '''
        @brief constructor with all parameters of the room.
        @param room_id: identifier of the room.
        @param room_type: type of the room.
        @param capacity: how many people can be acomodated.
        @param isEmpty: indicates if the room is ocupied.
        @param description: other information of the room.
        '''
        self.__room_id = room_id
        self.__room_type = room_type
        self.__capacity =  capacity
        self.__is_empty = isEmpty
        self.__description = description

    def __init__(self):
        '''
        @brief default constructor.
        '''
        self.__room_id = ""
        self.__room_type = ""
        self.__capacity = 0
        self.__is_empty = True
        self.__description = ""

    # SETTERS
    def set_empty(self):
        '''@brief empty = True'''
        self.__is_empty = True

    def set_full(self):
        '''@brief empty = False'''
        self.__is_empty = False

    def set_capacity(self, new_capacity: int):
        self.__capacity = new_capacity
    
    def set_description(self, new_description: str):
        self.__description = new_description

    # GETTERS
    def get_is_empty(self) -> bool:
        return self.__is_empty
    
    def get_capacity(self) -> int:
        return self.__capacity

    def get_room_id(self) -> str:
        return self.__room_id

    def get_room_type(self) -> str:
        return self.__room_type
    
    def get_description(self) -> str:
        return self.__description