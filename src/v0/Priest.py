class PriestSpells(object):
    def __init__(self):
        self.heal_r1 = dict(heal=100, mana=100, cast_time=1.5, heal_coef=.1, mana_coef=1, haste_coef=1)
        self.heal_r2 = dict(heal=275, mana=200, cast_time=1.5, heal_coef=.15, mana_coef=1, haste_coef=1)
        self.heal_r3 = dict(heal=450, mana=290, cast_time=2.0, heal_coef=.25, mana_coef=1, haste_coef=1)

    @staticmethod
    def int_validate(value):
        if not isinstance(value, int):
            return 0
        else:
            return value

    def _get_spells(self):
        return [self.heal_r1, self.heal_r2, self.heal_r3]

    def update_heal(self, int_val):
        for spell in self._get_spells():
            spell['heal'] = spell['heal'] + self.int_validate(int_val) * spell['heal_coef']
        # self.heal_r1['heal'] = self.heal_r1['heal'] + self.int_validate(int_val) * self.heal_r1['heal_coef']
        # self.heal_r2['heal'] = self.heal_r2['heal'] + self.int_validate(int_val) * self.heal_r2['heal_coef']
        # self.heal_r3['heal'] = self.heal_r3['heal'] + self.int_validate(int_val) * self.heal_r3['heal_coef']

    def update_heal_coef(self, int_val):
        for spell in self._get_spells():
            spell['heal_coef'] = spell['heal_coef'] + self.int_validate(int_val)
        # self.heal_r1['heal_coef'] = self.heal_r1['heal_coef'] + self.int_validate(int_val)
        # self.heal_r2['heal_coef'] = self.heal_r2['heal_coef'] + self.int_validate(int_val)
        # self.heal_r3['heal_coef'] = self.heal_r3['heal_coef'] + self.int_validate(int_val)

    def update_mana(self):
        for spell in self._get_spells():
            spell['mana'] = spell['mana'] * spell['mana_coef']
        # self.heal_r1['mana'] = self.heal_r1['mana'] * self.heal_r1['mana_coef']
        # self.heal_r2['mana'] = self.heal_r2['mana'] * self.heal_r2['mana_coef']
        # self.heal_r3['mana'] = self.heal_r3['mana'] * self.heal_r3['mana_coef']

    def update_mana_coef(self, int_val):
        for spell in self._get_spells():
            spell['mana_coef'] = spell['mana_coef'] + self.int_validate(int_val)
        # self.heal_r1['mana_coef'] = self.heal_r1['mana_coef'] + self.int_validate(int_val)
        # self.heal_r2['mana_coef'] = self.heal_r2['mana_coef'] + self.int_validate(int_val)
        # self.heal_r3['mana_coef'] = self.heal_r3['mana_coef'] + self.int_validate(int_val)

    def update_cast_time(self):
        for spell in self._get_spells():
            spell['cast_time'] = spell['cast_time'] * spell['haste_coef']
        # self.heal_r1['cast_time'] = self.heal_r1['cast_time'] * self.heal_r1['haste_coef']
        # self.heal_r2['cast_time'] = self.heal_r2['cast_time'] * self.heal_r2['haste_coef']
        # self.heal_r3['cast_time'] = self.heal_r3['cast_time'] * self.heal_r3['haste_coef']

    def update_haste_coef(self, int_val):
        if self.int_validate(int_val) == 0:
            int_val = 1
        for spell in self._get_spells():
            spell['haste_coef'] = spell['haste_coef'] * self.int_validate(int_val)
        # self.heal_r1['haste_coef'] = self.heal_r1['haste_coef'] * self.int_validate(int_val)
        # self.heal_r2['haste_coef'] = self.heal_r2['haste_coef'] * self.int_validate(int_val)
        # self.heal_r3['haste_coef'] = self.heal_r3['haste_coef'] * self.int_validate(int_val)

    def heal_efficiency(self):
        index = 0
        for spell in self._get_spells():
            index += 1
            print(f"Heal (Rank {index}) - HPS: {spell['heal'] / spell['cast_time']}, HPM:{spell['heal'] / self.heal_r1['mana']}, Cast Time: {spell['cast_time']}")
        # return f"Heal (Rank 1) - HPS: {self.heal_r1['heal']/self.heal_r1['cast_time']}, HPM:{self.heal_r1['heal']/self.heal_r1['mana']}, Cast Time: {self.heal_r1['cast_time']}\n" \
        #        f"Heal (Rank 2) - HPS: {self.heal_r2['heal']/self.heal_r2['cast_time']}, HPM:{self.heal_r2['heal']/self.heal_r2['mana']}, Cast Time: {self.heal_r2['cast_time']}\n" \
        #        f"Heal (Rank 3) - HPS: {self.heal_r3['heal']/self.heal_r3['cast_time']}, HPM:{self.heal_r3['heal']/self.heal_r3['mana']}, Cast Time: {self.heal_r3['cast_time']}"


class Priest(PriestSpells):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.class_label = 'Priest'
        self.intelligence = 0
        self.spirit = 0
        self.haste = 0

    def __repr__(self):
        return {'name': self.name, 'class': self.class_label, 'int': self.intelligence,
                'spirit': self.spirit, 'haste': self.haste}

    def __str__(self):
        return f'name: {self.name}, class: {self.class_label}, int: {self.intelligence},' \
               f' spirit: {self.spirit}, haste: {self.haste}'

    def set_int(self, int_val):
        self.intelligence = self.int_validate(int_val)
        self.update_heal(self.intelligence)

    def update_int(self, int_val):
        self.intelligence += self.int_validate(int_val)
        self.update_heal(self.intelligence)

    def set_spirit(self, int_val):
        self.spirit =self.int_validate(int_val)

    def update_spirit(self, int_val):
        self.spirit += self.int_validate(int_val)

    def set_haste(self, int_val):
        self.haste = self.int_validate(int_val)

    def update_haste(self, int_val):
        self.haste += self.int_validate(int_val)


oracle = Priest('Oracle')

print(oracle.heal_efficiency())

oracle.set_int(100)
oracle.set_spirit(75)

print(oracle.heal_efficiency())