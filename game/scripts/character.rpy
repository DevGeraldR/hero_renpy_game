# Class to create a character

init python:
    class character:
        def __init__(self, name, max_hp = 10, hp = 10, alive = True):
            self.name = name
            self.max_hp = max_hp
            self.hp = hp
            self.alive = alive
