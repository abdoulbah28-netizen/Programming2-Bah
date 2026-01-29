class Weapon:
    def __init__(self, damage, name, weapon_type, durability):
        self.damage = damage
        self.name = name
        self.weapon_type = weapon_type
        self.durability = durability

    def attack(self):
        if self.durability <= 0:
            print(f"Your {self.name} is broken!")
            return 0

        self.durability -= 1
        return self.damage


class Enemy:
    def __init__(self, name, race, hp, size, damage, description, xp_reward, weapon):
        self.name = name
        self.race = race
        self.hp = hp
        self.size = size
        self.damage = damage
        self.description = description
        self.xp_reward = xp_reward
        self.weapon = weapon
    
    def attack(self, hero, weapon):
        damage = weapon.damage
        if damage == 0:
            return
        hero.take_damage(damage)
    
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0
    
class Hero:
    def __init__(self, name, hp, weapon,):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.xp = 10
        self.xp_to_level = 20
        self.max_hp = hp
        self.level = 1
    def attack(self, enemy, weapon):
        damage = weapon.damage
        if damage == 0:
            return
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0    
    def is_alive(self):
        return self.hp > 0    
        
        enemy.take_damage(damage)
    

        print(f"{self.name} attacks {enemy.name} for {damage} damage.")
        print(f"{enemy.name} has {enemy.hp} HP left")
        if enemy.hp <= 0:
            print(f"{enemy.name} is defeated!")
            self.gain_xp(10)

    def gain_xp(self,amount):
        self.xp += amount
        print(f" you gained {amount} xp ({self.xp}/{self.xp_to_level})")
        if self.xp >= self.xp_to_level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp -= self.xp_to_level
        self.xp_to_level += 2
        
        print( "level up!")
        print(f"Level: {self.level}")
        print(f"Max HP: {self.max_hp}")
        print(f"Weapon Damage: {self.weapon.damage}")



def main():
    katana = Weapon(30, "Katana", "Sword", 5)
    hero = Hero("Hero", 100, katana)
    goblin = Enemy("goblin","mythical", 40, "small", 8, "a greenskin creature with sharp teeth and a rusty dagger",10)
    goblin_weapon = Weapon(10, "dagger","small sword",8)
    
    while goblin.hp > 0: 
        hero.attack(goblin, katana)
    if goblin.hp > 0:
        goblin.attack(hero)
    
    
 


if __name__ == "__main__":
    main()

