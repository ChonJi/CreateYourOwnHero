from Character import Character


class Peasant(Character):

    def __init__(self, name, life, mana):
        super().__init__(name = name, life = life, mana = mana)
        self.weapon = 'Twoją bronią są widły.'

    def __repr__(self):
        return f"Masz na imię {self.name}. Pan Bóg w zaciętości swojej przydzielił Ci rolę chłopa. {self.weapon} \nZdrowie: {self.life} \nMagia: {self.mana}"

