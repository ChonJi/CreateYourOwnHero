from Character import Character


class Mage(Character):

    def __init__(self, name, life, mana):
        super().__init__(name = name, life = life, mana = mana)
        self.weapon = "Twoja broń to posoch."

    def __repr__(self):
        return f"Masz na imię {self.name}. Gratulacje zostałeś magiem. {self.weapon} \nŻycie: {self.life} \nMagia: {self.mana}"