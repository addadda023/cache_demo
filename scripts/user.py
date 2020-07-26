# User data graph


class User:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.friends = set()

    def is_friend(self, other):
        return other in self.friends

    def add_friend(self, other):
        self.friends.add(other)
