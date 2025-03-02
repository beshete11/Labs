class Item:
    rarities = {"common": 1.0, "uncommon": 1.0, "epic": 1.0, "legendary": 1.15}

    def __init__(self, name, description, rarity):
        self.name = name
        self.description = description
        self.rarity = rarity
        self.ownership = None

    def __str__(self):
        if self.rarity == "legendary":
            return f"""
            🌟🌟🌟 LEGENDARY ITEM 🌟🌟🌟
            """


    def pick_up(self, character_name):
        self.ownership = character_name
        print(f"{self.name} is now owned by {character_name}. ")

    def throw_away(self):
        self.ownership = None
        print(f"{self.name} is thrown away")

    def use(self):
        if not self.ownership:
            print("can not be used")
            return
        return f"{self.name} is used"


class Inventory:
    def __init__(self, owner):
        self.owner = owner
        self.items = []
        self._index = 0

    def add_item(self, item):
        if item in self.items:
            print("This item is already in the inventory.")
            return
        item.ownership = self.owner
        self.items.append(item)

    def remove_item(self, item):
        if item not in self.items:
            print("This item is not in the inventory.")
            return
        self.items.remove(item)
        item.ownership = None


    def view(self, type = None):
        if type:
            type_map = {"weapon": Weapon, "shield": Shield, "potion": Potion}
            type_class = type_map.get(type.lower())

            if not type_class:
                return "INVALID TYPE"

            filtered_items = [item for item in self.items if isinstance(item, type_class)]
        else:
            filtered_items = [item for item in self.items]

        return filtered_items if filtered_items else ["No Items"]

    def __str__(self):
        return (f"{self.owner} Inventory:\n" + "\n".join(self.view()))

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index >= len(self.items):
            raise StopIteration
        item = self.items[self._index]
        self._index += 1
        return item

    def __contains__(self,item):
        return item in self.items



class Weapon(Item):
    def __init__(self, name, description = "", rarity = "common", weapon_type = "Single-handed", damage = 0):
        super().__init__(name, description, rarity,)
        self.weapon_type= weapon_type
        self.damage = damage
        self.active = False

    def equip(self):
        self.active = True
        print(f"{self.name} is equipped by {self.ownership}")

    def attack_move(self):
        if self.weapon_type == "Single-handed":
            return self._slash()
        elif self.weapon_type == "Double-handed":
            return self._spin()
        elif self.weapon_type == "Pike":
            return self._thrust()
        elif self.weapon_type == "Ranged":
            return self._shoot()

    def _slash(self):
        return " slash"

    def _thrust(self):
        return " thrust"

    def _spin(self):
        return " spin"

    def _shoot(self):
        return " shoots"

    def use(self):
        if not self.active:
            print(f"{self.name} is not equipped")
            return
        if not self.ownership:
            print(f"{self.name} is not owned")
            return
        attack_type = self.attack_move()
        weapon_damage = self.damage * Item.rarities[self.rarity]
        print(f"{self.ownership}{attack_type} using {self.name},dealing {weapon_damage} damage")


class Shield(Item):
    def __init__(self, name, description = "", rarity = "common", defense = 0, broken = False):
        super().__init__(name, description, rarity)
        self.defense = defense
        self.active = False
        self.broken = False

    def equip(self):
        self.active = True
        print(f"{self.name} is equipped by {self.ownership}")

    def break_shield(self):
        self.broken = True
        print(f"{self.name} is broken")

    def use(self):
        if not self.active:
            print(f"{self.name} is not equipped")
            return
        if not self.ownership:
            print(f"{self.name} is not owned")
            return
        if self.broken:
            modifier = 0.5
            total_defense = self.defense*modifier
            print(f"{self.name} is used, blocking {total_defense} damage")
        else:
            total_defense = self.defense*Item.rarities[self.rarity]
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
            return
        self.used = True
        print(f'{self.ownership} used {self.name} increasing {self.value}{self.potion_type} boost for {self.effective_time} seconds')


beleg_backpack = Inventory(owner = "Beleg")
###item information for testing
master_sword = Weapon(name= "Master Sword", rarity = 'legendary', weapon_type = "Single-handed", damage = 300)
belthronding = Weapon(name="Belthronding", rarity = 'legendary', weapon_type = "Ranged", damage = 500)
muramasa = Weapon(name= "Muramasa", rarity = 'legendary', weapon_type = "Double-handed", damage = 580)
gungnir = Weapon(name = "Gungnir", rarity = 'legendary', weapon_type = "Pike", damage = 290)

broken_pot_lid = Shield(name='wooden lid', description='A lid made of wood, useful in cooking. No one will choose it willingly for a shield', defense = 5, broken = True)

###add items to inventory
beleg_backpack.add_item(belthronding)
beleg_backpack.add_item(master_sword)
beleg_backpack.add_item(broken_pot_lid)
beleg_backpack.add_item(muramasa)
beleg_backpack.add_item(gungnir)


print(master_sword)
master_sword.use()
master_sword.equip()
master_sword.use()
