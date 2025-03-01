class Item:
    rarities = {"common": 1.0, "uncommon": 1.0, "epic": 1.0, "legendary": 1.15}

    def __init__(self, name, description, rarity):
        self.name = name
        self.description = description
        self.rarity = rarity
        self.ownership = ""

    def pick_up(self, character_name):
        self.ownership = character_name
        print(f"{self.name} is now owned by {character_name}. ")

    def throw_away(self):
        self.ownership = ""
        print(f"{self.name} is thrown away")

    def use(self):
        if not self.ownership:
            print("can not be used")
        return f"{self.name} is used"



class Weapon(Item):
    def __init__(self, name, description = "", rarity = "common", weapon_type = "", damage = 0):
        super().__init__(name, description, rarity,)
        self.weapon_type= weapon_type
        self.damage = damage
        self.active = False

    def equip(self):
        self.active = True
        print(f"{self.name} is equipped by {self.ownership}")

    def use(self):
        if not self.active:
            print(f"{self.name} is not equipped")
        if not self.ownership:
            print(f"{self.name} is not owned")
        weapon_damage = self.damage * self.rarities[self.rarity]
        print(f"{self.name} is used,dealing {weapon_damage} damage")


class Shield(Item):
    def __init__(self, name, description = "", rarity = "common", defense = 0):
        super().__init__(name, description, rarity)
        self.defense = defense
        self.active = False
        self.broken = False

    def equip(self):
        self.active = True
        print(f"{self.name} is equipped by {self.ownership}")

    def broken_sheild(self):
        self.broken = True
        print(f"{self.name} is broken")

    def use(self):
        if not self.active:
            print(f"{self.name} is not equipped")
        if not self.ownership:
            print(f"{self.name} is not owned")
        if self.broken:
            modifier = 0.5
            total_defense = self.defense*modifier
            print(f"{self.name} is used, blocking {total_defense} damage")
        total_defense = self.defense*self.rarities[self.rarity]
        print(f"{self.name} is used, blocking {total_defense} damage")

class Potion(Item):
    def __init__(self, name, description = "", rarity = "common",potion_type ="", value=0, effective_time = 0):
        super().__init__(name,description,rarity)
        self.potion_type = potion_type
        self.value = value
        self.effective_time = effective_time
        self.used = False

    def use(self):
        if not self.ownership:
            print(f"{self.name} is not owned")
        self.used = True
        print(f'{self.ownership} used {self.name} increasing {self.value}{self.potion_type} boost for {self.effective_time} seconds')


belthronding = Weapon(name = 'Belthronding', rarity = 'legendary', damage = 5000, weapon_type = 'bow')
belthronding.pick_up('Beleg')
belthronding.equip()
belthronding.use()