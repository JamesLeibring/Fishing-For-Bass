# The Player Class

class Player:
    def __init__(self, player):
        self.player = player
        self.color = 'blue'

        self.territories = []
        self.coasts = []

        self.units = {
            'Land': [],
            'Sea': [],
            'Air': []   
        }

        self.resources = [0, 0, 0, 0]
