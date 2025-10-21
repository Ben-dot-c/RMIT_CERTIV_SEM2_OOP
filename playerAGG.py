class Player:
    def __init__(self, name, position, teamObj):
        self.__name = name
        self.__position = position
        self.__teamObj = teamObj

    def get_name(self):
        return self.__name

    def get_position(self):
        return self.__position

    def get_teamObj(self):
        return self.__teamObj

    def __str__(self):
        return f"name = {self.__name}, position = {self.__position}"

#test