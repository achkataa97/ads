class Location:
    def __init__(self, name: str, description: str, enemy: Enemy = None) -> None:
        self.name = name
        self.description = description
        self.enemy = enemy
