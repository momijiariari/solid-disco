class Gameboard():

    def __init__(self, num):
        Repair = num
        Bom = 1
        Silent = 4 * num - 1
        self.card = (Repair, Bom, Silent)
        self.unrepair = Repair

    def discard(self, card):
        self.card[card] -= 1

    def repair(self):
        self.unrepair -= 1
