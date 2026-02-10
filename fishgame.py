# Fishing Game - Hub Island Edition
import os
import json
import hashlib
import platform
import time
import random
import sys
import subprocess
from colorama import Fore, Style, init
from datetime import datetime

#SIMGA!
RAINBOW = [
    Fore.RED,
    Fore.LIGHTRED_EX,
    Fore.YELLOW,
    Fore.GREEN,
    Fore.CYAN,
    Fore.LIGHTBLUE_EX,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.LIGHTMAGENTA_EX
]

def gradient_char(c, t):
    """Smooth diagonal color shift."""
    return RAINBOW[t % len(RAINBOW)] + c + Style.RESET_ALL

def print_frame(lines, t):
    """Overwrite the previous frame WITHOUT clearing the screen."""
    # Move cursor to top (no flashing)
    sys.stdout.write("\x1b[H")
    for y, line in enumerate(lines):
        colored = ""
        for x, ch in enumerate(line):
            index = x + y + t  # diagonal movement
            colored += gradient_char(ch, index)
        sys.stdout.write(colored + "\n")
    sys.stdout.flush()

def show_intro():
    intro = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║  ██╗   ██╗███████╗██████╗ ██╗   ██╗                          ║
    ║  ██║   ██║██╔════╝██╔══██╗╚██╗ ██╔╝                          ║
    ║  ██║   ██║█████╗  ██████╔╝ ╚████╔╝                           ║
    ║  ╚██╗ ██╔╝██╔══╝  ██╔══██╗  ╚██╔╝                            ║
    ║   ╚████╔╝ ███████╗██║  ██║   ██║                             ║
    ║    ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝                             ║
    ║                                                              ║
    ║   ██████╗ ██████╗  ██████╗ ██╗                               ║
    ║  ██╔════╝██╔═══██╗██╔═══██╗██║                               ║
    ║  ██║     ██║   ██║██║   ██║██║                               ║
    ║  ██║     ██║   ██║██║   ██║██║                               ║
    ║  ╚██████╗╚██████╔╝╚██████╔╝███████╗                          ║
    ║   ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝                          ║
    ║                                                              ║
    ║   ██████╗  █████╗ ███╗   ███╗██╗███╗   ██╗ ██████╗  ©        ║
    ║  ██╔════╝ ██╔══██╗████╗ ████║██║████╗  ██║██╔════╝           ║
    ║  ██║  ███╗███████║██╔████╔██║██║██╔██╗ ██║██║  ███╗          ║
    ║  ██║   ██║██╔══██║██║╚██╔╝██║██║██║╚██╗██║██║   ██║          ║
    ║  ╚██████╔╝██║  ██║██║ ╚═╝ ██║██║██║ ╚████║╚██████╔╝          ║
    ║   ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝           ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """

    lines = intro.split("\n")

    # Reserve screen space (avoid scrolling)
    print("\n" * (len(lines) + 2))

    # Animation frames
    for t in range(150):
        print_frame(lines, t)
        time.sleep(0.02)

    # pause
    time.sleep(1)

    # clear
    sys.stdout.write("\x1b[2J\x1b[H")
    sys.stdout.flush()
    
init(autoreset=True)

DID_YOU_KNOW_FACTS = [
    "Real blobfish don't look blobby underwater – they only deform at low pressure!",
    "Sturgeon are older than dinosaurs and can live for over 100 years.",
    "The Kraken myth likely began after sailors spotted giant squid.",
    "Pike are known as 'water wolves' because of their sudden ambush attacks.",
    "Barreleye fish have transparent heads so their eyes can look straight upward.",
    "Anglerfish males fuse into the female's body permanently in real life.",
    "Blue whales are the largest animals to ever exist – larger than any dinosaur.",
    "The Arapaima can breathe air using a modified swim bladder.",
    "Greenland sharks can live up to 500 years – the longest-lived vertebrate.",
    "Oarfish sightings historically caused sea serpent legends.",
    "Some deep-sea creatures produce red bioluminescence – invisible to most predators!",
    "Salmon can smell their home stream from miles away in the ocean.",
    "Electric eels can generate up to 860 volts – enough to stun a horse!",
    "Manta rays have the largest brain-to-body ratio of all fish species.",
    "Some fish can recognize human faces and remember them for months.",
    "The fastest fish is the black marlin, which can swim over 80 mph.",
    "Catfish have over 100,000 taste buds all over their body!",
    "Flying fish can glide through the air for over 650 feet.",
    "Lungfish can survive out of water for up to 4 years by burrowing in mud.",
    "Parrotfish create 85% of the sand on tropical beaches by eating coral.",
    "The oldest known fish lived 200 million years before dinosaurs appeared.",
    "Coelacanths were thought extinct for 66 million years until found in 1938.",
    "Some sharks must keep swimming or they'll sink – they have no swim bladder.",    
    "Fishing during storms increases your chances of catching rare fish!",
    "Dawn and dusk are the best times to encounter mythical creatures.",
    "Magical mutations are the rarest – only 0.01% of fish have them!",
    "Upgrading your patience stat makes minigames significantly easier.",
    "The Blobfish is so rare that most players never catch one!",
    "You can earn skill points by leveling up and completing certain achievements.",
    "Higher difficulty settings give you more XP per catch – risk equals reward!",
    "Some fish are only available in specific locations – explore them all!",
    "Trophy fish can be preserved in your trophy room before selling.",
    "The Deep Sea location has the highest concentration of legendary fish.",
    "Night fishing can trigger special mutations and rare spawns.",
    "Your rod durability decreases with each catch – remember to repair it!",
    "Golden mutations can sell for 5x the normal price!",
    "Completing the encyclopedia gives massive rewards and skill points.",
    "The Space location has fish that defy the laws of physics!",
    "Weather changes randomly, so adapt your strategy accordingly.",
    "Jormungandr is the serpent that encircles the entire world in Norse mythology.",
    "Kappa from Japanese folklore can be defeated by bowing politely.",
    "In Celtic mythology, salmon were considered the wisest of all creatures.",
    "The Leviathan appears in multiple ancient cultures as a chaos monster.",
    "Japanese legend says koi that swim up waterfalls become dragons.",
    "Ancient Polynesians navigated oceans by watching fish behavior.",
    "Vikings believed certain fish could predict storms and weather changes.",
    "Also try Minecraft!",
    "Visit the Hub Island shop to upgrade your gear!",
    "The Aquarium displays all your trophy catches!",
    "Complete quests for rare rewards and unlock new locations!",
    "The dock connects you to distant fishing grounds!",
]

def get_random_fact():
    return random.choice(DID_YOU_KNOW_FACTS)




# ===== MODELS =====
class Fish:
    def __init__(self, name, min_weight, max_weight, rarity, rarity_weight, xp_reward, real_world_info="", sell_price=10):
        self.name = name
        self.min_weight = min_weight
        self.max_weight = max_weight
        self.rarity = rarity
        self.rarity_weight = rarity_weight
        self.xp_reward = xp_reward
        self.real_world_info = real_world_info
        self.sell_price = sell_price
        self.weight = self.generate_random_weight()
        self.mutation = "normal"
        self.catch_time = None
        self.debug_mode = getattr(self, "debug_mode", False)
        self.rod_durability = 100  # 0-100
        self.rod_max_durability = 100

    def to_dict(self):
        return {
            'name': self.name,
            'min_weight': self.min_weight,
            'max_weight': self.max_weight,
            'rarity': self.rarity,
            'rarity_weight': self.rarity_weight,
            'xp_reward': self.xp_reward,
            'real_world_info': self.real_world_info,
            'sell_price': self.sell_price,
            'weight': self.weight,
            'mutation': self.mutation,
            'catch_time': self.catch_time
        }


    def generate_random_weight(self):
        return round(random.uniform(self.min_weight, self.max_weight), 2)

    def apply_mutation(self):
        """Rolls for random mutations"""
        roll = random.random()
        
        if roll < 0.0001:  # 0.01% chance for magical
            self.mutation = "magical"
            self.sell_price = int(self.sell_price * 10)
            self.xp_reward = int(self.xp_reward * 5)
        elif roll < 0.001:  # 0.1% chance for shiny
            self.mutation = "shiny"
            self.sell_price = int(self.sell_price * 3)
            self.xp_reward = int(self.xp_reward * 2)
        elif roll < 0.01:  # 1% chance for golden
            self.mutation = "golden"
            self.sell_price = int(self.sell_price * 5)
            self.xp_reward = int(self.xp_reward * 3)
        elif roll < 0.05:  # 5% chance for albino
            self.mutation = "albino"
            self.sell_price = int(self.sell_price * 2)
            self.xp_reward = int(self.xp_reward * 1.5)

    def get_color(self):
        """Returns colorama color based on rarity and mutation"""
        mutation_colors = {
            "magical": Fore.LIGHTMAGENTA_EX,
            "shiny": Fore.LIGHTCYAN_EX,
            "golden": Fore.LIGHTYELLOW_EX,
            "albino": Fore.WHITE
        }
        
        if self.mutation != "normal":
            return mutation_colors.get(self.mutation, Fore.WHITE)
        
        rarity_colors = {
            "Common": Fore.WHITE,
            "Uncommon": Fore.GREEN,
            "Rare": Fore.BLUE,
            "Epic": Fore.MAGENTA,
            "Legendary": Fore.YELLOW,
            "Mythical": Fore.RED
        }
        return rarity_colors.get(self.rarity, Fore.WHITE)

    def __str__(self):
        color = self.get_color()
        mutation_prefix = f"[{self.mutation.upper()}] " if self.mutation != "normal" else ""
        return f"{color}{mutation_prefix}{self.name}{Style.RESET_ALL} ({self.weight} kg)"


class Rod:
    def __init__(self, name, bonus_chance, bonus_weight, price, unlock_level=1, durability_bonus=0):
        self.name = name
        self.bonus_chance = bonus_chance  # Better fish chance
        self.bonus_weight = bonus_weight  # Heavier catches
        self.price = price
        self.unlock_level = unlock_level
        self.durability_bonus = durability_bonus


class Bait:
    def __init__(self, name, bonus_xp, bonus_rarity, price, unlock_level=1):
        self.name = name
        self.bonus_xp = bonus_xp
        self.bonus_rarity = bonus_rarity
        self.price = price
        self.unlock_level = unlock_level


class Location:
    def __init__(self, name, fish_pool, weather_effects, unlock_level=1, description=""):
        self.name = name
        self.fish_pool = fish_pool
        self.weather_effects = weather_effects
        self.unlock_level = unlock_level
        self.description = description


lake_fish = [
    Fish("Trout", 0.5, 2.5, "Common", 10, 15, "Trout are freshwater fish commonly found in rivers and lakes.", 20),
    Fish("Bass", 4.5, 10.0, "Uncommon", 5, 25, "Bass are popular game fish found in many lakes and rivers.", 50),
    Fish("Pike", 5.0, 15.0, "Rare", 2, 50, "Pike are carnivorous fish found in lakes and rivers.", 100),
    Fish("Perch", 0.3, 1.5, "Common", 12, 10, "Perch are small freshwater fish with distinctive stripes.", 15),
    Fish("Walleye", 3.0, 8.0, "Uncommon", 6, 30, "Walleye are prized for their excellent taste.", 60),
    Fish("Bluegill", 0.2, 1.0, "Common", 15, 8, "Small panfish popular with beginners.", 12),
    Fish("Crappie", 0.5, 2.0, "Common", 11, 12, "Black and white crappie are both delicious.", 18),
    Fish("Sunfish", 0.1, 0.8, "Common", 14, 7, "Colorful small fish found near shores.", 10),
    Fish("Pickerel", 2.0, 4.0, "Uncommon", 7, 22, "Smaller cousin of the pike with sharp teeth.", 45),
    Fish("White Bass", 1.0, 3.0, "Common", 9, 18, "Schooling fish that put up a good fight.", 25),
    Fish("Channel Catfish", 2.0, 20.0, "Uncommon", 6, 28, "Bottom feeders with whisker-like barbels.", 55),
    Fish("Bowfin", 3.0, 9.0, "Uncommon", 5, 32, "Ancient fish with a long dorsal fin.", 65),
    Fish("Gar", 4.0, 12.0, "Rare", 3, 45, "Prehistoric-looking fish with long snout.", 90),
    Fish("Lake Trout", 2.0, 30.0, "Rare", 2, 55, "Deep water trout that grows very large.", 110),
    Fish("Tiger Muskie", 8.0, 25.0, "Rare", 2, 60, "Hybrid of muskie and pike, very aggressive.", 150),
    Fish("Mirror Carp", 8.0, 30.0, "Rare", 2, 60, "Mirror carp have large reflective scales.", 120),
    Fish("Leather Carp", 10.0, 35.0, "Rare", 2, 65, "Carp with few or no scales.", 130),
    Fish("Golden Trout", 1.5, 2.5, "Legendary", 1, 100, "The golden trout is a rare species of mutated trout.", 300),
    Fish("Mutant Bass", 15.0, 40.0, "Legendary", 0.8, 120, "An unusually large and aggressive bass.", 400),
    Fish("Ghost Pike", 20.0, 50.0, "Legendary", 0.5, 150, "A pale, ethereal pike rarely seen by fishermen.", 500),
    Fish("Loch Ness Monster", 1000, 5000, "Mythical", 0.05, 1000, "The Loch Ness Monster is a legendary creature said to inhabit Loch Ness.", 10000),
    Fish("Crystal Leviathan", 2000, 8000, "Mythical", 0.02, 2000, "A massive transparent creature dwelling in the deepest lakes.", 25000),
    Fish("Hylian Pike", 2, 4, "Rare", 0.7, 14, "A majestic river fish with ancient markings on its scales.", 50),
    Fish("Nordic Dragon Salmon", 5, 9, "Epic", 0.5, 16, "A salmon with tiny horns and a powerful voice for some reason.", 80),
    Fish("Magicarp", 8, 12, "Rare", 1.5, 50, "A strange orange and yellow fish.", 300)
]

ocean_fish = [
    Fish("Cod", 2.7, 5.5, "Common", 15, 10, "Cod are a common fish found in the ocean.", 25),
    Fish("Mackerel", 0.5, 2.0, "Common", 12, 8, "Mackerel are fast-swimming fish found in large schools.", 18),
    Fish("Herring", 0.2, 1.0, "Common", 16, 7, "Small oily fish that travel in huge schools.", 15),
    Fish("Pollock", 1.0, 8.0, "Common", 11, 12, "Related to cod, popular commercial fish.", 22),
    Fish("Flounder", 0.5, 3.0, "Common", 13, 10, "Flatfish that lives on the ocean floor.", 20),
    Fish("Sea Bass", 1.5, 5.0, "Uncommon", 8, 20, "Prized for its delicate white flesh.", 45),
    Fish("Snapper", 2.0, 12.0, "Uncommon", 6, 28, "Colorful reef fish with excellent flavor.", 60),
    Fish("Grouper", 5.0, 200.0, "Uncommon", 5, 35, "Large bottom-dwelling fish.", 80),
    Fish("Halibut", 10.0, 200.0, "Uncommon", 4, 40, "Massive flatfish prized by fishermen.", 90),
    Fish("Tuna", 3.0, 25.0, "Uncommon", 7, 25, "Fast-swimming pelagic fish.", 55),
    Fish("Yellowfin Tuna", 180.0, 450.0, "Rare", 3, 50, "Yellowfin is a fast-swimming tuna species.", 200),
    Fish("Bluefin Tuna", 220.0, 680.0, "Rare", 2, 70, "Bluefin is the largest and most prized tuna.", 400),
    Fish("Mahi-Mahi", 7.0, 18.0, "Uncommon", 6, 35, "Mahi-mahi are colorful fish known for their speed.", 80),
    Fish("Wahoo", 8.0, 80.0, "Rare", 3, 55, "One of the fastest fish in the ocean.", 180),
    Fish("Barracuda", 5.0, 50.0, "Uncommon", 5, 38, "Aggressive predator with razor-sharp teeth.", 85),
    Fish("Sailfish", 30.0, 90.0, "Rare", 2, 75, "Known for its spectacular dorsal fin.", 250),
    Fish("Marlin", 100.0, 600.0, "Rare", 2, 80, "Powerful game fish that can weigh over 500kg.", 350),
    Fish("Swordfish", 90.0, 540.0, "Rare", 2, 70, "Swordfish are known for their long bill.", 350),
    Fish("Shark (Reef)", 10.0, 70.0, "Rare", 3, 60, "Medium-sized reef shark.", 200),
    Fish("Hammerhead Shark", 150.0, 450.0, "Rare", 2, 85, "Distinctive shark with hammer-shaped head.", 400),
    Fish("Tiger Shark", 200.0, 635.0, "Rare", 2, 90, "Large aggressive shark with dark stripes.", 450),
    Fish("Great White Shark", 680.0, 1100.0, "Rare", 2, 100, "Great white shark is a large and powerful predator.", 500),
    Fish("Manta Ray", 300.0, 1350.0, "Rare", 2, 95, "Graceful giant that glides through the water.", 480),
    Fish("Bluefin Trevally", 3.0, 43.0, "Uncommon", 6, 30, "Beautiful blue fish found near reefs.", 70),
    Fish("Amberjack", 5.0, 80.0, "Uncommon", 5, 42, "Strong fighting fish found in warm waters.", 95),
    Fish("King Mackerel", 5.0, 40.0, "Uncommon", 6, 36, "Large fast mackerel species.", 75),
    Fish("Cobia", 10.0, 60.0, "Uncommon", 5, 45, "Large game fish with excellent meat.", 100),
    Fish("Tarpon", 20.0, 130.0, "Rare", 2, 80, "Silver king of the sea, legendary fighter.", 300),
    Fish("Giant Grouper", 200.0, 400.0, "Legendary", 1, 150, "Massive grouper that can grow to enormous size.", 600),
    Fish("Blue Whale", 50000, 150000, "Mythical", 0.001, 5000, "The largest animal to ever exist on Earth.", 100000),
    Fish("Megalodon", 10000, 50000, "Mythical", 0.01, 5000, "An ancient massive shark thought to be extinct.", 50000),
    Fish("Jormungandr", 100000, 500000, "Mythical", 0.0005, 8000, "Jormungandr is a legendary sea serpent said to be the child of Loki.", 100000),
    Fish("Blockfish Creeper", 3, 6, "Rare", 1.2, 12, "A green, blocky fish that hisses softly underwater. It looks unstable.", 40),
    Fish("Vault Carp", 2, 5, "Epic", 0.8, 18, "A carp wearing a tiny blue-and-yellow jumpsuit. It seems oddly optimistic.", 65),
    Fish("Plumber's Tuna", 1, 3, "Uncommon", 2.5, 9, "A red-and-blue tuna that looks like it jumps higher than it swims.", 30),
    Fish("Glow Reef Angelfish", 3, 6, "Rare", 1.4, 20, "An elegant neon fish that drifts like it's in zero-gravity water.", 90)

]

river_fish = [
    Fish("Salmon", 3.6, 5.4, "Common", 10, 15, "Salmon are anadromous fish that migrate from the ocean to rivers.", 40),
    Fish("Catfish", 1.0, 50.0, "Common", 10, 15, "Catfish are bottom-dwelling fish found in rivers.", 30),
    Fish("Carp", 2.0, 14.0, "Uncommon", 5, 25, "Carp are a common fish found in rivers.", 35),
    Fish("Rainbow Trout", 1.0, 4.0, "Common", 9, 20, "Rainbow trout are colorful freshwater fish.", 25),
    Fish("Brown Trout", 0.8, 6.0, "Common", 9, 18, "Native to Europe, introduced worldwide.", 28),
    Fish("Brook Trout", 0.3, 3.0, "Common", 11, 16, "Small beautiful trout with distinctive markings.", 22),
    Fish("Smallmouth Bass", 1.0, 5.0, "Uncommon", 7, 24, "Aggressive fighter, bronze-colored bass.", 48),
    Fish("Largemouth Bass", 2.0, 10.0, "Uncommon", 6, 28, "Popular game fish with large mouth.", 55),
    Fish("Northern Pike", 4.0, 25.0, "Uncommon", 5, 32, "Aggressive predator with sharp teeth.", 70),
    Fish("Muskie", 10.0, 30.0, "Rare", 3, 55, "Muskellunge are large predatory fish.", 150),
    Fish("Steelhead", 3.0, 20.0, "Uncommon", 6, 35, "Rainbow trout that migrates to the ocean.", 75),
    Fish("Chinook Salmon", 4.0, 30.0, "Uncommon", 5, 38, "King salmon, the largest Pacific salmon.", 85),
    Fish("Coho Salmon", 3.0, 15.0, "Uncommon", 6, 30, "Silver salmon with excellent fighting ability.", 65),
    Fish("Sturgeon", 100.0, 227.0, "Rare", 2, 50, "Sturgeon are ancient fish found in rivers.", 300),
    Fish("Paddlefish", 20.0, 90.0, "Rare", 2, 60, "Strange fish with a long paddle-like snout.", 180),
    Fish("Alligator Gar", 50.0, 130.0, "Rare", 2, 70, "Massive gar with alligator-like head.", 250),
    Fish("Flathead Catfish", 5.0, 55.0, "Uncommon", 5, 40, "Large predatory catfish.", 90),
    Fish("Blue Catfish", 10.0, 70.0, "Uncommon", 4, 45, "Largest catfish species in North America.", 100),
    Fish("Zander", 2.0, 10.0, "Uncommon", 6, 32, "European predator fish similar to walleye.", 68),
    Fish("Asp", 1.0, 8.0, "Uncommon", 7, 28, "Predatory cyprinid found in European rivers.", 58),
    Fish("Wels Catfish", 50.0, 200.0, "Rare", 2, 75, "Giant European catfish that can grow massive.", 280),
    Fish("Taimen", 15.0, 50.0, "Rare", 2, 65, "Largest salmonid species in the world.", 200),
    Fish("Arapaima", 100.0, 200.0, "Legendary", 1, 200, "One of the world's largest freshwater fish.", 800),
    Fish("Giant Mekong Catfish", 150.0, 300.0, "Legendary", 0.8, 220, "Critically endangered giant catfish.", 900),
    Fish("Nile Perch", 50.0, 200.0, "Legendary", 1, 180, "Massive African predator fish.", 750),
    Fish("River Dragon", 500, 2000, "Mythical", 0.02, 3000, "Mythical serpentine creature said to guard river treasures.", 30000),
    Fish("Kappa", 20, 100, "Mythical", 0.05, 1500, "Japanese water demon disguised as a turtle-like fish.", 15000),
    Fish("Pale King Mackerel", 2, 4, "Epic", 0.9, 25, "A luminescent white mackerel that rules its school with dignity.", 120),
    Fish("Mountain Spirit Trout", 1, 2, "Rare", 1.6, 18, "A shimmering trout that seems to be made of determination itself.", 75),
    Fish("Strawberry Koi", 0.5, 1.2, "Common", 5.2, 8, "A bright koi with flecks of red that resemble fruit.", 25),
    Fish("Slimey Gloopfish", 0.3, 0.7, "Common", 7.5, 5, "A cheerful blob-fish hybrid that wiggles adorably.", 15),
    Fish("Lambda Salmon", 1, 3, "Rare", 1.3, 12, "A salmon marked with a mysterious orange symbol. It resists authority.", 70),
    Fish("Resonance Catfish", 2, 5, "Uncommon", 2.2, 15, "A catfish that vibrates violently, as if stuck mid-experiment.", 50),
    Fish("ludvik laks", 10, 50, "Rare", 1, 100, "Big and bulky, but very nice!", 300)
]

deep_sea_fish = [
    Fish("Anglerfish", 0.5, 20.0, "Uncommon", 7, 40, "Deep sea fish with a bioluminescent lure.", 70),
    Fish("Gulper Eel", 0.3, 9.0, "Rare", 3, 60, "Bizarre deep sea eel with enormous mouth.", 100),
    Fish("Hatchetfish", 0.01, 0.05, "Common", 12, 15, "Small fish with light-producing organs.", 25),
    Fish("Viperfish", 0.1, 0.5, "Uncommon", 8, 35, "Terrifying fish with needle-like teeth.", 65),
    Fish("Fangtooth", 0.05, 0.2, "Uncommon", 9, 38, "Has the largest teeth relative to body size.", 68),
    Fish("Dragonfish", 0.1, 0.8, "Uncommon", 7, 42, "Bioluminescent predator of the deep.", 75),
    Fish("Barreleye", 0.05, 0.3, "Rare", 4, 50, "Fish with transparent head and tubular eyes.", 95),
    Fish("Goblin Shark", 50.0, 210.0, "Rare", 2, 70, "Pink shark with protruding jaws.", 220),
    Fish("Frilled Shark", 20.0, 90.0, "Rare", 3, 65, "Primitive shark species rarely seen.", 200),
    Fish("Megamouth Shark", 500.0, 1200.0, "Rare", 2, 80, "Extremely rare filter-feeding shark.", 350),
    Fish("Giant Squid", 150.0, 275.0, "Rare", 2, 80, "Mysterious deep sea creature with massive tentacles.", 400),
    Fish("Colossal Squid", 300.0, 495.0, "Legendary", 1, 150, "Even larger than giant squid with rotating hooks.", 700),
    Fish("Oarfish", 70.0, 270.0, "Legendary", 1, 150, "Longest bony fish in the world, rarely seen.", 600),
    Fish("Giant Isopod", 0.5, 1.7, "Uncommon", 6, 45, "Enormous deep-sea relative of the pill bug.", 80),
    Fish("Vampire Squid", 0.2, 0.5, "Uncommon", 7, 40, "Has the largest eyes relative to body size.", 72),
    Fish("Coelacanth", 40.0, 90.0, "Legendary", 1, 180, "Living fossil thought extinct for millions of years.", 850),
    Fish("Chimera", 2.0, 15.0, "Rare", 3, 55, "Ghost shark with venomous spine.", 140),
    Fish("Lanternfish", 0.01, 0.1, "Common", 14, 12, "Small bioluminescent fish, most abundant vertebrate.", 18),
    Fish("Stoplight Loosejaw", 0.05, 0.3, "Uncommon", 8, 36, "Can produce red bioluminescence.", 66),
    Fish("Pelican Eel", 0.2, 1.0, "Rare", 4, 48, "Eel with enormous mouth like a pelican.", 88),
    Fish("Sixgill Shark", 200.0, 590.0, "Rare", 2, 75, "Primitive shark that hunts in deep waters.", 280),
    Fish("Greenland Shark", 400.0, 1000.0, "Rare", 2, 85, "Can live over 400 years, slowest shark.", 380),
    Fish("Giant Grenadier", 5.0, 20.0, "Uncommon", 6, 42, "Deep-dwelling rattail fish.", 78),
    Fish("Snailfish", 0.01, 8.0, "Uncommon", 7, 38, "Gelatinous fish found at extreme depths.", 70),
    Fish("Blobfish", 2.0, 9.0, "Mythical", 0.00001, 100000, "Looks familuar.....", 105),
    Fish("Noko the blobfish", 2.0, 9.0, "Godly", 0.0000001, 1000000, "A blobfish that has been blessed by the gods.", 106),
    Fish("Abyssal Octopus", 5.0, 15.0, "Rare", 3, 58, "Rarely seen octopus from extreme depths.", 125),
    Fish("Kraken", 5000, 10000, "Mythical", 0.001, 10000, "Legendary sea monster said to drag ships to the depths.", 200000),
    Fish("Leviathan", 20000, 100000, "Mythical", 0.0003, 15000, "Biblical sea monster of enormous power.", 300000),
    Fish("Abyssal Horror", 1000, 5000, "Mythical", 0.003, 8000, "Nameless terror from the deepest trenches.", 150000),
    Fish("Abyss Watcher", 30, 55, "Legendary", 0.18, 70, "A shadowy fish with a burning ember heart and ancient duty.", 650),
    Fish("Ashen Knight Carp", 12, 20, "Legendary", 0.25, 55, "A solemn carp clad in smoldering ash, refusing to yield even underwater.", 500),
    Fish("Hollow Pike", 3, 6, "Rare", 1.1, 22, "A fish whose empty eyes hint at forgotten battles.", 80),
    Fish("Reaper Levi-Minnow", 25, 40, "Legendary", 0.3, 60, "A terrifying predator that screams through the water, despite its size.", 600),
    Fish("Warp Stalker", 7, 12, "Epic", 0.7, 35, "A fish that flickers in and out of existence when approached.", 180),
    Fish("Fallen Starfish", 0.8, 1.5, "Uncommon", 4.0, 10,"A fish that glows softly and seems to hum a familiar tune.", 40),
    Fish("Determined Eel", 3, 6, "Epic", 0.8, 22, "An eel that refuses to flee. Its eyes burn with fierce courage.", 120),
    Fish("Headcrab Eel", 6, 10, "Epic", 0.8, 30, "An eel with odd, grasping fins that latch onto anything nearby.", 150),
    Fish("Corrupt Bass", 1, 3, "Rare", 1.5, 16, "A bass infected by a spreading blue-purple corruption.", 60)
]
volcanic_lake_fish = [
    Fish("Ember Minnow", 0.1, 0.5, "Common", 12, 25, "Tiny fish that sparkles like hot coals.", 35),
    Fish("Ash Perch", 0.5, 2.0, "Common", 10, 30, "Gray fish covered in volcanic ash residue.", 50),
    Fish("Lava Carp", 1.0, 10.0, "Uncommon", 6, 50, "Lives in volcanic waters, glowing red.", 120),
    Fish("Obsidian Bass", 2.0, 8.0, "Uncommon", 5, 55, "Black as volcanic glass with sharp fins.", 130),
    Fish("Magma Eel", 3.0, 20.0, "Rare", 3, 75, "Slithers through molten vents.", 250),
    Fish("Fire Koi", 0.5, 3.0, "Rare", 2, 60, "Bright orange koi born from magma pools.", 200),
    Fish("Sulfur Pike", 5.0, 25.0, "Rare", 2, 85, "Predator fish that breathes toxic fumes.", 280),
    Fish("Inferno Salmon", 10.0, 40.0, "Legendary", 1, 200, "Burns with eternal flames.", 600),
    Fish("Plasma Sturgeon", 50.0, 150.0, "Legendary", 0.8, 250, "Ancient fish that survived eruptions for millennia.", 800),
    Fish("Phoenix Tuna", 30.0, 100.0, "Legendary", 0.5, 300, "Said to be reborn from its own ashes.", 1000),
    Fish("Volcanic Leviathan", 1000.0, 5000.0, "Mythical", 0.02, 5000, "Ancient guardian of magma lakes.", 30000),
    Fish("Prometheus Wyrm", 2000.0, 8000.0, "Mythical", 0.01, 7000, "Dragon-serpent that stole fire from the gods.", 50000),
    Fish("Fireflower Lionfish", 1, 3, "Rare", 1.3, 15, "A fiery lionfish whose fins burst with sparks when startled.", 70),
    Fish("Balrog Guppy", 10, 18, "Legendary", 0.2, 45, "A tiny fish wreathed in flame, somehow both cute and terrifying.", 450),
    Fish("Abyssal Serpent of Cinders", 450, 900, "Mythical", 0.1, 90, "A writhing serpent born from the dying flame beneath the waves.", 1500)

]
arctic_fish = [
    Fish("Snowflake Guppy", 0.05, 0.3, "Common", 14, 20, "Delicate white fish that freezes instantly when caught.", 30),
    Fish("Ice Cod", 1.0, 5.0, "Common", 10, 20, "Lives under the frozen tundra seas.", 40),
    Fish("Tundra Trout", 0.8, 4.0, "Common", 11, 25, "Hardy trout adapted to freezing waters.", 45),
    Fish("Frost Pike", 3.0, 15.0, "Uncommon", 5, 35, "Carnivorous fish found under thick ice.", 75),
    Fish("Glacial Char", 2.0, 10.0, "Uncommon", 6, 40, "Beautiful fish with ice-blue scales.", 85),
    Fish("Blizzard Bass", 4.0, 18.0, "Uncommon", 5, 50, "Aggressive predator of icy waters.", 110),
    Fish("Crystal Salmon", 2.0, 8.0, "Rare", 3, 80, "Translucent salmon that glows in the dark.", 200),
    Fish("Permafrost Sturgeon", 30.0, 120.0, "Rare", 2, 100, "Lives in waters so cold they should be solid.", 350),
    Fish("Aurora Marlin", 50.0, 200.0, "Rare", 2, 120, "Shimmers with colors of the northern lights.", 450),
    Fish("Glacier Whale", 500.0, 3000.0, "Legendary", 1, 400, "A whale trapped in eternal ice.", 800),
    Fish("Yeti Shark", 300.0, 1000.0, "Legendary", 0.8, 350, "White predator of the frozen depths.", 700),
    Fish("Ice Age Behemoth", 1000.0, 4000.0, "Legendary", 0.5, 500, "Prehistoric creature frozen in time.", 1200),
    Fish("Frost Dragon", 2000.0, 10000.0, "Mythical", 0.01, 10000, "An ancient dragon slumbering beneath glaciers.", 100000),
    Fish("Niflheim Serpent", 5000.0, 15000.0, "Mythical", 0.005, 12000, "Norse serpent of ice and mist.", 150000),
    Fish("Icebender Ray", 4, 9, "Epic", 0.6, 22, "A ray with fluid, sweeping fin movements that chill the water.", 150),
    Fish("Frostborn Walker", 20, 35, "Legendary", 0.25, 60, "A chilling creature with icy blue eyes and ancient cold energy.", 500)

]

space_fish = [
    Fish("Astro Guppy", 0.1, 1.0, "Common", 10, 40, "Tiny fish floating in zero gravity.", 80),
    Fish("Comet Minnow", 0.2, 1.5, "Common", 12, 35, "Leaves a trail of stardust as it swims.", 70),
    Fish("Meteor Carp", 2.0, 12.0, "Uncommon", 6, 60, "Covered in crater-like scales.", 140),
    Fish("Solar Flare Bass", 5.0, 25.0, "Uncommon", 5, 70, "Radiates intense heat and light.", 160),
    Fish("Asteroid Pike", 8.0, 40.0, "Uncommon", 5, 75, "Rocky exterior hides fierce predator.", 180),
    Fish("Nebula Ray", 10.0, 80.0, "Rare", 3, 150, "A cosmic creature glowing with plasma.", 400),
    Fish("Pulsar Eel", 15.0, 100.0, "Rare", 2, 160, "Emits rhythmic bursts of energy.", 450),
    Fish("Supernova Tuna", 50.0, 250.0, "Rare", 2, 200, "Explodes with brilliant light when hooked.", 600),
    Fish("Black Hole Grouper", 100.0, 500.0, "Legendary", 1, 350, "Warps space around itself, impossible to measure accurately.", 1500),
    Fish("Void Shark", 200.0, 1000.0, "Legendary", 1, 400, "Feeds on starlight and silence.", 2000),
    Fish("Galaxy Whale", 1000.0, 5000.0, "Legendary", 0.5, 600, "Contains entire solar systems in its body.", 3000),
    Fish("Quasar Dragon", 2000.0, 8000.0, "Mythical", 0.02, 8000, "The brightest and most powerful cosmic entity.", 80000),
    Fish("Singularity Eel", 1000.0, 5000.0, "Mythical", 0.01, 10000, "Can bend space-time with its body.", 30000),
    Fish("Cosmic Kraken", 5000.0, 20000.0, "Mythical", 0.005, 20000, "Devours stars and moons.", 500000),
    Fish("Celestial Leviathan", 10000.0, 50000.0, "Mythical", 0.001, 30000, "The universe made flesh, older than time itself.", 1000000),
    Fish("Redstone katten", 5, 40, "Mythical", 0.0067, 67000, "The famous Redstone Katten", 10000 ),
    Fish("Portal Eel", 10, 18, "Epic", 0.6, 40, "An eel that flickers between blue and orange, creating mini rifts.", 200),
    Fish("Cyberpunk Neon Koi", 3, 7, "Rare", 1.1, 25, "A glowing koi with chrome scales and attitude.", 120),
    Fish("Voidling Tadpole", 0.2, 0.5, "Uncommon", 3.8, 7, "A small tadpole radiating soft darkness, drifting with purpose.", 30),
    Fish("Starfury Guppy", 0.2, 0.6, "Epic", 1.0, 12, "A cosmic guppy trailing tiny falling-star sparks.", 100),
    Fish("Quantum Jelly", 0.5, 1.1, "Rare", 1.9, 18,"A jellyfish that shifts position every time you blink.", 80)

]

# Combine all fish into one master list for tracking
FISH_DATA = lake_fish + ocean_fish + river_fish + deep_sea_fish + volcanic_lake_fish + arctic_fish + space_fish
# Get unique fish names (in case any appear in multiple locations)
UNIQUE_FISH_NAMES = list(set([fish.name for fish in FISH_DATA]))

RODS = [
    Rod("Bamboo Rod", 0, 0.7, "Your starting rod"),
    Rod("Wooden Rod", 150, 0.73, "A slight upgrade from bamboo"),
    Rod("Fiberglass Rod", 400, 0.76, "A decent upgrade"),
    Rod("Composite Rod", 800, 0.80, "Blends strength and flexibility"),
    Rod("Carbon Rod", 1500, 0.84, "Professional quality"),
    Rod("Graphite Rod", 2500, 0.88, "Lightweight and sensitive"),
    Rod("Titanium Rod", 4000, 0.92, "Top of the line"),
    Rod("Reinforced Rod", 6500, 0.95, "Built to handle massive fish"),
    Rod("Legendary Rod", 10000, 0.98, "Never miss a catch"),
    Rod("Mythic Rod", 20000, 1.02, "Forged from celestial metal, improves rare catch chances"),
    Rod("Abyssal Rod", 35000, 1.05, "Can withstand extreme pressures of the deep sea"),
    Rod("Quantum Rod", 60000, 1.08, "Uses temporal resonance to always hook something"),
    Rod("Godly Rod", 100000, 1.12, "Said to catch even mythical creatures with ease"),
    Rod("Blobfish Rod", 2000000, 5.0, "The ultimate fishing rod designed specifically for catching the elusive Blobfish")
]

BAITS = [ 
    Bait("Worm", 0, 0, "Basic free bait"),
    Bait("Bread", 50, 0.05, "Simple but effective"),
    Bait("Cricket", 120, 0.08, "Insects attract small fish"),
    Bait("Minnow", 250, 0.12, "Small fish attract bigger fish"),
    Bait("Corn", 180, 0.10, "Surprisingly effective for many species"),
    Bait("Shrimp", 500, 0.15, "Good for ocean fishing"),
    Bait("Nightcrawler", 400, 0.14, "Premium worm for serious anglers"),
    Bait("Squid", 800, 0.18, "Attracts larger predators"),
    Bait("Cut Bait", 650, 0.16, "Fresh fish chunks work well"),
    Bait("Artificial Lure", 1200, 0.22, "Mimics prey movement"),
    Bait("Live Bait", 1500, 0.25, "The real deal for big catches"),
    Bait("Special Lure", 2500, 0.30, "Increases rare fish chances"),
    Bait("Premium Lure", 4000, 0.35, "Hand-crafted attractant"),
    Bait("Exotic Bait", 6500, 0.40, "Imported rare ingredients"),
    Bait("Master Bait", 50000, 0.50, "The ultimate fishing bait")
]

WEATHERS = ["Sunny", "Cloudy", "Rainy", "Stormy", "Foggy"]

WEATHER_BONUSES = {
    "Sunny": {"xp": 0, "rarity": 0, "message": "☀️ Clear skies make for pleasant fishing."},
    "Cloudy": {"xp": 10, "rarity": 5, "message": "☁️ Fish are more active in cloudy weather."},
    "Rainy": {"xp": 20, "rarity": 10, "message": "🌧️ Rain stirs up the water, attracting fish!"},
    "Stormy": {"xp": 50, "rarity": 30, "message": "⛈️ Dangerous conditions, but rare fish appear!"},
    "Foggy": {"xp": 15, "rarity": 15, "message": "🌫️ Mysterious fog blankets the water..."}
}

# ===== LOCATIONS =====
LOCATIONS = [
    Location("Hub Island - Calm Lake", 
             lake_fish, 
             WEATHER_BONUSES, 
             1,
             "A peaceful lake surrounded by trees. Perfect for beginners."),
    
    Location("Hub Island - Swift River", 
             river_fish, 
             WEATHER_BONUSES, 
             1,
             "A fast-flowing river with rocky shores. Trout and salmon thrive here."),
    
    Location("Ocean", 
             ocean_fish, 
             WEATHER_BONUSES, 
             5,
             "The vast open ocean. Anything could be lurking in its depths."),
    
    Location("Deep Sea", 
             ocean_fish + [fish for fish in ocean_fish if fish.rarity in ["Rare", "Legendary", "Mythical"]], 
             WEATHER_BONUSES, 
             10,
             "The abyssal zone. Dark, cold, and full of mysteries."),
    
    Location("Volcanic Lake", 
             volcanic_lake_fish, 
             WEATHER_BONUSES, 
             20,
             "A crater lake heated by geothermal activity. Strange fish dwell here."),
    
    Location("Arctic Waters", 
             arctic_fish, 
             WEATHER_BONUSES, 
             25,
             "Frozen seas where the ice never melts. Only the hardiest fish survive."),
    
    Location("Space Station Aquarium", 
             space_fish, 
             WEATHER_BONUSES, 
             30,
             "Zero-gravity fishing. The fish float, and so do you.")
]



# ===== INPUT HANDLING =====
def get_key():
    """Cross-platform key input"""
    if platform.system() == 'Windows':
        import msvcrt
        return msvcrt.getch().decode('utf-8').lower()
    else:
        import tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch.lower()


# ===== CHARACTER CREATION =====
def create_character():
    """Create a new player character"""
    print(Fore.CYAN + "\n╔═══════════════════════════════════════╗" + Style.RESET_ALL)
    print(Fore.CYAN + "║       CHARACTER CREATION             ║" + Style.RESET_ALL)
    print(Fore.CYAN + "╚═══════════════════════════════════════╝" + Style.RESET_ALL)
    
    name = input(Fore.GREEN + "\nEnter your fisherman's name: " + Style.RESET_ALL)
    
    print(Fore.YELLOW + "\nDistribute 15 points among these stats:" + Style.RESET_ALL)
    print(Fore.WHITE + "  Strength: Catch bigger fish" + Style.RESET_ALL)
    print(Fore.WHITE + "  Luck: Find rarer fish" + Style.RESET_ALL)
    print(Fore.WHITE + "  Patience: Easier minigames" + Style.RESET_ALL)
    
    points_left = 15
    stats = {'strength': 0, 'luck': 0, 'patience': 0}
    
    for stat in stats.keys():
        while True:
            try:
                val = int(input(Fore.CYAN + f"{stat.capitalize()} (Points left: {points_left}): " + Style.RESET_ALL))
                if 0 <= val <= points_left:
                    stats[stat] = val
                    points_left -= val
                    break
                else:
                    print(Fore.RED + f"Please enter 0-{points_left}" + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Invalid input!" + Style.RESET_ALL)
    
    print(Fore.YELLOW + "\nChoose difficulty:" + Style.RESET_ALL)
    print(Fore.GREEN + "1. Easy (1.5x XP, 1.5x Money)" + Style.RESET_ALL)
    print(Fore.YELLOW + "2. Normal (1x XP, 1x Money)" + Style.RESET_ALL)
    print(Fore.RED + "3. Hard (0.75x XP, 0.75x Money, but 2x Rarity Chance)" + Style.RESET_ALL)
    
    diff_choice = input(Fore.CYAN + "Difficulty: " + Style.RESET_ALL)
    difficulty_map = {
        '1': ('Easy', 1.5),
        '2': ('Normal', 1.0),
        '3': ('Hard', 0.75)
    }
    difficulty_name, difficulty_mult = difficulty_map.get(diff_choice, ('Normal', 1.0))
    
    return name, stats, difficulty_name, difficulty_mult


# ===== MINIGAMES =====
def button_mashing_minigame(patience_stat):
    """Player must press space rapidly"""
    print(Fore.YELLOW + "\n🎣 Mash SPACE as fast as you can!" + Style.RESET_ALL)
    
    target = max(10, 30 - patience_stat)  # Higher patience = lower target
    presses = 0
    start_time = time.time()
    
    print(Fore.CYAN + f"Press SPACE {target} times in 5 seconds!" + Style.RESET_ALL)
    
    while time.time() - start_time < 5:
        key = get_key()
        if key == ' ':
            presses += 1
            print(Fore.GREEN + f"Presses: {presses}/{target}" + Style.RESET_ALL, end='\r')
        if presses >= target:
            print(Fore.GREEN + f"\n✓ Success! ({presses} presses)" + Style.RESET_ALL)
            return True
    
    print(Fore.RED + f"\n✗ Failed! Only {presses}/{target} presses." + Style.RESET_ALL)
    return False


def timing_minigame(patience_stat):
    """Player must press space at the right moment"""
    print(Fore.YELLOW + "\n🎯 Press SPACE when the bar is in the green zone!" + Style.RESET_ALL)
    
    bar_width = 20
    green_zone_size = max(3, 8 - patience_stat // 3)
    green_start = random.randint(0, bar_width - green_zone_size)
    green_end = green_start + green_zone_size
    
    position = 0
    direction = 1
    
    for _ in range(40):  # 40 frames
        bar = ['░'] * bar_width
        for i in range(green_start, green_end):
            bar[i] = '█'
        bar[position] = '▼'
        
        print('\r' + Fore.CYAN + ''.join(bar) + Style.RESET_ALL, end='', flush=True)
        
        # Non-blocking input check
        if platform.system() == 'Windows':
            import msvcrt
            if msvcrt.kbhit():
                key = msvcrt.getch().decode('utf-8')
                if key == ' ':
                    if green_start <= position < green_end:
                        print(Fore.GREEN + "\n✓ Perfect timing!" + Style.RESET_ALL)
                        return True
                    else:
                        print(Fore.RED + "\n✗ Missed!" + Style.RESET_ALL)
                        return False
        else:
            # For Unix-like systems, simplified version
            import select
            if select.select([sys.stdin], [], [], 0.05)[0]:
                key = sys.stdin.read(1)
                if key == ' ':
                    if green_start <= position < green_end:
                        print(Fore.GREEN + "\n✓ Perfect timing!" + Style.RESET_ALL)
                        return True
                    else:
                        print(Fore.RED + "\n✗ Missed!" + Style.RESET_ALL)
                        return False
        
        time.sleep(0.1)
        position += direction
        if position >= bar_width or position < 0:
            direction *= -1
            position += direction * 2
    
    print(Fore.RED + "\n✗ Time's up!" + Style.RESET_ALL)
    return False


# ===== LOCATION MAP CLASS =====
class LocationMap:
    def __init__(self, name, layout, description=""):
        self.name = name
        self.layout = layout  # 2D list of characters
        self.description = description
        self.player_x = 1
        self.player_y = 1
        self.message = "Use WASD to move around."
        
        # Find initial player position (spawn point marked with 'P')
        for y, row in enumerate(layout):
            for x, tile in enumerate(row):
                if tile == 'P':
                    self.player_x = x
                    self.player_y = y
                    self.layout[y][x] = '.'  # Replace P with ground
    
    def move_player(self, dx, dy):
        new_x = self.player_x + dx
        new_y = self.player_y + dy
        
        # Check bounds
        if 0 <= new_y < len(self.layout) and 0 <= new_x < len(self.layout[new_y]):
            tile = self.layout[new_y][new_x]
            # Allow movement on walkable tiles
            if tile in ['.', '≈', '≋', '⊙', '◉', '🏠', '🏪', '🏛️', '📋', '⚓']:
                self.player_x = new_x
                self.player_y = new_y
                self.message = f"Moved to ({new_x}, {new_y})"
            elif tile == '█' or tile == '🌳' or tile == '▓':
                self.message = "Can't walk through that!"
            else:
                self.message = "Can't walk there!"
    
    def is_fishing_spot(self, x, y):
        """Check if location is a fishing spot"""
        tile = self.layout[y][x]
        return tile in ['⊙', '◉', '≈', '≋', '~', '♨', '❄', '⌬']
    
    def is_golden_spot(self, x, y):
        """Check if it's a golden fishing spot"""
        return self.layout[y][x] == '◉'
    
    def is_building(self, x, y):
        """Check if location is a building entrance"""
        tile = self.layout[y][x]
        return tile in ['🏪', '🏛️', '📋', '🏠']
    
    def get_building_type(self, x, y):
        """Get the type of building at this position"""
        tile = self.layout[y][x]
        building_map = {
            '🏪': 'shop',
            '🏛️': 'aquarium',
            '📋': 'quests',
            '🏠': 'home',
            '⚓': 'dock'
        }
        return building_map.get(tile, None)
    
    def render_tile(self, tile, is_player, is_spot, is_golden):
        """Render a single tile with appropriate coloring"""
        if is_player:
            return Fore.RED + '♦' + Style.RESET_ALL
        elif is_golden:
            return Fore.LIGHTYELLOW_EX + '◉' + Style.RESET_ALL
        elif is_spot or tile == '⊙':
            return Fore.CYAN + '⊙' + Style.RESET_ALL
        elif tile == '≈':  # Lake water
            return Fore.BLUE + '≈' + Style.RESET_ALL
        elif tile == '≋':  # River water
            return Fore.LIGHTBLUE_EX + '≋' + Style.RESET_ALL
        elif tile == '█':  # Wall
            return Fore.WHITE + '█' + Style.RESET_ALL
        elif tile == '🌳':  # Tree
            return Fore.GREEN + '🌳' + Style.RESET_ALL
        elif tile == '▓':  # Mountain
            return Fore.LIGHTBLACK_EX + '▓' + Style.RESET_ALL
        elif tile == '🏪':  # Shop
            return Fore.YELLOW + '🏪' + Style.RESET_ALL
        elif tile == '🏛️':  # Aquarium
            return Fore.MAGENTA + '🏛️' + Style.RESET_ALL
        elif tile == '📋':  # Quest board
            return Fore.CYAN + '📋' + Style.RESET_ALL
        elif tile == '🏠':  # Home
            return Fore.LIGHTRED_EX + '🏠' + Style.RESET_ALL
        elif tile == '⚓':  # Dock
            return Fore.LIGHTCYAN_EX + '⚓' + Style.RESET_ALL
        elif tile == '.':  # Ground
            return Fore.LIGHTBLACK_EX + '·' + Style.RESET_ALL
        else:
            return tile


# Create Hub Island map layout
HUB_ISLAND_LAYOUT = [
    ['█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█'],
    ['█', '🌳', '🌳', '▓', '▓', '▓', '▓', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '█'],
    ['█', '🌳', '🏛️', '.', '.', '▓', '▓', '▓', '🌳', '≋', '≋', '≋', '≋', '≋', '≋', '🌳', '🌳', '🌳', '🌳', '█'],
    ['█', '🌳', '.', '.', '.', '.', '▓', '▓', '🌳', '≋', '⊙', '≋', '≋', '⊙', '≋', '🌳', '🌳', '🌳', '🌳', '█'],
    ['█', '🌳', '🏠', '.', 'P', '.', '.', '🌳', '🌳', '≋', '≋', '≋', '≋', '≋', '≋', '🌳', '◉', '🌳', '🌳', '█'],
    ['█', '🌳', '.', '.', '.', '.', '.', '🌳', '≈', '≈', '≈', '≋', '≋', '≋', '🌳', '🌳', '🌳', '🌳', '🌳', '█'],
    ['█', '🌳', '.', '.', '🏪', '.', '.', '≈', '≈', '⊙', '≈', '≈', '≋', '≋', '≋', '🌳', '🌳', '🌳', '🌳', '█'],
    ['█', '🌳', '🌳', '.', '.', '.', '≈', '≈', '≈', '≈', '≈', '≈', '≈', '≋', '≋', '≋', '🌳', '🌳', '🌳', '█'],
    ['█', '🌳', '🌳', '.', '📋', '.', '≈', '⊙', '≈', '≈', '◉', '≈', '≈', '≈', '≋', '≋', '≋', '🌳', '🌳', '█'],
    ['█', '🌳', '🌳', '.', '.', '.', '≈', '≈', '≈', '≈', '≈', '≈', '≈', '≈', '≈', '≋', '≋', '≋', '🌳', '█'],
    ['█', '🌳', '🌳', '🌳', '.', '.', '.', '≈', '≈', '≈', '≈', '≈', '≈', '≈', '≈', '≈', '≋', '≋', '🌳', '█'],
    ['█', '🌳', '🌳', '🌳', '🌳', '.', '.', '.', '≈', '≈', '≈', '≈', '≈', '≈', '≈', '≈', '≋', '🌳', '🌳', '█'],
    ['█', '🌳', '🌳', '🌳', '🌳', '.', '.', '.', '.', '≈', '≈', '≈', '≈', '≈', '≈', '≈', '🌳', '🌳', '🌳', '█'],
    ['█', '🌳', '🌳', '🌳', '🌳', '🌳', '.', '.', '.', '.', '.', '.', '.', '.', '.', '⚓', '.', '🌳', '🌳', '█'],
    ['█', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '.', '.', '.', '.', '.', '.', '.', '.', '🌳', '🌳', '🌳', '█'],
    ['█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█'],
]

# Create location maps for other locations
OCEAN_LAYOUT = [
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '⊙', '~', '~', '~', '~', '~', '~', '~', '~', '~', '⊙', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '⊙', '~', '~', '~', '~', '~', '~', '~', '~', '~', '◉', '~', '~', '~', '~', '⊙', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', 'P', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '⊙', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '⊙', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '⊙', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
]

DEEP_SEA_LAYOUT = [
    ['▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓'],
    ['▓', '~', '~', '~', '~', '⊙', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '▓'],
    ['▓', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '⊙', '~', '~', '~', '~', '~', '▓'],
    ['▓', '~', '~', '⊙', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '▓'],
    ['▓', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '▓'],
    ['▓', '~', '~', '~', '~', '~', '~', '~', '~', '~', '◉', '~', '~', '~', '~', '~', '~', '~', '~', '▓'],
    ['▓', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '▓'],
    ['▓', '~', '~', '~', '~', '~', '~', '~', 'P', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '▓'],
    ['▓', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '▓'],
    ['▓', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '⊙', '~', '▓'],
    ['▓', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '▓'],
    ['▓', '~', '⊙', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '▓'],
    ['▓', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '▓'],
    ['▓', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '▓'],
    ['▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓'],
]

VOLCANIC_LAYOUT = [
    ['♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨'],
    ['♨', '▓', '▓', '▓', '▓', '♨', '♨', '♨', '⊙', '♨', '♨', '♨', '♨', '♨', '▓', '▓', '▓', '▓', '▓', '♨'],
    ['♨', '▓', '▓', '▓', '▓', '▓', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '▓', '▓', '▓', '▓', '▓', '▓', '♨'],
    ['♨', '▓', '▓', '▓', '▓', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '▓', '▓', '▓', '▓', '▓', '♨'],
    ['♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '▓', '▓', '▓', '♨', '♨'],
    ['♨', '♨', '⊙', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨'],
    ['♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨'],
    ['♨', '♨', '♨', '♨', '♨', '♨', '♨', 'P', '♨', '♨', '◉', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨'],
    ['♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨'],
    ['♨', '▓', '▓', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '⊙', '♨', '♨', '♨', '♨', '▓', '▓', '♨'],
    ['♨', '▓', '▓', '▓', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '▓', '▓', '▓', '♨'],
    ['♨', '▓', '▓', '▓', '▓', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '▓', '▓', '▓', '▓', '♨'],
    ['♨', '▓', '▓', '▓', '▓', '▓', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '▓', '▓', '▓', '▓', '▓', '♨'],
    ['♨', '♨', '▓', '▓', '▓', '▓', '▓', '♨', '♨', '♨', '♨', '♨', '▓', '▓', '▓', '▓', '▓', '▓', '♨', '♨'],
    ['♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨', '♨'],
]

SPACE_LAYOUT = [
    ['⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬'],
    ['⌬', '⌬', '⌬', '⌬', '⊙', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⊙', '⌬', '⌬', '⌬', '⌬'],
    ['⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬'],
    ['⌬', '⌬', '⊙', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⊙', '⌬', '⌬'],
    ['⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬'],
    ['⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬'],
    ['⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬'],
    ['⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', 'P', '⌬', '⌬', '◉', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬'],
    ['⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬'],
    ['⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬'],
    ['⌬', '⌬', '⊙', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⊙', '⌬', '⌬', '⌬'],
    ['⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⊙', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬'],
    ['⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬'],
    ['⌬', '⌬', '⌬', '⌬', '⊙', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⊙', '⌬', '⌬', '⌬', '⌬', '⌬'],
    ['⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬', '⌬'],
]

ARCTIC_LAYOUT = [
    ['❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄'],
    ['❄', '▓', '▓', '❄', '❄', '❄', '❄', '❄', '❄', '⊙', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '▓', '▓', '❄'],
    ['❄', '▓', '▓', '▓', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '▓', '▓', '▓', '❄'],
    ['❄', '❄', '▓', '▓', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '▓', '▓', '▓', '❄', '❄'],
    ['❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '▓', '❄', '❄', '❄'],
    ['❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄'],
    ['❄', '❄', '⊙', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄'],
    ['❄', '❄', '❄', '❄', '❄', '❄', '❄', 'P', '❄', '❄', '◉', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄'],
    ['❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄'],
    ['❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '⊙', '❄', '❄'],
    ['❄', '❄', '❄', '▓', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄'],
    ['❄', '❄', '▓', '▓', '▓', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '▓', '❄', '❄', '❄'],
    ['❄', '▓', '▓', '▓', '▓', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '▓', '▓', '▓', '❄', '❄'],
    ['❄', '▓', '▓', '▓', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '⊙', '❄', '❄', '▓', '▓', '▓', '❄'],
    ['❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄', '❄'],
]

# Add maps to locations
LOCATIONS[0].map = LocationMap("Hub Island - Calm Lake", HUB_ISLAND_LAYOUT, LOCATIONS[0].description)
LOCATIONS[1].map = LocationMap("Hub Island - Swift River", HUB_ISLAND_LAYOUT, LOCATIONS[1].description)
LOCATIONS[2].map = LocationMap("Ocean", OCEAN_LAYOUT, LOCATIONS[2].description)
LOCATIONS[3].map = LocationMap("Deep Sea", DEEP_SEA_LAYOUT, LOCATIONS[3].description)
LOCATIONS[4].map = LocationMap("Volcanic Lake", VOLCANIC_LAYOUT, LOCATIONS[4].description)
LOCATIONS[5].map = LocationMap("Arctic Waters", ARCTIC_LAYOUT, LOCATIONS[5].description)
LOCATIONS[6].map = LocationMap("Space Station Aquarium", SPACE_LAYOUT, LOCATIONS[6].description)


# ===== QUEST SYSTEM =====

class Quest:
    def __init__(self, title, description, target_fish, target_count, reward_money, reward_xp):
        self.title = title
        self.description = description
        self.target_fish = target_fish
        self.target_count = target_count
        self.reward_money = reward_money
        self.reward_xp = reward_xp
        self.progress = 0
        self.completed = False
    
    def check_progress(self, fish_name):
        """Update progress when a target fish is caught"""
        if fish_name == self.target_fish and not self.completed:
            self.progress += 1
            if self.progress >= self.target_count:
                self.completed = True
                return True
        return False


AVAILABLE_QUESTS = [
    Quest("Beginner's Luck", "Catch 5 Carp to prove yourself", "Carp", 5, 100, 50),
    Quest("Pike Hunter", "Catch 3 Pike from the river", "Pike", 3, 200, 100),
    Quest("Sturgeon Master", "Catch a massive Sturgeon", "Sturgeon", 1, 500, 300),
    Quest("Deep Diver", "Catch 2 fish from the Deep Sea", None, 2, 1000, 500),  # Any fish from Deep Sea
]


# ===== WORLD MAP CLASS =====
class WorldMap:
    """Navigable world map showing all fishing locations"""
    def __init__(self, game_instance):
        self.game = game_instance
        self.player_x = 5
        self.player_y = 3
        self.message = "Navigate to a location and press [E] to travel there!"
        
        # World map layout
        # H = Hub Island (home), O = Ocean, D = Deep Sea, V = Volcanic Lake, A = Arctic Waters, S = Space
        self.layout = [
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
            "~~~~~~~🌊O~~~~~~~~~❄️A~~~~~~~",
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
            "~~🏝️H~~~~~~~~~~~~~~~~~~~~~~~~",
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
            "~~~~~~~~~🌋V~~~~~~~🌊D~~~~~~~",
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
            "~~~~~~~~~~~🚀S~~~~~~~~~~~~~~~",
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        ]
        
        # Map location data to coordinates and LOCATIONS indices
        self.locations = {
            'H': {
                'name': 'Hub Island',
                'color': Fore.GREEN,
                'game_index': 0,  # Index in LOCATIONS array
                'unlock_level': 1,
                'x': 2,
                'y': 3,
                'map': None  # This is home, no map to enter
            },
            'O': {
                'name': 'Ocean',
                'color': Fore.BLUE,
                'game_index': 2,
                'unlock_level': 5,
                'x': 8,
                'y': 1
            },
            'D': {
                'name': 'Deep Sea',
                'color': Fore.LIGHTBLUE_EX,
                'game_index': 3,
                'unlock_level': 10,
                'x': 21,
                'y': 5
            },
            'V': {
                'name': 'Volcanic Lake',
                'color': Fore.LIGHTRED_EX,
                'game_index': 4,
                'unlock_level': 20,
                'x': 10,
                'y': 5
            },
            'A': {
                'name': 'Arctic Waters',
                'color': Fore.CYAN,
                'game_index': 5,
                'unlock_level': 25,
                'x': 19,
                'y': 1
            },
            'S': {
                'name': 'Space Station',
                'color': Fore.LIGHTMAGENTA_EX,
                'game_index': 6,
                'unlock_level': 30,
                'x': 12,
                'y': 7
            }
        }
        
        # Set map references
        for key, loc_data in self.locations.items():
            if key != 'H':  # Hub Island has no separate map
                loc_data['map'] = LOCATIONS[loc_data['game_index']].map
    
    def get_location_at(self, x, y):
        """Get location data at given coordinates"""
        for tile_char, loc in self.locations.items():
            if 'x' in loc and 'y' in loc and loc['x'] == x and loc['y'] == y:
                return loc
        return None
    
    def is_location_unlocked(self, location):
        """Check if player has unlocked this location"""
        return self.game.level >= location['unlock_level']
    
    def move_player(self, dx, dy):
        """Move player on world map"""
        new_x = self.player_x + dx
        new_y = self.player_y + dy
        
        # Check bounds
        if 0 <= new_y < len(self.layout) and 0 <= new_x < len(self.layout[0]):
            self.player_x = new_x
            self.player_y = new_y
            
            # Check if standing on a location
            location = self.get_location_at(new_x, new_y)
            if location:
                status = "✓ Unlocked" if self.is_location_unlocked(location) else f"🔒 Requires Level {location['unlock_level']}"
                self.message = f"{location['name']} - {status}. Press [E] to enter!"
            else:
                self.message = "Navigate to a location and press [E] to travel there!"
    
    def render_tile(self, tile, is_player=False):
        """Render a single tile with appropriate color"""
        if is_player:
            return Fore.YELLOW + "⛵" + Style.RESET_ALL
        elif tile in self.locations:
            loc = self.locations[tile]
            is_unlocked = self.is_location_unlocked(loc)
            color = loc['color'] if is_unlocked else Fore.LIGHTBLACK_EX
            
            # Use emoji/symbol from layout
            if tile == 'H':
                symbol = "🏝️"
            elif tile == 'O':
                symbol = "🌊"
            elif tile == 'D':
                symbol = "🌊"
            elif tile == 'V':
                symbol = "🌋"
            elif tile == 'A':
                symbol = "❄️"
            elif tile == 'S':
                symbol = "🚀"
            else:
                symbol = tile
                
            return color + symbol + Style.RESET_ALL
        elif tile == '~':
            return Fore.LIGHTBLUE_EX + "~" + Style.RESET_ALL
        else:
            return tile
    
    def render_overworld(self, clear_func):
        """Render the world map"""
        clear_func()
        
        print(Fore.CYAN + "╔════════════════════════════════════════════╗" + Style.RESET_ALL)
        print(Fore.CYAN + "║            🗺️  WORLD MAP 🗺️               ║" + Style.RESET_ALL)
        print(Fore.CYAN + "╚════════════════════════════════════════════╝" + Style.RESET_ALL)
        print()
        
        # Render map
        for y, row in enumerate(self.layout):
            line = ""
            for x, tile in enumerate(row):
                is_player = (x == self.player_x and y == self.player_y)
                
                # Handle multi-character emojis in layout
                if tile in ['🌊', '🏝️', '🌋', '❄️', '🚀']:
                    if is_player:
                        line += Fore.YELLOW + "⛵" + Style.RESET_ALL
                    else:
                        # Find which location this emoji represents
                        for loc_char, loc_data in self.locations.items():
                            if 'x' in loc_data and loc_data['x'] == x and loc_data['y'] == y:
                                is_unlocked = self.is_location_unlocked(loc_data)
                                color = loc_data['color'] if is_unlocked else Fore.LIGHTBLACK_EX
                                line += color + tile + Style.RESET_ALL
                                break
                        else:
                            line += tile
                else:
                    line += self.render_tile(tile, is_player)
            print(line)
        
        print()
        print(Fore.GREEN + f"Level: {self.game.level} | XP: {self.game.xp}/{self.game.xp_threshold} | Money: ${self.game.money}" + Style.RESET_ALL)
        print()
        print(Fore.YELLOW + self.message + Style.RESET_ALL)
        print()
        print(Fore.CYAN + "Locations:" + Style.RESET_ALL)
        for tile_char, loc in self.locations.items():
            if tile_char == 'H':  # Skip Hub Island
                continue
            is_unlocked = self.is_location_unlocked(loc)
            status = f"{Fore.GREEN}✓" if is_unlocked else f"{Fore.RED}🔒 Lvl{loc['unlock_level']}"
            color = loc['color'] if is_unlocked else Fore.LIGHTBLACK_EX
            print(f"  {color}{loc['name']:20s}{Style.RESET_ALL} {status}{Style.RESET_ALL}")
        
        print()
        print(Fore.WHITE + "[WASD] Move | [E] Enter Location | [Q] Return to Hub Island" + Style.RESET_ALL)
    
    def run(self):
        """Main world map navigation loop"""
        while True:
            self.render_overworld(self.game.clear_screen)
            
            key = get_key()
            
            if key == 'w':
                self.move_player(0, -1)
            elif key == 's':
                self.move_player(0, 1)
            elif key == 'a':
                self.move_player(-1, 0)
            elif key == 'd':
                self.move_player(1, 0)
            elif key == 'e':
                # Try to enter a location
                location = self.get_location_at(self.player_x, self.player_y)
                if location:
                    if location['name'] == 'Hub Island':
                        self.message = "You're already at Hub Island!"
                    elif self.is_location_unlocked(location):
                        self.game.current_location = LOCATIONS[location['game_index']]
                        print(Fore.GREEN + f"Traveling to {location['name']}..." + Style.RESET_ALL)
                        time.sleep(1)
                        # Return the location to enter
                        return LOCATIONS[location['game_index']]
                    else:
                        self.message = f"🔒 {location['name']} is locked! Requires level {location['unlock_level']} (You: Lvl {self.game.level})"
                else:
                    self.message = "Nothing to enter here. Navigate to a location!"
            elif key == 'q':
                return None  # Return to hub island



# ===== GAME CLASS =====
class Game:
    def __init__(self, character_data=None):
        # Character attributes
        if character_data:
            self.name = character_data['name']
            self.stats = character_data['stats']
            self.difficulty_name = character_data['difficulty_name']
            self.difficulty_mult = character_data['difficulty_mult']
        else:
            self.name = "Fisher"
            self.stats = {'strength': 5, 'luck': 5, 'patience': 5}
            self.difficulty_name = "Normal"
            self.difficulty_mult = 1.0
        
        # Game progress
        self.level = 1
        self.xp = 0
        self.xp_threshold = 100
        self.money = 100
        self.skill_points = 0
        
        # Inventory
        self.inventory = []
        self.owned_rods = [RODS[0]]
        self.owned_baits = [BAITS[0]]
        self.current_rod = RODS[0]
        self.current_bait = BAITS[0]
        
        # Rod durability
        self.rod_durability = 100
        self.rod_max_durability = 100
        
        # Collections
        self.encyclopedia = {}  # {fish_name: count_caught}
        self.trophy_room = []   # List of Fish objects for display
        
        # World state
        self.current_location = LOCATIONS[0]
        self.current_weather = random.choice(WEATHERS)
        
        # Quests
        self.active_quests = []
        self.completed_quests = []
        
        # Debug
        self.debug_mode = False
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def save_game(self):
        """Save game to JSON file"""
        save_data = {
            'name': self.name,
            'stats': self.stats,
            'difficulty_name': self.difficulty_name,
            'difficulty_mult': self.difficulty_mult,
            'level': self.level,
            'xp': self.xp,
            'xp_threshold': self.xp_threshold,
            'money': self.money,
            'skill_points': self.skill_points,
            'inventory': [fish.to_dict() for fish in self.inventory],
            'owned_rods': [rod.name for rod in self.owned_rods],
            'owned_baits': [bait.name for bait in self.owned_baits],
            'current_rod': self.current_rod.name,
            'current_bait': self.current_bait.name,
            'rod_durability': self.rod_durability,
            'rod_max_durability': self.rod_max_durability,
            'encyclopedia': self.encyclopedia,
            'trophy_room': [fish.to_dict() for fish in self.trophy_room],
            'current_location': self.current_location.name,
            'current_weather': self.current_weather,
        }
        
        # Create hash-based filename
        name_hash = hashlib.md5(self.name.encode()).hexdigest()[:8]
        filename = f"save_{name_hash}.json"
        
        with open(filename, 'w') as f:
            json.dump(save_data, f, indent=2)
        
        print(Fore.GREEN + f"Game saved to {filename}!" + Style.RESET_ALL)
    
    def load_game(self):
        """Load game from JSON file"""
        saves = [f for f in os.listdir('.') if f.startswith('save_') and f.endswith('.json')]
        
        if not saves:
            print(Fore.RED + "No save files found!" + Style.RESET_ALL)
            return False
        
        print(Fore.CYAN + "\n═══ SAVED GAMES ═══" + Style.RESET_ALL)
        for i, save_file in enumerate(saves, 1):
            try:
                with open(save_file, 'r') as f:
                    data = json.load(f)
                print(f"{Fore.GREEN}{i}. {data['name']} (Lvl {data['level']}){Style.RESET_ALL}")
            except:
                print(f"{Fore.RED}{i}. {save_file} (Corrupted){Style.RESET_ALL}")
        
        choice = input(Fore.CYAN + "\nSelect save file: " + Style.RESET_ALL)
        
        try:
            save_file = saves[int(choice) - 1]
            with open(save_file, 'r') as f:
                data = json.load(f)
            
            # Load character data
            self.name = data['name']
            self.stats = data['stats']
            self.difficulty_name = data['difficulty_name']
            self.difficulty_mult = data['difficulty_mult']
            self.level = data['level']
            self.xp = data['xp']
            self.xp_threshold = data['xp_threshold']
            self.money = data['money']
            self.skill_points = data['skill_points']
            
            # Load inventory
            self.inventory = []
            # Inventory loading skipped for simplicity
            
            # Load rods and baits
            self.owned_rods = [rod for rod in RODS if rod.name in data['owned_rods']]
            self.owned_baits = [bait for bait in BAITS if bait.name in data['owned_baits']]
            self.current_rod = next((rod for rod in RODS if rod.name == data['current_rod']), RODS[0])
            self.current_bait = next((bait for bait in BAITS if bait.name == data['current_bait']), BAITS[0])
            
            # Load durability
            self.rod_durability = data.get('rod_durability', 100)
            self.rod_max_durability = data.get('rod_max_durability', 100)
            
            # Load encyclopedia
            self.encyclopedia = data.get('encyclopedia', {})
            
            # Load trophy room
            self.trophy_room = []
            # Trophy loading skipped for simplicity
            
            # Load location
            loc_name = data.get('current_location', 'Calm Lake')
            self.current_location = next((loc for loc in LOCATIONS if loc.name == loc_name), LOCATIONS[0])
            
            self.current_weather = data.get('current_weather', random.choice(WEATHERS))
            
            print(Fore.GREEN + f"Loaded save for {self.name}!" + Style.RESET_ALL)
            time.sleep(1)
            return True
        
        except (IndexError, ValueError, FileNotFoundError):
            print(Fore.RED + "Invalid selection!" + Style.RESET_ALL)
            return False
    
    def gain_xp(self, amount):
        """Award XP and handle level-ups"""
        amount = int(amount * self.difficulty_mult)
        self.xp += amount
        
        print(Fore.CYAN + f"Gained {amount} XP!" + Style.RESET_ALL)
        
        while self.xp >= self.xp_threshold:
            self.level_up()
    
    def level_up(self):
        """Handle level-up logic"""
        self.level += 1
        self.xp -= self.xp_threshold
        self.xp_threshold = int(self.xp_threshold * 1.5)
        self.skill_points += 3
        
        print(Fore.LIGHTYELLOW_EX + f"\n🎉 LEVEL UP! You are now level {self.level}! 🎉" + Style.RESET_ALL)
        print(Fore.GREEN + f"Earned 3 skill points! Total: {self.skill_points}" + Style.RESET_ALL)
        time.sleep(2)
    
    def choose_fish(self):
        """Weighted random fish selection from current location"""
        fish_pool = self.current_location.fish_pool[:]
        
        # Apply rod and bait bonuses
        rarity_bonus = self.current_rod.bonus_chance + self.current_bait.bonus_rarity
        rarity_bonus += self.stats['luck'] * 2
        
        # Weather bonus
        weather_bonus = WEATHER_BONUSES[self.current_weather]['rarity']
        rarity_bonus += weather_bonus
        
        # Adjust rarity if Hard difficulty
        if self.difficulty_name == "Hard":
            rarity_bonus *= 2
        
        # Shift weights toward rarer fish
        weights = []
        for fish in fish_pool:
            weight = fish.rarity_weight * (1 + rarity_bonus / 100)
            weights.append(weight)
        
        return random.choices(fish_pool, weights=weights, k=1)[0]
    
    def fish(self, golden_spot=False):
        """Main fishing action"""
        self.clear_screen()
        
        # Durability check
        if self.rod_durability <= 0:
            print(Fore.RED + "⚠️ Your rod is broken! Repair it at the shop first!" + Style.RESET_ALL)
            time.sleep(2)
            return
        
        print(Fore.CYAN + f"╔═══════════════════════════════════════╗" + Style.RESET_ALL)
        print(Fore.CYAN + f"║  🎣 FISHING AT {self.current_location.name.upper().center(23)} ║" + Style.RESET_ALL)
        print(Fore.CYAN + f"╚═══════════════════════════════════════╝" + Style.RESET_ALL)
        print()
        
        print(Fore.YELLOW + f"Weather: {self.current_weather}" + Style.RESET_ALL)
        print(WEATHER_BONUSES[self.current_weather]['message'])
        
        if golden_spot:
            print(Fore.LIGHTYELLOW_EX + "✨ You're at a GOLDEN SPOT! Better chances!" + Style.RESET_ALL)
        
        print()
        print(Fore.WHITE + "Casting line..." + Style.RESET_ALL)
        time.sleep(1)
        
        # Choose fish
        caught_fish = self.choose_fish()
        
        # Create a fresh instance
        caught_fish = Fish(
            caught_fish.name, 
            caught_fish.min_weight, 
            caught_fish.max_weight,
            caught_fish.rarity,
            caught_fish.rarity_weight,
            caught_fish.xp_reward,
            caught_fish.real_world_info,
            caught_fish.sell_price
        )
        
        # Apply golden spot bonus
        if golden_spot:
            caught_fish.sell_price = int(caught_fish.sell_price * 1.5)
            caught_fish.xp_reward = int(caught_fish.xp_reward * 1.5)
        
        # Apply mutation
        caught_fish.apply_mutation()
        
        # Weight bonus from rod and strength
        weight_mult = 1 + (self.current_rod.bonus_weight + self.stats['strength'] * 3) / 100
        caught_fish.weight = round(caught_fish.weight * weight_mult, 2)
        
        # Minigame
        print(Fore.YELLOW + "\n🎣 Something's biting!" + Style.RESET_ALL)
        time.sleep(0.5)
        
        minigame_choice = random.choice([button_mashing_minigame, timing_minigame])
        success = minigame_choice(self.stats['patience'])
        
        if not success:
            print(Fore.RED + "\n❌ The fish got away!" + Style.RESET_ALL)
            # Reduce rod durability even on failure
            self.rod_durability -= 2
            time.sleep(2)
            return
        
        # Successfully caught!
        self.clear_screen()
        print(Fore.GREEN + "╔═══════════════════════════════════════╗" + Style.RESET_ALL)
        print(Fore.GREEN + "║          🎣 FISH CAUGHT! 🎣           ║" + Style.RESET_ALL)
        print(Fore.GREEN + "╚═══════════════════════════════════════╝" + Style.RESET_ALL)
        print()
        
        print(f"You caught a {caught_fish}!")
        print(Fore.LIGHTBLACK_EX + f"Rarity: {caught_fish.rarity}" + Style.RESET_ALL)
        
        if caught_fish.real_world_info:
            print(Fore.CYAN + f"ℹ️  {caught_fish.real_world_info}" + Style.RESET_ALL)
        
        # Add to inventory and encyclopedia
        self.inventory.append(caught_fish)
        
        if caught_fish.name in self.encyclopedia:
            self.encyclopedia[caught_fish.name] += 1
        else:
            self.encyclopedia[caught_fish.name] = 1
            print(Fore.LIGHTYELLOW_EX + f"🆕 NEW species discovered! Added to encyclopedia!" + Style.RESET_ALL)
        
        # XP reward
        xp_bonus = self.current_bait.bonus_xp + WEATHER_BONUSES[self.current_weather]['xp']
        total_xp = int(caught_fish.xp_reward * (1 + xp_bonus / 100))
        self.gain_xp(total_xp)
        
        # Reduce rod durability
        self.rod_durability -= 5
        if self.rod_durability < 0:
            self.rod_durability = 0
        
        # Quest progress check
        for quest in self.active_quests:
            if quest.check_progress(caught_fish.name):
                print(Fore.LIGHTYELLOW_EX + f"✓ Quest '{quest.title}' completed!" + Style.RESET_ALL)
        
        print()
        print(Fore.LIGHTBLACK_EX + f"Rod Durability: {self.rod_durability}/{self.rod_max_durability}" + Style.RESET_ALL)
        print()
        print(Fore.WHITE + "Press any key to continue..." + Style.RESET_ALL)
        get_key()
    
    def view_inventory(self):
        """Display player inventory"""
        self.clear_screen()
        print(Fore.CYAN + "╔═══════════════════════════════════════╗" + Style.RESET_ALL)
        print(Fore.CYAN + "║             INVENTORY                 ║" + Style.RESET_ALL)
        print(Fore.CYAN + "╚═══════════════════════════════════════╝" + Style.RESET_ALL)
        print()
        
        if not self.inventory:
            print(Fore.YELLOW + "Your inventory is empty. Go fishing!" + Style.RESET_ALL)
        else:
            for i, fish in enumerate(self.inventory, 1):
                print(f"{i}. {fish} - ${fish.sell_price}")
        
        print()
        print(Fore.GREEN + f"Total value: ${sum(f.sell_price for f in self.inventory)}" + Style.RESET_ALL)
        print()
        print(Fore.WHITE + "1. Sell all fish" + Style.RESET_ALL)
        print(Fore.WHITE + "2. Add a trophy fish to aquarium" + Style.RESET_ALL)
        print(Fore.WHITE + "3. Back" + Style.RESET_ALL)
        
        choice = input(Fore.CYAN + "\nChoice: " + Style.RESET_ALL)
        
        if choice == '1':
            total = sum(f.sell_price for f in self.inventory)
            total = int(total * self.difficulty_mult)
            self.money += total
            print(Fore.GREEN + f"Sold all fish for ${total}!" + Style.RESET_ALL)
            self.inventory = []
            time.sleep(1)
        elif choice == '2':
            if self.inventory:
                print(Fore.CYAN + "Select fish to add to aquarium (number): " + Style.RESET_ALL)
                try:
                    idx = int(input()) - 1
                    trophy_fish = self.inventory.pop(idx)
                    self.trophy_room.append(trophy_fish)
                    print(Fore.GREEN + f"Added {trophy_fish.name} to your aquarium!" + Style.RESET_ALL)
                    time.sleep(1)
                except:
                    print(Fore.RED + "Invalid choice!" + Style.RESET_ALL)
                    time.sleep(1)
    
    def visit_shop(self):
        """Shop menu"""
        while True:
            self.clear_screen()
            print(Fore.YELLOW + "╔═══════════════════════════════════════╗" + Style.RESET_ALL)
            print(Fore.YELLOW + "║            🏪 SHOP 🏪                  ║" + Style.RESET_ALL)
            print(Fore.YELLOW + "╚═══════════════════════════════════════╝" + Style.RESET_ALL)
            print()
            print(Fore.GREEN + f"💰 Money: ${self.money}" + Style.RESET_ALL)
            print()
            
            print(Fore.CYAN + "1. Buy Rods" + Style.RESET_ALL)
            print(Fore.CYAN + "2. Buy Bait" + Style.RESET_ALL)
            print(Fore.CYAN + "3. Repair Rod (${})".format(max(10, (100 - self.rod_durability) * 2)) + Style.RESET_ALL)
            print(Fore.CYAN + "4. Back" + Style.RESET_ALL)
            
            choice = input(Fore.YELLOW + "\nChoice: " + Style.RESET_ALL)
            
            if choice == '1':
                self.shop_rods()
            elif choice == '2':
                self.shop_baits()
            elif choice == '3':
                repair_cost = max(10, (100 - self.rod_durability) * 2)
                if self.money >= repair_cost:
                    self.money -= repair_cost
                    self.rod_durability = 100
                    print(Fore.GREEN + "Rod repaired to 100%!" + Style.RESET_ALL)
                    time.sleep(1)
                else:
                    print(Fore.RED + "Not enough money!" + Style.RESET_ALL)
                    time.sleep(1)
            elif choice == '4':
                break
    
    def shop_rods(self):
        """Rod shop"""
        self.clear_screen()
        print(Fore.CYAN + "═══ RODS ═══" + Style.RESET_ALL)
        print()
        
        for i, rod in enumerate(RODS, 1):
            owned = "✓ Owned" if rod in self.owned_rods else f"${rod.price}"
            locked = "" if self.level >= rod.unlock_level else f"🔒 Lvl{rod.unlock_level}"
            print(f"{i}. {rod.name} - {owned} {locked}")
            print(f"   Chance: +{rod.bonus_chance}% | Weight: +{rod.bonus_weight}% | Durability: +{rod.durability_bonus}")
        
        print()
        choice = input(Fore.CYAN + "Buy rod (number) or 0 to cancel: " + Style.RESET_ALL)
        
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(RODS):
                rod = RODS[idx]
                if self.level < rod.unlock_level:
                    print(Fore.RED + f"Requires level {rod.unlock_level}!" + Style.RESET_ALL)
                    time.sleep(1)
                elif rod in self.owned_rods:
                    print(Fore.YELLOW + "You already own this rod!" + Style.RESET_ALL)
                    time.sleep(1)
                elif self.money >= rod.price:
                    self.money -= rod.price
                    self.owned_rods.append(rod)
                    print(Fore.GREEN + f"Bought {rod.name}!" + Style.RESET_ALL)
                    time.sleep(1)
                else:
                    print(Fore.RED + "Not enough money!" + Style.RESET_ALL)
                    time.sleep(1)
        except ValueError:
            pass
    
    def shop_baits(self):
        """Bait shop"""
        self.clear_screen()
        print(Fore.CYAN + "═══ BAIT ═══" + Style.RESET_ALL)
        print()
        
        for i, bait in enumerate(BAITS, 1):
            owned = "✓ Owned" if bait in self.owned_baits else f"${bait.price}"
            locked = "" if self.level >= bait.unlock_level else f"🔒 Lvl{bait.unlock_level}"
            print(f"{i}. {bait.name} - {owned} {locked}")
            print(f"   XP Bonus: +{bait.bonus_xp}% | Rarity Bonus: +{bait.bonus_rarity}%")
        
        print()
        choice = input(Fore.CYAN + "Buy bait (number) or 0 to cancel: " + Style.RESET_ALL)
        
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(BAITS):
                bait = BAITS[idx]
                if self.level < bait.unlock_level:
                    print(Fore.RED + f"Requires level {bait.unlock_level}!" + Style.RESET_ALL)
                    time.sleep(1)
                elif bait in self.owned_baits:
                    print(Fore.YELLOW + "You already own this bait!" + Style.RESET_ALL)
                    time.sleep(1)
                elif self.money >= bait.price:
                    self.money -= bait.price
                    self.owned_baits.append(bait)
                    print(Fore.GREEN + f"Bought {bait.name}!" + Style.RESET_ALL)
                    time.sleep(1)
                else:
                    print(Fore.RED + "Not enough money!" + Style.RESET_ALL)
                    time.sleep(1)
        except ValueError:
            pass
    
    def visit_aquarium(self):
        """Trophy room / aquarium"""
        self.clear_screen()
        print(Fore.MAGENTA + "╔═══════════════════════════════════════╗" + Style.RESET_ALL)
        print(Fore.MAGENTA + "║          🏛️ AQUARIUM 🏛️                ║" + Style.RESET_ALL)
        print(Fore.MAGENTA + "╚═══════════════════════════════════════╝" + Style.RESET_ALL)
        print()
        
        if not self.trophy_room:
            print(Fore.YELLOW + "Your aquarium is empty. Add trophy fish from your inventory!" + Style.RESET_ALL)
        else:
            print(Fore.CYAN + "Your Trophy Collection:" + Style.RESET_ALL)
            print()
            for i, fish in enumerate(self.trophy_room, 1):
                print(f"{i}. {fish}")
        
        print()
        print(Fore.WHITE + "Press any key to return..." + Style.RESET_ALL)
        get_key()
    
    def view_quests(self):
        """Quest board"""
        self.clear_screen()
        print(Fore.CYAN + "╔═══════════════════════════════════════╗" + Style.RESET_ALL)
        print(Fore.CYAN + "║          📋 QUEST BOARD 📋            ║" + Style.RESET_ALL)
        print(Fore.CYAN + "╚═══════════════════════════════════════╝" + Style.RESET_ALL)
        print()
        
        print(Fore.YELLOW + "Active Quests:" + Style.RESET_ALL)
        if not self.active_quests:
            print(Fore.LIGHTBLACK_EX + "  No active quests" + Style.RESET_ALL)
        else:
            for quest in self.active_quests:
                status = f"{quest.progress}/{quest.target_count}"
                print(f"  • {quest.title} - {status}")
                print(f"    {quest.description}")
        
        print()
        print(Fore.GREEN + "Available Quests:" + Style.RESET_ALL)
        available = [q for q in AVAILABLE_QUESTS if q not in self.active_quests and q not in self.completed_quests]
        
        if not available:
            print(Fore.LIGHTBLACK_EX + "  No quests available" + Style.RESET_ALL)
        else:
            for i, quest in enumerate(available, 1):
                print(f"{i}. {quest.title}")
                print(f"   {quest.description}")
                print(f"   Reward: ${quest.reward_money}, {quest.reward_xp} XP")
        
        print()
        print(Fore.WHITE + "1. Accept a quest" + Style.RESET_ALL)
        print(Fore.WHITE + "2. Claim completed quest rewards" + Style.RESET_ALL)
        print(Fore.WHITE + "3. Back" + Style.RESET_ALL)
        
        choice = input(Fore.CYAN + "\nChoice: " + Style.RESET_ALL)
        
        if choice == '1' and available:
            try:
                idx = int(input(Fore.CYAN + "Quest number: " + Style.RESET_ALL)) - 1
                quest = available[idx]
                self.active_quests.append(quest)
                print(Fore.GREEN + f"Quest '{quest.title}' accepted!" + Style.RESET_ALL)
                time.sleep(1)
            except:
                pass
        elif choice == '2':
            completed = [q for q in self.active_quests if q.completed]
            if completed:
                for quest in completed:
                    self.money += quest.reward_money
                    self.gain_xp(quest.reward_xp)
                    self.active_quests.remove(quest)
                    self.completed_quests.append(quest)
                    print(Fore.GREEN + f"Quest '{quest.title}' rewards claimed!" + Style.RESET_ALL)
                time.sleep(2)
            else:
                print(Fore.YELLOW + "No completed quests to claim." + Style.RESET_ALL)
                time.sleep(1)
    
    def visit_dock(self):
        """Dock - travel to other locations via world map"""
        world_map = WorldMap(self)
        return world_map.run()
    
    def hub_island_interaction(self, building_type):
        """Handle interactions with buildings on hub island"""
        if building_type == 'shop':
            self.visit_shop()
        elif building_type == 'aquarium':
            self.visit_aquarium()
        elif building_type == 'quests':
            self.view_quests()
        elif building_type == 'home':
            self.clear_screen()
            print(Fore.LIGHTRED_EX + "╔═══════════════════════════════════════╗" + Style.RESET_ALL)
            print(Fore.LIGHTRED_EX + "║              🏠 HOME 🏠                 ║" + Style.RESET_ALL)
            print(Fore.LIGHTRED_EX + "╚═══════════════════════════════════════╝" + Style.RESET_ALL)
            print()
            print(Fore.GREEN + "A cozy place to rest and save your progress." + Style.RESET_ALL)
            print()
            print(Fore.WHITE + "1. Save Game" + Style.RESET_ALL)
            print(Fore.WHITE + "2. View Stats" + Style.RESET_ALL)
            print(Fore.WHITE + "3. Back" + Style.RESET_ALL)
            
            choice = input(Fore.CYAN + "\nChoice: " + Style.RESET_ALL)
            
            if choice == '1':
                self.save_game()
                time.sleep(1)
            elif choice == '2':
                self.view_character_stats()
        elif building_type == 'dock':
            return self.visit_dock()  # May return a new location
        
        return None
    
    def view_character_stats(self):
        """Display character information"""
        self.clear_screen()
        print(Fore.CYAN + "╔═══════════════════════════════════════╗" + Style.RESET_ALL)
        print(Fore.CYAN + "║          CHARACTER STATS              ║" + Style.RESET_ALL)
        print(Fore.CYAN + "╚═══════════════════════════════════════╝" + Style.RESET_ALL)
        print()
        
        print(Fore.GREEN + f"Name: {self.name}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"Level: {self.level}" + Style.RESET_ALL)
        print(Fore.CYAN + f"XP: {self.xp}/{self.xp_threshold}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Money: ${self.money}" + Style.RESET_ALL)
        print(Fore.MAGENTA + f"Skill Points: {self.skill_points}" + Style.RESET_ALL)
        print()
        print(Fore.WHITE + f"Strength: {self.stats['strength']}" + Style.RESET_ALL)
        print(Fore.WHITE + f"Luck: {self.stats['luck']}" + Style.RESET_ALL)
        print(Fore.WHITE + f"Patience: {self.stats['patience']}" + Style.RESET_ALL)
        print()
        print(Fore.LIGHTBLACK_EX + f"Difficulty: {self.difficulty_name}" + Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + f"Current Rod: {self.current_rod.name}" + Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + f"Current Bait: {self.current_bait.name}" + Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + f"Rod Durability: {self.rod_durability}/{self.rod_max_durability}" + Style.RESET_ALL)
        print()
        print(Fore.YELLOW + f"Species Discovered: {len(self.encyclopedia)}/{len(UNIQUE_FISH_NAMES)}" + Style.RESET_ALL)
        print(Fore.MAGENTA + f"Trophy Fish: {len(self.trophy_room)}" + Style.RESET_ALL)
        print()
        print(Fore.WHITE + "Press any key to return..." + Style.RESET_ALL)
        get_key()
    
    def start_game(self):
        """Main game loop using hub island"""
        hub_map = LOCATIONS[0].map  # Hub island map
        
        while True:
            # Render hub island
            self.clear_screen()
            
            print(Fore.CYAN + f"╔═══════════════════════════════════════╗" + Style.RESET_ALL)
            print(Fore.CYAN + f"║        🏝️ HUB ISLAND 🏝️               ║" + Style.RESET_ALL)
            print(Fore.CYAN + f"╚═══════════════════════════════════════╝" + Style.RESET_ALL)
            print()
            
            # Render the map
            for y, row in enumerate(hub_map.layout):
                line = ""
                for x, tile in enumerate(row):
                    is_player = (x == hub_map.player_x and y == hub_map.player_y)
                    is_spot = hub_map.is_fishing_spot(x, y)
                    is_golden = hub_map.is_golden_spot(x, y)
                    line += hub_map.render_tile(tile, is_player, is_spot, is_golden)
                print(line)
            
            print()
            print(Fore.GREEN + f"Level: {self.level} | XP: {self.xp}/{self.xp_threshold} | Money: ${self.money}" + Style.RESET_ALL)
            print(Fore.LIGHTBLACK_EX + f"Rod: {self.rod_durability}/{self.rod_max_durability} | Weather: {self.current_weather}" + Style.RESET_ALL)
            print()
            print(Fore.YELLOW + hub_map.message + Style.RESET_ALL)
            print()
            print(Fore.WHITE + "🏪 Shop | 🏛️ Aquarium | 📋 Quests | 🏠 Home | ⚓ Dock | ⊙ Fish Spot | ◉ Golden Spot" + Style.RESET_ALL)
            print(Fore.WHITE + "[WASD] Move | [E] Interact | [I] Inventory | [C] Stats | [Q] Quit" + Style.RESET_ALL)
            
            # Get input
            key = get_key()
            
            if key == 'w':
                hub_map.move_player(0, -1)
            elif key == 's':
                hub_map.move_player(0, 1)
            elif key == 'a':
                hub_map.move_player(-1, 0)
            elif key == 'd':
                hub_map.move_player(1, 0)
            elif key == 'e':
                # Check for interactions
                if hub_map.is_fishing_spot(hub_map.player_x, hub_map.player_y):
                    is_golden = hub_map.is_golden_spot(hub_map.player_x, hub_map.player_y)
                    self.fish(golden_spot=is_golden)
                elif hub_map.is_building(hub_map.player_x, hub_map.player_y):
                    building_type = hub_map.get_building_type(hub_map.player_x, hub_map.player_y)
                    new_location = self.hub_island_interaction(building_type)
                    
                    # If dock returns a location, enter that location's map
                    if new_location:
                        self.explore_remote_location(new_location)
                else:
                    hub_map.message = "Nothing to interact with here."
            elif key == 'i':
                self.view_inventory()
            elif key == 'c':
                self.view_character_stats()
            elif key == 'q':
                print(Fore.YELLOW + "\nThanks for playing! 🎣" + Style.RESET_ALL)
                break
    
    def explore_remote_location(self, location):
        """Explore a remote location (Ocean, Deep Sea, etc.)"""
        location_map = location.map
        
        while True:
            self.clear_screen()
            
            print(Fore.CYAN + f"╔═══════════════════════════════════════╗" + Style.RESET_ALL)
            print(Fore.CYAN + f"║  {location.name.center(37)}  ║" + Style.RESET_ALL)
            print(Fore.CYAN + f"╚═══════════════════════════════════════╝" + Style.RESET_ALL)
            print(Fore.YELLOW + location.description + Style.RESET_ALL)
            print()
            
            # Render the map
            for y, row in enumerate(location_map.layout):
                line = ""
                for x, tile in enumerate(row):
                    is_player = (x == location_map.player_x and y == location_map.player_y)
                    is_spot = location_map.is_fishing_spot(x, y)
                    is_golden = location_map.is_golden_spot(x, y)
                    line += location_map.render_tile(tile, is_player, is_spot, is_golden)
                print(line)
            
            print()
            print(Fore.GREEN + f"Level: {self.level} | XP: {self.xp}/{self.xp_threshold} | Money: ${self.money}" + Style.RESET_ALL)
            print(Fore.LIGHTBLACK_EX + f"Rod: {self.rod_durability}/{self.rod_max_durability} | Weather: {self.current_weather}" + Style.RESET_ALL)
            print()
            print(Fore.YELLOW + location_map.message + Style.RESET_ALL)
            print()
            print(Fore.WHITE + "[WASD] Move | [E] Fish | [Q] Return to Hub Island" + Style.RESET_ALL)
            
            # Get input
            key = get_key()
            
            if key == 'w':
                location_map.move_player(0, -1)
            elif key == 's':
                location_map.move_player(0, 1)
            elif key == 'a':
                location_map.move_player(-1, 0)
            elif key == 'd':
                location_map.move_player(1, 0)
            elif key == 'e':
                if location_map.is_fishing_spot(location_map.player_x, location_map.player_y):
                    is_golden = location_map.is_golden_spot(location_map.player_x, location_map.player_y)
                    self.fish(golden_spot=is_golden)
                else:
                    location_map.message = "You need to be at a fishing spot (⊙) to fish!"
            elif key == 'q':
                # Return to hub island
                self.current_location = LOCATIONS[0]
                break


# ===== MAIN =====
if __name__ == "__main__":
    show_intro()
    print(Fore.CYAN + "╔═══════════════════════════════════════╗" + Style.RESET_ALL)
    print(Fore.CYAN + "║       🎣 FISHING GAME 🎣              ║" + Style.RESET_ALL)
    print(Fore.CYAN + "║       Hub Island Edition              ║" + Style.RESET_ALL)
    print(Fore.CYAN + "║         V.0.5.0 BETA                  ║" + Style.RESET_ALL)
    print(Fore.CYAN + "╚═══════════════════════════════════════╝" + Style.RESET_ALL)
    print()
    print(Fore.GREEN + "1. New Game" + Style.RESET_ALL)
    print(Fore.GREEN + "2. Load Game" + Style.RESET_ALL)
    print(Fore.GREEN + "3. Exit" + Style.RESET_ALL)
    
    choice = input(Fore.CYAN + "\nChoose an option: " + Style.RESET_ALL)
    
    if choice == '1':
        name, stats, difficulty_name, difficulty_mult = create_character()
        character_data = {
            'name': name,
            'stats': stats,
            'difficulty_name': difficulty_name,
            'difficulty_mult': difficulty_mult
        }
        game = Game(character_data)
        game.start_game()
    elif choice == '2':
        game = Game()
        game.load_game()
        game.start_game()
    elif choice == '3':
        print(Fore.GREEN + "Thanks for playing! 🎣" + Style.RESET_ALL)
    elif choice == '99':  #dev mode
        print(Fore.MAGENTA + "[DEV MODE ENABLED]" + Style.RESET_ALL)
        character_data = {
            'name': 'DEV_Player',
            'stats': {'strength': 10, 'luck': 10, 'patience': 10},
            'difficulty_name': 'Easy',
            'difficulty_mult': 0.5
        }
        game = Game(character_data)
        game.money = 999999
        game.level = 50
        game.xp = 999999
        game.xp_threshold = 999999
        game.owned_rods = RODS[:]  # all rods
        game.owned_baits = BAITS[:]  # all baits
        game.current_rod = RODS[-1]
        game.current_bait = BAITS[-1]
        game.debug_mode = True
        print(Fore.LIGHTMAGENTA_EX + "All rods, baits, and locations unlocked!" + Style.RESET_ALL)
        time.sleep(1)
        game.start_game()

    else:
        print(Fore.RED + "Invalid choice." + Style.RESET_ALL)