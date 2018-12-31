from Character import Character


class Warrior(Character):

    def __init__(self, name, life, mana):
        super().__init__(name = name, life = life, mana = mana)
        self.weapon = 'Twoją bronią są miecz i tarcza.'

    def __repr__(self):
        return f"Masz na imię {self.name}. Twoja tężyzna fizyczna klasyfikuje Cię jako wojownika. {self.weapon} \nŻycie: {self.life} \nMagia: {self.mana}"

