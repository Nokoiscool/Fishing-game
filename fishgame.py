# Fishing Game - Enhanced Version (Fixed)
import os
import json
import hashlib
import platform
import time
import random
import sys
from colorama import Fore, Style, init
from datetime import datetime

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
    
    print(Fore.CYAN + intro + Style.RESET_ALL)
    time.sleep(2)
    os.system("cls")

init(autoreset=True)

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

    def catch(self):
        self.weight = self.generate_random_weight()
        self.mutation = self.assign_mutation()
        self.catch_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def assign_mutation(self):
        mutations = ["normal", "albino", "glowing", "spotted", "golden", "shadow", "magical"]
        weights = [79.99, 5, 5, 5, 3, 2, 0.01]
        return random.choices(mutations, weights=weights)[0]

    mutation_colors = {
        "normal": Fore.WHITE,
        "albino": Fore.LIGHTWHITE_EX, 
        "glowing": Fore.GREEN,
        "spotted": Fore.YELLOW,
        "golden": Fore.LIGHTYELLOW_EX,
        "shadow": Fore.LIGHTBLACK_EX,
        "magical": Fore.MAGENTA
    }

    mutation_multipliers = {
        "normal": 1.0,
        "albino": 2.0,
        "glowing": 2.5,
        "spotted": 1.5,
        "golden": 5.0,
        "shadow": 3.0,
        "magical": 10.0
    }

    def get_color(self):
        return self.mutation_colors.get(self.mutation, Fore.WHITE)

    def get_sell_price(self):
        base_price = self.sell_price
        weight_bonus = self.weight * 2
        mutation_bonus = base_price * self.mutation_multipliers.get(self.mutation, 1.0)
        return int(base_price + weight_bonus + mutation_bonus)

    def __str__(self):
        color = self.get_color()
        mutation_str = f" ({self.mutation})" if self.mutation != "normal" else ""
        return f"{color}{self.name}{mutation_str} (Weight: {self.weight:.2f} kg, Rarity: {self.rarity}, Size: {self.get_size()}){Style.RESET_ALL}"

    def get_size(self):
        if self.weight > 1000.0:
            return "Gigantic"
        elif self.weight > 100.0:
            return "Huge"
        elif self.weight > 10.0:
            return "Medium"
        else:
            return "Small"


class Bait:
    def __init__(self, name, cost, rarity_boost, description):
        self.name = name
        self.cost = cost
        self.rarity_boost = rarity_boost
        self.description = description


class Rod:
    def __init__(self, name, cost, catch_bonus, description):
        self.name = name
        self.cost = cost
        self.catch_bonus = catch_bonus
        self.description = description


class Location:
    def __init__(self, name, fish_list, unlock_level=1, weather_affects=True):
        self.name = name
        self.fish = fish_list
        self.unlock_level = unlock_level
        self.weather_affects = weather_affects

    def get_random_fish(self, weather="sunny", bait_boost=0, time_of_day="day"):
        weighted_fish = []
        for fish in self.fish:
            weight = int(fish.rarity_weight * (1 + bait_boost))
            
            # Weather effects
            if weather == "rainy":
                weight = int(weight * 1.2)
            elif weather == "stormy":
                if fish.rarity in ["Rare", "Legendary", "Mythical"]:
                    weight = int(weight * 1.5)
            
            # Time effects - NEW
            if time_of_day == "night":
                if fish.rarity in ["Rare", "Legendary"]:
                    weight = int(weight * 1.3)
            elif time_of_day == "dawn" or time_of_day == "dusk":
                if fish.rarity == "Mythical":
                    weight = int(weight * 2.0)
            
            weighted_fish.extend([fish] * max(1, weight))
        
        return random.choice(weighted_fish) if weighted_fish else None


class Esky:
    def __init__(self):
        self.fish = []
        self.max_capacity = 50

    def add_fish(self, fish):
        if len(self.fish) < self.max_capacity:
            self.fish.append(fish)
            return True
        return False

    def is_full(self):
        return len(self.fish) >= self.max_capacity


class Encyclopedia:
    def __init__(self):
        self.caught_fish = {}

    def add_fish(self, fish):
        if fish.name not in self.caught_fish:
            self.caught_fish[fish.name] = {
                'name': fish.name,
                'min_weight': fish.min_weight,
                'max_weight': fish.max_weight,
                'rarity': fish.rarity,
                'xp_reward': fish.xp_reward,
                'real_world_info': fish.real_world_info,
                'times_caught': 1,
                'heaviest': fish.weight,
                'mutations_found': [fish.mutation] if fish.mutation != "normal" else []
            }
        else:
            self.caught_fish[fish.name]['times_caught'] += 1
            if fish.weight > self.caught_fish[fish.name]['heaviest']:
                self.caught_fish[fish.name]['heaviest'] = fish.weight
            if fish.mutation != "normal" and fish.mutation not in self.caught_fish[fish.name]['mutations_found']:
                self.caught_fish[fish.name]['mutations_found'].append(fish.mutation)

    def display(self):
        if not self.caught_fish:
            print(Fore.YELLOW + "No fish caught yet! Go fishing to fill your encyclopedia." + Style.RESET_ALL)
            return
        
        print(Fore.CYAN + "=== Fishing Encyclopedia ===" + Style.RESET_ALL)
        print(Fore.CYAN + f"Total Species Caught: {len(self.caught_fish)}" + Style.RESET_ALL)
        
        for fish_name, fish_info in sorted(self.caught_fish.items()):
            print(Fore.GREEN + f"\n{fish_name}:" + Style.RESET_ALL)
            print(f"  Rarity: {fish_info['rarity']}")
            print(f"  Weight range: {fish_info['min_weight']}kg - {fish_info['max_weight']}kg")
            print(f"  Heaviest caught: {fish_info['heaviest']:.2f}kg")
            print(f"  XP reward: {fish_info['xp_reward']} XP")
            print(f"  Times caught: {fish_info['times_caught']}")
            if fish_info['mutations_found']:
                print(f"  Mutations found: {', '.join(fish_info['mutations_found'])}")
            print(f"  Info: {fish_info.get('real_world_info', 'No information available.')}")

    def get_completion_percentage(self, all_fish):
        return (len(self.caught_fish) / len(all_fish)) * 100 if all_fish else 0


# ===== FISH DATA =====
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
    Fish("Abyssal Octopus", 5.0, 15.0, "Rare", 3, 58, "Rarely seen octopus from extreme depths.", 125),
    Fish("Kraken", 5000, 10000, "Mythical", 0.001, 10000, "Legendary sea monster said to drag ships to the depths.", 200000),
    Fish("Leviathan", 20000, 100000, "Mythical", 0.0003, 15000, "Biblical sea monster of enormous power.", 300000),
    Fish("Abyssal Horror", 1000, 5000, "Mythical", 0.003, 8000, "Nameless terror from the deepest trenches.", 150000),
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
]


# ===== EQUIPMENT DATA =====
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

RODS =  [
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


def create_character():
    """Character creation at game start"""
    print(Fore.CYAN + "╔═══════════════════════════════════════╗" + Style.RESET_ALL)
    print(Fore.CYAN + "║       CHARACTER CREATION              ║" + Style.RESET_ALL)
    print(Fore.CYAN + "╚═══════════════════════════════════════╝" + Style.RESET_ALL)
    print()
    
    # Name
    name = input(Fore.GREEN + "Enter your fisherman's name: " + Style.RESET_ALL).strip()
    if not name:
        name = "Angler"
    
    print()
    print(Fore.CYAN + "Choose your starting stats (10 points to distribute):" + Style.RESET_ALL)
    print(Fore.YELLOW + "Strength: Increases fish catch rate" + Style.RESET_ALL)
    print(Fore.YELLOW + "Luck: Increases rare fish chances" + Style.RESET_ALL)
    print(Fore.YELLOW + "Patience: Easier minigames" + Style.RESET_ALL)
    print()
    
    points_remaining = 10
    stats = {'strength': 0, 'luck': 0, 'patience': 0}
    
    while points_remaining > 0:
        print(Fore.GREEN + f"\nPoints remaining: {points_remaining}" + Style.RESET_ALL)
        print(f"Current stats - Strength: {stats['strength']}, Luck: {stats['luck']}, Patience: {stats['patience']}")
        
        stat_choice = input(Fore.CYAN + "Add point to (s)trength, (l)uck, or (p)atience? " + Style.RESET_ALL).lower()
        
        if stat_choice == 's' and points_remaining > 0:
            stats['strength'] += 1
            points_remaining -= 1
        elif stat_choice == 'l' and points_remaining > 0:
            stats['luck'] += 1
            points_remaining -= 1
        elif stat_choice == 'p' and points_remaining > 0:
            stats['patience'] += 1
            points_remaining -= 1
    
    print()
    print(Fore.CYAN + "Choose difficulty:" + Style.RESET_ALL)
    print(Fore.GREEN + "1. Easy (Relaxed fishing)" + Style.RESET_ALL)
    print(Fore.YELLOW + "2. Normal (Balanced challenge)" + Style.RESET_ALL)
    print(Fore.RED + "3. Hard (True fisherman's test)" + Style.RESET_ALL)
    print(Fore.MAGENTA + "4. Legendary (For the brave)" + Style.RESET_ALL)
    
    difficulty_choice = input(Fore.CYAN + "\nChoose (1-4): " + Style.RESET_ALL)
    difficulty_map = {
        '1': ('Easy', 0.8),
        '2': ('Normal', 1.0),
        '3': ('Hard', 1.3),
        '4': ('Legendary', 1.6)
    }
    difficulty_name, difficulty_mult = difficulty_map.get(difficulty_choice, ('Normal', 1.0))
    
    print()
    print(Fore.GREEN + f"Welcome, {name}!" + Style.RESET_ALL)
    print(Fore.YELLOW + f"Stats - Strength: {stats['strength']}, Luck: {stats['luck']}, Patience: {stats['patience']}" + Style.RESET_ALL)
    print(Fore.YELLOW + f"Difficulty: {difficulty_name}" + Style.RESET_ALL)
    input(Fore.CYAN + "\nPress Enter to begin your fishing journey..." + Style.RESET_ALL)
    
    return name, stats, difficulty_name, difficulty_mult

# ===== MINI GAME =====
def reaction_minigame(difficulty_modifier=1.0):
    """Fast-paced reaction time game - NOW HARDER WITH DIFFICULTY"""
    print(Fore.YELLOW + "Get ready... Wait for the signal!" + Style.RESET_ALL)
    time_to_wait = random.uniform(1.5, 4.0)
    time.sleep(time_to_wait)
    
    print(Fore.GREEN + ">>> NOW! Press Enter!" + Style.RESET_ALL)
    start_time = time.time()
    
    try:
        input()
        reaction_time = time.time() - start_time
    except:
        reaction_time = 999
    
    # Harder difficulty = stricter timing windows
    target_time = 0.8 * difficulty_modifier  # Base time affected by difficulty
    good_time = target_time * 1.5
    
    if reaction_time < target_time:
        print(Fore.GREEN + f"Perfect! ({reaction_time:.3f}s)" + Style.RESET_ALL)
        return True
    elif reaction_time < good_time:
        print(Fore.YELLOW + f"Good! ({reaction_time:.3f}s)" + Style.RESET_ALL)
        return True
    else:
        print(Fore.RED + f"Too slow! ({reaction_time:.3f}s) [Target: <{good_time:.2f}s]" + Style.RESET_ALL)
        return False


def sequence_minigame(difficulty_modifier=1.0):
    """Memory sequence game - NOW HARDER WITH DIFFICULTY"""
    # Difficulty increases sequence length
    base_length = 3
    sequence_length = int(base_length + (difficulty_modifier * 1.5))
    
    symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    sequence = [random.choice(symbols) for _ in range(sequence_length)]
    
    print(Fore.CYAN + "Memorize this sequence:" + Style.RESET_ALL)
    print(Fore.YELLOW + " ".join(sequence) + Style.RESET_ALL)
    
    # Less time to memorize on higher difficulty
    memorize_time = max(1.5, 2.5 - (difficulty_modifier * 0.3))
    time.sleep(memorize_time + sequence_length * 0.25)
    
    print("\n" * 50)
    print(Fore.CYAN + "Enter the sequence (separate with spaces):" + Style.RESET_ALL)
    print(Fore.YELLOW + f"[{sequence_length} items to remember]" + Style.RESET_ALL)
    user_input = input(Fore.GREEN + "> " + Style.RESET_ALL).strip().upper().split()
    
    if user_input == sequence:
        print(Fore.GREEN + "Perfect memory!" + Style.RESET_ALL)
        return True
    else:
        print(Fore.RED + f"Wrong! It was: {' '.join(sequence)}" + Style.RESET_ALL)
        return False


def pattern_minigame(difficulty_modifier=1.0):
    """Pattern matching game - NOW HARDER WITH DIFFICULTY"""
    # Difficulty increases pattern length and speed
    base_length = 4
    length = int(base_length + (difficulty_modifier * 1.2))
    pattern = ''.join(random.choices(['L', 'R'], k=length))
    
    print(Fore.CYAN + "The fish is moving! Follow the pattern:" + Style.RESET_ALL)
    print(Fore.YELLOW + "Watch carefully..." + Style.RESET_ALL)
    time.sleep(0.8)
    
    # Display speed increases with difficulty
    display_speed = max(0.2, 0.5 - (difficulty_modifier * 0.08))
    
    for char in pattern:
        direction = "LEFT" if char == 'L' else "RIGHT"
        print(Fore.YELLOW + f"  {direction}" + Style.RESET_ALL)
        time.sleep(display_speed)
    
    time.sleep(0.3)
    print("\n" * 50)
    
    print(Fore.CYAN + f"\nEnter the pattern ({length} moves - L for left, R for right, no spaces):" + Style.RESET_ALL)
    print(Fore.CYAN + "Example: LRRL" + Style.RESET_ALL)
    user_input = input(Fore.GREEN + "> " + Style.RESET_ALL).strip().upper()
    
    if user_input == pattern:
        print(Fore.GREEN + "You followed perfectly!" + Style.RESET_ALL)
        return True
    else:
        print(Fore.RED + f"Wrong! Pattern was: {pattern}" + Style.RESET_ALL)
        return False
    
def fishing_mini_game(difficulty_modifier=1.0, fish_name=""):
    """Main fishing minigame - randomly selects one of the minigames"""
    print(Fore.YELLOW + f"You hooked a {fish_name}!" + Style.RESET_ALL)
    time.sleep(0.5)
    
    minigames = [reaction_minigame, sequence_minigame, pattern_minigame]
    selected_game = random.choice(minigames)
    
    success = selected_game(difficulty_modifier)
    
    if not success:
        input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)
    
    return success

# ===== GAME CLASS =====
class Game:
    def __init__(self, character_data=None):
        lake = Location("Lake", lake_fish, unlock_level=1)
        ocean = Location("Ocean", ocean_fish, unlock_level=3)
        river = Location("River", river_fish, unlock_level=2)
        deep_sea = Location("Deep Sea", deep_sea_fish, unlock_level=5)
        volcanic_lake = Location("Volcanic Lake", volcanic_lake_fish, unlock_level=7)
        arctic = Location("Arctic", arctic_fish, unlock_level=9)
        space = Location("Space", space_fish, unlock_level=12)

        self.locations = [lake, river, ocean, deep_sea, volcanic_lake, arctic, space]
        self.esky = Esky()
        self.level = 1
        self.xp = 0
        self.xp_threshold = 100
        self.money = 100
        self.encyclopedia = Encyclopedia()
        
        # NEW FEATURES - Initialize BEFORE character_data
        self.skill_points = 0
        self.skills = {
            'rare_finder': 0,
            'quick_reflexes': 0,
            'master_angler': 0,
            'lucky_fisherman': 0,
            'bargain_hunter': 0,
            'iron_grip': 0,
        }
        self.rod_durability = 100
        self.rod_max_durability = 100
        self.time_of_day = "day"
        self.time_counter = 0
        self.trophy_room = []
        self.active_quests = []
        self.completed_quests = 0
        
        # Character data (existing code continues...)
        if character_data:
            self.player_name = character_data['name']
            self.stats = character_data['stats']
            self.difficulty_name = character_data['difficulty_name']
            self.difficulty_mult = character_data['difficulty_mult']
        else:
            self.player_name = "Angler"
            self.stats = {'strength': 3, 'luck': 3, 'patience': 4}
            self.difficulty_name = "Normal"
            self.difficulty_mult = 1.0
            # Skill tree
            self.skill_points = 0
            self.skills = {
                'rare_finder': 0,  # Max 5: +2% rare chance per level
                'quick_reflexes': 0,  # Max 5: -5% minigame difficulty per level
                'master_angler': 0,  # Max 5: +5% catch rate per level
                'lucky_fisherman': 0,  # Max 5: +10% mutation chance per level
                'bargain_hunter': 0,  # Max 3: +10% sell price per level
                'iron_grip': 0,  # Max 3: +15% XP gain per level
            }
        
        self.current_rod = RODS[0]
        self.current_bait = BAITS[0]
        self.owned_rods = [RODS[0]]
        self.owned_baits = [BAITS[0]]
        
        self.weather = self.generate_weather()
        self.weather_changes = 0
        
        # Achievements
        self.achievements = {
            'first_catch': False,
            'first_rare': False,
            'first_legendary': False,
            'first_mythical': False,
            'fisherman': False,
            'master_fisherman': False,
            'millionaire': False,
            'mutation_hunter': False,
            'encyclopedia_25': False,
            'encyclopedia_50': False,
            'encyclopedia_100': False,
        }
        
        # Setup save directory
        documents_directory = os.path.join(os.path.expanduser("~"), "Documents")
        self.game_folder = os.path.join(documents_directory, 'FiskeSpill')
        os.makedirs(self.game_folder, exist_ok=True)

    def generate_weather(self):
        weathers = ["sunny", "cloudy", "rainy", "stormy"]
        weights = [50, 30, 15, 5]
        return random.choices(weathers, weights=weights)[0]

    def advance_time(self):
        self.time_counter += 1
        if self.time_counter >= 5:  # Change time every 5 fishing attempts
            self.time_counter = 0
            times = ["dawn", "day", "dusk", "night"]
            current_idx = times.index(self.time_of_day)
            self.time_of_day = times[(current_idx + 1) % 4]
            
            time_colors = {"dawn": Fore.LIGHTYELLOW_EX, "day": Fore.YELLOW, 
                        "dusk": Fore.LIGHTMAGENTA_EX, "night": Fore.BLUE}
            color = time_colors.get(self.time_of_day, Fore.WHITE)
            print(color + f"🌅 Time changed to: {self.time_of_day.upper()}" + Style.RESET_ALL)
            time.sleep(1)

    def check_achievements(self):
        total_caught = sum(info['times_caught'] for info in self.encyclopedia.caught_fish.values())
        
        if total_caught >= 1 and not self.achievements['first_catch']:
            self.achievements['first_catch'] = True
            print(Fore.LIGHTCYAN_EX + "🏆 Achievement Unlocked: First Catch!" + Style.RESET_ALL)
        
        if total_caught >= 50 and not self.achievements['fisherman']:
            self.achievements['fisherman'] = True
            print(Fore.LIGHTCYAN_EX + "🏆 Achievement Unlocked: Fisherman (50 fish caught)!" + Style.RESET_ALL)
            self.money += 500
        
        if total_caught >= 200 and not self.achievements['master_fisherman']:
            self.achievements['master_fisherman'] = True
            print(Fore.LIGHTCYAN_EX + "🏆 Achievement Unlocked: Master Fisherman (200 fish caught)!" + Style.RESET_ALL)
            self.money += 2000
        
        if self.money >= 1000000 and not self.achievements['millionaire']:
            self.achievements['millionaire'] = True
            print(Fore.LIGHTCYAN_EX + "🏆 Achievement Unlocked: Millionaire!" + Style.RESET_ALL)
        
        species_count = len(self.encyclopedia.caught_fish)
        if species_count >= 10 and not self.achievements['encyclopedia_25']:
            self.achievements['encyclopedia_25'] = True
            print(Fore.LIGHTCYAN_EX + "🏆 Achievement Unlocked: Encyclopedia 25% Complete!" + Style.RESET_ALL)

    def clear_screen(self):
        os.system('cls' if platform.system() == 'Windows' else 'clear')

    def start_game(self):
        """Main game loop"""
        self.clear_screen()
        while True:
            self.display_menu()

    def print_header(self):
        # Calculate padding needed for the name
        name_text = f"🎣 {self.player_name}'s FISHING GAME 🎣"
        # Minimum width for aesthetics
        min_width = 47
        # Calculate required width based on name length
        content_width = len(name_text) + 8  # 8 for spacing (4 on each side)
        box_width = max(min_width, content_width)
        
        # Create the border
        top_border = "╔" + "═" * box_width + "╗"
        bottom_border = "╚" + "═" * box_width + "╝"
        
        # Center the name text
        padding = (box_width - len(name_text)) // 2
        right_padding = box_width - padding - len(name_text)
        content_line = "║" + " " * padding + name_text + " " * right_padding + "║"
        
        # Print with colors
        print(Fore.CYAN + top_border + Style.RESET_ALL)
        print(Fore.CYAN + content_line + Style.RESET_ALL)
        print(Fore.CYAN + bottom_border + Style.RESET_ALL)

    def display_menu(self):
        while True:
            self.clear_screen()
            
            weather_colors = {
                "sunny": Fore.YELLOW,
                "cloudy": Fore.LIGHTBLACK_EX,
                "rainy": Fore.BLUE,
                "stormy": Fore.RED
            }
            weather_color = weather_colors.get(self.weather, Fore.WHITE)
            
            self.print_header()
            print(Fore.YELLOW + f"Level: {self.level} | XP: {self.xp}/{self.xp_threshold} | 💰: ${self.money}" + Style.RESET_ALL)
            print(weather_color + f"Weather: {self.weather.capitalize()}" + Style.RESET_ALL)
            print(Fore.MAGENTA + f"Difficulty: {self.difficulty_name}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Rod: {self.current_rod.name} | Bait: {self.current_bait.name}" + Style.RESET_ALL)
            print(Fore.MAGENTA + f"Esky: {len(self.esky.fish)}/{self.esky.max_capacity}" + Style.RESET_ALL)
            print()
            print(Fore.YELLOW + "1. Fish" + Style.RESET_ALL)
            print(Fore.YELLOW + "2. View Inventory" + Style.RESET_ALL)
            print(Fore.YELLOW + "3. Sell Fish" + Style.RESET_ALL)
            print(Fore.YELLOW + "4. Shop" + Style.RESET_ALL)
            print(Fore.YELLOW + "5. View Encyclopedia" + Style.RESET_ALL)
            print(Fore.YELLOW + "6. Quests" + Style.RESET_ALL)
            print(Fore.YELLOW + "7. Trophy Room" + Style.RESET_ALL)
            print(Fore.YELLOW + "8. View Achievements" + Style.RESET_ALL)
            print(Fore.YELLOW + "9. Stats" + Style.RESET_ALL)
            print(Fore.YELLOW + "10. Skill Tree" + Style.RESET_ALL)
            print(Fore.CYAN + "----------------------------------------" + Style.RESET_ALL)
            print(Fore.YELLOW + "11. Save Game" + Style.RESET_ALL)
            print(Fore.YELLOW + "12. Load Game" + Style.RESET_ALL)
            print(Fore.YELLOW + "13. Exit" + Style.RESET_ALL)

            menu_actions = {
                '1': self.choose_location,
                '2': self.view_inventory,
                '3': self.sell_fish_menu,
                '4': self.shop_menu,
                '5': lambda: (self.clear_screen(), self.encyclopedia.display(), input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)),
                '6': self.quest_menu,  # NEW
                '7': self.trophy_room_menu,  # was 6
                '8': self.view_achievements,  # was 7
                '9': self.view_stats,  # was 8
                '10': self.skill_tree_menu,  # was 9
                '11': lambda: (self.save_game(), print(Fore.GREEN + "Game saved successfully!" + Style.RESET_ALL), input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)),  # was 10
                '12': lambda: (self.load_game(), print(Fore.GREEN + "Game loaded successfully!" + Style.RESET_ALL), input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)),  # was 11
                '13': lambda: (print(Fore.GREEN + "Thanks for playing! 🎣" + Style.RESET_ALL), sys.exit()),  # was 12
            }
            # Add debug menu conditionally
            if getattr(self, 'debug_mode', False):
                menu_actions['99'] = self.debug_menu
            
            choice = input(Fore.GREEN + "Choose an option: " + Style.RESET_ALL)
            if choice in menu_actions:
                menu_actions[choice]()
            else:
                print(Fore.RED + "Invalid choice. Please select a valid option." + Style.RESET_ALL)
                input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)
    def add_xp(self, amount):
    # Apply difficulty multiplier to XP (harder = more XP)
        difficulty_bonus = self.difficulty_mult  # 0.8x for Easy, 1.6x for Legendary
        skill_bonus = (1 + self.skills['iron_grip'] * 0.15)
        
        amount = int(amount * difficulty_bonus * skill_bonus)
        self.xp += amount
        
        # Show bonus indicator for hard difficulties
        if self.difficulty_mult > 1.0:
            bonus_pct = int((self.difficulty_mult - 1.0) * 100)
            print(Fore.LIGHTGREEN_EX + f"You gained {amount} XP! (+{bonus_pct}% difficulty bonus)" + Style.RESET_ALL)
        else:
            print(Fore.LIGHTGREEN_EX + f"You gained {amount} XP!" + Style.RESET_ALL)
        
        while self.xp >= self.xp_threshold:
            self.xp -= self.xp_threshold
            self.level_up()

    def save_game(self):
        save_path = os.path.join(self.game_folder, "game_save.json")
        game_data = {
            'level': self.level,
            'xp': self.xp,
            'xp_threshold': self.xp_threshold,
            'money': self.money,
            'player_name': self.player_name,
            'stats': self.stats,
            'difficulty_name': self.difficulty_name,
            'difficulty_mult': self.difficulty_mult,
            'weather': self.weather,
            'achievements': self.achievements,
            'skill_points': self.skill_points,
            'skills': self.skills,
            'rod_durability': self.rod_durability,
            'rod_max_durability': self.rod_max_durability,
            'time_of_day': self.time_of_day,
            'time_counter': self.time_counter,
            'trophy_room': self.trophy_room,
            'active_quests': self.active_quests,
            'completed_quests': self.completed_quests,
            'encyclopedia': self.encyclopedia.caught_fish,
            'current_rod': self.current_rod.name,
            'current_bait': self.current_bait.name,
            'owned_rods': [rod.name for rod in self.owned_rods],
            'owned_baits': [bait.name for bait in self.owned_baits],
            'fish': [fish.to_dict() for fish in self.esky.fish]
        }
    
        with open(save_path, "w") as f:
            json.dump({'data': game_data}, f, indent=4)
    
    def load_game(self):
        load_path = os.path.join(self.game_folder, "game_save.json")
        try:
            with open(load_path, "r") as f:
                saved_data = json.load(f)
                game_data = saved_data['data']
                
                self.level = game_data['level']
                self.xp = game_data['xp']
                self.xp_threshold = game_data['xp_threshold']
                self.money = game_data.get('money', 100)
                self.player_name = game_data.get('player_name', 'Angler')
                self.stats = game_data.get('stats', {'strength': 3, 'luck': 3, 'patience': 4})
                self.difficulty_name = game_data.get('difficulty_name', 'Normal')
                self.difficulty_mult = game_data.get('difficulty_mult', 1.0)
                self.weather = game_data.get('weather', 'sunny')
                self.achievements = game_data.get('achievements', self.achievements)
                
                # NEW FEATURES - Use .get(d) with defaults for backwards compatibility
                self.skill_points = game_data.get('skill_points', 0)
                self.skills = game_data.get('skills', {
                    'rare_finder': 0,
                    'quick_reflexes': 0,
                    'master_angler': 0,
                    'lucky_fisherman': 0,
                    'bargain_hunter': 0,
                    'iron_grip': 0,
                })
                self.rod_durability = game_data.get('rod_durability', 100)
                self.rod_max_durability = game_data.get('rod_max_durability', 100)
                self.time_of_day = game_data.get('time_of_day', 'day')
                self.time_counter = game_data.get('time_counter', 0)
                self.trophy_room = game_data.get('trophy_room', [])
                self.active_quests = game_data.get('active_quests', [])
                self.completed_quests = game_data.get('completed_quests', 0)
                # Load encyclopedia
                self.encyclopedia.caught_fish = game_data.get('encyclopedia', {})
                
                # Load equipment
                rod_name = game_data.get('current_rod', 'Bamboo Rod')
                self.current_rod = next((r for r in RODS if r.name == rod_name), RODS[0])
                
                bait_name = game_data.get('current_bait', 'Worm')
                self.current_bait = next((b for b in BAITS if b.name == bait_name), BAITS[0])
                
                owned_rod_names = game_data.get('owned_rods', ['Bamboo Rod'])
                self.owned_rods = [r for r in RODS if r.name in owned_rod_names]
                
                owned_bait_names = game_data.get('owned_baits', ['Worm'])
                self.owned_baits = [b for b in BAITS if b.name in owned_bait_names]
                
                # Load fish
                self.esky.fish = []
                for fish_data in game_data.get('fish', []):
                    fish = Fish(
                        fish_data['name'],
                        fish_data['min_weight'],
                        fish_data['max_weight'],
                        fish_data['rarity'],
                        fish_data['rarity_weight'],
                        fish_data['xp_reward'],
                        fish_data.get('real_world_info', ""),
                        fish_data.get('sell_price', 10)
                    )
                    fish.weight = fish_data['weight']
                    fish.mutation = fish_data['mutation']
                    fish.catch_time = fish_data.get('catch_time')
                    self.esky.fish.append(fish)
                
                print(Fore.GREEN + "Game loaded successfully!" + Style.RESET_ALL)
        except FileNotFoundError:
            print(Fore.RED + "No saved game found." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error loading game: {e}" + Style.RESET_ALL)

    def choose_location(self):
        self.clear_screen()
        print(Fore.CYAN + "Choose a location to fish:" + Style.RESET_ALL)
        
        available_locations = []
        for i, location in enumerate(self.locations, start=1):
            if self.level >= location.unlock_level:
                print(Fore.GREEN + f"{i}: {location.name} (Unlocked)" + Style.RESET_ALL)
                available_locations.append(i-1)
            else:
                print(Fore.RED + f"{i}: {location.name} (Unlock at level {location.unlock_level})" + Style.RESET_ALL)
        
        choice = input(Fore.GREEN + "\nEnter the number of your choice: " + Style.RESET_ALL)
        try:
            location_index = int(choice) - 1
            if location_index in available_locations:
                self.fish(self.locations[location_index])
            else:
                print(Fore.RED + "Location locked or invalid choice." + Style.RESET_ALL)
                input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Please enter a valid number." + Style.RESET_ALL)
            input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)

    def fish(self, location):
        if self.esky.is_full():
            print(Fore.RED + "Your esky is full! Sell some fish first." + Style.RESET_ALL)
            input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)
            return
        
        # Weather might change
        if random.random() < 0.15:
            self.weather = self.generate_weather()
            print(Fore.CYAN + f"The weather changed to {self.weather}!" + Style.RESET_ALL)
            time.sleep(1)
        
        # Get the fish template first
        fish_template = location.get_random_fish(self.weather, self.current_bait.rarity_boost, self.time_of_day)
        if not fish_template:
            print(Fore.RED + "No fish were available to catch!" + Style.RESET_ALL)
            input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)
            return
        
        # Calculate difficulty based on multiple factors
        rarity_difficulty = {
            "Common": 1.0,
            "Uncommon": 1.3,
            "Rare": 1.6,
            "Legendary": 2.0,
            "Mythical": 2.5
        }
        
        base_difficulty = 1 + (self.level * 0.05)  # Scales with level
        fish_difficulty = rarity_difficulty.get(fish_template.rarity, 1.0)
        player_difficulty = self.difficulty_mult
        patience_reduction = (1 - self.stats['patience'] * 0.03)  # Max 30% reduction
        skill_reduction = (1 - self.skills.get('quick_reflexes', 0) * 0.05)  # Max 25% reduction
        
        # Combined difficulty
        total_difficulty = base_difficulty * fish_difficulty * player_difficulty * patience_reduction * skill_reduction
        
        success_chance = self.current_rod.catch_bonus * (1 + self.stats['strength'] * 0.02)
        success_chance *= (1 + self.skills.get('master_angler', 0) * 0.05)
        
        if random.random() > success_chance:
            print(Fore.RED + "The fish got away before you could react!" + Style.RESET_ALL)
            input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)
            return
        
        # Create a NEW instance of the fish
        caught_fish = Fish(
            fish_template.name,
            fish_template.min_weight,
            fish_template.max_weight,
            fish_template.rarity,
            fish_template.rarity_weight,
            fish_template.xp_reward,
            fish_template.real_world_info,
            fish_template.sell_price
        )
        
        # Pass the calculated difficulty to minigame
        if fishing_mini_game(total_difficulty, caught_fish.name):
            caught_fish.catch()
            self.esky.add_fish(caught_fish)
            self.encyclopedia.add_fish(caught_fish)
            print(Fore.GREEN + f"Caught: {caught_fish}" + Style.RESET_ALL)
            print(Fore.LIGHTGREEN_EX + f"Sell value: ${caught_fish.get_sell_price()}" + Style.RESET_ALL)
            self.add_xp(caught_fish.xp_reward)
            
            # Achievement checks
            if caught_fish.rarity == "Rare" and not self.achievements['first_rare']:
                self.achievements['first_rare'] = True
                print(Fore.LIGHTCYAN_EX + "🏆 Achievement Unlocked: First Rare Fish!" + Style.RESET_ALL)
            elif caught_fish.rarity == "Legendary" and not self.achievements['first_legendary']:
                self.achievements['first_legendary'] = True
                print(Fore.LIGHTCYAN_EX + "🏆 Achievement Unlocked: First Legendary Fish!" + Style.RESET_ALL)
            elif caught_fish.rarity == "Mythical" and not self.achievements['first_mythical']:
                self.achievements['first_mythical'] = True
                print(Fore.LIGHTCYAN_EX + "🏆 Achievement Unlocked: First Mythical Fish!" + Style.RESET_ALL)
            
            self.check_achievements()
        else:
            print(Fore.RED + "The fish escaped during the struggle!" + Style.RESET_ALL)
        
        # Rod durability
        durability_loss = random.randint(1, 3)
        self.rod_durability = max(0, self.rod_durability - durability_loss)
        if self.rod_durability < 20:
            print(Fore.RED + f"⚠️ Rod condition low: {self.rod_durability}%" + Style.RESET_ALL)
        if self.rod_durability == 0:
            print(Fore.RED + "💥 Your rod broke! Reverting to Bamboo Rod." + Style.RESET_ALL)
            self.current_rod = RODS[0]
            self.rod_durability = 100
        
        input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)

    def debug_menu(self):
        while True:
            self.clear_screen()
            print(Fore.MAGENTA + "=== DEBUG MENU ===" + Style.RESET_ALL)
            print("1. Add $10,000")
            print("2. Level up instantly")
            print("3. Spawn random fish")
            print("4. Change weather")
            print("5. Unlock all achievements")
            print("6. Back to main menu")
            choice = input(Fore.CYAN + "\nChoose: " + Style.RESET_ALL)

            if choice == '1':
                self.money += 10000
                print(Fore.GREEN + "Added $10,000" + Style.RESET_ALL)
            elif choice == '2':
                self.level_up()
            elif choice == '3':
                loc = random.choice(self.locations)
                fish = random.choice(loc.fish)
                caught = Fish(
                    fish.name, fish.min_weight, fish.max_weight,
                    fish.rarity, fish.rarity_weight, fish.xp_reward,
                    fish.real_world_info, fish.sell_price
                )
                caught.catch()
                self.esky.add_fish(caught)
                self.encyclopedia.add_fish(caught)
                print(Fore.GREEN + f"Spawned {caught.name} ({caught.weight}kg)" + Style.RESET_ALL)
            elif choice == '4':
                self.weather = random.choice(["sunny", "cloudy", "rainy", "stormy"])
                print(Fore.YELLOW + f"Weather changed to {self.weather}" + Style.RESET_ALL)
            elif choice == '5':
                for key in self.achievements.keys():
                    self.achievements[key] = True
                print(Fore.LIGHTCYAN_EX + "All achievements unlocked!" + Style.RESET_ALL)
            elif choice == '6':
                break

            input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)

    
    def view_inventory(self):
        self.clear_screen()
        print(Fore.CYAN + "╔═════════════════════════════════════╗" + Style.RESET_ALL)
        print(Fore.CYAN + "║         YOUR INVENTORY              ║" + Style.RESET_ALL)
        print(Fore.CYAN + "╚═════════════════════════════════════╝" + Style.RESET_ALL)
        
        if not self.esky.fish:
            print(Fore.YELLOW + "Your inventory is empty. Go catch some fish!" + Style.RESET_ALL)
        else:
            total_weight = 0
            total_value = 0
            
            # Sort fish by rarity
            rarity_order = {"Mythical": 0, "Legendary": 1, "Rare": 2, "Uncommon": 3, "Common": 4}
            sorted_fish = sorted(self.esky.fish, key=lambda f: (rarity_order.get(f.rarity, 5), f.name))
            
            for i, fish in enumerate(sorted_fish, 1):
                color = fish.get_color()
                mutation_info = f" ({fish.mutation})" if fish.mutation != "normal" else ""
                sell_price = fish.get_sell_price()
                print(f"{i}. {color}{fish.name}{mutation_info}{Style.RESET_ALL} - {fish.weight:.2f}kg - ${sell_price}")
                total_weight += fish.weight
                total_value += sell_price
            
            print(Fore.GREEN + f"\nTotal Fish: {len(self.esky.fish)}/{self.esky.max_capacity}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Total Weight: {total_weight:.2f} kg" + Style.RESET_ALL)
            print(Fore.GREEN + f"Total Value: ${total_value}" + Style.RESET_ALL)
        
        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)

    def quest_menu(self):
        self.clear_screen()
        print(Fore.CYAN + "╔═══════════════════════════════════╗" + Style.RESET_ALL)
        print(Fore.CYAN + "║            QUESTS                 ║" + Style.RESET_ALL)
        print(Fore.CYAN + "╚═══════════════════════════════════╝" + Style.RESET_ALL)
        print(Fore.YELLOW + f"Completed Quests: {self.completed_quests}" + Style.RESET_ALL)
        print()
        
        if not self.active_quests:
            print(Fore.GREEN + "No active quests. Generating new quest..." + Style.RESET_ALL)
            self.active_quests.append(self.generate_quest())
        
        for i, quest in enumerate(self.active_quests, 1):
            if quest['type'] == 'catch_species':
                print(f"{i}. Catch a {quest['target']} ({quest['progress']}/{quest['goal']}) - Reward: ${quest['reward']}")
            elif quest['type'] == 'catch_weight':
                print(f"{i}. Catch a fish weighing {quest['target']}kg+ ({quest['progress']}/{quest['goal']}) - Reward: ${quest['reward']}")
            elif quest['type'] == 'catch_rarity':
                print(f"{i}. Catch {quest['goal']} {quest['target']} fish ({quest['progress']}/{quest['goal']}) - Reward: ${quest['reward']}")
        
        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)

        def check_quest_completion(self, caught_fish):
            """Check if any active quests were completed"""
            completed = []
            
            for quest in self.active_quests:
                if quest['type'] == 'catch_species':
                    if caught_fish.name == quest['target']:
                        quest['progress'] += 1
                        if quest['progress'] >= quest['goal']:
                            completed.append(quest)
                elif quest['type'] == 'catch_weight':
                    if caught_fish.weight >= quest['target']:
                        quest['progress'] += 1
                        if quest['progress'] >= quest['goal']:
                            completed.append(quest)
                elif quest['type'] == 'catch_rarity':
                    if caught_fish.rarity == quest['target']:
                        quest['progress'] += 1
                        if quest['progress'] >= quest['goal']:
                            completed.append(quest)
            
            for quest in completed:
                self.money += quest['reward']
                self.completed_quests += 1
                self.active_quests.remove(quest)
                print(Fore.LIGHTCYAN_EX + f"🎉 Quest Completed! Earned ${quest['reward']}" + Style.RESET_ALL)
                # Generate new quest
                self.active_quests.append(self.generate_quest())

    def generate_quest(self):
        """Generate a random quest"""
        all_fish_names = []
        for location in self.locations:
            for fish in location.fish:
                all_fish_names.append(fish.name)
        
        quest_types = [
            {
                "type": "catch_species", 
                "target": random.choice(all_fish_names), 
                "reward": 500,
                "progress": 0,
                "goal": 1
            },
            {
                "type": "catch_weight", 
                "target": random.randint(10, 100), 
                "reward": 300,
                "progress": 0,
                "goal": 1
            },
            {
                "type": "catch_rarity", 
                "target": random.choice(["Rare", "Legendary"]), 
                "count": random.randint(1, 3), 
                "reward": 800,
                "progress": 0,
                "goal": random.randint(1, 3)
            },
        ]
        return random.choice(quest_types)

    def trophy_room_menu(self):
        self.clear_screen()
        print(Fore.CYAN + "╔═══════════════════════════════════╗" + Style.RESET_ALL)
        print(Fore.CYAN + "║         TROPHY ROOM               ║" + Style.RESET_ALL)
        print(Fore.CYAN + "╚═══════════════════════════════════╝" + Style.RESET_ALL)
        
        if not self.trophy_room:
            print(Fore.YELLOW + "No trophies yet! Catch memorable fish to display them here." + Style.RESET_ALL)
        else:
            for i, trophy in enumerate(self.trophy_room, 1):
                mutation_str = f" ({trophy['mutation']})" if trophy['mutation'] != "normal" else ""
                print(Fore.GREEN + f"{i}. {trophy['name']}{mutation_str}" + Style.RESET_ALL)
                print(f"   Weight: {trophy['weight']:.2f}kg | Caught: {trophy['date']}")
        
        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)

    def sell_fish_menu(self):
        while True:
            self.clear_screen()
            print(Fore.CYAN + "╔═════════════════════════════════════╗" + Style.RESET_ALL)
            print(Fore.CYAN + "║           FISH MARKET               ║" + Style.RESET_ALL)
            print(Fore.CYAN + "╚═════════════════════════════════════╝" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Current Money: ${self.money}" + Style.RESET_ALL)
            print()
            
            if not self.esky.fish:
                print(Fore.RED + "No fish to sell!" + Style.RESET_ALL)
                input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)
                return
            
            print(Fore.GREEN + "1. Sell all fish" + Style.RESET_ALL)
            print(Fore.GREEN + "2. Sell by rarity" + Style.RESET_ALL)
            print(Fore.GREEN + "3. Sell individual fish" + Style.RESET_ALL)
            print(Fore.GREEN + "4. Back to menu" + Style.RESET_ALL)
            
            choice = input(Fore.CYAN + "\nChoose an option: " + Style.RESET_ALL)
            
            if choice == '1':
                total = sum(fish.get_sell_price() for fish in self.esky.fish)
                count = len(self.esky.fish)
                self.money += total
                self.esky.fish = []
                print(Fore.GREEN + f"Sold {count} fish for ${total}!" + Style.RESET_ALL)
                input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)
                return
            elif choice == '2':
                self.sell_by_rarity()
            elif choice == '3':
                self.sell_individual()
            elif choice == '4':
                return

    def sell_by_rarity(self):
        self.clear_screen()
        print(Fore.CYAN + "Sell fish by rarity:" + Style.RESET_ALL)
        rarities = ["Common", "Uncommon", "Rare", "Legendary", "Mythical"]
        
        for i, rarity in enumerate(rarities, 1):
            fish_of_rarity = [f for f in self.esky.fish if f.rarity == rarity]
            value = sum(f.get_sell_price() for f in fish_of_rarity)
            print(f"{i}. {rarity}: {len(fish_of_rarity)} fish (${value})")
        
        print("6. Cancel")
        
        choice = input(Fore.CYAN + "\nChoose rarity to sell: " + Style.RESET_ALL)
        try:
            idx = int(choice) - 1
            if 0 <= idx < 5:
                target_rarity = rarities[idx]
                fish_to_sell = [f for f in self.esky.fish if f.rarity == target_rarity]
                if fish_to_sell:
                    total = sum(f.get_sell_price() for f in fish_to_sell)
                    self.money += total
                    self.esky.fish = [f for f in self.esky.fish if f.rarity != target_rarity]
                    print(Fore.GREEN + f"Sold {len(fish_to_sell)} {target_rarity} fish for ${total}!" + Style.RESET_ALL)
                else:
                    print(Fore.RED + f"No {target_rarity} fish to sell!" + Style.RESET_ALL)
                input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)
        except ValueError:
            pass

    def sell_individual(self):
        while True:
            self.clear_screen()
            print(Fore.CYAN + "Select fish to sell (0 to cancel):" + Style.RESET_ALL)
            
            for i, fish in enumerate(self.esky.fish, 1):
                color = fish.get_color()
                mutation_info = f" ({fish.mutation})" if fish.mutation != "normal" else ""
                print(f"{i}. {color}{fish.name}{mutation_info}{Style.RESET_ALL} - {fish.weight:.2f}kg - ${fish.get_sell_price()}")
            
            keep = input(Fore.CYAN + "Add to trophy room before selling? (y/n): " + Style.RESET_ALL)
            if keep.lower() == 'y':
                self.trophy_room.append({
                    'name': fish.name,
                    'weight': fish.weight,
                    'mutation': fish.mutation,
                    'date': fish.catch_time or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
            print(Fore.LIGHTCYAN_EX + "🏆 Added to trophy room!" + Style.RESET_ALL)
            choice = input(Fore.CYAN + "\nEnter fish number: " + Style.RESET_ALL)
            try:
                idx = int(choice)
                if idx == 0:
                    return
                if 1 <= idx <= len(self.esky.fish):
                    fish = self.esky.fish[idx - 1]
                    price = fish.get_sell_price()
                    self.money += price
                    self.esky.fish.pop(idx - 1)
                    print(Fore.GREEN + f"Sold {fish.name} for ${price}!" + Style.RESET_ALL)
                    input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)
                    if not self.esky.fish:
                        return
            except ValueError:
                pass

    def shop_menu(self):
        while True:
            self.clear_screen()
            print(Fore.CYAN + "╔═════════════════════════════════════╗" + Style.RESET_ALL)
            print(Fore.CYAN + "║          FISHING SHOP               ║" + Style.RESET_ALL)
            print(Fore.CYAN + "╚═════════════════════════════════════╝" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Money: ${self.money}" + Style.RESET_ALL)
            print()
            print(Fore.GREEN + "1. Buy Rods" + Style.RESET_ALL)
            print(Fore.GREEN + "2. Buy Bait" + Style.RESET_ALL)
            print(Fore.GREEN + "3. Upgrade Esky Capacity" + Style.RESET_ALL)
            print(Fore.GREEN + "4. Repair Rod" + Style.RESET_ALL)
            print(Fore.GREEN + "5. Back" + Style.RESET_ALL)
            
            choice = input(Fore.CYAN + "\nChoose an option: " + Style.RESET_ALL)
            
            if choice == '1':
                self.buy_rods()
            elif choice == '2':
                self.buy_bait()
            elif choice == '3':
                self.upgrade_esky()
            elif choice == '4':
                self.repair_rod()
                input(Fore.YELLOW + "Press Enter..." + Style.RESET_ALL)
            elif choice == '5':
                return

    def buy_rods(self):
        self.clear_screen()
        print(Fore.CYAN + "╔═════════════════════════════════════╗" + Style.RESET_ALL)
        print(Fore.CYAN + "║            ROD SHOP                 ║" + Style.RESET_ALL)
        print(Fore.CYAN + "╚═════════════════════════════════════╝" + Style.RESET_ALL)
        print(Fore.YELLOW + f"Money: ${self.money}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Current: {self.current_rod.name}" + Style.RESET_ALL)
        print()
        
        for i, rod in enumerate(RODS, 1):
            owned = " (OWNED)" if rod in self.owned_rods else ""
            current = " [EQUIPPED]" if rod == self.current_rod else ""
            color = Fore.GREEN if rod in self.owned_rods else Fore.YELLOW
            print(color + f"{i}. {rod.name} - ${rod.cost} - Catch Rate: {rod.catch_bonus*100:.0f}%{owned}{current}" + Style.RESET_ALL)
            print(f"   {rod.description}")
        
        print(f"\n{len(RODS)+1}. Back")
        
        choice = input(Fore.CYAN + "\nBuy or equip rod: " + Style.RESET_ALL)
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(RODS):
                rod = RODS[idx]
                if rod in self.owned_rods:
                    self.current_rod = rod
                    print(Fore.GREEN + f"Equipped {rod.name}!" + Style.RESET_ALL)
                elif self.money >= rod.cost:
                    self.money -= rod.cost
                    self.owned_rods.append(rod)
                    self.current_rod = rod
                    print(Fore.GREEN + f"Purchased and equipped {rod.name}!" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Not enough money!" + Style.RESET_ALL)
                input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)
        except ValueError:
            pass

    def buy_bait(self):
        self.clear_screen()
        print(Fore.CYAN + "╔═════════════════════════════════════╗" + Style.RESET_ALL)
        print(Fore.CYAN + "║            BAIT SHOP                ║" + Style.RESET_ALL)
        print(Fore.CYAN + "╚═════════════════════════════════════╝" + Style.RESET_ALL)
        print(Fore.YELLOW + f"Money: ${self.money}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Current: {self.current_bait.name}" + Style.RESET_ALL)
        print()
        
        for i, bait in enumerate(BAITS, 1):
            owned = " (OWNED)" if bait in self.owned_baits else ""
            current = " [EQUIPPED]" if bait == self.current_bait else ""
            color = Fore.GREEN if bait in self.owned_baits else Fore.YELLOW
            boost_pct = bait.rarity_boost * 100
            print(color + f"{i}. {bait.name} - ${bait.cost} - Rarity Boost: +{boost_pct:.0f}%{owned}{current}" + Style.RESET_ALL)
            print(f"   {bait.description}")
        
        print(f"\n{len(BAITS)+1}. Back")
        
        choice = input(Fore.CYAN + "\nBuy or equip bait: " + Style.RESET_ALL)
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(BAITS):
                bait = BAITS[idx]
                if bait in self.owned_baits:
                    self.current_bait = bait
                    print(Fore.GREEN + f"Equipped {bait.name}!" + Style.RESET_ALL)
                elif self.money >= bait.cost:
                    self.money -= bait.cost
                    self.owned_baits.append(bait)
                    self.current_bait = bait
                    print(Fore.GREEN + f"Purchased and equipped {bait.name}!" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Not enough money!" + Style.RESET_ALL)
                input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)
        except ValueError:
            pass

    def upgrade_esky(self):
        self.clear_screen()
        print(Fore.CYAN + "╔═════════════════════════════════════╗" + Style.RESET_ALL)
        print(Fore.CYAN + "║        ESKY UPGRADE                 ║" + Style.RESET_ALL)
        print(Fore.CYAN + "╚═════════════════════════════════════╝" + Style.RESET_ALL)
        print(Fore.YELLOW + f"Money: ${self.money}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Current Capacity: {self.esky.max_capacity}" + Style.RESET_ALL)
        print()
        
        upgrade_cost = self.esky.max_capacity * 10
        print(f"Upgrade to {self.esky.max_capacity + 10} capacity for ${upgrade_cost}?")
        print("1. Yes")
        print("2. No")
        
        choice = input(Fore.CYAN + "\nChoose: " + Style.RESET_ALL)
        if choice == '1':
            if self.money >= upgrade_cost:
                self.money -= upgrade_cost
                self.esky.max_capacity += 10
                print(Fore.GREEN + f"Upgraded! New capacity: {self.esky.max_capacity}" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Not enough money!" + Style.RESET_ALL)
            input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)

    def view_achievements(self):
        self.clear_screen()
        print(Fore.CYAN + "╔═════════════════════════════════════╗" + Style.RESET_ALL)
        print(Fore.CYAN + "║          ACHIEVEMENTS               ║" + Style.RESET_ALL)
        print(Fore.CYAN + "╚═════════════════════════════════════╝" + Style.RESET_ALL)
        print()
        
        achievement_descriptions = {
            'first_catch': "Catch your first fish",
            'first_rare': "Catch a rare fish",
            'first_legendary': "Catch a legendary fish",
            'first_mythical': "Catch a mythical fish",
            'fisherman': "Catch 50 fish total",
            'master_fisherman': "Catch 200 fish total",
            'millionaire': "Earn $1,000,000",
            'mutation_hunter': "Find all mutation types",
            'encyclopedia_25': "Discover 10 species",
            'encyclopedia_50': "Discover 20 species",
            'encyclopedia_100': "Discover all species",
        }
        
        unlocked = sum(1 for v in self.achievements.values() if v)
        total = len(self.achievements)
        
        print(Fore.YELLOW + f"Progress: {unlocked}/{total} achievements unlocked\n" + Style.RESET_ALL)
        
        for name, unlocked in self.achievements.items():
            status = Fore.GREEN + "✓" if unlocked else Fore.RED + "✗"
            desc = achievement_descriptions.get(name, name)
            print(f"{status} {desc}{Style.RESET_ALL}")
        
        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)

    def view_stats(self):
        self.clear_screen()
        print(Fore.CYAN + "╔═════════════════════════════════════╗" + Style.RESET_ALL)
        print(Fore.CYAN + "║            STATISTICS               ║" + Style.RESET_ALL)
        print(Fore.CYAN + "╚═════════════════════════════════════╝" + Style.RESET_ALL)
        print()
        
        total_caught = sum(info['times_caught'] for info in self.encyclopedia.caught_fish.values())
        species_count = len(self.encyclopedia.caught_fish)
        
        # Count all possible fish
        all_fish_species = set()
        for location in self.locations:
            for fish in location.fish:
                all_fish_species.add(fish.name)
        
        completion = (species_count / len(all_fish_species) * 100) if all_fish_species else 0
        
        # Find heaviest fish
        heaviest_name = "None"
        heaviest_weight = 0
        for name, info in self.encyclopedia.caught_fish.items():
            if info['heaviest'] > heaviest_weight:
                heaviest_weight = info['heaviest']
                heaviest_name = name
        
        print(Fore.YELLOW + f"Level: {self.level}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"Total XP: {self.xp}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"Money: ${self.money}" + Style.RESET_ALL)
        print(Fore.GREEN + f"\nTotal Fish Caught: {total_caught}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Species Discovered: {species_count}/{len(all_fish_species)}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Encyclopedia Completion: {completion:.1f}%" + Style.RESET_ALL)
        print(Fore.GREEN + f"Heaviest Fish: {heaviest_name} ({heaviest_weight:.2f}kg)" + Style.RESET_ALL)
        print(Fore.CYAN + f"\nCurrent Rod: {self.current_rod.name}" + Style.RESET_ALL)
        print(Fore.CYAN + f"Current Bait: {self.current_bait.name}" + Style.RESET_ALL)
        print(Fore.CYAN + f"Esky Capacity: {self.esky.max_capacity}" + Style.RESET_ALL)
        
        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)

    def skill_tree_menu(self):
        while True:
            self.clear_screen()
            print(Fore.CYAN + "╔═══════════════════════════════════╗" + Style.RESET_ALL)
            print(Fore.CYAN + "║           SKILL TREE              ║" + Style.RESET_ALL)
            print(Fore.CYAN + "╚═══════════════════════════════════╝" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Skill Points Available: {self.skill_points}" + Style.RESET_ALL)
            print()
            
            skill_info = {
                'rare_finder': ('Rare Finder', 5, '+2% rare fish chance per level'),
                'quick_reflexes': ('Quick Reflexes', 5, '-5% minigame difficulty per level'),
                'master_angler': ('Master Angler', 5, '+5% catch rate per level'),
                'lucky_fisherman': ('Lucky Fisherman', 5, '+10% mutation chance per level'),
                'bargain_hunter': ('Bargain Hunter', 3, '+10% sell price per level'),
                'iron_grip': ('Iron Grip', 3, '+15% XP gain per level'),
            }
            
            i = 1
            for skill_key, (name, max_level, desc) in skill_info.items():
                current_level = self.skills.get(skill_key, 0)
                color = Fore.GREEN if current_level < max_level else Fore.LIGHTBLACK_EX
                status = f"[{current_level}/{max_level}]"
                print(color + f"{i}. {name} {status}" + Style.RESET_ALL)
                print(f"   {desc}")
                i += 1
            
            print(f"\n{i}. Back to menu")
            
            choice = input(Fore.CYAN + "\nUpgrade skill (or back): " + Style.RESET_ALL)
            
            try:
                choice_idx = int(choice) - 1
                if choice_idx == len(skill_info):
                    return
                
                skill_keys = list(skill_info.keys())
                if 0 <= choice_idx < len(skill_keys):
                    skill_key = skill_keys[choice_idx]
                    skill_name, max_level, _ = skill_info[skill_key]
                    current_level = self.skills.get(skill_key, 0)
                    
                    if current_level >= max_level:
                        print(Fore.RED + f"{skill_name} is already maxed out!" + Style.RESET_ALL)
                    elif self.skill_points > 0:
                        self.skills[skill_key] = current_level + 1
                        self.skill_points -= 1
                        print(Fore.GREEN + f"Upgraded {skill_name} to level {self.skills[skill_key]}!" + Style.RESET_ALL)
                    else:
                        print(Fore.RED + "Not enough skill points!" + Style.RESET_ALL)
                    
                    input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)
            except ValueError:
                pass


    def level_up(self):
        self.level += 1
        self.xp_threshold = int(100 * (self.level ** 1.5))
        print(Fore.LIGHTCYAN_EX + f"🎉 Congratulations! You've reached level {self.level}!" + Style.RESET_ALL)
        
        # Bonus rewards for leveling
        bonus_money = self.level * 50
        self.money += bonus_money
        print(Fore.YELLOW + f"Level up bonus: ${bonus_money}" + Style.RESET_ALL)
        # Skill point reward
        self.skill_points += 1
        print(Fore.LIGHTCYAN_EX + "🌟 Gained 1 Skill Point!" + Style.RESET_ALL)

    def repair_rod(self):
        repair_cost = int((self.rod_max_durability - self.rod_durability) * 5)
        if repair_cost == 0:
            print(Fore.GREEN + "Your rod is already in perfect condition!" + Style.RESET_ALL)
            return
        
        print(Fore.YELLOW + f"Rod condition: {self.rod_durability}/{self.rod_max_durability}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"Repair cost: ${repair_cost}" + Style.RESET_ALL)
        print("1. Repair")
        print("2. Cancel")
        
        choice = input(Fore.CYAN + "Choose an option (1-12): " + Style.RESET_ALL)
        if choice == '1' and self.money >= repair_cost:
            self.money -= repair_cost
            self.rod_durability = self.rod_max_durability
            print(Fore.GREEN + "Rod repaired!" + Style.RESET_ALL)
        elif choice == '1':
            print(Fore.RED + "Not enough money!" + Style.RESET_ALL)
            return



# ===== MAIN =====
if __name__ == "__main__":
    show_intro()
    print(Fore.CYAN + "╔═══════════════════════════════════════╗" + Style.RESET_ALL)
    print(Fore.CYAN + "║       🎣 FISHING GAME 🎣              ║" + Style.RESET_ALL)
    print(Fore.CYAN + "║         open beta V.0.3               ║" + Style.RESET_ALL)
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
        
