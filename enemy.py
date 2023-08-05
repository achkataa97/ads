class Enemy:
    def __init__(self, name: str, health: int, attack: int, defense: int) -> None:
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def is_alive(self) -> bool:
        return self.health > 0
