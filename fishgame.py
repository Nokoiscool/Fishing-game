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

#kant
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
    "The coelacanth is a 'living fossil' fish that was thought extinct for 66 million years.",
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
    "Boss fights can be triggered using special items found while fishing!",
    "Sparing bosses gives you positive karma - killing them gives negative karma!",
    "Each location has a unique boss waiting to be discovered!",
    "The River Guardian is said to be over 1000 years old!",
    "Pike are ambush predators known as 'water wolves' in nature!",
    "The River Guardian protects the sacred rapids from those who would harm them!",
    "You must defeat or spare bosses to unlock new fishing locations!",
    "Defeat the Loch Ness Monster to unlock the River location!",
    "The River Guardian must be conquered before you can explore the Ocean!",
    "Boss progression is required - defeat them in order to advance!",
    "A fish is a creature that lives in water!",
    "The Crimson Tide fights against corporate greed in the oceans!",
    "Captain Redbeard and his crew are rebels, not villains!",
    "Sparing the pirate ship unlocks Captain Redbeard as an ally at the docks!",
    "AquaTech Industries has been exploiting the ocean's resources!",
    "The rebellion grows stronger with every guardian you spare!",
    "Pirates have their own code of honor on the high seas!",
    "Sometimes the real monsters are the corporations, not the creatures!",
    "The Kraken is the last of its kind - an ancient guardian of the deep!",
    "Kraken legends appear in Norse, Greek, and many other mythologies!",
    "The Kraken can only be encountered after dealing with the pirates!",
    "Sparing the Kraken grants you the blessing of the ancient seas!",
    "The Kraken's tentacles can reach over 100 feet in the legends!",
    "Some say the Kraken is older than human civilization itself!",
    
]

def get_random_fact():
    return random.choice(DID_YOU_KNOW_FACTS)


# ===== BOSS FIGHT SYSTEM =====
class Boss:
    def __init__(self, name, hp, defense, attacks, ascii_art, dialogue, spare_threshold=50):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.attacks = attacks  # List of attack patterns
        self.ascii_art = ascii_art
        self.dialogue = dialogue  # Dict with different dialogue states
        self.spare_threshold = spare_threshold  # HP % when boss can be spared
        self.mercy_level = 0  # Increases when you ACT
        self.is_spareable = False
        
    def take_damage(self, damage):
        actual_damage = max(1, damage - self.defense)
        self.hp -= actual_damage
        if self.hp < 0:
            self.hp = 0
        
        # Check if spareable
        hp_percent = (self.hp / self.max_hp) * 100
        if hp_percent <= self.spare_threshold and self.mercy_level >= 3:
            self.is_spareable = True
            
        return actual_damage
    
    def get_dialogue(self, state="default"):
        return self.dialogue.get(state, self.dialogue.get("default", ["..."]))
    
    def get_random_attack(self):
        return random.choice(self.attacks)

class BossAttack:
    def __init__(self, name, pattern_func, damage_range, description):
        self.name = name
        self.pattern_func = pattern_func  # Function that generates attack pattern
        self.damage_range = damage_range  # (min, max)
        self.description = description
    
    def execute(self):
        return self.pattern_func()

# ===== BOSS ATTACK PATTERNS =====
def loch_ness_wave_attack():
    """Simple wave pattern - original attack (kept for variety)"""
    pattern_length = 40
    safe_spots = []
    
    print(Fore.CYAN + "\n💧 Waves incoming! 💧\n" + Style.RESET_ALL)
    
    for wave_num in range(3):
        wave_pos = random.randint(0, pattern_length - 10)
        
        for frame in range(10):
            pattern = [' '] * pattern_length
            wave_start = max(0, wave_pos - 2 + frame)
            wave_end = min(pattern_length, wave_pos + 10 + frame)
            
            for i in range(wave_start, wave_end):
                if i < pattern_length:
                    offset = abs((i - wave_start) - 5)
                    if offset == 0:
                        pattern[i] = '≋'
                    elif offset <= 2:
                        pattern[i] = '~'
                    else:
                        pattern[i] = '˜'
            
            display = Fore.CYAN + "[" + ''.join(pattern) + "]" + Style.RESET_ALL
            sys.stdout.write("\r" + display)
            sys.stdout.flush()
            time.sleep(0.05)
        
        print()
        
        for i in range(pattern_length):
            if i < wave_pos or i >= wave_pos + 8:
                safe_spots.append(i)
    
    print()
    print(Fore.YELLOW + "Choose a safe position to dodge (0-39):" + Style.RESET_ALL)
    try:
        player_pos = int(input(Fore.GREEN + "> " + Style.RESET_ALL))
        if 0 <= player_pos <= pattern_length and player_pos in safe_spots:
            print(Fore.GREEN + "✓ Perfect dodge!" + Style.RESET_ALL)
            time.sleep(0.5)
            return 0
        else:
            for _ in range(3):
                print(Fore.RED + "💥 SPLASH! 💥" + Style.RESET_ALL)
                time.sleep(0.1)
                sys.stdout.write("\r" + " " * 20 + "\r")
                sys.stdout.flush()
                time.sleep(0.1)
            print(Fore.RED + "You got hit by the wave!" + Style.RESET_ALL)
            return random.randint(10, 20)
    except:
        print(Fore.RED + "Invalid input! You got hit!" + Style.RESET_ALL)
        return random.randint(10, 20)


def loch_ness_water_blast():
    """Multiple choice dodge - original attack (kept for variety)"""
    print(Fore.CYAN + "\n💦 The monster is charging a water blast! 💦\n" + Style.RESET_ALL)
    
    charging_frames = ["  (  )", "  ( O )", "  ( ⚡ )", "  (💧💧)", "  (💦💦)"]
    
    for frame in charging_frames:
        sys.stdout.write("\r" + Fore.LIGHTBLUE_EX + frame + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.3)
    
    print("\n")
    
    print(Fore.YELLOW + "Which way do you dodge?" + Style.RESET_ALL)
    print(Fore.WHITE + "1. ⬅️  Left   2. ➡️  Right   3. ⬆️  Jump   4. ⬇️  Duck" + Style.RESET_ALL)
    
    correct = random.randint(1, 4)
    hints = {
        1: "💭 You see ripples to the right...", 
        2: "💭 You see ripples to the left...",
        3: "💭 The blast is aimed low...",
        4: "💭 The blast is aimed high..."
    }
    
    print(Fore.LIGHTBLACK_EX + hints[correct] + Style.RESET_ALL)
    print()
    
    try:
        choice = int(input(Fore.GREEN + "Choice > " + Style.RESET_ALL))
        
        print()
        for i in range(5):
            blast = "💦" * (i + 1)
            sys.stdout.write("\r" + Fore.CYAN + f"BLAST! {blast}" + Style.RESET_ALL)
            sys.stdout.flush()
            time.sleep(0.1)
        print()
        
        if choice == correct:
            for _ in range(2):
                print(Fore.GREEN + "✨ PERFECT DODGE! ✨" + Style.RESET_ALL)
                time.sleep(0.1)
            return 0
        else:
            for _ in range(3):
                print(Fore.RED + "💥 SPLASH! 💥" + Style.RESET_ALL)
                time.sleep(0.1)
                sys.stdout.write("\r" + " " * 20 + "\r")
                sys.stdout.flush()
                time.sleep(0.1)
            print(Fore.RED + "Direct hit!" + Style.RESET_ALL)
            return random.randint(12, 18)
    except:
        print(Fore.RED + "Invalid input! You got blasted!" + Style.RESET_ALL)
        return random.randint(12, 18)


def loch_ness_tidal_wave():
    """ENHANCED: Multi-wave attack with different speeds and sizes"""
    pattern_length = 50
    print(Fore.CYAN + "\n🌊 TIDAL WAVE INCOMING! 🌊\n" + Style.RESET_ALL)
    
    waves = []
    for i in range(5):
        wave = {
            'position': random.randint(0, 10),
            'speed': random.randint(2, 5),
            'size': random.randint(4, 8),
            'damage': random.randint(3, 6)
        }
        waves.append(wave)
    
    for frame in range(15):
        pattern = [' '] * pattern_length
        
        for wave in waves:
            wave_pos = wave['position'] + (wave['speed'] * frame)
            wave_size = wave['size']
            
            for i in range(wave_pos, min(wave_pos + wave_size, pattern_length)):
                if 0 <= i < pattern_length:
                    if i - wave_pos <= 1:
                        pattern[i] = '≋'
                    elif i - wave_pos <= wave_size // 2:
                        pattern[i] = '~'
                    else:
                        pattern[i] = '˜'
        
        display = Fore.CYAN + "[" + ''.join(pattern) + "]" + Style.RESET_ALL
        sys.stdout.write("\r" + display)
        sys.stdout.flush()
        time.sleep(0.08)
    
    print("\n")
    
    final_positions = []
    for wave in waves:
        final_pos = wave['position'] + (wave['speed'] * 14)
        final_positions.append((final_pos, final_pos + wave['size']))
    
    print(Fore.YELLOW + f"Choose position to stand (0-{pattern_length-1}):" + Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX + "💭 Tip: Look for gaps between the waves!" + Style.RESET_ALL)
    
    try:
        player_pos = int(input(Fore.GREEN + "> " + Style.RESET_ALL))
        
        total_damage = 0
        hit_count = 0
        for wave_start, wave_end in final_positions:
            if wave_start <= player_pos < wave_end:
                hit_count += 1
                total_damage += waves[final_positions.index((wave_start, wave_end))]['damage']
        
        if hit_count == 0:
            print(Fore.GREEN + "✓ PERFECT DODGE! You found the safe zone!" + Style.RESET_ALL)
            return 0
        elif hit_count == 1:
            print(Fore.YELLOW + f"💦 Caught by 1 wave! (-{total_damage} HP)" + Style.RESET_ALL)
            return total_damage
        else:
            print(Fore.RED + f"💥 CRUSHED by {hit_count} waves! (-{total_damage} HP)" + Style.RESET_ALL)
            return total_damage
            
    except:
        print(Fore.RED + "Invalid input! Swept away!" + Style.RESET_ALL)
        return 20


def loch_ness_whirlpool():
    """ENHANCED: Button mashing to escape spinning vortex"""
    print(Fore.BLUE + "\n🌀 WHIRLPOOL! You're being pulled in! 🌀\n" + Style.RESET_ALL)
    
    whirlpool_frames = [
        "      ≈≈≈      ",
        "    ≈≈≈≈≈≈     ",
        "   ≈≈≈◉≈≈≈≈    ",
        "  ≈≈≈≈◉≈≈≈≈≈   ",
        " ≈≈≈≈◉◉◉≈≈≈≈≈  ",
        "≈≈≈≈◉◉◉◉◉≈≈≈≈≈ ",
    ]
    
    for frame in whirlpool_frames:
        sys.stdout.write("\r" + Fore.BLUE + frame + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.2)
    
    print("\n")
    print(Fore.RED + "MASH THE CORRECT BUTTONS TO ESCAPE!" + Style.RESET_ALL)
    
    buttons = ['W', 'A', 'S', 'D']
    required_sequence = [random.choice(buttons) for _ in range(5)]
    
    print(Fore.YELLOW + f"Enter: {' → '.join(required_sequence)}" + Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX + "(Type them quickly, then press Enter!)" + Style.RESET_ALL)
    
    start_time = time.time()
    try:
        player_input = input(Fore.GREEN + "> " + Style.RESET_ALL).upper()
        elapsed_time = time.time() - start_time
        
        correct_input = ''.join(required_sequence)
        
        if player_input == correct_input and elapsed_time < 3:
            print(Fore.GREEN + "✨ ESCAPED! Perfect button mashing!" + Style.RESET_ALL)
            return 0
        elif player_input == correct_input:
            print(Fore.YELLOW + "⚡ Escaped, but took some damage from the pull!" + Style.RESET_ALL)
            return 8
        else:
            correct_count = sum(1 for i, char in enumerate(player_input) if i < len(required_sequence) and char == required_sequence[i])
            damage = 20 - (correct_count * 3)
            print(Fore.RED + f"💫 Pulled under! Got {correct_count}/5 correct (-{damage} HP)" + Style.RESET_ALL)
            return damage
    except:
        print(Fore.RED + "💥 Sucked into the whirlpool! (-20 HP)" + Style.RESET_ALL)
        return 20


def loch_ness_tail_sweep():
    """ENHANCED: Prediction-based dodge with tells"""
    print(Fore.GREEN + "\n🐉 The Loch Ness Monster winds up its massive tail... 🐉\n" + Style.RESET_ALL)
    
    directions = ['LEFT', 'RIGHT', 'CENTER']
    correct_dir = random.choice(directions)
    
    if correct_dir == 'LEFT':
        print(Fore.LIGHTBLACK_EX + "💭 The monster's body is leaning right..." + Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + "💭 Its tail is on the right side..." + Style.RESET_ALL)
    elif correct_dir == 'RIGHT':
        print(Fore.LIGHTBLACK_EX + "💭 The monster's body is leaning left..." + Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + "💭 Its tail is on the left side..." + Style.RESET_ALL)
    else:
        print(Fore.LIGHTBLACK_EX + "💭 The monster is perfectly balanced..." + Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + "💭 Its tail is raised high above..." + Style.RESET_ALL)
    
    time.sleep(1)
    
    charge_frames = ["▁", "▂", "▃", "▄", "▅", "▆", "▇", "█"]
    for frame in charge_frames:
        sys.stdout.write("\r" + Fore.YELLOW + f"CHARGING: {frame * 10}" + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.15)
    
    print("\n")
    print(Fore.RED + "⚠️  TAIL SWEEP INCOMING! ⚠️" + Style.RESET_ALL)
    print()
    print(Fore.CYAN + "Which way do you dodge?" + Style.RESET_ALL)
    print(Fore.WHITE + "1. 🏃 Dodge LEFT" + Style.RESET_ALL)
    print(Fore.WHITE + "2. 🏃 Dodge RIGHT" + Style.RESET_ALL)
    print(Fore.WHITE + "3. 🤸 Stay CENTER" + Style.RESET_ALL)
    
    try:
        choice = input(Fore.GREEN + "> " + Style.RESET_ALL)
        
        print()
        if correct_dir == 'LEFT':
            sweep = "〰️〰️〰️〰️〰️=====>"
        elif correct_dir == 'RIGHT':
            sweep = "<=====〰️〰️〰️〰️〰️"
        else:
            sweep = "    ↓↓↓↓↓    "
        
        for i in range(3):
            sys.stdout.write("\r" + Fore.GREEN + sweep + Style.RESET_ALL)
            sys.stdout.flush()
            time.sleep(0.15)
        print()
        
        choice_map = {'1': 'LEFT', '2': 'RIGHT', '3': 'CENTER'}
        player_choice = choice_map.get(choice, 'INVALID')
        
        if player_choice == correct_dir:
            print(Fore.GREEN + "✓ PERFECT READ! You dodged it!" + Style.RESET_ALL)
            return 0
        else:
            print(Fore.RED + f"💥 SMASHED! The tail swept {correct_dir}!" + Style.RESET_ALL)
            return random.randint(15, 22)
            
    except:
        print(Fore.RED + "Invalid input! Got hit!" + Style.RESET_ALL)
        return 20


def loch_ness_deep_dive_slam():
    """ENHANCED: Two-phase attack - dive then slam"""
    print(Fore.BLUE + "\n🌊 The Loch Ness Monster DIVES beneath the surface! 🌊\n" + Style.RESET_ALL)
    
    dive_frames = [
        "     🐉     ",
        "     🐉~    ",
        "     🐉~~   ",
        "     ~🐉~~  ",
        "     ~~🐉~~ ",
        "     ~~~💦  ",
        "     ~~~    ",
        "     ...    ",
    ]
    
    for frame in dive_frames:
        sys.stdout.write("\r" + Fore.CYAN + frame + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.2)
    
    print("\n")
    print(Fore.YELLOW + "💭 It's gone under... where will it emerge?" + Style.RESET_ALL)
    time.sleep(1)
    
    zones = 7
    emerge_zone = random.randint(0, zones - 1)
    
    print(Fore.CYAN + f"Choose a safe zone (0-{zones-1}):" + Style.RESET_ALL)
    print(Fore.WHITE + "[0] [1] [2] [3] [4] [5] [6]" + Style.RESET_ALL)
    
    try:
        phase1_choice = int(input(Fore.GREEN + "> " + Style.RESET_ALL))
        
        print()
        zone_display = ["[ ]"] * zones
        zone_display[emerge_zone] = "[🐉]"
        
        for i in range(3):
            print("\r" + Fore.GREEN + " ".join(zone_display) + Style.RESET_ALL)
            time.sleep(0.3)
        
        phase1_damage = 0
        if phase1_choice == emerge_zone:
            print(Fore.RED + "💥 It emerged RIGHT where you were! (-12 HP)" + Style.RESET_ALL)
            phase1_damage = 12
        else:
            print(Fore.GREEN + "✓ Safe from the emergence!" + Style.RESET_ALL)
        
        time.sleep(0.8)
        
        print()
        print(Fore.RED + "\n⚠️  NOW IT'S GOING FOR A BODY SLAM! ⚠️\n" + Style.RESET_ALL)
        print(Fore.CYAN + "Quick! Dodge direction?" + Style.RESET_ALL)
        print(Fore.WHITE + "1. ⬅️  Roll LEFT   2. ➡️  Roll RIGHT" + Style.RESET_ALL)
        
        slam_dir = random.choice([1, 2])
        
        phase2_choice = int(input(Fore.GREEN + "> " + Style.RESET_ALL))
        
        print()
        for i in range(3):
            if slam_dir == 1:
                print(Fore.GREEN + "    🐉 <<<====" + Style.RESET_ALL)
            else:
                print(Fore.GREEN + "====>>> 🐉    " + Style.RESET_ALL)
            time.sleep(0.15)
        
        phase2_damage = 0
        if phase2_choice == slam_dir:
            print(Fore.GREEN + "✓ Perfect dodge roll!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "💥 CRUSHED by the body slam! (-15 HP)" + Style.RESET_ALL)
            phase2_damage = 15
        
        total_damage = phase1_damage + phase2_damage
        if total_damage == 0:
            print()
            print(Fore.LIGHTGREEN_EX + "★★★ FLAWLESS! Both phases dodged! ★★★" + Style.RESET_ALL)
        
        return total_damage
        
    except:
        print(Fore.RED + "Invalid input! Got hit by everything! (-27 HP)" + Style.RESET_ALL)
        return 27


def loch_ness_mist_breath():
    """ENHANCED: Memory test with obscured vision"""
    print(Fore.LIGHTCYAN_EX + "\n💨 The Loch Ness Monster breathes out a thick mist! 💨\n" + Style.RESET_ALL)
    
    positions = ['🪨', '🌊', '⚓', '🐚', '🪨']
    safe_pos = random.randint(0, 4)
    positions[safe_pos] = '✨'
    
    print(Fore.GREEN + "MEMORIZE THE SAFE ZONE:" + Style.RESET_ALL)
    print(Fore.YELLOW + " | ".join([f"[{i}]: {pos}" for i, pos in enumerate(positions)]) + Style.RESET_ALL)
    
    time.sleep(3)
    
    print()
    for _ in range(3):
        sys.stdout.write("\r" + Fore.WHITE + "💨💨💨 MIST RISING 💨💨💨" + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write("\r" + " " * 30 + "\r")
        sys.stdout.flush()
        time.sleep(0.2)
    
    print()
    print(Fore.LIGHTBLACK_EX + "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓" + Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX + "▓  YOU CAN'T SEE!    ▓" + Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX + "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓" + Style.RESET_ALL)
    print()
    
    print(Fore.CYAN + "Where was the safe zone (✨)? (0-4)" + Style.RESET_ALL)
    
    try:
        choice = int(input(Fore.GREEN + "> " + Style.RESET_ALL))
        
        print()
        print(Fore.WHITE + "The mist clears..." + Style.RESET_ALL)
        time.sleep(0.5)
        print(Fore.YELLOW + " | ".join([f"[{i}]: {pos}" for i, pos in enumerate(positions)]) + Style.RESET_ALL)
        
        if choice == safe_pos:
            print(Fore.GREEN + "✓ PERFECT MEMORY! You found the safe zone!" + Style.RESET_ALL)
            return 0
        else:
            print(Fore.RED + f"💥 Wrong! You hit {positions[choice]} (-14 HP)" + Style.RESET_ALL)
            return 14
            
    except:
        print(Fore.RED + "Invalid! Wandered into danger! (-14 HP)" + Style.RESET_ALL)
        return 14


def loch_ness_combo_attack():
    """ENHANCED: Ultimate combo attack - only used when HP < 30%"""
    print(Fore.RED + "\n💢 THE LOCH NESS MONSTER IS ENRAGED! 💢" + Style.RESET_ALL)
    print(Fore.RED + "⚡ ULTIMATE COMBO ATTACK! ⚡\n" + Style.RESET_ALL)
    time.sleep(1)
    
    total_damage = 0
    
    # Part 1: Quick wave dodge
    print(Fore.CYAN + "Part 1: RAPID WAVES!" + Style.RESET_ALL)
    wave_dir = random.choice(['L', 'R'])
    print(Fore.YELLOW + f"Wave coming from the {'LEFT' if wave_dir == 'L' else 'RIGHT'}!" + Style.RESET_ALL)
    print(Fore.WHITE + "Type 'L' for left or 'R' for right!" + Style.RESET_ALL)
    
    try:
        p1_input = input(Fore.GREEN + "> " + Style.RESET_ALL).upper()
        if p1_input != wave_dir:
            print(Fore.RED + "💦 Hit by wave! (-8 HP)" + Style.RESET_ALL)
            total_damage += 8
        else:
            print(Fore.GREEN + "✓ Dodged!" + Style.RESET_ALL)
    except:
        total_damage += 8
    
    time.sleep(0.5)
    
    # Part 2: Focus check
    print()
    print(Fore.MAGENTA + "Part 2: FOCUS CHECK!" + Style.RESET_ALL)
    num1 = random.randint(5, 15)
    num2 = random.randint(1, 10)
    answer = num1 + num2
    
    print(Fore.YELLOW + f"Quick! What's {num1} + {num2}?" + Style.RESET_ALL)
    
    try:
        p2_input = int(input(Fore.GREEN + "> " + Style.RESET_ALL))
        if p2_input != answer:
            print(Fore.RED + "❌ Wrong! Distracted! (-6 HP)" + Style.RESET_ALL)
            total_damage += 6
        else:
            print(Fore.GREEN + "✓ Correct!" + Style.RESET_ALL)
    except:
        total_damage += 6
    
    time.sleep(0.5)
    
    # Part 3: Final slam
    print()
    print(Fore.RED + "Part 3: FINAL TAIL SLAM!" + Style.RESET_ALL)
    positions = [' ', ' ', ' ', ' ', ' ']
    safe = random.randint(0, 4)
    positions[safe] = '✓'
    
    print(Fore.YELLOW + "Pick safe position: " + " | ".join([f"[{i}]" for i in range(5)]) + Style.RESET_ALL)
    
    try:
        p3_input = int(input(Fore.GREEN + "> " + Style.RESET_ALL))
        if p3_input != safe:
            print(Fore.RED + "💥 SLAM! (-10 HP)" + Style.RESET_ALL)
            total_damage += 10
        else:
            print(Fore.GREEN + "✓ Safe!" + Style.RESET_ALL)
    except:
        total_damage += 10
    
    print()
    if total_damage == 0:
        print(Fore.LIGHTGREEN_EX + "★★★ INCREDIBLE! SURVIVED THE COMBO! ★★★" + Style.RESET_ALL)
    elif total_damage < 15:
        print(Fore.YELLOW + f"You survived with {total_damage} damage!" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"The combo devastated you! {total_damage} damage!" + Style.RESET_ALL)
    
    return total_damage


# ===== RIVER GUARDIAN ATTACK PATTERNS =====
def river_rapids_dodge():
    """Navigate through rushing rapids"""
    print(Fore.CYAN + "\n🌊 THE RAPIDS SURGE FORWARD! 🌊\n" + Style.RESET_ALL)
    
    path_length = 60
    safe_path = []
    obstacles = []
    
    # Generate safe path
    current_pos = random.randint(10, 20)
    for _ in range(8):
        safe_path.append(current_pos)
        current_pos += random.randint(-3, 3)
        current_pos = max(5, min(path_length - 5, current_pos))
    
    # Generate obstacles
    for i in range(path_length):
        if i not in safe_path:
            obstacles.append(i)
    
    # Show the rapids
    for frame in range(10):
        display = [' '] * path_length
        for obs in obstacles[:20]:  # Show some obstacles
            if obs < path_length:
                display[obs] = '≋' if frame % 2 == 0 else '~'
        
        for safe in safe_path[:frame//2 + 1]:
            if safe < path_length:
                display[safe] = '·'
        
        print("\r" + Fore.CYAN + "[" + ''.join(display) + "]" + Style.RESET_ALL, end='')
        sys.stdout.flush()
        time.sleep(0.1)
    
    print("\n")
    print(Fore.YELLOW + "Follow the safe path! Enter position (0-59):" + Style.RESET_ALL)
    
    try:
        choice = int(input(Fore.GREEN + "> " + Style.RESET_ALL))
        if choice in safe_path:
            print(Fore.GREEN + "✓ Expertly navigated!" + Style.RESET_ALL)
            return 0
        else:
            print(Fore.RED + "💥 Slammed into rocks! (-18 HP)" + Style.RESET_ALL)
            return 18
    except:
        print(Fore.RED + "Invalid! Swept away! (-18 HP)" + Style.RESET_ALL)
        return 18


def river_bite_sequence():
    """Quick reaction test - dodge the pike's bites"""
    print(Fore.RED + "\n🦈 THE GUARDIAN ATTACKS WITH RAZOR TEETH! 🦈\n" + Style.RESET_ALL)
    
    total_damage = 0
    num_bites = 4
    
    print(Fore.YELLOW + "Press the correct key quickly to dodge!" + Style.RESET_ALL)
    time.sleep(1)
    
    for i in range(num_bites):
        direction = random.choice(['W', 'A', 'S', 'D'])
        direction_name = {'W': '⬆️  UP', 'A': '⬅️  LEFT', 'S': '⬇️  DOWN', 'D': '➡️  RIGHT'}
        
        print()
        print(Fore.CYAN + f"Bite #{i+1} - Dodge {direction_name[direction]}!" + Style.RESET_ALL)
        print(Fore.WHITE + f"Press '{direction}':" + Style.RESET_ALL)
        
        # Charging animation
        for _ in range(3):
            sys.stdout.write("\r" + Fore.RED + " >>" * (i+1) + " 🦈 " + Style.RESET_ALL)
            sys.stdout.flush()
            time.sleep(0.15)
        
        try:
            user_input = input(Fore.GREEN + "\n> " + Style.RESET_ALL).upper()
            if user_input == direction:
                print(Fore.GREEN + "✓ Dodged!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "💥 Bitten! (-7 HP)" + Style.RESET_ALL)
                total_damage += 7
        except:
            total_damage += 7
        
        time.sleep(0.3)
    
    if total_damage == 0:
        print(Fore.LIGHTGREEN_EX + "\n★ PERFECT! All bites dodged! ★" + Style.RESET_ALL)
    
    return total_damage


def river_current_spin():
    """Spinning current trap"""
    print(Fore.BLUE + "\n🌀 THE GUARDIAN CREATES A WHIRLPOOL! 🌀\n" + Style.RESET_ALL)
    
    # Show spinning animation
    spin_frames = ['|', '/', '-', '\\']
    for _ in range(12):
        for frame in spin_frames:
            sys.stdout.write("\r" + Fore.CYAN + f"    {frame} SPINNING {frame}    " + Style.RESET_ALL)
            sys.stdout.flush()
            time.sleep(0.08)
    
    print("\n")
    print(Fore.YELLOW + "The whirlpool stops! Which direction?" + Style.RESET_ALL)
    print(Fore.WHITE + "1. North  2. East  3. South  4. West" + Style.RESET_ALL)
    
    safe_dir = random.randint(1, 4)
    hints = {
        1: "💭 You feel a northern breeze...",
        2: "💭 The eastern current feels calmer...",
        3: "💭 Something pulls you south...",
        4: "💭 The western waters seem safer..."
    }
    
    print(Fore.LIGHTBLACK_EX + hints[safe_dir] + Style.RESET_ALL)
    
    try:
        choice = int(input(Fore.GREEN + "\n> " + Style.RESET_ALL))
        if choice == safe_dir:
            print(Fore.GREEN + "✓ Escaped the whirlpool!" + Style.RESET_ALL)
            return 0
        else:
            print(Fore.RED + "💥 Pulled under! (-16 HP)" + Style.RESET_ALL)
            return 16
    except:
        print(Fore.RED + "Invalid! Dragged down! (-16 HP)" + Style.RESET_ALL)
        return 16


def river_tail_strike():
    """Timing-based dodge"""
    print(Fore.GREEN + "\n⚡ MASSIVE TAIL INCOMING! ⚡\n" + Style.RESET_ALL)
    
    print(Fore.YELLOW + "Get ready to dodge!" + Style.RESET_ALL)
    time.sleep(0.5)
    
    # Build-up
    for i in range(5):
        sys.stdout.write("\r" + Fore.YELLOW + "." * (i+1) + "   ")
        sys.stdout.flush()
        time.sleep(0.4)
    
    print()
    
    # Random window for dodge
    dodge_window = random.uniform(0.5, 2.0)
    
    print(Fore.RED + "\nPress ENTER when you see 'NOW!':" + Style.RESET_ALL)
    time.sleep(dodge_window)
    
    start_time = time.time()
    print(Fore.LIGHTGREEN_EX + ">>> NOW! <<<" + Style.RESET_ALL)
    
    try:
        input()
        reaction_time = time.time() - start_time
        
        if reaction_time < 0.5:
            print(Fore.GREEN + f"✓ Lightning reflexes! ({reaction_time:.2f}s)" + Style.RESET_ALL)
            return 0
        elif reaction_time < 1.0:
            print(Fore.YELLOW + f"Grazed! ({reaction_time:.2f}s) (-10 HP)" + Style.RESET_ALL)
            return 10
        else:
            print(Fore.RED + f"Too slow! ({reaction_time:.2f}s) (-20 HP)" + Style.RESET_ALL)
            return 20
    except:
        print(Fore.RED + "Missed! (-20 HP)" + Style.RESET_ALL)
        return 20


def river_wrath_combo():
    """Ultimate attack - only used at low HP"""
    print(Fore.RED + "\n⚡💢 RIVER'S WRATH UNLEASHED! 💢⚡\n" + Style.RESET_ALL)
    time.sleep(1)
    
    total_damage = 0
    
    # Phase 1: Quick choice
    print(Fore.CYAN + "Phase 1: THE CURRENT SHIFTS!" + Style.RESET_ALL)
    print(Fore.WHITE + "Swim LEFT or RIGHT? (L/R)" + Style.RESET_ALL)
    
    correct = random.choice(['L', 'R'])
    try:
        choice = input(Fore.GREEN + "> " + Style.RESET_ALL).upper()
        if choice != correct:
            print(Fore.RED + "💦 Wrong way! (-12 HP)" + Style.RESET_ALL)
            total_damage += 12
        else:
            print(Fore.GREEN + "✓ Safe!" + Style.RESET_ALL)
    except:
        total_damage += 12
    
    time.sleep(0.5)
    
    # Phase 2: Memorize positions
    print()
    print(Fore.MAGENTA + "Phase 2: RAPIDS MAZE!" + Style.RESET_ALL)
    
    safe_zones = random.sample(range(5), 2)
    display = ['🪨' if i not in safe_zones else '✨' for i in range(5)]
    
    print(Fore.GREEN + "MEMORIZE: " + " | ".join([f"[{i}]: {display[i]}" for i in range(5)]) + Style.RESET_ALL)
    time.sleep(2.5)
    
    print(Fore.LIGHTBLACK_EX + "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓" + Style.RESET_ALL)
    print(Fore.CYAN + "Pick a safe zone (0-4):" + Style.RESET_ALL)
    
    try:
        choice = int(input(Fore.GREEN + "> " + Style.RESET_ALL))
        if choice in safe_zones:
            print(Fore.GREEN + "✓ Safe!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "💥 Hit rocks! (-15 HP)" + Style.RESET_ALL)
            total_damage += 15
    except:
        total_damage += 15
    
    time.sleep(0.5)
    
    # Phase 3: Final strike
    print()
    print(Fore.RED + "Phase 3: FINAL GUARDIAN STRIKE!" + Style.RESET_ALL)
    print(Fore.YELLOW + "Type 'DODGE' quickly!" + Style.RESET_ALL)
    
    start = time.time()
    try:
        response = input(Fore.GREEN + "> " + Style.RESET_ALL).upper()
        elapsed = time.time() - start
        
        if response == "DODGE" and elapsed < 2:
            print(Fore.GREEN + "✓ Dodged!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "💥 STRUCK! (-18 HP)" + Style.RESET_ALL)
            total_damage += 18
    except:
        total_damage += 18
    
    print()
    if total_damage == 0:
        print(Fore.LIGHTGREEN_EX + "★★★ FLAWLESS VICTORY! ★★★" + Style.RESET_ALL)
    
    return total_damage


# ===== PIRATE SHIP ATTACK PATTERNS =====
def pirate_cannon_barrage():
    """Dodge incoming cannonballs"""
    print(Fore.RED + "\n💣 CANNON BARRAGE INCOMING! 💣\n" + Style.RESET_ALL)
    
    total_damage = 0
    num_shots = 5
    
    print(Fore.YELLOW + "Dodge the cannonballs! Watch for the indicators!" + Style.RESET_ALL)
    time.sleep(1)
    
    for i in range(num_shots):
        position = random.randint(1, 5)
        
        # Show cannon charging
        print()
        print(Fore.CYAN + f"Shot #{i+1}!" + Style.RESET_ALL)
        time.sleep(0.3)
        
        # Show positions with one being the danger zone
        display = ['[ ]' if j != position else '[💣]' for j in range(1, 6)]
        print(Fore.WHITE + "Positions: " + ' '.join(display) + Style.RESET_ALL)
        print(Fore.YELLOW + "Where do you move? (1-5):" + Style.RESET_ALL)
        
        try:
            choice = int(input(Fore.GREEN + "> " + Style.RESET_ALL))
            if choice == position:
                print(Fore.RED + "💥 DIRECT HIT! (-8 HP)" + Style.RESET_ALL)
                total_damage += 8
            else:
                print(Fore.GREEN + "✓ Dodged!" + Style.RESET_ALL)
        except:
            total_damage += 8
        
        time.sleep(0.4)
    
    if total_damage == 0:
        print(Fore.LIGHTGREEN_EX + "\n★ UNTOUCHABLE! Perfect evasion! ★" + Style.RESET_ALL)
    
    return total_damage


def pirate_harpoon_strike():
    """Quick reaction to dodge harpoon"""
    print(Fore.CYAN + "\n🔱 HARPOON STRIKE! 🔱\n" + Style.RESET_ALL)
    
    print(Fore.YELLOW + "The pirates are aiming their harpoon..." + Style.RESET_ALL)
    time.sleep(1)
    
    # Show aiming
    aim_chars = ['·', ':', '•', '●']
    for char in aim_chars * 2:
        sys.stdout.write("\r" + Fore.RED + f"Targeting... {char}" + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.2)
    
    print("\n")
    print(Fore.RED + "Type 'DIVE' to dodge!" + Style.RESET_ALL)
    
    start = time.time()
    try:
        response = input(Fore.GREEN + "> " + Style.RESET_ALL).upper()
        elapsed = time.time() - start
        
        if response == "DIVE":
            if elapsed < 1.5:
                print(Fore.GREEN + f"✓ Ducked in time! ({elapsed:.2f}s)" + Style.RESET_ALL)
                return 0
            else:
                print(Fore.YELLOW + f"Grazed! ({elapsed:.2f}s) (-12 HP)" + Style.RESET_ALL)
                return 12
        else:
            print(Fore.RED + "Wrong input! Got harpooned! (-20 HP)" + Style.RESET_ALL)
            return 20
    except:
        print(Fore.RED + "Too slow! (-20 HP)" + Style.RESET_ALL)
        return 20


def pirate_broadside_ram():
    """Predict and avoid ship ramming"""
    print(Fore.MAGENTA + "\n⚓ THE SHIP IS RAMMING! ⚓\n" + Style.RESET_ALL)
    
    print(Fore.YELLOW + "Watch the ship's movement!" + Style.RESET_ALL)
    time.sleep(1)
    
    # Show ship approaching
    directions = ['PORT (LEFT)', 'STARBOARD (RIGHT)', 'STERN (BACK)']
    correct = random.choice(directions)
    
    # Give hint based on direction
    if 'LEFT' in correct:
        print(Fore.LIGHTBLACK_EX + "💭 The ship is turning starboard..." + Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + "💭 It's coming from the right..." + Style.RESET_ALL)
    elif 'RIGHT' in correct:
        print(Fore.LIGHTBLACK_EX + "💭 The ship is turning port..." + Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + "💭 It's coming from the left..." + Style.RESET_ALL)
    else:
        print(Fore.LIGHTBLACK_EX + "💭 The ship is backing up..." + Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + "💭 Watch your stern!" + Style.RESET_ALL)
    
    time.sleep(1.5)
    
    # Show charging animation
    for i in range(5):
        sys.stdout.write("\r" + Fore.RED + "INCOMING! " + ">" * (i+1) + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.25)
    
    print("\n")
    print(Fore.CYAN + "Where do you dodge?" + Style.RESET_ALL)
    print(Fore.WHITE + "1. PORT (LEFT)  2. STARBOARD (RIGHT)  3. STERN (BACK)" + Style.RESET_ALL)
    
    try:
        choice = input(Fore.GREEN + "> " + Style.RESET_ALL)
        choice_map = {'1': 'PORT (LEFT)', '2': 'STARBOARD (RIGHT)', '3': 'STERN (BACK)'}
        player_choice = choice_map.get(choice, 'INVALID')
        
        if player_choice == correct:
            print(Fore.GREEN + "✓ Perfect dodge!" + Style.RESET_ALL)
            return 0
        else:
            print(Fore.RED + f"💥 RAMMED! Should have dodged {correct}! (-25 HP)" + Style.RESET_ALL)
            return 25
    except:
        print(Fore.RED + "Invalid! Got crushed! (-25 HP)" + Style.RESET_ALL)
        return 25


def pirate_net_toss():
    """Escape from a net by matching sequence"""
    print(Fore.BLUE + "\n🕸️  NET TOSSED! 🕸️\n" + Style.RESET_ALL)
    
    print(Fore.YELLOW + "You're caught in a fishing net!" + Style.RESET_ALL)
    time.sleep(1)
    
    # Generate escape sequence
    sequence_length = 4
    sequence = ''.join(random.choices(['W', 'A', 'S', 'D'], k=sequence_length))
    
    print(Fore.CYAN + "Cut the ropes in sequence!" + Style.RESET_ALL)
    print(Fore.WHITE + f"Input: {' → '.join(sequence)}" + Style.RESET_ALL)
    time.sleep(2)
    
    # Hide sequence
    print(Fore.LIGHTBLACK_EX + "▓" * 20 + Style.RESET_ALL)
    
    print(Fore.GREEN + "Type the sequence now:" + Style.RESET_ALL)
    
    try:
        player_input = input(Fore.GREEN + "> " + Style.RESET_ALL).upper()
        
        if player_input == sequence:
            print(Fore.GREEN + "✓ Escaped the net!" + Style.RESET_ALL)
            return 0
        else:
            correct_count = sum(1 for i, char in enumerate(player_input) if i < len(sequence) and char == sequence[i])
            damage = 15 - (correct_count * 3)
            print(Fore.YELLOW + f"Partially cut! Got {correct_count}/{sequence_length} correct (-{damage} HP)" + Style.RESET_ALL)
            return damage
    except:
        print(Fore.RED + "💥 Tangled in the net! (-15 HP)" + Style.RESET_ALL)
        return 15


def pirate_ultimate_assault():
    """Multi-phase pirate attack"""
    print(Fore.RED + "\n🏴‍☠️💥 ALL HANDS ON DECK! 💥🏴‍☠️\n" + Style.RESET_ALL)
    print(Fore.MAGENTA + "CAPTAIN REDBEARD: GIVE 'EM EVERYTHING WE'VE GOT!" + Style.RESET_ALL)
    time.sleep(1.5)
    
    total_damage = 0
    
    # Phase 1: Quick dodge
    print()
    print(Fore.CYAN + "Phase 1: GRAPPLING HOOKS!" + Style.RESET_ALL)
    print(Fore.WHITE + "Duck LEFT or RIGHT? (L/R)" + Style.RESET_ALL)
    
    correct = random.choice(['L', 'R'])
    try:
        choice = input(Fore.GREEN + "> " + Style.RESET_ALL).upper()
        if choice != correct:
            print(Fore.RED + "🪝 Hooked! (-10 HP)" + Style.RESET_ALL)
            total_damage += 10
        else:
            print(Fore.GREEN + "✓ Dodged!" + Style.RESET_ALL)
    except:
        total_damage += 10
    
    time.sleep(0.7)
    
    # Phase 2: Cannon timing
    print()
    print(Fore.MAGENTA + "Phase 2: CANNON FIRE!" + Style.RESET_ALL)
    print(Fore.YELLOW + "Press SPACE when you see the shot!" + Style.RESET_ALL)
    
    delay = random.uniform(1, 2.5)
    time.sleep(delay)
    
    start = time.time()
    print(Fore.RED + "💥 BOOM! 💥" + Style.RESET_ALL)
    
    try:
        input()
        reaction = time.time() - start
        if reaction < 0.8:
            print(Fore.GREEN + f"✓ Dodged! ({reaction:.2f}s)" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"💣 Hit! ({reaction:.2f}s) (-15 HP)" + Style.RESET_ALL)
            total_damage += 15
    except:
        total_damage += 15
    
    time.sleep(0.7)
    
    # Phase 3: Final sequence
    print()
    print(Fore.RED + "Phase 3: BOARDING PARTY!" + Style.RESET_ALL)
    print(Fore.CYAN + "Fight them off! Type 'FIGHT':" + Style.RESET_ALL)
    
    try:
        response = input(Fore.GREEN + "> " + Style.RESET_ALL).upper()
        if response == "FIGHT":
            print(Fore.GREEN + "✓ Repelled!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "⚔️  Overwhelmed! (-12 HP)" + Style.RESET_ALL)
            total_damage += 12
    except:
        total_damage += 12
    
    print()
    if total_damage == 0:
        print(Fore.LIGHTGREEN_EX + "★★★ LEGENDARY DEFENSE! ★★★" + Style.RESET_ALL)
    
    return total_damage


# ===== KRAKEN ATTACK PATTERNS =====
def kraken_tentacle_slam():
    """Dodge multiple tentacle slams"""
    print(Fore.MAGENTA + "\n🐙 TENTACLES RISE FROM THE DEPTHS! 🐙\n" + Style.RESET_ALL)
    
    total_damage = 0
    num_slams = 6
    
    print(Fore.YELLOW + "Watch the tentacles and dodge!" + Style.RESET_ALL)
    time.sleep(1)
    
    for i in range(num_slams):
        positions = [1, 2, 3, 4, 5]
        danger_zones = random.sample(positions, 2)  # 2 tentacles attack
        
        print()
        print(Fore.CYAN + f"Slam #{i+1}!" + Style.RESET_ALL)
        
        # Show tentacles rising
        display = []
        for pos in positions:
            if pos in danger_zones:
                display.append('[🐙]')
            else:
                display.append('[ ]')
        
        print(Fore.WHITE + "Positions: " + ' '.join(display) + Style.RESET_ALL)
        print(Fore.YELLOW + "Safe position? (1-5):" + Style.RESET_ALL)
        
        try:
            choice = int(input(Fore.GREEN + "> " + Style.RESET_ALL))
            if choice in danger_zones:
                print(Fore.RED + "💥 CRUSHED! (-10 HP)" + Style.RESET_ALL)
                total_damage += 10
            else:
                print(Fore.GREEN + "✓ Safe!" + Style.RESET_ALL)
        except:
            total_damage += 10
        
        time.sleep(0.3)
    
    if total_damage == 0:
        print(Fore.LIGHTGREEN_EX + "\n★ PERFECT! Dodged all tentacles! ★" + Style.RESET_ALL)
    
    return total_damage


def kraken_ink_cloud():
    """Navigate through ink cloud - memory test"""
    print(Fore.LIGHTBLACK_EX + "\n💨 THE KRAKEN RELEASES INK! 💨\n" + Style.RESET_ALL)
    
    print(Fore.YELLOW + "Memorize the safe path before the ink clouds your vision!" + Style.RESET_ALL)
    time.sleep(1)
    
    # Show safe path
    path_length = 7
    safe_path = random.sample(range(1, 10), path_length)
    
    print(Fore.GREEN + "SAFE PATH: " + Style.RESET_ALL, end='')
    for step in safe_path:
        print(Fore.CYAN + f"[{step}] ", end='')
        sys.stdout.flush()
        time.sleep(0.4)
    
    print("\n")
    time.sleep(1.5)
    
    # Hide with ink
    for _ in range(3):
        print(Fore.LIGHTBLACK_EX + "█" * 40 + Style.RESET_ALL)
    
    print()
    print(Fore.YELLOW + "Enter the path (numbers separated by spaces):" + Style.RESET_ALL)
    
    try:
        user_input = input(Fore.GREEN + "> " + Style.RESET_ALL)
        user_path = [int(x) for x in user_input.split()]
        
        if user_path == safe_path:
            print(Fore.GREEN + "✓ Perfect memory! Navigated through!" + Style.RESET_ALL)
            return 0
        else:
            correct_count = sum(1 for i, num in enumerate(user_path) if i < len(safe_path) and num == safe_path[i])
            damage = 20 - (correct_count * 2)
            print(Fore.YELLOW + f"Got {correct_count}/{path_length} correct (-{damage} HP)" + Style.RESET_ALL)
            return damage
    except:
        print(Fore.RED + "💥 Lost in the ink! (-20 HP)" + Style.RESET_ALL)
        return 20


def kraken_whirlpool_grab():
    """Escape the kraken's whirlpool"""
    print(Fore.BLUE + "\n🌀 THE KRAKEN CREATES A MASSIVE WHIRLPOOL! 🌀\n" + Style.RESET_ALL)
    
    print(Fore.YELLOW + "You're being pulled in! Swim against the current!" + Style.RESET_ALL)
    time.sleep(1)
    
    # Button mashing challenge
    target = 15
    print(Fore.CYAN + f"Press SPACE {target} times quickly!" + Style.RESET_ALL)
    
    count = 0
    start_time = time.time()
    time_limit = 5
    
    print(Fore.WHITE + "GO!" + Style.RESET_ALL)
    
    while count < target and (time.time() - start_time) < time_limit:
        key = get_key()
        if key == ' ':
            count += 1
            # Show progress
            progress = "█" * count + "░" * (target - count)
            sys.stdout.write(f"\r{Fore.CYAN}[{progress}] {count}/{target}{Style.RESET_ALL}")
            sys.stdout.flush()
    
    print()
    elapsed = time.time() - start_time
    
    if count >= target:
        print(Fore.GREEN + f"✓ Escaped! ({elapsed:.1f}s)" + Style.RESET_ALL)
        return 0
    else:
        damage = 25 - (count * 1)
        print(Fore.RED + f"💥 Pulled under! Only {count}/{target} (-{damage} HP)" + Style.RESET_ALL)
        return damage


def kraken_beak_strike():
    """Quick reaction to dodge the kraken's beak"""
    print(Fore.RED + "\n🦑 THE KRAKEN'S BEAK STRIKES! 🦑\n" + Style.RESET_ALL)
    
    print(Fore.YELLOW + "The creature lunges at you with its massive beak!" + Style.RESET_ALL)
    time.sleep(1)
    
    # Show the kraken approaching
    approach_frames = [
        "       🐙",
        "      🐙 ",
        "     🐙  ",
        "    🐙   ",
        "   🐙    ",
        "  🐙     "
    ]
    
    for frame in approach_frames:
        sys.stdout.write("\r" + Fore.MAGENTA + frame + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.2)
    
    print("\n")
    
    directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    safe_dir = random.choice(directions)
    
    print(Fore.RED + "DODGE WHICH WAY?" + Style.RESET_ALL)
    print(Fore.WHITE + "1. UP  2. DOWN  3. LEFT  4. RIGHT" + Style.RESET_ALL)
    
    dir_map = {'1': 'UP', '2': 'DOWN', '3': 'LEFT', '4': 'RIGHT'}
    
    start = time.time()
    try:
        choice = input(Fore.GREEN + "> " + Style.RESET_ALL)
        elapsed = time.time() - start
        
        if dir_map.get(choice) == safe_dir and elapsed < 2:
            print(Fore.GREEN + "✓ Dodged the beak!" + Style.RESET_ALL)
            return 0
        elif elapsed >= 2:
            print(Fore.RED + f"💥 Too slow! Bitten! (-28 HP)" + Style.RESET_ALL)
            return 28
        else:
            print(Fore.RED + f"💥 Wrong direction! The beak got you! (-22 HP)" + Style.RESET_ALL)
            return 22
    except:
        print(Fore.RED + "💥 Paralyzed by fear! (-28 HP)" + Style.RESET_ALL)
        return 28


def kraken_crushing_grip():
    """Escape from tentacle grip - timing challenge"""
    print(Fore.MAGENTA + "\n🐙 TENTACLES WRAP AROUND YOU! 🐙\n" + Style.RESET_ALL)
    
    print(Fore.RED + "You're caught in the Kraken's crushing grip!" + Style.RESET_ALL)
    time.sleep(1)
    
    print(Fore.YELLOW + "Press the correct keys to break free!" + Style.RESET_ALL)
    time.sleep(1)
    
    total_damage = 0
    grip_phases = 4
    
    for phase in range(grip_phases):
        key = random.choice(['W', 'A', 'S', 'D'])
        key_names = {'W': 'UP ⬆️', 'A': 'LEFT ⬅️', 'S': 'DOWN ⬇️', 'D': 'RIGHT ➡️'}
        
        print()
        print(Fore.CYAN + f"Phase {phase + 1}: Press '{key}' ({key_names[key]})" + Style.RESET_ALL)
        
        # Squeezing animation
        for i in range(3):
            sys.stdout.write("\r" + Fore.RED + "SQUEEZING! " + "◉" * (i + 1) + Style.RESET_ALL)
            sys.stdout.flush()
            time.sleep(0.2)
        
        print()
        try:
            response = input(Fore.GREEN + "> " + Style.RESET_ALL).upper()
            if response == key:
                print(Fore.GREEN + "✓ Loosened!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "💥 CRUSHED! (-8 HP)" + Style.RESET_ALL)
                total_damage += 8
        except:
            total_damage += 8
        
        time.sleep(0.3)
    
    if total_damage == 0:
        print(Fore.LIGHTGREEN_EX + "\n★ FREED YOURSELF! ★" + Style.RESET_ALL)
    
    return total_damage


def kraken_tidal_fury():
    """Ultimate Kraken attack - multi-phase"""
    print(Fore.RED + "\n🌊🐙 RELEASE THE KRAKEN'S FURY! 🐙🌊\n" + Style.RESET_ALL)
    print(Fore.MAGENTA + "THE KRAKEN: *Roars from the abyss*" + Style.RESET_ALL)
    time.sleep(2)
    
    total_damage = 0
    
    # Phase 1: Tentacle barrage
    print()
    print(Fore.CYAN + "Phase 1: TENTACLE BARRAGE!" + Style.RESET_ALL)
    
    for i in range(3):
        position = random.randint(1, 3)
        print(Fore.YELLOW + f"Tentacle {i+1} strikes position {position}!" + Style.RESET_ALL)
        print(Fore.WHITE + "Dodge to? (1/2/3):" + Style.RESET_ALL)
        
        try:
            choice = int(input(Fore.GREEN + "> " + Style.RESET_ALL))
            if choice == position:
                total_damage += 8
                print(Fore.RED + "💥 Hit!" + Style.RESET_ALL)
            else:
                print(Fore.GREEN + "✓ Dodged!" + Style.RESET_ALL)
        except:
            total_damage += 8
        
        time.sleep(0.3)
    
    # Phase 2: Ink cloud
    print()
    print(Fore.LIGHTBLACK_EX + "Phase 2: INK STORM!" + Style.RESET_ALL)
    
    sequence = ''.join(random.choices(['W', 'A', 'S', 'D'], k=3))
    print(Fore.GREEN + f"Remember: {' → '.join(sequence)}" + Style.RESET_ALL)
    time.sleep(2)
    print(Fore.LIGHTBLACK_EX + "████████████" + Style.RESET_ALL)
    
    print(Fore.YELLOW + "Type sequence:" + Style.RESET_ALL)
    try:
        response = input(Fore.GREEN + "> " + Style.RESET_ALL).upper()
        if response == sequence:
            print(Fore.GREEN + "✓ Navigated!" + Style.RESET_ALL)
        else:
            total_damage += 12
            print(Fore.RED + "💥 Lost! (-12 HP)" + Style.RESET_ALL)
    except:
        total_damage += 12
    
    time.sleep(0.5)
    
    # Phase 3: Final strike
    print()
    print(Fore.RED + "Phase 3: THE BEAK DESCENDS!" + Style.RESET_ALL)
    print(Fore.YELLOW + "Type 'SWIM' to escape!" + Style.RESET_ALL)
    
    start = time.time()
    try:
        response = input(Fore.GREEN + "> " + Style.RESET_ALL).upper()
        elapsed = time.time() - start
        
        if response == "SWIM" and elapsed < 2.5:
            print(Fore.GREEN + "✓ Escaped!" + Style.RESET_ALL)
        else:
            total_damage += 15
            print(Fore.RED + "💥 STRUCK! (-15 HP)" + Style.RESET_ALL)
    except:
        total_damage += 15
    
    print()
    if total_damage == 0:
        print(Fore.LIGHTGREEN_EX + "★★★ LEGENDARY SURVIVAL! ★★★" + Style.RESET_ALL)
    
    return total_damage


# ===== BOSS DEFINITIONS =====
LOCH_NESS_ASCII = r"""
                                _..--+~/@-@--.
                        _-=~      (  .    )
                        _-~     _.--=.\ \''''
                    _~      _-       \ \_\
                    =      _=          '--'
                    '      =                             .
                :      :                              '=_. ___
                |      ;                                  '~--.~.
                ;      ;                                       } |
                =       \             __..-...__           ___/__/__
                :        =_     _.-~~          ~~--.__
                __  \         ~-+-~                   ___~=_______
                    ~@ ~~ == ...______ __ ___ _--~~--_
"""

LOCH_NESS_MONSTER = Boss(
    name="Loch Ness Monster",
    hp=200,
    defense=5,
attacks=[
        # Original attacks (kept for variety)
        BossAttack("Wave Crash", loch_ness_wave_attack, (12, 25), "Sends powerful waves"),
        BossAttack("Water Blast", loch_ness_water_blast, (15, 22), "Fires a concentrated water jet"),
        # NEW Enhanced attacks
        BossAttack("Tidal Wave", loch_ness_tidal_wave, (0, 35), "Multi-wave barrage!"),
        BossAttack("Whirlpool", loch_ness_whirlpool, (0, 25), "Spinning vortex trap!"),
        BossAttack("Tail Sweep", loch_ness_tail_sweep, (0, 28), "Massive tail attack!"),
        BossAttack("Deep Dive Slam", loch_ness_deep_dive_slam, (0, 32), "Two-phase combo!"),
        BossAttack("Mist Breath", loch_ness_mist_breath, (0, 18), "Vision obscured!"),
        BossAttack("ULTIMATE COMBO", loch_ness_combo_attack, (0, 30), "Devastating triple attack!")
    ],
    ascii_art=LOCH_NESS_ASCII,
    dialogue={
        "intro": ["*The water trembles...*", "*A massive shape rises from the depths!*", "*The Loch Ness Monster emerges!*"],
        "default": ["*The monster watches you carefully*", "*It circles in the water*", "*Steam rises from its nostrils*"],
        "hit": ["*It roars in pain!*", "*The monster thrashes!*", "*Waves splash everywhere!*"],
        "low_hp": ["*The monster looks tired*", "*It's breathing heavily*", "*Maybe it doesn't want to fight...*"],
        "merciful": ["*The monster seems calmer*", "*It's listening to you*", "*You sense it doesn't want conflict*"],
        "spare_ready": ["*The Loch Ness Monster can be SPARED*"],
        "spared": ["*The monster nods gratefully*", "*It sinks back into the depths peacefully*", "*You feel warmth in your heart*"],
        "killed": ["*The legendary creature falls...*", "*The water turns red*", "*You feel a weight in your chest*"]
    },
    spare_threshold=40
)

# River Guardian Boss
RIVER_GUARDIAN_ASCII = """
                                  ~≈~
                           ~≈~   /   \\   ~≈~
                    ~≈~         /  O  \\         ~≈~
              ~≈~            __/       \\__            ~≈~
        ~≈~               _/   \\_____/   \\_               ~≈~
                       __/  /\\ |     | /\\  \\__
                     _/    /  \\|     |/  \\    \\_
                   _/     /    |  ^  |    \\     \\_
         ~≈~     _/      /     | / \\ |     \\      \\_     ~≈~
               /        /      |/   \\|      \\        \\
              /        /       '     '       \\        \\
        ~≈~ /        /    THE RIVER GUARDIAN  \\        \\  ~≈~
           /________/___________________________\\________\\
         ~≈~   ~≈~   Ancient Pike of the Rapids   ~≈~   ~≈~
"""

RIVER_GUARDIAN = Boss(
    name="The River Guardian",
    hp=800,
    defense=15,
    attacks=[
        BossAttack("Rapids Rush", river_rapids_dodge, (0, 28), "Navigate treacherous rapids!"),
        BossAttack("Torrential Bite", river_bite_sequence, (0, 38), "Dodge rapid bite attacks!"),
        BossAttack("Whirlpool Spin", river_current_spin, (0, 24), "Escape the spinning vortex!"),
        BossAttack("Tail Strike", river_tail_strike, (0, 30), "Perfect timing required!"),
        BossAttack("RIVER'S WRATH", river_wrath_combo, (0, 55), "The Guardian's ultimate fury!")
    ],
    ascii_art=RIVER_GUARDIAN_ASCII,
    dialogue={
        "intro": [
            "*The river begins to churn and boil...*",
            "*A massive shadow rises from the depths!*",
            "*The River Guardian emerges, ancient and territorial!*",
            "*'YOU DARE DISTURB THESE SACRED WATERS?!'*"
        ],
        "default": [
            "*The Guardian circles in the current*",
            "*Ancient eyes watch your every move*",
            "*The water ripples with primal power*"
        ],
        "hit": [
            "*It thrashes violently!*",
            "*The Guardian roars!*",
            "*Rapids surge in all directions!*"
        ],
        "low_hp": [
            "*The Guardian's movements slow...*",
            "*'Perhaps... you are worthy...'*",
            "*The water calms around it*"
        ],
        "merciful": [
            "*You show respect for the ancient waters*",
            "*The Guardian acknowledges your understanding*",
            "*Its rage begins to subside*"
        ],
        "spare_ready": [
            "*The River Guardian can be SPARED*",
            "*It awaits your decision with ancient wisdom*"
        ],
        "spared": [
            "*You extend your hand in peace...*",
            "*The River Guardian pauses, considering...*",
            "*'You have proven yourself, young fisher.'*",
            "*'These rapids are under my protection.'*",
            "*'But I see now... you understand their value.'*",
            "*The Guardian bows its massive head!*",
            "*It grants you the blessing of the river!*",
            "*The waters themselves acknowledge you!*"
        ],
        "killed": [
            "*The Guardian lets out a final, mournful cry...*",
            "*'The river... will remember this...'*",
            "*Its ancient form sinks into the depths...*",
            "*The waters grow still... too still...*",
            "*You feel a profound loss*"
        ]
    },
    spare_threshold=40
)

# Pirate Ship Boss
PIRATE_SHIP_ASCII = """
    ╔════════════════════════════════════════════════════╗
    ║         🏴‍☠️  THE CRIMSON TIDE  🏴‍☠️                 ║
    ║              [Rebel Pirate Vessel]                 ║
    ╚════════════════════════════════════════════════════╝
    
                                                    _  _
                                                   ' \/ '
   _  _                        <|
    \/              __'__     __'__      __'__
                   /    /    /    /     /    /
                  /\____\    \____\     \____\               _  _
                 / ___!___   ___!___    ___!___               \/
               // (      (  (      (   (      (
             / /   \______\  \______\   \______\
           /  /   ____!_____ ___!______ ____!_____
         /   /   /         //         //         /
       /    /   |         ||         ||         |
     /_____/     \         \\         \\         \   
           \      \_________\\_________\\_________\
            \         |          |         |
             \________!__________!_________!________/
              \|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_/|
               \    _______________                /
^^^%%%^%^^^%^%%^\_"/_)/_)_/_)__)/_)/)/)_)_"_'_"_//)/)/)/)%%%^^^%^^%%%%^
"""

PIRATE_SHIP = Boss(
    name="The Crimson Tide",
    hp=350,
    defense=12,
    attacks=[
        BossAttack("Cannon Barrage", pirate_cannon_barrage, (0, 50), "Dodge incoming cannonballs!"),
        BossAttack("Harpoon Strike", pirate_harpoon_strike, (0, 28), "Duck the harpoon!"),
        BossAttack("Broadside Ram", pirate_broadside_ram, (0, 35), "Avoid the ramming ship!"),
        BossAttack("Net Toss", pirate_net_toss, (0, 22), "Cut yourself free!"),
        BossAttack("ALL HANDS ASSAULT", pirate_ultimate_assault, (0, 48), "The crew's full might!")
    ],
    ascii_art=PIRATE_SHIP_ASCII,
    dialogue={
        "intro": [
            "*A weathered pirate ship emerges from the ocean mist!*",
            "*Cannons swivel in your direction!*",
            "CAPTAIN REDBEARD: 'Ahoy there! Another AquaTech vessel!'",
            "CAPTAIN REDBEARD: 'We're the Crimson Tide - we fight for freedom!'",
            "*You try to signal you're not with AquaTech...*",
            "CAPTAIN REDBEARD: 'Wait... ye don't look like their usual dogs...'",
            "CAPTAIN REDBEARD: 'Blimey! We thought ye were corporate scum!'",
            "CAPTAIN REDBEARD: 'Well... we already fired a warning shot...'",
            "CAPTAIN REDBEARD: 'Can't back down now! EN GARDE!'"
        ],
        "default": [
            "*The ship circles, cannons at the ready*",
            "*Pirates shout battle cries from the deck*",
            "*CAPTAIN REDBEARD watches you intently*"
        ],
        "hit": [
            "*The ship rocks from the impact!*",
            "CAPTAIN REDBEARD: 'Good hit, landlubber!'",
            "*Pirates scramble to repair damage*"
        ],
        "low_hp": [
            "*The ship is taking on water...*",
            "CAPTAIN REDBEARD: 'Yer a fierce one, I'll give ye that!'",
            "CAPTAIN REDBEARD: 'Perhaps we misjudged ye...'",
            "*The crew looks uncertain about continuing*"
        ],
        "merciful": [
            "*You lower your weapon and shout that you're allies!*",
            "CAPTAIN REDBEARD: 'Hold fire, lads! HOLD FIRE!'",
            "*The pirates pause, looking to their captain*",
            "CAPTAIN REDBEARD: 'AquaTech's been plunderin' these waters for years!'",
            "CAPTAIN REDBEARD: 'We fight to keep the seas free from their greed!'"
        ],
        "spare_ready": [
            "*The Crimson Tide can be SPARED*",
            "CAPTAIN REDBEARD: 'If ye truly oppose AquaTech... prove it!'"
        ],
        "spared": [
            "*You shout: 'I'M NOT YOUR ENEMY! I FIGHT AQUATECH TOO!'*",
            "CAPTAIN REDBEARD: 'CEASE FIRE! CEASE ALL FIRE!'",
            "*The cannons go silent...*",
            "CAPTAIN REDBEARD: 'By Davy Jones... ye really aren't with them!'",
            "CAPTAIN REDBEARD: 'We've been fightin' those corporate pirates so long...'",
            "CAPTAIN REDBEARD: 'We started seein' enemies in every sail!'",
            "*The captain extends his hand across the water*",
            "CAPTAIN REDBEARD: 'Any enemy of AquaTech is a friend of ours!'",
            "CAPTAIN REDBEARD: 'Ye can find us at the Hub Island docks!'",
            "CAPTAIN REDBEARD: 'Together, we'll make 'em pay for what they've done!'",
            "*The Crimson Tide raises a flag of truce!*",
            "*A new ally has joined your cause!*",
            "🏴‍☠️ CAPTAIN REDBEARD is now at the docks! 🏴‍☠️"
        ],
        "killed": [
            "*The ship lists heavily to one side...*",
            "*Pirates abandon ship, jumping into the water*",
            "CAPTAIN REDBEARD: 'Curse ye... we only wanted... freedom...'",
            "CAPTAIN REDBEARD: 'The rebellion... will remember... this betrayal...'",
            "*The Crimson Tide slowly sinks beneath the waves*",
            "*The water bubbles as it disappears into the depths*",
            "*You feel a profound weight in your chest...*",
            "*You've destroyed those who fought against tyranny*"
        ]
    },
    spare_threshold=35
)

# Kraken Boss
KRAKEN_ASCII = """
    ╔════════════════════════════════════════════════════╗
    ║              🌊 THE KRAKEN 🌊                      ║
    ║           [Ancient Terror of the Deep]             ║
    ╚════════════════════════════════════════════════════╝
    
                                  ___
                              .-'   `'.
                             /         \\
                             |         ;
                             |         |           ___.--,
                    _.._     |0) ~ (0) |    _.---'`__.-( (_.
             __.--'`_.. '.__.\    '--. \_.-' ,.--'`     `""`
            ( ,.--'`   ',__ /./;   ;, '.__.'`    __
            _`) )  .---.__.' / |   |\\   \\__..--""  \"\"\"--.,_
           `---' .'.''-._.-'`_./  /\\ '.  \\ _.-~~~````~~~-._`-.__.'
                 | |  .' _.-' |  |  \\  \\  '.               `~---`
                  \\ \\/ .'     \\  \\   '. '-._)
                   \\/ /        \\  \\    `=.__`~-.
                   / /\\         `) )    / / `"".`\\
             , _.-'.'\\ \\        / /    ( (     / /
              `--~`   ) )    .-'.'      '.'.  | (
                     (/`    ( (`          ) )  '-;
                      `      '-;         (-'
"""

KRAKEN = Boss(
    name="The Kraken",
    hp=500,
    defense=18,
    attacks=[
        BossAttack("Tentacle Slam", kraken_tentacle_slam, (0, 75), "Dodge the massive tentacles!"),
        BossAttack("Ink Cloud", kraken_ink_cloud, (0, 30), "Navigate through the murky ink!"),
        BossAttack("Whirlpool Grab", kraken_whirlpool_grab, (0, 35), "Escape the pulling vortex!"),
        BossAttack("Beak Strike", kraken_beak_strike, (0, 40), "Avoid the crushing beak!"),
        BossAttack("Crushing Grip", kraken_crushing_grip, (0, 45), "Break free from tentacles!"),
        BossAttack("TIDAL FURY", kraken_tidal_fury, (0, 50), "The Kraken's ultimate wrath!")
    ],
    ascii_art=KRAKEN_ASCII,
    dialogue={
        "intro": [
            "*The ocean grows unnaturally still...*",
            "*Massive bubbles rise from the depths*",
            "*Something ENORMOUS stirs below...*",
            "*ENORMOUS TENTACLES burst from the water!*",
            "*THE KRAKEN HAS AWAKENED!*",
            "THE KRAKEN: *An ancient, gurgling roar echoes across the waves*",
            "*It's been sleeping for centuries... until now*"
        ],
        "default": [
            "*Tentacles writhe through the water*",
            "*The beast's massive eye watches you*",
            "*The ocean trembles with its power*"
        ],
        "hit": [
            "*The Kraken recoils!*",
            "*A tentacle splashes back into the water*",
            "*The creature roars in fury!*"
        ],
        "low_hp": [
            "*The Kraken's movements slow...*",
            "*Several tentacles hang limp in the water*",
            "THE KRAKEN: *A mournful, echoing cry*",
            "*The ancient being seems... tired*"
        ],
        "merciful": [
            "*You stop attacking and float peacefully*",
            "*The Kraken pauses... watching you*",
            "*Its massive eye shows... curiosity?*",
            "THE KRAKEN: *A low, resonating rumble*",
            "*It remembers a time before humans hunted it...*"
        ],
        "spare_ready": [
            "*The Kraken can be SPARED*",
            "*The ancient creature awaits your choice*"
        ],
        "spared": [
            "*You raise your hands in peace*",
            "*The Kraken's tentacles stop thrashing*",
            "*Slowly... it sinks back into the depths*",
            "THE KRAKEN: *A deep, rumbling sound... almost like... gratitude?*",
            "*Before it disappears, one tentacle gently touches your boat*",
            "*You feel an ancient blessing flow through you*",
            "*The Kraken has recognized your kindness*",
            "*The ocean will remember this mercy*",
            "🐙 The Kraken has blessed you! 🐙",
            "*You can feel its presence watching over the seas*"
        ],
        "killed": [
            "*The Kraken lets out a final, earthshaking roar...*",
            "*Its tentacles thrash violently one last time*",
            "THE KRAKEN: *A sound of ancient sorrow*",
            "*The last of its kind...*",
            "*The massive body slowly sinks into the abyss*",
            "*The ocean grows dark and cold*",
            "*Sailors' legends spoke of this creature for millennia...*",
            "*Now... it's gone forever*",
            "*You feel the weight of what you've done*"
        ]
    },
    spare_threshold=30
)

# Boss item that triggers the fight
class BossItem:
    def __init__(self, name, boss, description, location):
        self.name = name
        self.boss = boss
        self.description = description
        self.location = location  # Which area it's found in

BOSS_ITEMS = {
    "Ancient Scale": BossItem(
        "Ancient Scale",
        LOCH_NESS_MONSTER,
        "A shimmering scale from an ancient creature. Using it might summon something...",
        "Hub Island - Calm Lake"
    ),
    "River Stone": BossItem(
        "River Stone",
        RIVER_GUARDIAN,
        "A smooth stone carved with ancient symbols. The river's power flows within it...",
        "Hub Island - Swift River"
    ),
    "Pirate Flag": BossItem(
        "Pirate Flag",
        PIRATE_SHIP,
        "A tattered black flag with a skull and crossbones. It smells of salt and rebellion...",
        "Ocean"
    ),
    "Kraken's Tooth": BossItem(
        "Kraken's Tooth",
        KRAKEN,
        "A massive, serrated tooth from the deep. Holding it makes the ocean feel... watchful...",
        "Ocean"
    ),
    # Add more boss items for other locations here
}

# ===== COMBAT ITEMS SYSTEM =====
class CombatItem:
    def __init__(self, name, item_type, bonus_value, price, description, unlock_level=1):
        self.name = name
        self.item_type = item_type  # "attack", "defense", "hp"
        self.bonus_value = bonus_value  # Amount of bonus
        self.price = price
        self.description = description
        self.unlock_level = unlock_level

# Combat Items - Attack Items
COMBAT_ITEMS_ATTACK = [
    CombatItem("Rusty Harpoon", "attack", 5, 150, "A basic weapon. +5 Attack", 1),
    CombatItem("Sharp Fishing Spear", "attack", 10, 400, "A well-crafted spear. +10 Attack", 3),
    CombatItem("Enchanted Trident", "attack", 18, 900, "Glows with ocean magic. +18 Attack", 6),
    CombatItem("Kraken Slayer Blade", "attack", 28, 2000, "Forged to slay giants. +28 Attack", 10),
    CombatItem("Poseidon's Wrath", "attack", 40, 5000, "The god's own weapon. +40 Attack", 15),
    CombatItem("Leviathan's Fang", "attack", 55, 10000, "Ancient beast's tooth. +55 Attack", 20),
]

# Combat Items - Defense Items
COMBAT_ITEMS_DEFENSE = [
    CombatItem("Leather Vest", "defense", 3, 200, "Basic protection. +3 Defense", 1),
    CombatItem("Scale Mail", "defense", 8, 500, "Made from fish scales. +8 Defense", 3),
    CombatItem("Coral Shield", "defense", 15, 1100, "Living coral armor. +15 Defense", 6),
    CombatItem("Turtle Shell Plate", "defense", 22, 2500, "Ancient turtle shell. +22 Defense", 10),
    CombatItem("Diamond Coral Armor", "defense", 32, 6000, "Crystallized protection. +32 Defense", 15),
    CombatItem("Abyssal Carapace", "defense", 45, 12000, "Deep sea guardian's shell. +45 Defense", 20),
]

# Combat Items - HP Items
COMBAT_ITEMS_HP = [
    CombatItem("Healing Salve", "hp", 20, 100, "Restores 20 HP. +20 Max HP", 1),
    CombatItem("Vitality Potion", "hp", 50, 350, "Increases vitality. +50 Max HP", 3),
    CombatItem("Whale Heart Extract", "hp", 100, 800, "Power of giants. +100 Max HP", 6),
    CombatItem("Phoenix Scale", "hp", 150, 1800, "Regenerative powers. +150 Max HP", 10),
    CombatItem("Elder Dragon Blood", "hp", 220, 4500, "Legendary resilience. +220 Max HP", 15),
    CombatItem("Immortal Jellyfish Core", "hp", 300, 9000, "Near immortality. +300 Max HP", 20),
]

# Boss requirements for unlocking locations
# Maps location name to the boss that must be defeated/spared
LOCATION_BOSS_REQUIREMENTS = {
    "Hub Island - Calm Lake": None,  # Starting location
    "Hub Island - Swift River": "Loch Ness Monster",  # Must defeat/spare Loch Ness first
    "Ocean": "The River Guardian",  # Must defeat/spare River Guardian
    "Deep Sea": "The River Guardian",  # Also requires River Guardian (or you could add an Ocean boss)
    "Volcanic Lake": "The River Guardian",  # Could add more bosses for progression
    "Arctic Waters": "The River Guardian",
    "Space Station Aquarium": "The River Guardian"
}


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
    
    @staticmethod
    def from_dict(data):
        """Recreate a Fish object from saved dictionary"""
        fish = Fish(
            name=data['name'],
            min_weight=data['min_weight'],
            max_weight=data['max_weight'],
            rarity=data['rarity'],
            rarity_weight=data['rarity_weight'],
            xp_reward=data['xp_reward'],
            real_world_info=data.get('real_world_info', ''),
            sell_price=data['sell_price']
        )
        fish.weight = data['weight']
        fish.mutation = data.get('mutation', 'normal')
        fish.catch_time = data.get('catch_time')
        return fish

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
    Fish("Magicarp", 8, 12, "Rare", 1.5, 50, "A strange orange and yellow fish.", 300),
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
    Fish("Glow Reef Angelfish", 3, 6, "Rare", 1.4, 20, "An elegant neon fish that drifts like it's in zero-gravity water.", 90),
    #TODO: make the german fish say a random number of fishes in german
    Fish("Ein kleiner Fisch", 0.1, 0.5, "Common", 0.5, 10, 'A tiny fish that seems to be singing in German. its saying "Fünf kleine Fische, die schwammen im Meer, blub blub blub blub"', 10),
    Fish("Ein großer Hai", 10, 50, "Rare", 0.1, 50, 'A large shark that seems to be singing in German. its saying "Ein großer Hai, der schwamm im Meer, blub blub blub blub"', 100),

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
    # name, xp_bonus, rarity_bonus, price
    # ===== EARLY GAME: learning & comfort =====
    Rod("Bamboo Rod",      0.00, 0.70,        0),     # Tutorial / very safe
    Rod("Wooden Rod",      0.02, 0.73,      150),
    Rod("Fiberglass Rod",  0.04, 0.76,      400),
    Rod("Composite Rod",   0.06, 0.80,      800),

    # ===== MID GAME: steady power =====
    Rod("Carbon Rod",      0.08, 0.84,     1500),
    Rod("Graphite Rod",    0.10, 0.88,     2500),
    Rod("Titanium Rod",    0.12, 0.92,     4000),
    Rod("Reinforced Rod",  0.14, 0.96,     6500),

    # ===== TRANSITION =====
    Rod("Legendary Rod",   0.16, 1.00,    10000),

    # ===== ENDGAME SPECIALIZATION =====
    Rod("Mythic Rod",      0.30, 0.95,    20000),  # XP grinder
    Rod("Abyssal Rod",     0.10, 1.25,    35000),  # Mutation / rarity hunter
    Rod("Quantum Rod",     0.20, 1.10,    60000),  # RNG chaos
    Rod("Godly Rod",       0.18, 1.05,   100000),  # Boss control

    # ===== CHAOS / JOKE / SECRET =====
    Rod("Blobfish Rod",    0.00, 1.00,  2000000),  # Breaks rules, not numbers
]

BAITS = [ 
    Bait("Worm", 0, 0, 0),
    Bait("Bread", 5, 0.05, 50),
    Bait("Cricket", 8, 0.08, 120),
    Bait("Minnow", 12, 0.12, 250),
    Bait("Corn", 10, 0.10, 180),
    Bait("Shrimp", 15, 0.15, 500),
    Bait("Nightcrawler", 14, 0.14, 400),
    Bait("Squid", 18, 0.18, 800),
    Bait("Cut Bait", 16, 0.16, 650),
    Bait("Artificial Lure", 22, 0.22, 1200),
    Bait("Live Bait", 25, 0.25, 1500),
    Bait("Special Lure", 30, 0.30, 2500),
    Bait("Premium Lure", 35, 0.35, 4000),
    Bait("Exotic Bait", 40, 0.40, 6500),
    Bait("Master Bait", 50, 0.50, 50000)
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
        key = msvcrt.getch()
        
        # Handle special keys (arrow keys, function keys, etc.)
        if key in [b'\x00', b'\xe0']:  # Special key prefix
            # Read the second byte and ignore it
            msvcrt.getch()
            return ''  # Return empty string for special keys
        
        try:
            return key.decode('utf-8').lower()
        except UnicodeDecodeError:
            # If we can't decode it, just ignore it
            return ''
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


def pattern_minigame(patience_stat):
    """Player must repeat a pattern of keys"""
    print(Fore.YELLOW + "\n🔁 Repeat the pattern of keys!" + Style.RESET_ALL)
    
    length = max(3, 6 - patience_stat // 3)
    pattern = ''.join(random.choice('WASD') for _ in range(length))
    
    print(Fore.CYAN + f"Pattern: {pattern}" + Style.RESET_ALL)
    time.sleep(2)
    
    print(Fore.YELLOW + "Now repeat it!" + Style.RESET_ALL)
    input_pattern = input(Fore.GREEN + "Input: " + Style.RESET_ALL).upper()
    
    if input_pattern == pattern:
        print(Fore.GREEN + "✓ Correct!" + Style.RESET_ALL)
        return True
    else:
        print(Fore.RED + f"✗ Incorrect! The pattern was {pattern}" + Style.RESET_ALL)
        return False
    

def undertale_attack_minigame(strength_stat, difficulty_name="Normal"):
    """Undertale-style attack timing bar - returns damage multiplier (0.5 to 2.0)
    Difficulty affects zone size and speed"""
    print()
    print(Fore.YELLOW + "⚔️  ATTACK! Press SPACE at the right moment! ⚔️" + Style.RESET_ALL)
    print()
    
    bar_width = 30
    
    # Adjust zones based on difficulty
    if difficulty_name == "Easy":
        # Bigger zones, easier timing
        perfect_zone_start = 12
        perfect_zone_end = 18
        good_zone_start = 8
        good_zone_end = 22
    elif difficulty_name == "Hard":
        # Smaller zones, harder timing
        perfect_zone_start = 14
        perfect_zone_end = 16
        good_zone_start = 12
        good_zone_end = 18
    else:  # Normal
        # Medium zones
        perfect_zone_start = 13
        perfect_zone_end = 17
        good_zone_start = 10
        good_zone_end = 20
    
    position = 0
    direction = 1
    
    # Make the bar move faster with higher strength AND difficulty
    base_speed = 0.08 - (strength_stat * 0.003)
    
    # Adjust speed by difficulty
    if difficulty_name == "Easy":
        speed = base_speed * 1.3  # Slower
    elif difficulty_name == "Hard":
        speed = base_speed * 0.7  # Faster!
    else:
        speed = base_speed
    
    speed = max(0.03, min(0.12, speed))  # Clamp speed
    
    for frame in range(60):  # 60 frames
        # Build the attack bar
        bar = ['─'] * bar_width
        
        # Color the zones
        for i in range(good_zone_start, good_zone_end):
            bar[i] = '░'
        for i in range(perfect_zone_start, perfect_zone_end):
            bar[i] = '█'
        
        # Place the cursor
        bar[position] = '▼'
        
        # Display with colors
        display_bar = ""
        for i, char in enumerate(bar):
            if i == position:
                display_bar += Fore.YELLOW + char + Style.RESET_ALL
            elif perfect_zone_start <= i < perfect_zone_end:
                display_bar += Fore.GREEN + char + Style.RESET_ALL
            elif good_zone_start <= i < good_zone_end:
                display_bar += Fore.CYAN + char + Style.RESET_ALL
            else:
                display_bar += Fore.WHITE + char + Style.RESET_ALL
        
        sys.stdout.write('\r[' + display_bar + ']')
        sys.stdout.flush()
        
        # Check for input
        if platform.system() == 'Windows':
            import msvcrt
            if msvcrt.kbhit():
                key = msvcrt.getch()
                if key == b' ':
                    print()
                    if perfect_zone_start <= position < perfect_zone_end:
                        # Perfect hit!
                        for _ in range(3):
                            print(Fore.GREEN + "★★★ CRITICAL HIT! ★★★" + Style.RESET_ALL)
                            time.sleep(0.08)
                            sys.stdout.write("\r" + " " * 40 + "\r")
                            sys.stdout.flush()
                            time.sleep(0.08)
                        print(Fore.GREEN + "★★★ CRITICAL HIT! ★★★" + Style.RESET_ALL)
                        return 2.0  # Double damage!
                    elif good_zone_start <= position < good_zone_end:
                        print(Fore.CYAN + "✓ Good hit!" + Style.RESET_ALL)
                        return 1.5  # 1.5x damage
                    else:
                        print(Fore.YELLOW + "○ Weak hit..." + Style.RESET_ALL)
                        return 0.8  # Reduced damage
        else:
            # Unix-like systems
            import select
            if select.select([sys.stdin], [], [], 0)[0]:
                key = sys.stdin.read(1)
                if key == ' ':
                    print()
                    if perfect_zone_start <= position < perfect_zone_end:
                        print(Fore.GREEN + "★★★ CRITICAL HIT! ★★★" + Style.RESET_ALL)
                        return 2.0
                    elif good_zone_start <= position < good_zone_end:
                        print(Fore.CYAN + "✓ Good hit!" + Style.RESET_ALL)
                        return 1.5
                    else:
                        print(Fore.YELLOW + "○ Weak hit..." + Style.RESET_ALL)
                        return 0.8
        
        time.sleep(speed)
        position += direction
        if position >= bar_width or position < 0:
            direction *= -1
            position += direction * 2
    
    # Time ran out - miss
    print()
    print(Fore.RED + "✗ Miss! Too slow!" + Style.RESET_ALL)
    return 0.5  # Half damage for missing


# ===== LOCATION MAP CLASS =====
class LocationMap:
    def __init__(self, name, layout, description="", start_x=None, start_y=None):
        self.name = name
        self.layout = layout  # 2D list of characters
        self.description = description
        self.player_x = 1
        self.player_y = 1
        self.message = "Use WASD to move around. Stand in water and press [E] to fish!"
        
        # Find initial player position (spawn point marked with 'P')
        for y, row in enumerate(layout):
            for x, tile in enumerate(row):
                if tile == 'P':
                    self.player_x = x
                    self.player_y = y
                    self.layout[y][x] = '.'  # Replace P with ground
        
        # Override with custom start position if provided
        if start_x is not None and start_y is not None:
            self.player_x = start_x
            self.player_y = start_y
    
    def move_player(self, dx, dy):
        new_x = self.player_x + dx
        new_y = self.player_y + dy
        
        # Check bounds
        if 0 <= new_y < len(self.layout) and 0 <= new_x < len(self.layout[new_y]):
            tile = self.layout[new_y][new_x]
            # Allow movement on walkable tiles (including all water types and NPC)
            if tile in ['.', '≈', '≋', '~', 'V', 'A', 'S', '⊙', '◉', '🏠', '🏪', '🏛️', '📋', '⚓', 'F']:
                self.player_x = new_x
                self.player_y = new_y
                self.message = f"Moved to ({new_x}, {new_y})"
            elif tile == '█' or tile == '🌳' or tile == '▓':
                self.message = "Can't walk through that!"
            else:
                self.message = "Can't walk there!"
    
    def is_fishing_spot(self, x, y):
        """Check if location is a fishing spot - any water tile"""
        tile = self.layout[y][x]
        return tile in ['≈', '≋', '~', 'V', 'A', 'S', '⊙', '◉']
    
    def is_golden_spot(self, x, y):
        """Check if it's a golden fishing spot"""
        return self.layout[y][x] == '◉'
    
    def is_building(self, x, y):
        """Check if location is a building entrance"""
        tile = self.layout[y][x]
        return tile in ['🏪', '🏛️', '📋', '🏠', '⚓']
    
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
    
    def get_water_type(self, x, y):
        """Get the type of water at this position"""
        tile = self.layout[y][x]
        if tile == '≈':
            return 'lake'
        elif tile == '≋':
            return 'river'
        elif tile == '~':
            return 'ocean'
        elif tile == 'V':
            return 'volcanic'
        elif tile == 'A':
            return 'arctic'
        elif tile == 'S':
            return 'space'
        return None
    
    def is_npc_fisherman(self, x, y):
        """Check if location has the NPC fisherman"""
        return self.layout[y][x] == 'F'
    
    def render_tile(self, tile, is_player, is_spot, is_golden):
        """Render a single tile with appropriate coloring"""
        if is_player:
            return Fore.YELLOW + '☻' + Style.RESET_ALL
        elif is_golden or tile == '◉':
            return Fore.LIGHTYELLOW_EX + '◉' + Style.RESET_ALL
        elif tile == '≈':  # Lake water
            return Fore.BLUE + '≈' + Style.RESET_ALL
        elif tile == '≋':  # River water
            return Fore.LIGHTBLUE_EX + '≋' + Style.RESET_ALL
        elif tile == '~':  # Ocean water
            return Fore.BLUE + '~' + Style.RESET_ALL
        elif tile == 'V':  # Volcanic water
            return Fore.RED + '≋' + Style.RESET_ALL
        elif tile == 'A':  # Arctic water
            return Fore.CYAN + '≈' + Style.RESET_ALL
        elif tile == 'S':  # Space
            return Fore.MAGENTA + '·' + Style.RESET_ALL
        elif tile == '⊙':  # Old fishing spot marker (treat as regular water)
            return Fore.CYAN + '≈' + Style.RESET_ALL
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
        elif tile == 'F':  # NPC Fisherman
            return Fore.GREEN + '🎣' + Style.RESET_ALL
        elif tile == '.':  # Ground
            return Fore.LIGHTBLACK_EX + '·' + Style.RESET_ALL
        else:
            return tile


# Create Hub Island map layout
#litteral torture
HUB_ISLAND_LAYOUT = [
    ['█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█',  '█', '█', '█', '█', '█', '█', '█', '█', '█', '█'],
    ['█', '🌳', '🌳', '▓', '▓', '▓', '▓', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '█'],
    ['█', '🌳', '🏛️', '.', '.', '.', '▓', '▓', '▓', '🌳', '≋', '≋', '≋', '≋', '≋', '≋', '🌳', '🌳', '🌳', '🌳', '🌳',  '█'],
    ['█', '🌳', '.', '.', '.', '▓', '▓', '🌳', '≋', '≋', '≋', '≋', '≋', '≋', '◉', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '█'],
    ['█', '🌳', '🏠', '.', '.', 'P', '.', '.', '.', '🌳', '🌳', '≋', '≋', '≋', '≋', '≋', '≋', '🌳', '🌳', '🌳', '🌳', '█'],
    ['█', '🌳', '.', '.', '.', '.', '.', '.', '🌳', '≈', '≈', '≈', '≋', '≋', '≋', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '█'],
    ['█', '🌳', '.', '.', '🏪', '.', '.', '≈', '≈', '≈', '≈', '≈', '≋', '≋', '≋', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '█'],
    ['█', '🌳', '🌳', '.', '.', '.', '.', '≈', '≈', '≈', '≈', '≈', '≈', '≈', '≋', '≋', '≋', '🌳', '🌳', '🌳', '🌳', '🌳', '█'],
    ['█', '🌳', '🌳', '.', '📋', '.', '.', '≈', '≈', '≈', '≈', '◉', '≈', '≈', '≈', '≋', '≋', '≋', '🌳', '🌳', '🌳', '🌳', '█'],
    ['█', '🌳', '🌳', '.', '.', '.',  '.', 'F', '≈', '≈', '≈', '≈', '≈', '≈', '≈', '≈', '≋', '≋', '≋', '🌳', '🌳', '🌳', '🌳', '█'],
    ['█', '🌳', '🌳', '🌳', '.', '.', '.',  '.', '.', '≈', '≈', '≈', '≈', '≈', '≈', '≈', '≈', '≈', '≋', '≋', '🌳', '🌳', '🌳', '█'],
    ['█', '🌳', '🌳', '🌳', '🌳', '.', '.', '.', '≈', '≈', '≈', '≈', '≈', '≈', '≈', '≈', '≋', '🌳', '🌳', '🌳', '🌳', '█'],
    ['█', '🌳', '🌳', '🌳', '🌳', '.', '.', '.', '.', '.', '≈', '≈', '≈', '≈', '≈', '≈', '≈', '🌳', '🌳', '🌳', '🌳', '█'],
    ['█', '🌳', '🌳', '🌳', '🌳', '🌳', '.', '.', '.', '.', '.', '.', '.', '.', '.', '⚓', '.', '🌳', '🌳', '🌳', '█'],
    ['█', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '🌳', '.', '.', '.', '.', '.', '.', '.', '.', '🌳', '🌳', '🌳', '█'],
    ['█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█',  '█', '█', '█', '█', '█', '█', '█', '█', '█', '█'],
]

# Create location maps for other locations
OCEAN_LAYOUT = [
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '◉', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', 'P', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
]

DEEP_SEA_LAYOUT = [
    ['▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓'],
    ['▓', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '▓'],
    ['▓', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '▓'],
    ['▓', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '▓'],
    ['▓', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '▓'],
    ['▓', '~', '~', '~', '~', '~', '~', '~', '~', '~', '◉', '~', '~', '~', '~', '~', '~', '~', '~', '▓'],
    ['▓', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '▓'],
    ['▓', '~', '~', '~', '~', '~', '~', '~', 'P', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '▓'],
    ['▓', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '▓'],
    ['▓', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '▓'],
    ['▓', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '▓'],
    ['▓', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '▓'],
    ['▓', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '▓'],
    ['▓', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '▓'],
    ['▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓'],
]

VOLCANIC_LAYOUT = [
    ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
    ['V', '▓', '▓', '▓', '▓', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', '▓', '▓', '▓', '▓', '▓', 'V'],
    ['V', '▓', '▓', '▓', '▓', '▓', 'V', 'V', 'V', 'V', 'V', 'V', 'V', '▓', '▓', '▓', '▓', '▓', '▓', 'V'],
    ['V', '▓', '▓', '▓', '▓', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', '▓', '▓', '▓', '▓', '▓', 'V'],
    ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', '▓', '▓', '▓', 'V', 'V'],
    ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
    ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
    ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'P', 'V', 'V', '◉', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
    ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
    ['V', '▓', '▓', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', '▓', '▓', 'V'],
    ['V', '▓', '▓', '▓', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', '▓', '▓', '▓', 'V'],
    ['V', '▓', '▓', '▓', '▓', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', '▓', '▓', '▓', '▓', 'V'],
    ['V', '▓', '▓', '▓', '▓', '▓', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', '▓', '▓', '▓', '▓', '▓', 'V'],
    ['V', 'V', '▓', '▓', '▓', '▓', '▓', 'V', 'V', 'V', 'V', 'V', '▓', '▓', '▓', '▓', '▓', '▓', 'V', 'V'],
    ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'],
]

SPACE_LAYOUT = [
    ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'P', 'S', 'S', '◉', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
]

ARCTIC_LAYOUT = [
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', '▓', '▓', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', '▓', '▓', 'A'],
    ['A', '▓', '▓', '▓', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', '▓', '▓', '▓', 'A'],
    ['A', 'A', '▓', '▓', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', '▓', '▓', '▓', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', '▓', 'A', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'P', 'A', 'A', '◉', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', 'A', 'A', '▓', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', 'A', '▓', '▓', '▓', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', '▓', 'A', 'A', 'A'],
    ['A', '▓', '▓', '▓', '▓', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', '▓', '▓', '▓', 'A', 'A'],
    ['A', '▓', '▓', '▓', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', '▓', '▓', '▓', 'A'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
]

# Add maps to locations
LOCATIONS[0].map = LocationMap("Hub Island - Calm Lake", HUB_ISLAND_LAYOUT, LOCATIONS[0].description, start_x=9, start_y=8)  # Lake spot
LOCATIONS[1].map = LocationMap("Hub Island - Swift River", HUB_ISLAND_LAYOUT, LOCATIONS[1].description, start_x=11, start_y=3)  # River spot
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
        # First check level requirement
        if self.game.level < location['unlock_level']:
            return False
        
        # Then check boss requirement
        location_name = location['name']
        required_boss = LOCATION_BOSS_REQUIREMENTS.get(location_name)
        
        # If a boss is required, check if it's been defeated or spared
        if required_boss and required_boss not in self.game.defeated_bosses:
            return False
        
        return True
    
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
                if self.is_location_unlocked(location):
                    status = "✓ Unlocked"
                else:
                    # Check what's blocking
                    requirements = []
                    if self.game.level < location['unlock_level']:
                        requirements.append(f"Level {location['unlock_level']}")
                    
                    required_boss = LOCATION_BOSS_REQUIREMENTS.get(location['name'])
                    if required_boss and required_boss not in self.game.defeated_bosses:
                        requirements.append(f"Defeat {required_boss}")
                    
                    status = f"🔒 Requires: {', '.join(requirements)}"
                
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
            
            # Build status message
            if is_unlocked:
                status = f"{Fore.GREEN}✓"
            else:
                requirements = []
                if self.game.level < loc['unlock_level']:
                    requirements.append(f"Lvl{loc['unlock_level']}")
                
                required_boss = LOCATION_BOSS_REQUIREMENTS.get(loc['name'])
                if required_boss and required_boss not in self.game.defeated_bosses:
                    requirements.append(f"Beat {required_boss}")
                
                status = f"{Fore.RED}🔒 {', '.join(requirements)}"
            
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
                        # Build requirements message
                        requirements = []
                        if self.game.level < location['unlock_level']:
                            requirements.append(f"Level {location['unlock_level']} (You: Lvl {self.game.level})")
                        
                        required_boss = LOCATION_BOSS_REQUIREMENTS.get(location['name'])
                        if required_boss and required_boss not in self.game.defeated_bosses:
                            requirements.append(f"Defeat {required_boss}")
                        
                        self.message = f"🔒 {location['name']} is locked! Requires: {', '.join(requirements)}"
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
        self.boss_inventory = []  # NEW: Separate inventory for boss items
        self.karma = 0  # NEW: Karma system (positive for sparing, negative for killing)
        self.defeated_bosses = []  # NEW: Track defeated bosses
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
        
        # Player HP for boss fights
        self.max_hp = 100
        self.current_hp = 100
        
        # Combat items (NEW)
        self.owned_combat_items = {
            'attack': [],
            'defense': [],
            'hp': []
        }
        self.equipped_combat_items = {
            'attack': None,
            'defense': None,
            'hp': None
        }
        
        # NPC interactions
        self.received_pirate_gift = False
        
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
            'boss_inventory': [{'name': item.name, 'boss': item.boss.name, 'description': item.description, 'location': item.location} for item in self.boss_inventory],
            'karma': self.karma,
            'defeated_bosses': self.defeated_bosses,
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
            'active_quests': [{'title': q.title, 'description': q.description} for q in self.active_quests],
            'completed_quests': [{'title': q.title, 'description': q.description} for q in self.completed_quests],
            'max_hp': self.max_hp,
            'current_hp': self.current_hp,
            'owned_combat_items': {
                'attack': [item.name for item in self.owned_combat_items['attack']],
                'defense': [item.name for item in self.owned_combat_items['defense']],
                'hp': [item.name for item in self.owned_combat_items['hp']]
            },
            'equipped_combat_items': {
                'attack': self.equipped_combat_items['attack'].name if self.equipped_combat_items['attack'] else None,
                'defense': self.equipped_combat_items['defense'].name if self.equipped_combat_items['defense'] else None,
                'hp': self.equipped_combat_items['hp'].name if self.equipped_combat_items['hp'] else None
            },
            'received_pirate_gift': self.received_pirate_gift,
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
            
            # Load inventory - ACTUALLY LOAD IT NOW
            self.inventory = [Fish.from_dict(fish_data) for fish_data in data.get('inventory', [])]
            
            # Load boss inventory
            self.boss_inventory = []
            for item_data in data.get('boss_inventory', []):
                # Find the matching boss item from BOSS_ITEMS
                if item_data['name'] in BOSS_ITEMS:
                    self.boss_inventory.append(BOSS_ITEMS[item_data['name']])
            
            # Load karma and defeated bosses
            self.karma = data.get('karma', 0)
            self.defeated_bosses = data.get('defeated_bosses', [])
            
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
            
            # Load trophy room - ACTUALLY LOAD IT NOW
            self.trophy_room = [Fish.from_dict(fish_data) for fish_data in data.get('trophy_room', [])]
            
            # Load location
            loc_name = data.get('current_location', 'Calm Lake')
            self.current_location = next((loc for loc in LOCATIONS if loc.name == loc_name), LOCATIONS[0])
            
            self.current_weather = data.get('current_weather', random.choice(WEATHERS))
            
            # Load quests (we'll skip loading the actual Quest objects and just track completion)
            # Since quests are generated dynamically, we just need to know which ones are completed
            self.active_quests = []  # Reset active quests
            self.completed_quests = []  # We could reconstruct these if needed, but not critical
            
            # Load HP
            self.max_hp = data.get('max_hp', 100)
            self.current_hp = data.get('current_hp', 100)
            
            # Load combat items
            owned_combat_data = data.get('owned_combat_items', {'attack': [], 'defense': [], 'hp': []})
            self.owned_combat_items = {
                'attack': [item for item in COMBAT_ITEMS_ATTACK if item.name in owned_combat_data.get('attack', [])],
                'defense': [item for item in COMBAT_ITEMS_DEFENSE if item.name in owned_combat_data.get('defense', [])],
                'hp': [item for item in COMBAT_ITEMS_HP if item.name in owned_combat_data.get('hp', [])]
            }
            
            equipped_combat_data = data.get('equipped_combat_items', {'attack': None, 'defense': None, 'hp': None})
            self.equipped_combat_items = {
                'attack': next((item for item in COMBAT_ITEMS_ATTACK if item.name == equipped_combat_data.get('attack')), None),
                'defense': next((item for item in COMBAT_ITEMS_DEFENSE if item.name == equipped_combat_data.get('defense')), None),
                'hp': next((item for item in COMBAT_ITEMS_HP if item.name == equipped_combat_data.get('hp')), None)
            }
            
            # Load NPC interactions
            self.received_pirate_gift = data.get('received_pirate_gift', False)
            
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
    
    def get_attack_bonus(self):
        """Calculate total attack bonus from equipped items"""
        bonus = 0
        if self.equipped_combat_items['attack']:
            bonus += self.equipped_combat_items['attack'].bonus_value
        return bonus
    
    def get_defense_bonus(self):
        """Calculate total defense bonus from equipped items"""
        bonus = 0
        if self.equipped_combat_items['defense']:
            bonus += self.equipped_combat_items['defense'].bonus_value
        return bonus
    
    def get_max_hp_bonus(self):
        """Calculate total max HP bonus from equipped items"""
        bonus = 0
        if self.equipped_combat_items['hp']:
            bonus += self.equipped_combat_items['hp'].bonus_value
        return bonus
    
    def update_max_hp(self):
        """Update max HP based on equipped items"""
        base_hp = 100
        self.max_hp = base_hp + self.get_max_hp_bonus()
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp
    
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

        if random.random() < 0.05:  # 5% chance
            location_name = self.current_location.name
            boss_item = None
            for item_name, item in BOSS_ITEMS.items():
                if item.location == location_name:
                    # Special case: Kraken's Tooth only spawns after pirates defeated
                    if item_name == "Kraken's Tooth":
                        if "The Crimson Tide" not in self.defeated_bosses:
                            continue  # Skip Kraken's Tooth if pirates not defeated yet
                    
                    boss_item = item
                    break
            
            # Don't give boss item if already in inventory OR if boss already defeated
            if boss_item:
                already_have_item = boss_item.name in [i.name for i in self.boss_inventory]
                already_defeated = boss_item.boss.name in self.defeated_bosses
                
                if not already_have_item and not already_defeated:
                    self.boss_inventory.append(boss_item)
                    print(Fore.MAGENTA + f"\n⚡ You found a special item: {boss_item.name}! ⚡" + Style.RESET_ALL)
                    print(Fore.YELLOW + boss_item.description + Style.RESET_ALL)
                    time.sleep(2)
        
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
        
        minigame_choice = random.choice([button_mashing_minigame, timing_minigame, pattern_minigame])
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
        """Display player inventory (fish + boss items)"""
        self.clear_screen()

        # Header
        print(Fore.CYAN + "╔═══════════════════════════════════════╗" + Style.RESET_ALL)
        print(Fore.CYAN + "║             INVENTORY                 ║" + Style.RESET_ALL)
        print(Fore.CYAN + "╚═══════════════════════════════════════╝" + Style.RESET_ALL)
        print()

        # Empty check
        if not self.inventory and not self.boss_inventory:
            print(Fore.YELLOW + "Your inventory is empty. Go fishing!" + Style.RESET_ALL)
            print()
            input(Fore.CYAN + "Press Enter to go back..." + Style.RESET_ALL)
            return

        # === FISH INVENTORY ===
        if self.inventory:
            print(Fore.GREEN + "=== FISH ===" + Style.RESET_ALL)
            for i, fish in enumerate(self.inventory, 1):
                mutation_str = (
                    f"[{fish.mutation.upper()}]" if getattr(fish, "mutation", "normal") != "normal" else ""
                )
                print(
                    Fore.WHITE
                    + f"{i}. {fish.name} {mutation_str} - "
                    f"{fish.weight:.2f}kg - ${fish.sell_price}"
                    + Style.RESET_ALL
                )
            print()

        # === BOSS ITEMS ===
        if self.boss_inventory:
            print(Fore.MAGENTA + "=== BOSS ITEMS ===" + Style.RESET_ALL)
            for i, item in enumerate(self.boss_inventory, 1):
                print(Fore.YELLOW + f"{i}. {item.name}" + Style.RESET_ALL)
                print(Fore.LIGHTBLACK_EX + f"   {item.description}" + Style.RESET_ALL)
            print()

        # Total fish value
        if self.inventory:
            total_value = sum(f.sell_price for f in self.inventory)
            total_value = int(total_value * self.difficulty_mult)
            print(Fore.GREEN + f"Total fish value: ${total_value}" + Style.RESET_ALL)
            print()

        # Options
        print(Fore.CYAN + "Options:" + Style.RESET_ALL)
        print(Fore.WHITE + "[S]ell Fish | [K]eep as Trophy | [U]se Boss Item | [B]ack" + Style.RESET_ALL)

        choice = input(Fore.GREEN + "> " + Style.RESET_ALL).lower()

        if choice == 's':
            self.sell_fish()
        elif choice == 'k':
            self.keep_trophy()
        elif choice == 'u':
            self.use_boss_item()
        elif choice == 'b':
            return

    def sell_fish(self):
        """Sell fish from inventory"""
        if not self.inventory:
            print(Fore.YELLOW + "No fish to sell!" + Style.RESET_ALL)
            input(Fore.CYAN + "Press Enter to continue..." + Style.RESET_ALL)
            return
        
        self.clear_screen()
        print(Fore.CYAN + "╔═══════════════════════════════════════╗" + Style.RESET_ALL)
        print(Fore.CYAN + "║           SELL FISH                   ║" + Style.RESET_ALL)
        print(Fore.CYAN + "╚═══════════════════════════════════════╝" + Style.RESET_ALL)
        print()
        
        # Show fish
        for i, fish in enumerate(self.inventory, 1):
            mutation_str = (
                f"[{fish.mutation.upper()}]" if getattr(fish, "mutation", "normal") != "normal" else ""
            )
            sell_value = int(fish.sell_price * self.difficulty_mult)
            print(
                Fore.WHITE
                + f"{i}. {fish.name} {mutation_str} - "
                f"{fish.weight:.2f}kg - ${sell_value}"
                + Style.RESET_ALL
            )
        
        print()
        print(Fore.YELLOW + "[A]ll Fish | [S]pecific Fish | [B]ack" + Style.RESET_ALL)
        choice = input(Fore.GREEN + "> " + Style.RESET_ALL).lower()
        
        if choice == 'a':
            # Sell all fish
            total = sum(int(f.sell_price * self.difficulty_mult) for f in self.inventory)
            self.money += total
            count = len(self.inventory)
            self.inventory.clear()
            print(Fore.GREEN + f"Sold {count} fish for ${total}!" + Style.RESET_ALL)
            input(Fore.CYAN + "Press Enter to continue..." + Style.RESET_ALL)
        elif choice == 's':
            # Sell specific fish
            try:
                idx = int(input(Fore.CYAN + "Enter fish number: " + Style.RESET_ALL)) - 1
                if 0 <= idx < len(self.inventory):
                    fish = self.inventory.pop(idx)
                    value = int(fish.sell_price * self.difficulty_mult)
                    self.money += value
                    print(Fore.GREEN + f"Sold {fish.name} for ${value}!" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Invalid fish number!" + Style.RESET_ALL)
                input(Fore.CYAN + "Press Enter to continue..." + Style.RESET_ALL)
            except (ValueError, IndexError):
                print(Fore.RED + "Invalid input!" + Style.RESET_ALL)
                input(Fore.CYAN + "Press Enter to continue..." + Style.RESET_ALL)
    
    def keep_trophy(self):
        """Move a fish from inventory to trophy room"""
        if not self.inventory:
            print(Fore.YELLOW + "No fish to keep as trophy!" + Style.RESET_ALL)
            input(Fore.CYAN + "Press Enter to continue..." + Style.RESET_ALL)
            return
        
        self.clear_screen()
        print(Fore.CYAN + "╔═══════════════════════════════════════╗" + Style.RESET_ALL)
        print(Fore.CYAN + "║         KEEP AS TROPHY                ║" + Style.RESET_ALL)
        print(Fore.CYAN + "╚═══════════════════════════════════════╝" + Style.RESET_ALL)
        print()
        
        # Show fish
        for i, fish in enumerate(self.inventory, 1):
            mutation_str = (
                f"[{fish.mutation.upper()}]" if getattr(fish, "mutation", "normal") != "normal" else ""
            )
            print(
                Fore.WHITE
                + f"{i}. {fish.name} {mutation_str} - "
                f"{fish.weight:.2f}kg"
                + Style.RESET_ALL
            )
        
        print()
        try:
            idx = int(input(Fore.CYAN + "Enter fish number (0 to cancel): " + Style.RESET_ALL)) - 1
            if idx == -1:
                return
            if 0 <= idx < len(self.inventory):
                fish = self.inventory.pop(idx)
                self.trophy_room.append(fish)
                print(Fore.GREEN + f"{fish.name} added to trophy room!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Invalid fish number!" + Style.RESET_ALL)
            input(Fore.CYAN + "Press Enter to continue..." + Style.RESET_ALL)
        except (ValueError, IndexError):
            print(Fore.RED + "Invalid input!" + Style.RESET_ALL)
            input(Fore.CYAN + "Press Enter to continue..." + Style.RESET_ALL)
    
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
            print(Fore.CYAN + "3. Buy Combat Items ⚔️🛡️❤️" + Style.RESET_ALL)
            print(Fore.CYAN + "4. Repair Rod (${})".format(max(10, (100 - self.rod_durability) * 2)) + Style.RESET_ALL)
            print(Fore.CYAN + "5. Back" + Style.RESET_ALL)
            
            choice = input(Fore.YELLOW + "\nChoice: " + Style.RESET_ALL)
            
            if choice == '1':
                self.shop_rods()
            elif choice == '2':
                self.shop_baits()
            elif choice == '3':
                self.shop_combat_items()
            elif choice == '4':
                repair_cost = max(10, (100 - self.rod_durability) * 2)
                if self.money >= repair_cost:
                    self.money -= repair_cost
                    self.rod_durability = 100
                    print(Fore.GREEN + "Rod repaired to 100%!" + Style.RESET_ALL)
                    time.sleep(1)
                else:
                    print(Fore.RED + "Not enough money!" + Style.RESET_ALL)
                    time.sleep(1)
            elif choice == '5':
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
    
    def shop_combat_items(self):
        """Combat items shop with categories"""
        while True:
            self.clear_screen()
            print(Fore.RED + "═══ ⚔️ COMBAT ITEMS ⚔️ ═══" + Style.RESET_ALL)
            print(Fore.GREEN + f"💰 Money: ${self.money}" + Style.RESET_ALL)
            print()
            print(Fore.CYAN + "1. Attack Items ⚔️" + Style.RESET_ALL)
            print(Fore.CYAN + "2. Defense Items 🛡️" + Style.RESET_ALL)
            print(Fore.CYAN + "3. HP Items ❤️" + Style.RESET_ALL)
            print(Fore.CYAN + "4. View/Equip Items" + Style.RESET_ALL)
            print(Fore.CYAN + "5. Back" + Style.RESET_ALL)
            
            choice = input(Fore.YELLOW + "\nChoice: " + Style.RESET_ALL)
            
            if choice == '1':
                self.shop_combat_category('attack', COMBAT_ITEMS_ATTACK, "⚔️ ATTACK ITEMS ⚔️")
            elif choice == '2':
                self.shop_combat_category('defense', COMBAT_ITEMS_DEFENSE, "🛡️ DEFENSE ITEMS 🛡️")
            elif choice == '3':
                self.shop_combat_category('hp', COMBAT_ITEMS_HP, "❤️ HP ITEMS ❤️")
            elif choice == '4':
                self.equip_combat_items()
            elif choice == '5':
                break
    
    def shop_combat_category(self, category, items_list, title):
        """Shop for a specific combat item category"""
        self.clear_screen()
        print(Fore.RED + f"═══ {title} ═══" + Style.RESET_ALL)
        print(Fore.GREEN + f"💰 Money: ${self.money}" + Style.RESET_ALL)
        print()
        
        for i, item in enumerate(items_list, 1):
            owned = "✓ Owned" if item in self.owned_combat_items[category] else f"${item.price}"
            equipped = "⭐ EQUIPPED" if item == self.equipped_combat_items[category] else ""
            locked = "" if self.level >= item.unlock_level else f"🔒 Lvl{item.unlock_level}"
            print(f"{i}. {item.name} - {owned} {locked} {equipped}")
            print(f"   {item.description}")
        
        print()
        choice = input(Fore.CYAN + "Buy item (number) or 0 to cancel: " + Style.RESET_ALL)
        
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(items_list):
                item = items_list[idx]
                if self.level < item.unlock_level:
                    print(Fore.RED + f"Requires level {item.unlock_level}!" + Style.RESET_ALL)
                    time.sleep(1)
                elif item in self.owned_combat_items[category]:
                    print(Fore.YELLOW + "You already own this item!" + Style.RESET_ALL)
                    time.sleep(1)
                elif self.money >= item.price:
                    self.money -= item.price
                    self.owned_combat_items[category].append(item)
                    print(Fore.GREEN + f"Bought {item.name}!" + Style.RESET_ALL)
                    time.sleep(1)
                else:
                    print(Fore.RED + "Not enough money!" + Style.RESET_ALL)
                    time.sleep(1)
        except ValueError:
            pass
    
    def equip_combat_items(self):
        """Equip owned combat items"""
        self.clear_screen()
        print(Fore.YELLOW + "═══ EQUIP COMBAT ITEMS ═══" + Style.RESET_ALL)
        print()
        
        # Show currently equipped
        print(Fore.CYAN + "Currently Equipped:" + Style.RESET_ALL)
        attack_equipped = self.equipped_combat_items['attack'].name if self.equipped_combat_items['attack'] else "None"
        defense_equipped = self.equipped_combat_items['defense'].name if self.equipped_combat_items['defense'] else "None"
        hp_equipped = self.equipped_combat_items['hp'].name if self.equipped_combat_items['hp'] else "None"
        
        print(f"⚔️  Attack: {attack_equipped} (+{self.get_attack_bonus()})")
        print(f"🛡️  Defense: {defense_equipped} (+{self.get_defense_bonus()})")
        print(f"❤️  HP: {hp_equipped} (+{self.get_max_hp_bonus()}, Max HP: {self.max_hp})")
        print()
        
        print(Fore.CYAN + "1. Equip Attack Item" + Style.RESET_ALL)
        print(Fore.CYAN + "2. Equip Defense Item" + Style.RESET_ALL)
        print(Fore.CYAN + "3. Equip HP Item" + Style.RESET_ALL)
        print(Fore.CYAN + "4. Back" + Style.RESET_ALL)
        
        choice = input(Fore.YELLOW + "\nChoice: " + Style.RESET_ALL)
        
        if choice == '1':
            self.equip_item_category('attack', "⚔️ ATTACK")
        elif choice == '2':
            self.equip_item_category('defense', "🛡️ DEFENSE")
        elif choice == '3':
            self.equip_item_category('hp', "❤️ HP")
    
    def equip_item_category(self, category, title):
        """Equip an item from a specific category"""
        if not self.owned_combat_items[category]:
            print(Fore.YELLOW + f"You don't own any {title} items yet!" + Style.RESET_ALL)
            time.sleep(1)
            return
        
        self.clear_screen()
        print(Fore.YELLOW + f"═══ EQUIP {title} ITEM ═══" + Style.RESET_ALL)
        print()
        
        for i, item in enumerate(self.owned_combat_items[category], 1):
            equipped = "⭐ EQUIPPED" if item == self.equipped_combat_items[category] else ""
            print(f"{i}. {item.name} {equipped}")
            print(f"   {item.description}")
        
        print(f"{len(self.owned_combat_items[category]) + 1}. Unequip")
        print()
        choice = input(Fore.CYAN + "Equip which item? " + Style.RESET_ALL)
        
        try:
            idx = int(choice) - 1
            if idx == len(self.owned_combat_items[category]):
                # Unequip
                self.equipped_combat_items[category] = None
                if category == 'hp':
                    self.update_max_hp()
                print(Fore.GREEN + f"Unequipped {title} item!" + Style.RESET_ALL)
                time.sleep(1)
            elif 0 <= idx < len(self.owned_combat_items[category]):
                item = self.owned_combat_items[category][idx]
                self.equipped_combat_items[category] = item
                if category == 'hp':
                    self.update_max_hp()
                print(Fore.GREEN + f"Equipped {item.name}!" + Style.RESET_ALL)
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
        # Check if Pirate Captain is available
        if "The Crimson Tide" in self.defeated_bosses and self.karma > 0:
            # Show pirate captain option
            self.clear_screen()
            print(Fore.CYAN + "╔═══════════════════════════════════════╗" + Style.RESET_ALL)
            print(Fore.CYAN + "║              THE DOCKS                ║" + Style.RESET_ALL)
            print(Fore.CYAN + "╚═══════════════════════════════════════╝" + Style.RESET_ALL)
            print()
            print(Fore.YELLOW + "🏴‍☠️ The Crimson Tide is moored at the dock!" + Style.RESET_ALL)
            print()
            print(Fore.WHITE + "1. Travel to other locations" + Style.RESET_ALL)
            print(Fore.WHITE + "2. Talk to Captain Redbeard" + Style.RESET_ALL)
            print(Fore.LIGHTBLACK_EX + "3. Leave" + Style.RESET_ALL)
            
            choice = input(Fore.CYAN + "\nYour choice: " + Style.RESET_ALL)
            
            if choice == '1':
                world_map = WorldMap(self)
                return world_map.run()
            elif choice == '2':
                self.interact_with_pirate_captain()
                return None
            else:
                return None
        else:
            # Normal dock behavior
            world_map = WorldMap(self)
            return world_map.run()
    
    def interact_with_pirate_captain(self):
        """Talk to Captain Redbeard after sparing the pirate ship"""
        while True:
            self.clear_screen()
            
            pirate_art = """
            🏴‍☠️ Captain Redbeard - The Crimson Tide 🏴‍☠️
            
                     ___
                   _/   \\_
                  / | @ @|\\
                 |  |  >  ||     "Freedom or death!"
                  \\ | === |/
                   \\|_____|
                    |     |
                   _|_____|_
                  /   ⚓⚓   \\
                 |  CAPTAIN  |
                 |  REDBEARD |
                  \\__________/
            """
            
            print(Fore.RED + pirate_art + Style.RESET_ALL)
            print()
            
            if random.random() < 0.3:
                greetings = [
                    "Ahoy, matey! Welcome aboard!",
                    "Well met, friend! Ready to strike back at AquaTech?",
                    "Aye, there ye are! Our rebel ally!",
                    "Welcome to the Crimson Tide, comrade!",
                    "Good to see ye! The seas need more like you.",
                ]
                print(Fore.GREEN + random.choice(greetings) + Style.RESET_ALL)
                print()
            
            print(Fore.YELLOW + "What would you like to discuss?" + Style.RESET_ALL)
            print()
            print(Fore.WHITE + "1. Ask about AquaTech Industries" + Style.RESET_ALL)
            print(Fore.WHITE + "2. Ask about the rebellion" + Style.RESET_ALL)
            print(Fore.WHITE + "3. Ask about pirate life" + Style.RESET_ALL)
            print(Fore.WHITE + "4. Get a gift from the captain" + Style.RESET_ALL)
            print(Fore.LIGHTBLACK_EX + "5. Leave" + Style.RESET_ALL)
            print()
            
            choice = input(Fore.CYAN + "Your choice: " + Style.RESET_ALL)
            
            if choice == '1':
                self.clear_screen()
                print(Fore.RED + pirate_art + Style.RESET_ALL)
                print()
                print(Fore.RED + "Captain Redbeard:" + Style.RESET_ALL)
                print(Fore.WHITE + "\"AquaTech... those corporate scoundrels.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"They claim they're 'managing the seas responsibly.'\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"But we know the truth - they're plunderin' everything!\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"Overfishing, pollution, drivin' out the guardians...\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"We were fishermen once, honest folk.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"But when they seized our ancestral waters...\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.RED + "\"We became pirates. Rebels. Defenders of the free seas!\"" + Style.RESET_ALL)
                time.sleep(2)
                print()
                print(Fore.LIGHTBLACK_EX + "Press any key to continue..." + Style.RESET_ALL)
                get_key()
                
            elif choice == '2':
                self.clear_screen()
                print(Fore.RED + pirate_art + Style.RESET_ALL)
                print()
                print(Fore.RED + "Captain Redbeard:" + Style.RESET_ALL)
                print(Fore.WHITE + "\"The rebellion grows stronger every day!\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"Ships from all corners join our cause.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"Even some of the guardians ye spared have blessed us.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"Together, we'll break AquaTech's stranglehold!\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"The seas belong to all, not just the highest bidder!\"" + Style.RESET_ALL)
                time.sleep(2)
                print()
                print(Fore.LIGHTBLACK_EX + "Press any key to continue..." + Style.RESET_ALL)
                get_key()
                
            elif choice == '3':
                self.clear_screen()
                print(Fore.RED + pirate_art + Style.RESET_ALL)
                print()
                print(Fore.RED + "Captain Redbeard:" + Style.RESET_ALL)
                print(Fore.WHITE + "\"Aye, the pirate life! Freedom on the open water!\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"No corporate overlords tellin' us what to do.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"We fish where we want, sail where we please.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"It's dangerous, sure. But it's OURS.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"Every sunrise on deck is worth the risk!\"" + Style.RESET_ALL)
                time.sleep(2)
                print()
                print(Fore.LIGHTBLACK_EX + "Press any key to continue..." + Style.RESET_ALL)
                get_key()
                
            elif choice == '4':
                self.clear_screen()
                print(Fore.RED + pirate_art + Style.RESET_ALL)
                print()
                
                # Check if already received gift
                if self.received_pirate_gift:
                    print(Fore.RED + "Captain Redbeard:" + Style.RESET_ALL)
                    print(Fore.WHITE + "\"Ye already got yer share of the booty, matey!\"" + Style.RESET_ALL)
                    time.sleep(1)
                    print(Fore.WHITE + "\"Can't be givin' away all our treasure now, can we?\"" + Style.RESET_ALL)
                    time.sleep(1.5)
                    print(Fore.YELLOW + "\"But yer always welcome aboard the Crimson Tide!\"" + Style.RESET_ALL)
                    time.sleep(1.5)
                else:
                    # Give reward based on karma
                    if self.karma >= 3:
                        reward = random.randint(200, 500)
                        self.money += reward
                        print(Fore.RED + "Captain Redbeard:" + Style.RESET_ALL)
                        print(Fore.WHITE + "\"Ye've proven yerself a true friend of the rebellion!\"" + Style.RESET_ALL)
                        time.sleep(1)
                        print(Fore.YELLOW + f"\"Take this - {reward} gold pieces from our latest raid!\"" + Style.RESET_ALL)
                        print(Fore.GREEN + f"+${reward} received!" + Style.RESET_ALL)
                        self.received_pirate_gift = True
                    else:
                        reward = random.randint(50, 150)
                        self.money += reward
                        print(Fore.RED + "Captain Redbeard:" + Style.RESET_ALL)
                        print(Fore.WHITE + "\"Here, have some coin for the road, mate!\"" + Style.RESET_ALL)
                        print(Fore.GREEN + f"+${reward} received!" + Style.RESET_ALL)
                        self.received_pirate_gift = True
                
                time.sleep(2)
                print()
                print(Fore.LIGHTBLACK_EX + "Press any key to continue..." + Style.RESET_ALL)
                get_key()
                
            elif choice == '5':
                break
            else:
                print(Fore.RED + "Invalid choice!" + Style.RESET_ALL)
                time.sleep(1)
    
    def interact_with_npc_fisherman(self):
        """Talk to the NPC fisherman and get a random fact"""
        while True:  # Keep dialog open until player chooses to leave
            self.clear_screen()
            
            # Display ASCII art of fisherman
            fisherman_art = """
            
                🎣 Old Fisherman by the Lake 🎣
            
                   ,@@@@@@@,
             ,,,.   ,@@@@@@/@@,  .oo8888o.
          ,&%%&%&&%,@@@@@/@@@@@@,8888\\88/8o
         ,%&\\%&&%&&%,@@@\\@@@/@@@88\\88888/88'
         %&&%&%&/%&&%@@\\@@/ /@@@88888\\88888'
         %&&%/ %&%%&&@@\\ V /@@' `88\\8 `/88'
         `&%\\ ` /%&'    |.|        \\ '|8'
             |o|        | |         | |
             |.|        | |         | |
          \\/ ._\\//_/__/  ,\\_//__\\/.  \\_//__/_
            """
            
            print(Fore.CYAN + fisherman_art + Style.RESET_ALL)
            print()
            
            # Greeting only on first interaction (or randomly)
            if random.random() < 0.3:
                greetings = [
                    "Ahoy there, young angler!",
                    "Well, well… another fisher visits my spot!",
                    "Greetings, friend! Beautiful day for fishing, eh?",
                    "Ah, a fellow fisher! Come, sit a spell.",
                    "Welcome to my humble fishing spot.",
                    "The water speaks to those patient enough to listen.",
                    "Fish aren't caught with strength alone — calm hands matter more.",
                ]
                print(Fore.GREEN + random.choice(greetings) + Style.RESET_ALL)
                print()
            
            # Dialog menu
            print(Fore.YELLOW + "What would you like to talk about?" + Style.RESET_ALL)
            print()
            print(Fore.WHITE + "1. Ask for fishing wisdom" + Style.RESET_ALL)
            print(Fore.WHITE + "2. Ask about the lake" + Style.RESET_ALL)
            print(Fore.WHITE + "3. Ask about the dangerous creatures" + Style.RESET_ALL)
            print(Fore.WHITE + "4. Ask about recent troubles" + Style.RESET_ALL)
            print(Fore.LIGHTBLACK_EX + "5. Leave" + Style.RESET_ALL)
            print()
            
            choice = input(Fore.CYAN + "Your choice: " + Style.RESET_ALL)
            
            if choice == '1':
                # Random fishing fact/wisdom
                self.clear_screen()
                print(Fore.CYAN + fisherman_art + Style.RESET_ALL)
                print()
                fact = get_random_fact()
                print(Fore.GREEN + "Old Fisherman:" + Style.RESET_ALL)
                print(Fore.WHITE + f"\"Did you know? {fact}\"" + Style.RESET_ALL)
                print()
                time.sleep(2)
                print(Fore.LIGHTBLACK_EX + "Press any key to continue..." + Style.RESET_ALL)
                get_key()
                
            elif choice == '2':
                # Talk about the lake
                self.clear_screen()
                print(Fore.CYAN + fisherman_art + Style.RESET_ALL)
                print()
                print(Fore.GREEN + "Old Fisherman:" + Style.RESET_ALL)
                print(Fore.WHITE + "\"This lake... I've fished here for nigh on fifty years.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"My father fished here, and his father before him.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"The waters run deep, deeper than most folk realize.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"There's old magic here. Ancient things that keep the balance.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print()
                print(Fore.LIGHTBLACK_EX + "Press any key to continue..." + Style.RESET_ALL)
                get_key()
                
            elif choice == '3':
                # Talk about the guardians/protectors
                self.clear_screen()
                print(Fore.CYAN + fisherman_art + Style.RESET_ALL)
                print()
                print(Fore.GREEN + "Old Fisherman:" + Style.RESET_ALL)
                print(Fore.WHITE + "\"Ah, you've encountered them, have you?\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"Those great beasts... most call them monsters, threats to be eliminated.\"" + Style.RESET_ALL)
                time.sleep(2)
                print(Fore.YELLOW + "\"But they're not monsters at all. They're guardians.\"" + Style.RESET_ALL)
                time.sleep(2)
                print(Fore.WHITE + "\"Each one watches over its domain, keeping the natural order.\"" + Style.RESET_ALL)
                time.sleep(2)
                print(Fore.WHITE + "\"The great serpent in this lake, for instance...\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"She's been here longer than human memory. Protects the waters from corruption.\"" + Style.RESET_ALL)
                time.sleep(2)
                print()
                print(Fore.CYAN + "\"But lately... they've been different. Aggressive. Desperate, even.\"" + Style.RESET_ALL)
                time.sleep(2)
                print(Fore.CYAN + "\"Something's got them riled up fierce.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print()
                print(Fore.LIGHTBLACK_EX + "Press any key to continue..." + Style.RESET_ALL)
                get_key()
                
            elif choice == '4':
                # Talk about the corporation
                self.clear_screen()
                print(Fore.CYAN + fisherman_art + Style.RESET_ALL)
                print()
                print(Fore.GREEN + "Old Fisherman:" + Style.RESET_ALL)
                time.sleep(0.5)
                print(Fore.WHITE + "*The old man's expression darkens*" + Style.RESET_ALL)
                time.sleep(1.5)
                print()
                print(Fore.RED + "\"AquaTech Industries.\"" + Style.RESET_ALL)
                time.sleep(2)
                print(Fore.WHITE + "\"Big corporation out of the city. Been sending suits around here for months.\"" + Style.RESET_ALL)
                time.sleep(2)
                print(Fore.WHITE + "\"Want to buy up the lake. 'Development opportunities,' they call it.\"" + Style.RESET_ALL)
                time.sleep(2)
                print(Fore.YELLOW + "\"Luxury resorts. Industrial fishing operations. 'Eco-tourism.'\"" + Style.RESET_ALL)
                time.sleep(2)
                print(Fore.WHITE + "\"Bah! They don't care about this place. Just want to drain it dry.\"" + Style.RESET_ALL)
                time.sleep(2)
                print()
                print(Fore.CYAN + "\"The guardians know. They can sense it.\"" + Style.RESET_ALL)
                time.sleep(2)
                print(Fore.CYAN + "\"That's why they've been so aggressive lately - they're trying to protect their homes.\"" + Style.RESET_ALL)
                time.sleep(2)
                print(Fore.WHITE + "\"AquaTech's been sending 'specialists' to deal with the 'problem wildlife.'\"" + Style.RESET_ALL)
                time.sleep(2)
                print(Fore.WHITE + "\"But those creatures... they're not the problem. Never were.\"" + Style.RESET_ALL)
                time.sleep(2)
                print()
                print(Fore.LIGHTYELLOW_EX + "*He sighs heavily*" + Style.RESET_ALL)
                time.sleep(1.5)
                print()
                print(Fore.GREEN + "\"I've been refusing to sell my fishing rights, but I'm just one old man.\"" + Style.RESET_ALL)
                time.sleep(2)
                print(Fore.GREEN + "\"If they get the lake... everything changes. Forever.\"" + Style.RESET_ALL)
                time.sleep(2)
                print()
                print(Fore.LIGHTBLACK_EX + "Press any key to continue..." + Style.RESET_ALL)
                get_key()
                
            elif choice == '5':
                # Leave
                self.clear_screen()
                print(Fore.CYAN + fisherman_art + Style.RESET_ALL)
                print()
                farewell = [
                    "\"Tight lines, friend. May the waters be kind to you.\"",
                    "\"Be safe out there. The guardians remember kindness.\"",
                    "\"Come back anytime. These old bones enjoy the company.\"",
                    "\"Fish well, and respect the waters. They're watching.\"",
                ]
                print(Fore.GREEN + "Old Fisherman:" + Style.RESET_ALL)
                print(Fore.WHITE + random.choice(farewell) + Style.RESET_ALL)
                print()
                time.sleep(1.5)
                print(Fore.LIGHTBLACK_EX + "Press any key to continue..." + Style.RESET_ALL)
                get_key()
                break
            else:
                # Invalid choice - loop again
                continue
    
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
            print(Fore.WHITE + "🏪 Shop | 🏛️ Aquarium | 📋 Quests | 🏠 Home | ⚓ Dock | 🎣 NPC | ⊙ Fish Spot | ◉ Golden Spot" + Style.RESET_ALL)
            if self.debug_mode:
                    print(Fore.MAGENTA + "[DEV] [B]oss Menu | [WASD] Move | [E] Interact | [I] Inventory | [C] Stats | [Q] Quit" + Style.RESET_ALL)
            else:
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
                if hub_map.is_npc_fisherman(hub_map.player_x, hub_map.player_y):
                    # Talk to the NPC fisherman
                    self.interact_with_npc_fisherman()
                elif hub_map.is_fishing_spot(hub_map.player_x, hub_map.player_y):
                    is_golden = hub_map.is_golden_spot(hub_map.player_x, hub_map.player_y)
                    
                    # Determine which location based on water type
                    water_type = hub_map.get_water_type(hub_map.player_x, hub_map.player_y)
                    original_location = self.current_location
                    
                    if water_type == 'river':
                        target_location = LOCATIONS[1]  # Hub Island - Swift River
                    elif water_type == 'lake':
                        target_location = LOCATIONS[0]  # Hub Island - Calm Lake
                    else:
                        target_location = self.current_location
                    
                    # Check if this location requires a boss to be defeated
                    required_boss = LOCATION_BOSS_REQUIREMENTS.get(target_location.name)
                    if required_boss and required_boss not in self.defeated_bosses:
                        hub_map.message = f"🔒 {target_location.name} is blocked! You must defeat {required_boss} first!"
                        print(Fore.RED + hub_map.message + Style.RESET_ALL)
                        time.sleep(1.5)
                    else:
                        # Allowed to fish here
                        self.current_location = target_location
                        self.fish(golden_spot=is_golden)
                    
                    # Restore original location
                    self.current_location = original_location
                    
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
            elif key == 'b' and self.debug_mode:
                self.dev_boss_menu()
    
    def explore_remote_location(self, location):
        """Explore a remote location (Ocean, Deep Sea, etc.)"""
        # Set current location so fishing uses the correct fish pool
        old_location = self.current_location
        self.current_location = location
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
                    
                    # For Hub Island locations, check water type to ensure correct fish pool
                    target_location = location
                    if location.name in ["Hub Island - Calm Lake", "Hub Island - Swift River"]:
                        water_type = location_map.get_water_type(location_map.player_x, location_map.player_y)
                        if water_type == 'river':
                            target_location = LOCATIONS[1]  # Hub Island - Swift River
                        elif water_type == 'lake':
                            target_location = LOCATIONS[0]  # Hub Island - Calm Lake
                    
                    # Check if this location requires a boss to be defeated
                    required_boss = LOCATION_BOSS_REQUIREMENTS.get(target_location.name)
                    if required_boss and required_boss not in self.defeated_bosses:
                        location_map.message = f"🔒 {target_location.name} is blocked! You must defeat {required_boss} first!"
                        print(Fore.RED + location_map.message + Style.RESET_ALL)
                        time.sleep(1.5)
                    else:
                        self.current_location = target_location
                        self.fish(golden_spot=is_golden)
                    
                    # Restore location after fishing
                    self.current_location = location
                else:
                    location_map.message = "You need to be in water to fish!"
            elif key == 'q':
                # Return to previous location
                self.current_location = old_location
                break

    def start_boss_fight(self, boss):
        """Undertale-style boss fight system"""
        self.clear_screen()
        
        # Reset boss HP for new fight
        boss.hp = boss.max_hp
        boss.mercy_level = 0
        boss.is_spareable = False
        
        # Reset player HP
        self.current_hp = self.max_hp
        
        # Dramatic entrance animation
        print()
        print()
        for _ in range(3):
            print(Fore.RED + "!" * 60 + Style.RESET_ALL)
            time.sleep(0.2)
            sys.stdout.write("\r" + " " * 60 + "\r")
            sys.stdout.flush()
            time.sleep(0.2)
        
        print()
        
        # Show boss appearing line by line
        print(Fore.RED + "=" * 60 + Style.RESET_ALL)
        boss_lines = boss.ascii_art.split('\n')
        for line in boss_lines:
            print(Fore.YELLOW + line + Style.RESET_ALL)
            time.sleep(0.08)
        print(Fore.RED + "=" * 60 + Style.RESET_ALL)
        print()
        
        # Boss name reveal
        name_frames = [
            ".",
            "..",
            "...",
            f"... {boss.name[0]}",
            f"... {boss.name[:5]}",
            f"... {boss.name[:10]}",
            f"... {boss.name}!",
        ]
        
        for frame in name_frames:
            sys.stdout.write("\r" + Fore.RED + frame + Style.RESET_ALL)
            sys.stdout.flush()
            time.sleep(0.2)
        
        print("\n")
        
        for line in boss.get_dialogue("intro"):
            print(Fore.CYAN + line + Style.RESET_ALL)
            time.sleep(1)
        
        input(Fore.LIGHTBLACK_EX + "\nPress Enter to begin battle..." + Style.RESET_ALL)
        
        # Battle loop
        while boss.hp > 0 and self.current_hp > 0:
            self.clear_screen()
            
            # Display battle status
            print(Fore.RED + "=" * 60 + Style.RESET_ALL)
            print(Fore.YELLOW + f"{boss.name}" + Style.RESET_ALL)
            print(Fore.RED + f"HP: {'❤' * (boss.hp * 20 // boss.max_hp)}{'♡' * (20 - (boss.hp * 20 // boss.max_hp))} {boss.hp}/{boss.max_hp}" + Style.RESET_ALL)
            if boss.is_spareable:
                print(Fore.YELLOW + "⭐ * The monster can be SPARED *" + Style.RESET_ALL)
            print()
            print(Fore.GREEN + f"You" + Style.RESET_ALL)
            print(Fore.GREEN + f"HP: {'❤' * (self.current_hp * 20 // self.max_hp)}{'♡' * (20 - (self.current_hp * 20 // self.max_hp))} {self.current_hp}/{self.max_hp}" + Style.RESET_ALL)
            print(Fore.RED + "=" * 60 + Style.RESET_ALL)
            print()
            
            # Player turn
            print(Fore.CYAN + "What do you do?" + Style.RESET_ALL)
            print(Fore.WHITE + "[F]ight | [A]ct | [S]pare | [R]un" + Style.RESET_ALL)
            
            action = input(Fore.GREEN + "> " + Style.RESET_ALL).lower()
            
            if action == 'f':
                # Fight with attack animation AND minigame!
                print()
                
                # Undertale-style attack minigame (adjusted by difficulty)
                damage_multiplier = undertale_attack_minigame(self.stats['strength'], self.difficulty_name)
                
                # Show attack animation
                attack_frames = [
                    "    ⚔️         ",
                    "      ⚔️       ",
                    "        ⚔️     ",
                    "          ⚔️   ",
                    "            ⚔️ ",
                    "          💥  ",
                ]
                
                for frame in attack_frames:
                    sys.stdout.write("\r" + Fore.YELLOW + frame + Style.RESET_ALL)
                    sys.stdout.flush()
                    time.sleep(0.1)
                
                print()
                
                # Calculate damage with multiplier from minigame
                base_damage = random.randint(15, 25) + (self.stats['strength'] * 2) + self.get_attack_bonus()
                damage = int(base_damage * damage_multiplier)
                actual_damage = boss.take_damage(damage)
                
                # Flash damage number with color based on hit quality
                damage_color = Fore.RED
                if damage_multiplier >= 2.0:
                    damage_color = Fore.LIGHTMAGENTA_EX  # Critical
                elif damage_multiplier >= 1.5:
                    damage_color = Fore.YELLOW  # Good
                elif damage_multiplier < 1.0:
                    damage_color = Fore.LIGHTBLACK_EX  # Weak
                
                for _ in range(2):
                    print(damage_color + f"        -{actual_damage} HP!" + Style.RESET_ALL)
                    time.sleep(0.1)
                    sys.stdout.write("\r" + " " * 30 + "\r")
                    sys.stdout.flush()
                    time.sleep(0.1)
                
                print(damage_color + f"You dealt {actual_damage} damage!" + Style.RESET_ALL)
                time.sleep(0.8)
                
                # Boss reaction
                for line in boss.get_dialogue("hit"):
                    print(Fore.YELLOW + line + Style.RESET_ALL)
                    time.sleep(0.8)
                
            elif action == 'a':
                # Act (mercy option)
                print()
                print(Fore.CYAN + "You try to calm the monster..." + Style.RESET_ALL)
                boss.mercy_level += 1
                time.sleep(1)
                
                for line in boss.get_dialogue("merciful"):
                    print(Fore.YELLOW + line + Style.RESET_ALL)
                    time.sleep(0.8)
                
            elif action == 's':
                # Spare
                if boss.is_spareable:
                    # Boss spared - celebration animation!
                    self.clear_screen()
                    
                    # Sparkling mercy animation
                    mercy_frames = [
                        "     ✨              ",
                        "   ✨  ✨            ",
                        " ✨  💚  ✨          ",
                        "✨  MERCY  ✨        ",
                        "  ✨  💚  ✨         ",
                        "    ✨  ✨           ",
                        "      ✨             ",
                    ]
                    
                    for frame in mercy_frames:
                        sys.stdout.write("\r" + Fore.YELLOW + frame + Style.RESET_ALL)
                        sys.stdout.flush()
                        time.sleep(0.2)
                    
                    print("\n")
                    
                    print(Fore.YELLOW + "=" * 60 + Style.RESET_ALL)
                    for line in boss.get_dialogue("spared"):
                        print(Fore.GREEN + line + Style.RESET_ALL)
                        time.sleep(1)
                    print(Fore.YELLOW + "=" * 60 + Style.RESET_ALL)
                    
                    # Rewards for sparing
                    self.karma += 10
                    reward_xp = 500
                    reward_money = 1000
                    self.gain_xp(reward_xp)
                    self.money += reward_money
                    
                    print()
                    print(Fore.GREEN + f"You gained {reward_xp} XP and ${reward_money}!" + Style.RESET_ALL)
                    print(Fore.MAGENTA + f"Karma +10 (Total: {self.karma})" + Style.RESET_ALL)
                    
                    # Mark boss as defeated
                    if boss.name not in self.defeated_bosses:
                        self.defeated_bosses.append(boss.name)
                    
                    input(Fore.LIGHTBLACK_EX + "\nPress Enter to continue..." + Style.RESET_ALL)
                    return
                else:
                    print()
                    print(Fore.YELLOW + "The monster isn't ready to be spared yet..." + Style.RESET_ALL)
                    time.sleep(1)
            
            elif action == 'r':
                # Run away
                if random.random() < 0.5:
                    print()
                    print(Fore.YELLOW + "You escaped!" + Style.RESET_ALL)
                    time.sleep(1)
                    return
                else:
                    print()
                    print(Fore.RED + "You couldn't escape!" + Style.RESET_ALL)
                    time.sleep(1)
            
            # Check if boss defeated
            if boss.hp <= 0:
                # Boss killed - dramatic animation
                self.clear_screen()
                
                # Fading animation
                defeat_art = """
                    ╔═══════════════════════════════════╗
                    ║                                   ║
                    ║          BOSS DEFEATED            ║
                    ║                                   ║
                    ╚═══════════════════════════════════╝
                """
                
                for intensity in range(5):
                    self.clear_screen()
                    if intensity % 2 == 0:
                        print(Fore.RED + defeat_art + Style.RESET_ALL)
                    else:
                        print(Fore.LIGHTBLACK_EX + defeat_art + Style.RESET_ALL)
                    time.sleep(0.2)
                
                self.clear_screen()
                print(Fore.RED + "=" * 60 + Style.RESET_ALL)
                for line in boss.get_dialogue("killed"):
                    print(Fore.RED + line + Style.RESET_ALL)
                    time.sleep(1)
                print(Fore.RED + "=" * 60 + Style.RESET_ALL)
                
                # Negative karma
                self.karma -= 15
                reward_xp = 300
                reward_money = 500
                self.gain_xp(reward_xp)
                self.money += reward_money
                
                print()
                print(Fore.GREEN + f"You gained {reward_xp} XP and ${reward_money}." + Style.RESET_ALL)
                print(Fore.RED + f"Karma -15 (Total: {self.karma})" + Style.RESET_ALL)
                
                # Mark boss as defeated
                if boss.name not in self.defeated_bosses:
                    self.defeated_bosses.append(boss.name)
                
                input(Fore.LIGHTBLACK_EX + "\nPress Enter to continue..." + Style.RESET_ALL)
                return
            
            # Boss turn
            input(Fore.LIGHTBLACK_EX + "\nPress Enter for enemy attack..." + Style.RESET_ALL)
            print()
            print(Fore.RED + f"{boss.name}'s turn!" + Style.RESET_ALL)
            time.sleep(1)
            
            # Get random attack
            attack = boss.get_random_attack()
            print(Fore.YELLOW + f"{boss.name} uses {attack.name}!" + Style.RESET_ALL)
            print(Fore.LIGHTBLACK_EX + attack.description + Style.RESET_ALL)
            print()
            time.sleep(1)
            
            # Execute attack pattern
            damage_taken = attack.execute()
            
            if damage_taken > 0:
                # Apply defense reduction
                defense_bonus = self.get_defense_bonus()
                damage_taken = max(1, damage_taken - defense_bonus)  # Minimum 1 damage
                
                self.current_hp -= damage_taken
                print()
                
                # Screen shake effect
                shake_frames = ["💔", "  💔", "    💔", "  💔", "💔"]
                for frame in shake_frames:
                    sys.stdout.write("\r" + Fore.RED + frame + Style.RESET_ALL)
                    sys.stdout.flush()
                    time.sleep(0.08)
                
                print()
                
                # Flash damage
                for _ in range(3):
                    print(Fore.RED + f"    YOU TOOK {damage_taken} DAMAGE!" + Style.RESET_ALL)
                    time.sleep(0.1)
                    sys.stdout.write("\r" + " " * 40 + "\r")
                    sys.stdout.flush()
                    time.sleep(0.1)
                
                print(Fore.RED + f"You took {damage_taken} damage!" + Style.RESET_ALL)
                time.sleep(0.5)
            
            # Check low HP dialogue
            hp_percent = (boss.hp / boss.max_hp) * 100
            if hp_percent < 40:
                for line in boss.get_dialogue("low_hp"):
                    print(Fore.YELLOW + line + Style.RESET_ALL)
                    time.sleep(0.8)
            
            # Check if player defeated
            if self.current_hp <= 0:
                self.clear_screen()
                
                # Defeat animation
                defeat_frames = [
                    "  YOU",
                    "  YOU  ",
                    "  YOU   WERE",
                    "  YOU   WERE   ",
                    "  YOU   WERE   DEFEATED...",
                ]
                
                for frame in defeat_frames:
                    sys.stdout.write("\r" + Fore.RED + frame + Style.RESET_ALL)
                    sys.stdout.flush()
                    time.sleep(0.3)
                
                print("\n")
                time.sleep(0.5)
                
                print(Fore.RED + "=" * 60 + Style.RESET_ALL)
                print(Fore.RED + "         💀 GAME OVER 💀         " + Style.RESET_ALL)
                print(Fore.RED + "=" * 60 + Style.RESET_ALL)
                
                # Restore HP and return
                self.current_hp = self.max_hp
                #take 15% of money as penalty for losing
                penalty = int(self.money * 0.15)
                self.money -= penalty
                print(Fore.YELLOW + f"You lost ${penalty}!" + Style.RESET_ALL)
                #take some fish too
                if self.inventory:
                    lost_fish = random.sample(self.inventory, min(3, len(self.inventory)))
                    for fish in lost_fish:
                        self.inventory.remove(fish)
                    print(Fore.YELLOW + f"You lost {len(lost_fish)} fish from your inventory!" + Style.RESET_ALL)
                
                input(Fore.LIGHTBLACK_EX + "\nPress Enter to continue..." + Style.RESET_ALL)
                return
            
            input(Fore.LIGHTBLACK_EX + "\nPress Enter to continue..." + Style.RESET_ALL)
    
    def use_boss_item(self):
        """Use a boss item to trigger boss fight"""
        if not self.boss_inventory:
            print(Fore.YELLOW + "No boss items to use!" + Style.RESET_ALL)
            return
        
        print(Fore.CYAN + "Enter boss item number to use:" + Style.RESET_ALL)
        choice = input(Fore.GREEN + "> " + Style.RESET_ALL)
        
        try:
            index = int(choice) - 1
            if 0 <= index < len(self.boss_inventory):
                boss_item = self.boss_inventory[index]
                
                # Check if boss already defeated
                if boss_item.boss.name in self.defeated_bosses:
                    print(Fore.YELLOW + f"You've already defeated {boss_item.boss.name}!" + Style.RESET_ALL)
                    print(Fore.CYAN + "Use the item again? (Y/N)" + Style.RESET_ALL)
                    retry = input(Fore.GREEN + "> " + Style.RESET_ALL).lower()
                    if retry != 'y':
                        return
                
                # Remove item and start boss fight
                self.boss_inventory.pop(index)
                self.start_boss_fight(boss_item.boss)
            else:
                print(Fore.RED + "Invalid number!" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid input!" + Style.RESET_ALL)
    
    def dev_boss_menu(self):
        """DEV MODE: Spawn any boss"""
        self.clear_screen()
        print(Fore.MAGENTA + "╔═══════════════════════════════════════╗" + Style.RESET_ALL)
        print(Fore.MAGENTA + "║         [DEV] BOSS SPAWNER            ║" + Style.RESET_ALL)
        print(Fore.MAGENTA + "╚═══════════════════════════════════════╝" + Style.RESET_ALL)
        print()
        print(Fore.CYAN + "1. Loch Ness Monster (Lake)" + Style.RESET_ALL)
        print(Fore.CYAN + "2. River Guardian (River)" + Style.RESET_ALL)
        print(Fore.CYAN + "3. The Crimson Tide (Pirate Ship - Ocean)" + Style.RESET_ALL)
        print(Fore.CYAN + "4. The Kraken (Ocean)" + Style.RESET_ALL)
        print(Fore.CYAN + "5. [MORE BOSSES COMING SOON]" + Style.RESET_ALL)
        print(Fore.WHITE + "0. Back" + Style.RESET_ALL)
        
        choice = input(Fore.GREEN + "\nSpawn which boss? " + Style.RESET_ALL)
        
        if choice == '1':
            self.start_boss_fight(LOCH_NESS_MONSTER)
        elif choice == '2':
            self.start_boss_fight(RIVER_GUARDIAN)
        elif choice == '3':
            self.start_boss_fight(PIRATE_SHIP)
        elif choice == '4':
            self.start_boss_fight(KRAKEN)


# ===== MAIN =====
if __name__ == "__main__":
    show_intro()
    print(Fore.CYAN + "╔═══════════════════════════════════════╗" + Style.RESET_ALL)
    print(Fore.CYAN + "║       🎣 FISHING GAME 🎣              ║" + Style.RESET_ALL)
    print(Fore.CYAN + "║       BOSS BATTLES UPDATE             ║" + Style.RESET_ALL)
    print(Fore.CYAN + "║         V.0.6.0 BETA                  ║" + Style.RESET_ALL)
    print(Fore.CYAN + "╚═══════════════════════════════════════╝" + Style.RESET_ALL)
    print()
    print(
        Fore.YELLOW + "ℹ️   Did You Know?" + Style.RESET_ALL,
        random.choice(DID_YOU_KNOW_FACTS)
    )
    time.sleep(2)
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
    elif choice == 'up up down down left right A B':  #dev mode konami code
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
        game.boss_inventory = list(BOSS_ITEMS.values())  # all boss items
        print(Fore.LIGHTMAGENTA_EX + "All rods, baits, locations and bosses unlocked!" + Style.RESET_ALL)
        print(Fore.LIGHTMAGENTA_EX + "Press [B] in-game to spawn bosses directly!" + Style.RESET_ALL)
        time.sleep(1)
        game.start_game()

    else:
        print(Fore.RED + "Invalid choice." + Style.RESET_ALL)