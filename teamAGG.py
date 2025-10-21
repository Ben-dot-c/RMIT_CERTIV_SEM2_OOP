class Team:
    def __init__(self, name , sport, location):
        self.__name = name
        self.__sport = sport
        self.__location = location

    def get_name(self):
        return self.__name

    def get_sport(self):
        return self.__sport

    def get_location(self):
        return self.__location

    def __str__(self):
        return f"team Name = {self.__name}, sport = {self.__sport}, location = {self.__location}"

