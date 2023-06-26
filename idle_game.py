import random
import time

# Set variables
level = 0
hp = 0
mp = 0
expcap = 100
exp = 0

class Player:
    def __init__(self, name, hp, mp, level, expcap, exp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.level = level
        self.expcap = expcap
        self.exp = exp

    def levelup(self):
        self.level += 1
        self.hp += 100
        self.mp += 100
        self.expcap += 100 + expcap * 0.5
        self.exp = 0
        print("The stone emits a burst of noise—Congratulations on leveling up!")
        time.sleep(1)
        print(f"Your current level is {self.level}. You have {self.hp} health points and {self.mp} mana points!")
        time.sleep(1)
        print("You feel like your body has become stronger.")

class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

monster_names = {
    0: "Giant",
    1: "Leviathan",
    2: "Behemoth",
    3: "Titan",
    4: "Golem",
    5: "Stone",
    6: "Forgotten",
    7: "Giant Warrior",
    8: "Twilight of the Gods",
    9: "Apocalypse",
    10: "Cyclops",
    11: "Kraken",
    12: "Whirlpool",
    13: "Tyrant",
    14: "Retribution",
    15: "Abyss",
    16: "Moloch",
    17: "Hundred-Handed Giant",
    18: "Petrified Snake",
    19: "Chimera",
    20: "Goliath",
    21: "Catastrophe",
    22: "Yggdrasil",
    23: "Tiphon",
    24: "Bloodbane",
    25: "The Almighty",
    26: "Lord of the Abyss",
    27: "Harbinger of Doom",
    28: "Bulwark",
    29: "Claw of Terror",
    30: "Eclipse",
    31: "Ravager",
    32: "Sphinx",
    33: "Avalanche",
    34: "Zephyr",
    35: "Abyssal Beast",
    36: "Etherial Beast",
    37: "Rockslide",
    38: "Disaster",
    39: "Sharpfang",
    40: "Maw of Tartaros",
    41: "Void Tower",
    42: "Magido",
    43: "Wingstorm",
    44: "Messenger of the Stars",
    45: "Blade of the Black Tide",
    46: "Dragon Tide",
    47: "Behemoth",
    48: "Claw of Wrath",
    49: "Primordial"
}

def main_test():
    run = True
    while run:
        try:
            menu = int(input("1: Check player status\n2: Battle monster\n3: Unleash hands-free ultimate infinite AFK grinding> "))
        except ValueError:
            print("Please enter an integer.")
            continue
        if menu == 1:
            print(f"Menu".center(20, '-') + f"\nName: {p1.name} \nLevel: {p1.level} \nHealth Points: {p1.hp} \nMana Points: {p1.mp} \nExperience: {p1.exp}/{p1.expcap}")
        elif menu == 2:
            m1 = Monster(monster_names.get(random.randint(0, p1.level)), (p1.hp) + 10)
            print("Searching for a monster...")
            s = random.randint(1, 2)
            time.sleep(s)
            print(f"Monster found — {m1.name} Lv {p1.level}!")
            time.sleep(2)
            fighting = True
            while fighting:
                x = random.randint(p1.level, p1.level + p1.hp * 0.5 + 10)
                print(f"You dealt {x} damage to {m1.name}!")
                m1.hp = m1.hp - x if m1.hp - x > 0 else 0
                time.sleep(1)
                print(f"{m1.name} now has {m1.hp} health points remaining.")
                time.sleep(random.randint(1, 2))
                if m1.hp <= 0:
                    p1.exp += p1.hp * 0.5 + random.randint(50, 100)
                    if p1.exp >= p1.expcap:
                        p1.levelup()
                else:
                    continue
                fighting = False
        elif menu == 3:
            afk = 0
            try:
                afk = int(input("Please enter the number of rounds for infinite AFK grinding (1-300)"))
            except ValueError:
                print("Please enter an integer.")
            if afk > 300:
                afk = 300
            for i in range(afk):
                time.sleep(1)
                print(f"Round {i}/{afk} of AFK grinding", "(" + str(round(i/afk*100)) + "%)")
                m1 = Monster(monster_names.get(random.randint(0, p1.level) % 49), (p1.hp) + 10)
                print("Searching for a monster...")
                s = random.randint(1, 2)
                time.sleep(s)
                print(f"Monster found — {m1.name} Lv {p1.level}!")
                time.sleep(2)
                fighting = True
                while fighting:
                    x = random.randint(p1.level, p1.level + p1.hp * 0.5 + 10)
                    print(f"You dealt {x} damage to {m1.name}!")
                    m1.hp = m1.hp - x if m1.hp - x > 0 else 0
                    time.sleep(1)
                    print(f"{m1.name} now has {m1.hp} health points remaining.")
                    time.sleep(random.randint(1, 2))
                    if m1.hp <= 0:
                        p1.exp += p1.hp * 0.5 + random.randint(50, 100)
                        if p1.exp >= p1.expcap:
                            p1.levelup()
                    else:
                        continue
                    fighting = False

        else:
            print("Invalid selection. Please try again.")

pp = input("What is your name?\n > ")
time.sleep(2)
print("You hear a noise nearby... it seems like someone is nearby...")
time.sleep(2)
print("Suddenly, the corridor becomes brighter.")
time.sleep(2)
print("A shadow swiftly passes by and disappears before you can get a clear look.")
time.sleep(2)
print(f"Mysterious voice: \"Welcome, {pp}! My friend!\"")
time.sleep(2)
print(f"Mysterious voice: \"It's time for an adventure!!\"")
time.sleep(2)
print("You feel confused and rub your eyes.")
time.sleep(1)
print("Suddenly, a stone tablet rises in front of you... with something written on it...")
time.sleep(2)
p1 = Player(pp, hp, mp, level, expcap, exp)

if __name__ == "__main__":
    main_test()
