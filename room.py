class Room:
    room_id: str = None
    room_type: str = None
    capacity: int = None
    is_empty: bool = None
    description: str = None

    def __init__(self,room_id: str, room_type: str, capacity: int, isEmpty: bool, description: str):
        '''
        @brief constructor with all parameters of the room.
        @param room_id: identifier of the room.
        @param room_type: type of the room.
        @param capacity: how many people can be acomodated.
        @param isEmpty: indicates if the room is ocupied.
        @param description: other information of the room.
        '''
        self.room_id = room_id
        self.room_type = room_type
        self.capacity =  capacity
        self.is_empty = isEmpty
        self.description = description

    def __init(self):
        '''
        @brief default constructor.
        '''
        self.room_id = ""
        self.room_type = ""
        self.capacity = 0
        self.is_empty = True
        self.description = ""

    # SETTERS
    def set_empty(self):
        self.is_empty = True

    def set_full(self):
        self.is_empty = False

    def set_capacity(self, new_capacity: int):
        self.capacity = new_capacity
    
    def set_description(self, new_description: str):
        self.description = new_description

    # GETTERS
    def get_is_empty(self) -> bool:
        return self.is_empty
    
    def get_capacity(self) -> int:
        return self.capacity

    def get_room_id(self) -> str:
        return self.room_id

    def get_room_type(self) -> str:
        return self.room_type
    
    def get_description(self) -> str:
        return self.description