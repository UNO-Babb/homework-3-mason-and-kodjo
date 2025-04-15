class Player:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
        self.health = 100
        self.mental_state = 100
        self.inventory = {"food": 0, "water": 0, "medicine": 0}
        self.status = "alive"

class Shelter:
    def __init__(self):
        self.supplies = {"food": 10, "water": 10, "medicine": 5}
        self.days_survived = 0
        self.event_log = []

class GameState:
    def __init__(self):
        self.players = []
        self.shelter = Shelter()
        self.day = 1
        self.game_over = False
