import random
import time

# Set variables
level = 0
hp = 0
mp = 0
expcap = 100
exp = 0

monster_names = {
    0: "Colossus",
    1: "Leviathan",
    2: "Behemoth",
    3: "Titan",
    4: "Giant",
    5: "Golem",
    6: "Forgotten",
    7: "Giant Warrior",
    8: "Twilight of the Gods",
    9: "Apocalypse",
    10: "Cyclops",
    11: "Kraken",
    12: "Maelstrom",
    13: "Tyrant",
    14: "Retribution",
    15: "Abyss",
    16: "Moloch",
    17: "Hundred-Handed Giant",
    18: "Petrifying Serpent",
    19: "Chimera",
    20: "Golias",
    21: "Calamity",
    22: "Yggdrasil",
    23: "Tayfn",
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
    34: "West Wind",
    35: "Abyssal Beast",
    36: "Etherian Beast",
    37: "Landslide",
    38: "Cataclysm",
    39: "Sharpfang",
    40: "Tartaros' Mouth",
    41: "Tower of Void",
    42: "Magido",
    43: "Wing of the Storm",
    44: "Messenger of the Stars",
    45: "Blade of the Dark Tide",
    46: "Dragon Tide",
    47: "Giant",
    48: "Claw of Fury",
    49: "Primordial",
    50: "Mirror of Calamity, Illusory Chaotic Countenance and Broken Eye",
    51: "Purgatory of the Void, Roaring Flames of Endless Darkness",
    52: "Abyssal Golem, Iron-Blooded Giant of the Dark Creator and Corrupted Mark",
    53: "Judgment of Despair, Terrifying Judge of the Corrupted Sanctuary and Cursed Sword",
    54: "Chaos Abyss, Eternal Land of Boundless Void and Dark Devouring",
    55: "Winter King of the Dead, Frost Ruler of the Frozen Throne and Cold Domain",
    56: "Forbidden Contract, Betraying Black Book of the False Contractee and Taboo Secrets",
    57: "Fallen Angel, Exiled Wings of the Paradise and Broken Radiance",
    58: "Despair Shattered Image, Fallen Statue of the Forgotten Temple and Void Restraint",
    59: "Eerie Curse, Endless Deception of the Chaotic Phantom and Shadow Induction",
    60: "God of the Abyss, Ruthless Tyrant of the Chaotic Battlefield and Void Wrath",
    61: "Rage of Destruction, Burning Flames of the Heartless Avenger and Desperate Rage",
    62: "Fallen Phantom, Wailing Soul of the Abyssal Source and Cursed Resentment",
    63: "Soul Stealer, Merciless Sickle of the Abyssal Hunter and Blood Curse",
    64: "Demon King, Dark Monarch of the Infernal Abyss and Wicked Dominion",
    65: "Chaos Bringer, Unleashed Chaos of the Chaotic World and Havoc Prophecy",
    66: "Sorcerer of Doom, Cursed Staff of the Malevolent Magus and Ancient Spell",
    67: "Corrupted Guardian, Decaying Armor of the Fallen Knight and Cursed Vow",
    68: "Eternal Nightmare, Haunting Specter of the Fearful Nightmare and Sleepless Dream",
    69: "Shadow Master, Manipulating Threads of the Silent Puppeteer and Forbidden Art",
    70: "Crimson Reaper, Bloodstained Scythe of the Dark Harvester and Death's Embrace",
    71: "Tide of Darkness, Surging Torrent of the Abyssal Ocean and Eternal Twilight",
    72: "Cursed Horror, Malignant Curse of the Enchanted Doll and Broken Smile",
    73: "Sorrowsong, Melancholic Lament of the Lost Muse and Tragic Harmony",
    74: "Silent Assassin, Invisible Dagger of the Shrouded Phantom and Deadly Ambush",
    75: "Shadow Stalker, Elusive Shadow of the Whispering Assassin and Evasive Strike",
    76: "Fury of the Void, Raging Storm of the Chaotic Tempest and Unleashed Wrath",
    77: "Ruler of Chaos, Chaotic Scepter of the Turbulent King and Shattered Order",
    78: "Nightmare Weaver, Twisted Nightmare of the Distorted Dream and Tangled Illusion",
    79: "Soul Devourer, Ravenous Maw of the Hungry Beast and Endless Hunger",
    80: "Death's Embrace, Embracing Shadows of the Morbid Reaper and Eternal Rest",
    81: "Harbinger of Chaos, Omnipotent Herald of the Chaotic Void and Doomsday Prophecy",
    82: "Arcane Conjurer, Enigmatic Tome of the Mysterious Magician and Forbidden Knowledge",
    83: "Necrotic Specter, Ephemeral Shade of the Soulless Wraith and Hollow Echo",
    84: "Puppet Master, Sinister Strings of the Manipulative Marionette and Dark Control",
    85: "Cursed Sorceress, Malevolent Hex of the Vengeful Witch and Bitter Enchantment",
    86: "Vile Necromancer, Putrid Staff of the Blighted Warlock and Necrotic Ritual",
    87: "Voidreaver, Abyssal Scythe of the Eternally Damned and Void Corruption",
    88: "Doomcaller, Eclipsed Horn of the Apocalyptic Herald and Doomsday Chant",
    89: "Shadow Puppeteer, Wicked Strings of the Sinister Marionette and Twisted Manipulation",
    90: "Sinister Jester, Deranged Laughter of the Insane Clown and Madcap Trickery",
    91: "Eternal Tormentor, Merciless Whip of the Enduring Torturer and Eternal Agony",
    92: "Phantom Conjurer, Spectral Illusion of the Haunted Magician and Mysterious Illusion",
    93: "Wailing Banshee, Eerie Cry of the Mourning Ghost and Sorrowful Lament",
    94: "Plaguebringer, Contagious Pestilence of the Pestilent Abomination and Rotting Sickness",
    95: "Shadow Revenant, Lingering Spirit of the Forsaken Apparition and Vengeful Grudge",
    96: "Cursed Cryptkeeper, Malefic Keymaster of the Forbidden Vault and Haunted Relic",
    97: "Chaos Conjurer, Chaotic Tome of the Turbulent Magus and Unpredictable Magic",
    98: "Nightmare Harbinger, Dreadful Omen of the Terrifying Nightmare and Sinister Dreams",
    99: "Soulbound Enigma, Boundless Enigma of the Mysterious Soul and Forgotten Memories",
    100: "Abyssal Warlord, Demonic Commander of the Endless Abyss and Infernal Domination",
    101: "Dreadlord, Harbinger of Terror and Desolation",
    102: "Elder Dragon, Ancient Scale of the Mythical Beast and Celestial Roar"
}

badge_dict = {
    0: "《Badge of Incompetence》",
    1: "《Bronze of Perseverance》",
    2: "《Silver of Firm Belief》",
    3: "《Gold of Courage》",
    4: "《Platinum of Excellence》",
    5: "《Diamond of Stellar Excellence》",
    6: "《Master of Limitlessness》",
    7: "《Grandmaster of Radiance》",
    8: "《Apex of Ultimate Champions》",
    9: "《Elite》",
    10: "《Path of Legends》",
    11: "《Legendary》",
    12: "《Rock of Stability》",
    13: "《Invincible》",
    14: "《Unrivaled》",
    15: "《Pinnacle of Achievement》",
    16: "《Unmatched》",
    17: "《Infinite Charm》",
    18: "《Transcendent》",
    19: "《Mythical》",
    20: "《Grandmaster of Grandmasters》",
    21: "《Eternal Glory》",
    22: "《Destined Sage》",
    23: "《Transcendent Being》",
    24: "《Supreme and Unsurpassed》",
    25: "《Eternal King》",
    26: "《Ruler of the Divine Realm》",
    27: "《Immortal Supreme》",
    28: "《Lord of the Universe》",
    29: "《King of Legends》",
    30: "《Legend of Gods》",
    31: "《Representative of Gods》",
    32: "《Invincible in the Universe》",
    33: "《Eternal King of All Ages》",
    34: "《Lord of the Universe》",
    35: "《Ruler of the Stars》",
    36: "《Supreme and Immortal》",
    37: "《Creator of Worlds》",
    38: "《Creator of the Universe》",
    39: "《Endless Dominion》",
    40: "《Master of All Things》",
    41: "《King of the Universe》",
    42: "《Eternal Ruler of the Universe》",
    43: "《Supreme Being of the Universe》",
    44: "《Infinite Supreme》",
    45: "《Invincible in Heaven and Earth》",
    46: "《True God of the Universe》",
    47: "《Supreme Authority of the Universe》",
    48: "《Heart of the Universe》",
    49: "《Soulless in the Universe》",
    50: "《Master of the Universe》",
    51: "《Endless in the Universe》",
    52: "《Circle of the Universe》",
    53: "《Originator of the Universe》",
    54: "《Creator God of the Universe》",
    55: "《Terminator of the Universe》",
    56: "《Existence of the Universe》",
    57: "《Invincible in the Universe》",
    58: "《Wings of the Universe》",
    59: "《Messenger of the Universe》",
    60: "《Incarnation of the Universe》",
    61: "《Miracle of the Universe》",
    62: "《Surprise of the Universe》",
    63: "《Light of the Universe》",
    64: "《Overlord of the Universe》",
    65: "《Supreme Master of the Universe》",
    66: "《Truth of the Universe》",
    67: "《Will of the Universe》",
    68: "《King of the Universe》",
    69: "《Soul of the Universe》",
    70: "《Majesty of the Universe》",
    71: "《Order of the Universe》",
    72: "《Reality of the Universe》",
    73: "《Domain of the Universe》",
    74: "《Sage of the Universe》",
    75: "《Dancer of the Universe》",
    76: "《Traveler of the Universe》",
    77: "《Treasure of the Universe》",
    78: "《Power of the Universe》",
    79: "《Governor of the Universe》",
    80: "《Miracle of the Universe》",
    81: "《Wonder of the Universe》",
    82: "《Shocking of the Universe》",
    83: "《Legendary of the Universe》",
    84: "《Worship of the Universe》",
    85: "《Miracle of the Universe》",
    86: "《Seal of the Universe》",
    87: "《Transformation of the Universe》",
    88: "《Endless of the Universe》",
    89: "《Void of the Universe》",
    90: "《King of the Universe》",
    91: "《Flame of the Universe》",
    92: "《Shadow of the Universe》",
    93: "《Iron and Blood of the Universe》",
    94: "《Abyss of the Universe》",
    95: "《Destruction of the Universe》",
    96: "《Darkness of the Universe》",
    97: "《End of the Universe》",
    98: "《Silence of the Universe》",
    99: "《Annihilation of the Universe》",
    100: "《Root of the Universe》",
    101: "《Eternity of the Universe》",
    102: "《Ruler of the Universe》"
}

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
        print("The stone crackles... and a strange robotic voice bursts from nowhere: Congratulations on leveling up!")
        time.sleep(1)
        print(f"Your current level is {self.level}. You have {self.hp} health points and {self.mp} mana points!")
        time.sleep(1)
        print("You feel a bit stronger than before...")
        time.sleep(1)
        print("Promotion!")
        time.sleep(1)
        print(f"You notice that the {badge_dict.get(self.level-1)} badge on your body slowly fades away.")
        time.sleep(3)
        print("The stone tablet emits a noise.")
        time.sleep(3)
        print("Crackle...")
        time.sleep(2)
        print("Crack...")
        time.sleep(1)
        print(f"Congratulations, {self.name}, you have been promoted to {badge_dict.get(self.level, 'GodLike - Highest Rank in Current Patch')}!")
        time.sleep(1)

class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


def main_test():
    run = True
    while run:
        try:
            menu = int(input("1: Check player status\n2: Battle monster\n3: Unleash hands-free ultimate infinite AFK grinding> "))
        except ValueError:
            print("Please enter an integer.")
            continue
        if menu == 1:
            print(f"{'Menu'.center(20, '-')} \nName: {p1.name}\nLevel: {p1.level}\nRank: {badge_dict.get(p1.level, 'GodLike - Highest Rank in Current Patch')}\nHealth: {p1.hp}\nMagic: {p1.mp}\nExperience: {p1.exp}/{p1.expcap}")
        elif menu == 2:
            m1 = Monster(monster_names.get(random.randint(0, p1.level)), (p1.hp) + 10)
            print("You begin searching for a monster...")
            s = random.randint(1, 2)
            time.sleep(s)
            print(f"Monster found!! You discover {m1.name} Lv {p1.level}!")
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
                afk = int(input("Please enter the number of rounds for infinite AFK grinding (1-inifinity)"))
            except ValueError:
                print("Please enter an integer.")
            for i in range(afk):
                try:
                    print("\nAFK grinding in progress...\nCtrl+C to pause afk grinding... \n")
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
                except KeyboardInterrupt:
                    print("pausing AFK grinding...")
                    break
                    

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
