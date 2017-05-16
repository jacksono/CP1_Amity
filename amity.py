class Amity:
    '''Definitionof Amity class
    '''
    def __init__(self):
        self.all_rooms = []

    def create_room(self, name, type):
        self.all_rooms.append(name)
        return "{} has been successfully created".format(name)
