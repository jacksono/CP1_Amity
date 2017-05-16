class Amity:
    '''Definitionof Amity class
    '''
    def __init__(self):
        self.all_rooms = {}

    def create_room(self, room_name, room_type):
        self.all_rooms[room_name] = room_type
        return "{} has been successfully created".format(room_name)
