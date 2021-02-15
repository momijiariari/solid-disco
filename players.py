class Player():

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.acted = False
        self.voted = False
        self.vote_count = 0
