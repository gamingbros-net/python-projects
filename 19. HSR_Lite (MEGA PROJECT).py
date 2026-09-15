import random
import time
class Character:
    def __init__(self, name, hp, max_hp, attack_power):
        self.name = name
        self._hp = hp
        self.max_hp = max_hp
        self.ap = attack_power
        self.is_alive = True

    @property
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, value):
        if value < 0:
            self._hp = 0
            self.is_alive = False
        elif value > self.max_hp:
            print("Your Character is fully Healed")
            self._hp = self.max_hp
        else:
            self._hp = value

class DPS(Character):

    def __init__(self, name, hp, max_hp, attack_power, crit_chance, crit_damage):
        super().__init__(name, hp, max_hp, attack_power)
        self.crit_chance = crit_chance
        self.crit_damage = crit_damage

    def __str__(self):
        return f"{self.name} | HP: {self.hp}/{self.max_hp} | ATK: {self.ap} | Crit_rate = {self.crit_chance} | Crit_damage =  {self.crit_damage}"
    
    def crit(self):
        if random.random() < self.crit_chance:
            self.crit_attack = self.ap * self.crit_damage
            return self.crit_attack
        else:
            return self.ap
    
    def attack(self, target):
        damage = self.crit()
        if damage > self.ap:
            print(f"CRIT! {self.name} attacks {target.name} for {damage} damage!")
        else:
            print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.hp -= damage

class Support(Character):
    def __init__(self, name, hp, max_hp, attack_power, heal_power):
        super().__init__(name, hp, max_hp, attack_power)
        self.heal_power = heal_power

    def __str__(self):
        return f"{self.name} | HP: {self.hp}/{self.max_hp} | ATK: {self.ap} | Heal_power = {self.heal_power}"
    
    def heal(self, ally):
        if ally.hp == ally.max_hp:
            print("This unit is already at max HP!")
            return None
        elif ally.is_alive == False:
            print("This unit is already dead!")
        else:
            ally.hp += self.heal_power
            print(f"{self.name} heals {ally.name} for {self.heal_power} HP!")
    
    def attack(self, target):
        print(f"{self.name} attacks {target.name} for {self.ap} damage!")
        target.hp -= self.ap

Herta = DPS("Herta", 100, 100, 25, 0.6, 1.9)
Firefly = DPS("Firefly", 130, 130, 40, 0.2, 2.5)
Phainon = DPS("Phainon", 230, 230, 55, 0.7, 1.6)
Hyacine = Support("Hyacine", 120, 120, 10, 40)
Huohuo = Support("Huohuo", 110, 110, 5, 30)

round_num = 0
team = [Herta, Firefly, Hyacine]
enemy = [Phainon, Huohuo]

print("Your Team")
for character in team:
    print(character)
print()
print("Enemy Team")
for character in enemy:
    print(character)
print()

while True:
    alive_team = [c for c in team if c.hp > 0]
    alive_enemy  = [c for c in enemy if c.hp > 0]
    action_done_team = []
    action_done_enemy = []
    round_num += 1
    print()
    print()
    print("######################################################################")
    print(f"round {round_num}")
    print()
    print("Your Turn")
    print("----------------------------------------------------------------------")
    while True:
        available = [c for c in team if c.hp > 0 and c not in action_done_team]
        if not available:
            break
        alive_enemy = [c for c in enemy if c.hp > 0]
        if not alive_enemy:
            break
        team_char = random.choice(available)
        target = random.choice(alive_enemy)
        if isinstance(team_char, Support):
            injured = [c for c in team if c.hp > 0 and c.hp < c.max_hp * 0.7]
            if injured:
                weakest = min(injured, key=lambda c: c.hp)
                team_char.heal(weakest)
                action_done_team.append(team_char)
                print(weakest)
                print("----------------------------------------------------------------------")
            else:
                team_char.attack(target)
                action_done_team.append(team_char)
                print(target)
                print("----------------------------------------------------------------------")
        else:
            target = random.choice(alive_enemy)
            team_char.attack(target)   
            action_done_team.append(team_char)
            print(target)
            print("----------------------------------------------------------------------")
    print()
    print("Enemy Turn")
    print("----------------------------------------------------------------------")
    while True:
        available = [c for c in enemy if c.hp > 0 and c not in action_done_enemy]
        if not available:
            break
        alive_team = [c for c in team if c.hp > 0]
        if not alive_team:
            break
        enemy_char = random.choice(available)
        if isinstance(enemy_char, Support):
            injured = [c for c in enemy if c.hp > 0 and c.hp < c.max_hp * 0.7]
            if injured:
                weakest = min(injured, key=lambda c: c.hp)
                enemy_char.heal(weakest)
                action_done_enemy.append(enemy_char)
                print(weakest)
                print("----------------------------------------------------------------------")
            else:
                target = random.choice(alive_team)
                enemy_char.attack(target)
                action_done_enemy.append(enemy_char)
                print(target)
                print("----------------------------------------------------------------------")
        else:
            target = random.choice(alive_team)
            enemy_char.attack(target)   
            action_done_enemy.append(enemy_char)
            print(target)
            print("----------------------------------------------------------------------")
    print()
    print("----------------------------------------------------------------------")
    print("Your Team")
    for character in team:
        print(character)
    print()
    print("Enemy Team")
    for character in enemy:
        print(character)
    print("----------------------------------------------------------------------")
    alive_team = [c for c in team if c.hp > 0]
    alive_enemy  = [c for c in enemy if c.hp > 0]
    if alive_team == []:
        print("Your Team Loses!")
        break
    elif alive_enemy == []:
        print("Your Team Won!")
        break