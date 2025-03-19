import json
from abc import ABC, abstractmethod

class Item(ABC):
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

    @abstractmethod
    def to_json(self):
        """Returns a JSON dictionary"""
        return {
            "name": self.name,
            "description": self.description,
            "rarity": self.rarity,
            "ownership": self.ownership
        }

    @classmethod
    def from_json(cls, data):
        """Creates a new Item from a JSON dictionary"""
        return cls(data["name"], data["description"], data["rarity"])


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

    def to_json(self):
        return {
            "owner": self.owner,
            "items": [item.to_json() for item in self.items]

        }

    @classmethod
    def from_json(cls, data):
        """Creates a new Inventory from a JSON dictionary"""
        inventory = cls(owner=data["owner"])
        item_map = {"Weapon": Weapon, "Shield": Shield, "Potion": Potion}

        for item_data in data ["items"]:
            item_type = item_data.get("type")
            if item_type not in item_map:
                inventory.add_item(item_map[item_type].from_json(item_data))

        return inventory



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

    def to_json(self):
        data = super().to_json()
        data.update({
            "weapon_type": self.weapon_type,
            "damage": self.damage,
            "active": self.active
        })
        return data

    @classmethod
    def from_json(cls, data):
        """ Creates a weapons instance from a JSON dictionary"""
        return cls(
            name = data["name"],
            description = data.get("description", ""),
            rarity=data["rarity"],
            weapon_type=data["weapon_type"],
            damage=data["damage"]

        )

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

    def to_json(self):
        data = super().to_json()
        data.update({
            "defense": self.defense,
            "active": self.active,
            "broken": self.broken
        })
        return data

    @classmethod
    def from_json(cls,data):
        """Creates a shield instance from a JSON dictionary"""
        return cls(
            name=data["name"],
            description=data.get("description", ""),
            rarity=data["rarity"],
            defense=data["defense"],
            broken=data["broken"]
        )

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

    def to_json(self):
        data = super().to_json()
        data.update({
            "potion_type": self.potion_type,
            "value": self.value,
            "effective_time": self.effective_time,
            "used": self.used
        })
        return data

    @classmethod
    def from_json(cls, data):
        """Creates a potion instance from a JSON dictionary"""
        return cls(
            name=data["name"],
            description=data.get("description", ""),
            rarity=data["rarity"],
            potion_type=data["potion_type"],
            value=data["value"],
            effective_time=data["effective_time"],
        )

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


##convert inventory to JSON
json_string = json.dumps(beleg_backpack.to_json(), indent =4)
print(json_string)

##convert JSON back to Inventory
loaded_inventory = Inventory.from_json(json.loads(json_string))
print(loaded_inventory)