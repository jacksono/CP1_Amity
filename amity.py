class Amity:
    '''Definitionof Amity class
    '''
    def __init__(self):
        self.all_rooms = {}

    def create_room(self, name, room_type):
        self.all_rooms[name] = room_type
        return "{} has been successfully created".format(name)
