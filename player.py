class Player:
    def __init__(self, name: str, character_class: str) -> None:
        self.name = name
        self.character_class = character_class
        self.level = 1
        self.health = 100
        self.attack = 10 if character_class == "Warrior" else 5
        self.defense = 10 if character_class == "Warrior" else 5
        self.magic = 0 if character_class == "Warrior" else 10
        self.experience = 0
        self.inventory = []

    def add_item_to_inventory(self, item: str) -> None:
        self.inventory.append(item)

    def use_item(self, item: str) -> None:
        item in self.inventory:
            if item == "Health Potion":
                self.health += 20
                self.inventory.remove(item)
                print(f"You used {item}. Your health is now {self.health}.")
            else:
                print(f"The item {item} has no effect.")
        else:
            print(f"You don't have a {item} in your inventory.")

    def gain_experience(self, amount: int) -> None:
        self.experience += amount
        if self.experience >= self.level * 10:
            self.level_up()

    def level_up(self) -> None:
        self.level += 1
        self.health += 10
        self.attack += 5
        self.defense += 5
        if self.character_class != "Warrior":
            self.magic += 5
        print(f"Congratulations! You've leveled up to level {self.level}!")
