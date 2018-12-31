from Character import Character


class BattleMage(Character):

    def __init__(self, name, life, mana):
        super().__init__(name = name, life = life, mana = mana)
        self.weapon = "W lewej ręce dzierżysz posoch a w prawej topór."

    def __repr__(self):
        return f"Masz na imię {self.name}. Jesteś magiem bitewnym. {self.weapon} \nŻycie: {self.life} \nMagia: {self.mana}"