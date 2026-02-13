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

# Game version for save file compatibility
GAME_VERSION = "0.7.1"

# Music system - cross-platform support
current_music = None
music_enabled = True

def play_music(track_name):
    """Play background music with error handling"""
    global current_music, music_enabled
    
    if not music_enabled:
        return
    
    # Stop current music if playing
    stop_music()
    
    music_path = f"music/{track_name}.wav"
    
    if not os.path.exists(music_path):
        if current_music is None:  # Only print once per session
            print(Fore.YELLOW + f"♪ Music not found, audio disabled" + Style.RESET_ALL)
            music_enabled = False
        return
    
    try:
        if platform.system() == 'Windows':
            # Use os.startfile for Windows
            os.startfile(music_path)
            current_music = track_name
        elif platform.system() == 'Darwin':  # macOS
            subprocess.Popen(['afplay', music_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            current_music = track_name
        else:  # Linux
            subprocess.Popen(['aplay', music_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            current_music = track_name
    except Exception as e:
        if current_music is None:
            print(Fore.YELLOW + f"♪ Music playback error, audio disabled" + Style.RESET_ALL)
            music_enabled = False

def stop_music():
    """Stop currently playing music"""
    global current_music
    
    if current_music is None:
        return
    
    try:
        if platform.system() == 'Windows':
            # Windows doesn't provide easy control, so we skip stopping
            pass
        elif platform.system() == 'Darwin':  # macOS
            subprocess.run(['killall', 'afplay'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:  # Linux
            subprocess.run(['killall', 'aplay'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        pass
    
    current_music = None

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
    "Jörmungandr is the World Serpent from Norse mythology - so large it encircles the Earth!",
    "In Norse legend, Jörmungandr and Thor are destined to kill each other at Ragnarök!",
    "Jörmungandr's venom is said to be potent enough to poison the ocean itself!",
    "The World Serpent is one of Loki's three monstrous children in Norse mythology!",
    "Defeating Jörmungandr breaks ancient Norse prophecy - with unknown consequences!",
    
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
    os.system('cls' if os.name == 'nt' else 'clear')
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
    os.system('cls' if os.name == 'nt' else 'clear')
    
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
# ===== JÖRMUNGANDR ATTACKS =====

def jormungandr_world_coil():
    """Escape the World Serpent's crushing coils"""
    print(Fore.MAGENTA + "\n🐍 THE WORLD SERPENT COILS AROUND YOU! 🐍\n" + Style.RESET_ALL)
    
    print(Fore.YELLOW + "Break free before you're crushed! Match the sequence!" + Style.RESET_ALL)
    time.sleep(1)
    
    # Sequence matching challenge
    sequence_length = 6
    directions = ['↑', '↓', '←', '→']
    sequence = [random.choice(directions) for _ in range(sequence_length)]
    
    print(Fore.CYAN + "Memorize the escape sequence:" + Style.RESET_ALL)
    time.sleep(0.5)
    
    for symbol in sequence:
        print(Fore.GREEN + f" {symbol} ", end='', flush=True)
        time.sleep(0.6)
    
    print("\n")
    time.sleep(1)
    
    # Clear screen effect
    print(Fore.LIGHTBLACK_EX + "█" * 50 + Style.RESET_ALL)
    
    print(Fore.YELLOW + "Enter the sequence (use: up, down, left, right):" + Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX + "Example: up down left right" + Style.RESET_ALL)
    
    try:
        user_input = input(Fore.GREEN + "> " + Style.RESET_ALL).lower().split()
        
        # Convert input to symbols
        convert = {'up': '↑', 'down': '↓', 'left': '←', 'right': '→'}
        user_sequence = [convert.get(x, '') for x in user_input]
        
        if user_sequence == sequence:
            print(Fore.GREEN + "✓ Perfect! You broke free from the serpent's grip!" + Style.RESET_ALL)
            return 0
        else:
            correct = sum(1 for i, s in enumerate(user_sequence) if i < len(sequence) and s == sequence[i])
            damage = 35 - (correct * 5)
            print(Fore.YELLOW + f"Partially escaped! {correct}/{sequence_length} correct (-{damage} HP)" + Style.RESET_ALL)
            return damage
    except:
        print(Fore.RED + "💥 Crushed by the serpent's coils! (-35 HP)" + Style.RESET_ALL)
        return 35


def jormungandr_venom_rain():
    """Dodge falling venom droplets"""
    print(Fore.GREEN + "\n☠️ JÖRMUNGANDR'S VENOM RAINS DOWN! ☠️\n" + Style.RESET_ALL)
    
    print(Fore.YELLOW + "Dodge the poisonous drops! Watch carefully!" + Style.RESET_ALL)
    time.sleep(1)
    
    total_damage = 0
    rounds = 5
    
    for round_num in range(rounds):
        positions = list(range(1, 8))
        safe_spots = random.sample(positions, 3)  # Only 3 safe spots
        
        print()
        print(Fore.CYAN + f"💧 Venom Wave {round_num + 1}!" + Style.RESET_ALL)
        
        # Show where venom will fall
        display = []
        for pos in positions:
            if pos in safe_spots:
                display.append('[ ]')
            else:
                display.append('[☠️]')
        
        print(Fore.WHITE + "Positions: " + ' '.join(display) + Style.RESET_ALL)
        print(Fore.YELLOW + f"Choose safe spot (1-7):" + Style.RESET_ALL)
        
        try:
            choice = int(input(Fore.GREEN + "> " + Style.RESET_ALL))
            if choice not in safe_spots:
                print(Fore.RED + "💥 BURNED BY VENOM! (-8 HP)" + Style.RESET_ALL)
                total_damage += 8
            else:
                print(Fore.GREEN + "✓ Safe!" + Style.RESET_ALL)
        except:
            total_damage += 8
        
        time.sleep(0.4)
    
    if total_damage == 0:
        print(Fore.LIGHTGREEN_EX + "\n★ FLAWLESS! No venom touched you! ★" + Style.RESET_ALL)
    
    return total_damage


def jormungandr_tidal_wave():
    """Swim against the serpent's massive waves"""
    print(Fore.BLUE + "\n🌊 THE WORLD SERPENT THRASHES - CREATING COLOSSAL WAVES! 🌊\n" + Style.RESET_ALL)
    
    print(Fore.YELLOW + "Swim to stay afloat! Press ENTER repeatedly!" + Style.RESET_ALL)
    time.sleep(1)
    
    target_presses = 20
    presses = 0
    start_time = time.time()
    time_limit = 6
    
    print(Fore.CYAN + f"Press ENTER {target_presses} times!" + Style.RESET_ALL)
    print(Fore.WHITE + "GO!" + Style.RESET_ALL)
    
    while presses < target_presses and (time.time() - start_time) < time_limit:
        try:
            input()
            presses += 1
            progress = "█" * presses + "░" * (target_presses - presses)
            sys.stdout.write(f"\r{Fore.CYAN}[{progress}] {presses}/{target_presses}{Style.RESET_ALL}")
            sys.stdout.flush()
        except:
            break
    
    print()
    
    if presses >= target_presses:
        print(Fore.GREEN + "✓ You survived the waves!" + Style.RESET_ALL)
        return 0
    else:
        damage = 30 - presses
        print(Fore.YELLOW + f"Struggled against the current! (-{damage} HP)" + Style.RESET_ALL)
        return max(0, damage)


def jormungandr_ragnarok_fury():
    """Survive the World Serpent's ultimate attack - Ragnarök Fury"""
    print(Fore.RED + "\n⚡ RAGNARÖK FURY - THE WORLD-ENDING STRIKE! ⚡\n" + Style.RESET_ALL)
    
    print(Fore.LIGHTRED_EX + "The serpent channels the power of Ragnarök itself!" + Style.RESET_ALL)
    print(Fore.YELLOW + "Solve the Norse rune puzzle to deflect the attack!" + Style.RESET_ALL)
    time.sleep(1.5)
    
    # Math puzzle with Norse theme
    rune_values = {
        'ᚠ': random.randint(1, 5),
        'ᚢ': random.randint(1, 5),
        'ᚦ': random.randint(1, 5)
    }
    
    print(Fore.CYAN + "\nRune values:" + Style.RESET_ALL)
    for rune, value in rune_values.items():
        print(Fore.WHITE + f"  {rune} = {value}" + Style.RESET_ALL)
    
    time.sleep(1)
    
    # Create equation
    rune1, rune2, rune3 = list(rune_values.keys())
    answer = rune_values[rune1] * 2 + rune_values[rune2] - rune_values[rune3]
    
    print()
    print(Fore.YELLOW + f"Solve: ({rune1} × 2) + {rune2} - {rune3} = ?" + Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX + "You have 8 seconds!" + Style.RESET_ALL)
    
    start_time = time.time()
    time_limit = 8
    
    try:
        user_answer = int(input(Fore.GREEN + "> " + Style.RESET_ALL))
        elapsed = time.time() - start_time
        
        if elapsed > time_limit:
            print(Fore.RED + "⏱️ Too slow! The fury overwhelms you! (-45 HP)" + Style.RESET_ALL)
            return 45
        elif user_answer == answer:
            print(Fore.LIGHTGREEN_EX + "★ PERFECT! You deflected Ragnarök itself! ★" + Style.RESET_ALL)
            return 0
        else:
            print(Fore.YELLOW + f"Close, but not quite! (Answer was {answer}) (-25 HP)" + Style.RESET_ALL)
            return 25
    except:
        print(Fore.RED + "💥 The fury strikes! (-45 HP)" + Style.RESET_ALL)
        return 45


def jormungandr_serpent_gaze():
    """Face the hypnotic gaze of the World Serpent"""
    print(Fore.MAGENTA + "\n👁️ THE SERPENT'S ANCIENT GAZE LOCKS ONTO YOU! 👁️\n" + Style.RESET_ALL)
    
    print(Fore.YELLOW + "Don't be mesmerized! Focus and type the word correctly!" + Style.RESET_ALL)
    time.sleep(1)
    
    words = [
        "MIDGARD", "YGGDRASIL", "RAGNAROK", "VALHALLA", "ASGARD",
        "SERPENT", "JORMUNGANDR", "FENRIR", "THOR", "ODIN"
    ]
    
    word = random.choice(words)
    
    # Show word briefly then scramble
    print(Fore.CYAN + "\nRemember this word:" + Style.RESET_ALL)
    time.sleep(0.5)
    print(Fore.GREEN + f"  {word}  " + Style.RESET_ALL)
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Scramble effect
    print()
    for _ in range(3):
        scrambled = ''.join(random.sample(word, len(word)))
        sys.stdout.write(f"\r{Fore.LIGHTBLACK_EX}{scrambled}{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(0.2)
    
    print("\n")
    print(Fore.YELLOW + "Type the original word:" + Style.RESET_ALL)
    
    try:
        user_word = input(Fore.GREEN + "> " + Style.RESET_ALL).upper().strip()
        
        if user_word == word:
            print(Fore.GREEN + "✓ You resisted the serpent's gaze!" + Style.RESET_ALL)
            return 0
        else:
            print(Fore.YELLOW + f"The gaze weakened you! (Correct word: {word}) (-20 HP)" + Style.RESET_ALL)
            return 20
    except:
        print(Fore.RED + "💥 Hypnotized! (-20 HP)" + Style.RESET_ALL)
        return 20


def jormungandr_tail_whip():
    """React quickly to dodge the serpent's tail"""
    print(Fore.YELLOW + "\n⚡ THE SERPENT'S TAIL WHIPS AROUND! ⚡\n" + Style.RESET_ALL)
    
    print(Fore.YELLOW + "Quick! React to avoid it!" + Style.RESET_ALL)
    time.sleep(1)
    
    # Quick reaction challenge
    directions = ['DUCK', 'JUMP', 'LEFT', 'RIGHT']
    correct_action = random.choice(directions)
    
    print(Fore.CYAN + "Tail coming from the " + Style.RESET_ALL, end='')
    sys.stdout.flush()
    time.sleep(0.5)
    
    if correct_action == 'DUCK':
        print(Fore.RED + "TOP!" + Style.RESET_ALL)
    elif correct_action == 'JUMP':
        print(Fore.RED + "BOTTOM!" + Style.RESET_ALL)
    elif correct_action == 'LEFT':
        print(Fore.RED + "RIGHT!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "LEFT!" + Style.RESET_ALL)
    
    print(Fore.YELLOW + f"Type '{correct_action}' quickly!" + Style.RESET_ALL)
    
    start_time = time.time()
    
    try:
        response = input(Fore.GREEN + "> " + Style.RESET_ALL).upper().strip()
        elapsed = time.time() - start_time
        
        if response == correct_action and elapsed < 2:
            print(Fore.GREEN + "✓ Lightning reflexes!" + Style.RESET_ALL)
            return 0
        elif response == correct_action:
            print(Fore.YELLOW + "Too slow! Grazed by the tail! (-10 HP)" + Style.RESET_ALL)
            return 10
        else:
            print(Fore.RED + "💥 Hit! (-25 HP)" + Style.RESET_ALL)
            return 25
    except:
        print(Fore.RED + "💥 Hit! (-25 HP)" + Style.RESET_ALL)
        return 25


# ===== KRAKEN ATTACKS =====

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
    os.system('cls' if os.name == 'nt' else 'clear')
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


# ===== CTHULHU ATTACK PATTERNS =====
def cthulhu_madness_gaze():
    """The Dreaming God's psychic assault - symbols and sanity check"""
    print(Fore.MAGENTA + "\n👁️ THE DREAMING GOD'S GAZE FALLS UPON YOU! 👁️\n" + Style.RESET_ALL)
    
    total_damage = 0
    
    # Phase 1: Symbol Recognition (tests sanity/focus)
    print(Fore.YELLOW + "Phase 1: ELDER SYMBOLS BURN YOUR MIND!" + Style.RESET_ALL)
    print()
    
    symbols = ['⊗', '⊕', '⊙', '⊛', '⊚', '◉', '◎']
    target_symbols = random.sample(symbols, 3)
    
    print(Fore.CYAN + "Remember these symbols:" + Style.RESET_ALL)
    print(Fore.GREEN + f"  {' '.join(target_symbols)}" + Style.RESET_ALL)
    time.sleep(2.5)
    
    # Clear with "madness" text
    for _ in range(5):
        print(Fore.LIGHTBLACK_EX + "█" * 60 + Style.RESET_ALL)
    
    # Show mixed symbols
    print()
    print(Fore.MAGENTA + "Which symbols did you see? (Enter the positions 1-7)" + Style.RESET_ALL)
    all_symbols = random.sample(symbols, 7)
    for i, sym in enumerate(all_symbols, 1):
        print(Fore.WHITE + f"{i}. {sym}" + Style.RESET_ALL)
    
    correct_positions = [str(all_symbols.index(s) + 1) for s in target_symbols if s in all_symbols]
    
    try:
        response = input(Fore.GREEN + "Enter positions (e.g., '1 3 5'): " + Style.RESET_ALL).strip()
        if sorted(response.split()) == sorted(correct_positions):
            print(Fore.GREEN + "✓ Your mind holds firm!" + Style.RESET_ALL)
        else:
            total_damage += 15
            print(Fore.RED + "💥 MADNESS SEEPS IN! (-15 HP)" + Style.RESET_ALL)
    except:
        total_damage += 15
        print(Fore.RED + "💥 YOUR MIND SHATTERS! (-15 HP)" + Style.RESET_ALL)
    
    time.sleep(1)
    
    # Phase 2: Whispers of R'lyeh
    print()
    print(Fore.LIGHTMAGENTA_EX + "Phase 2: THE WHISPERS... THEY'RE GETTING LOUDER..." + Style.RESET_ALL)
    
    phrases = ["PH'NGLUI", "MGLW'NAFH", "CTHULHU", "R'LYEH", "WGAH'NAGL", "FHTAGN"]
    correct_phrase = random.choice(phrases)
    
    # Show corrupted text
    corrupted = list(correct_phrase)
    for _ in range(random.randint(2, 4)):
        pos = random.randint(0, len(corrupted) - 1)
        corrupted[pos] = random.choice(['█', '▓', '▒', '░', '?', '#', '@'])
    
    print(Fore.GREEN + f"The whispers speak: {Fore.YELLOW}{''.join(corrupted)}" + Style.RESET_ALL)
    print(Fore.CYAN + "What word do they utter?" + Style.RESET_ALL)
    
    # Show options
    options = random.sample(phrases, 3)
    if correct_phrase not in options:
        options[0] = correct_phrase
    random.shuffle(options)
    
    for i, phrase in enumerate(options, 1):
        print(Fore.WHITE + f"{i}. {phrase}" + Style.RESET_ALL)
    
    try:
        choice = int(input(Fore.GREEN + "> " + Style.RESET_ALL))
        if options[choice - 1] == correct_phrase:
            print(Fore.GREEN + "✓ You comprehend the madness!" + Style.RESET_ALL)
        else:
            total_damage += 12
            print(Fore.RED + "💥 THE WORDS BURN! (-12 HP)" + Style.RESET_ALL)
    except:
        total_damage += 12
    
    time.sleep(0.5)
    
    if total_damage == 0:
        print(Fore.LIGHTGREEN_EX + "\n★ YOUR SANITY HOLDS! ★" + Style.RESET_ALL)
    else:
        print(Fore.LIGHTBLACK_EX + "\n*You feel... different... wrong...*" + Style.RESET_ALL)
    
    return total_damage


def cthulhu_tentacle_rlyeh():
    """Massive tentacles emerge from the sunken city"""
    print(Fore.GREEN + "\n🐙 TENTACLES RISE FROM R'LYEH! 🐙\n" + Style.RESET_ALL)
    
    total_damage = 0
    grid_size = 5
    
    print(Fore.YELLOW + "Massive tentacles breach the surface!" + Style.RESET_ALL)
    print(Fore.CYAN + "Navigate to safety!" + Style.RESET_ALL)
    print()
    
    # Create grid
    tentacle_positions = []
    for _ in range(8):
        tentacle_positions.append((random.randint(0, grid_size-1), random.randint(0, grid_size-1)))
    
    # Show animated tentacles rising
    for frame in range(6):
        print("\r" + Fore.LIGHTBLACK_EX + "Rising..." + "." * frame + Style.RESET_ALL, end='')
        time.sleep(0.2)
    print("\n")
    
    # Display grid
    for y in range(grid_size):
        row = ""
        for x in range(grid_size):
            if (x, y) in tentacle_positions:
                row += Fore.GREEN + "🐙" + Style.RESET_ALL
            else:
                row += Fore.BLUE + "≈≈" + Style.RESET_ALL
        print(row)
    
    print()
    print(Fore.YELLOW + "Choose a safe position (row, col) - e.g., '2 3':" + Style.RESET_ALL)
    
    try:
        response = input(Fore.GREEN + "> " + Style.RESET_ALL).strip().split()
        y, x = int(response[0]), int(response[1])
        
        if 0 <= x < grid_size and 0 <= y < grid_size:
            if (x, y) not in tentacle_positions:
                print(Fore.GREEN + "✓ You find a safe spot!" + Style.RESET_ALL)
            else:
                total_damage += 20
                print(Fore.RED + "💥 TENTACLE CRUSHES YOU! (-20 HP)" + Style.RESET_ALL)
        else:
            total_damage += 20
            print(Fore.RED + "💥 OUT OF BOUNDS! GRABBED! (-20 HP)" + Style.RESET_ALL)
    except:
        total_damage += 20
        print(Fore.RED + "💥 CONFUSION! GRABBED! (-20 HP)" + Style.RESET_ALL)
    
    return total_damage


def cthulhu_dream_paralysis():
    """Reality distorts as Cthulhu dreams - rapid timing challenge"""
    print(Fore.CYAN + "\n😴 YOU ENTER THE DREAMING GOD'S NIGHTMARE! 😴\n" + Style.RESET_ALL)
    
    total_damage = 0
    
    print(Fore.LIGHTMAGENTA_EX + "Reality bends... time flows strangely..." + Style.RESET_ALL)
    print(Fore.YELLOW + "You must act QUICKLY before you're trapped forever!" + Style.RESET_ALL)
    print()
    
    # Rapid-fire sequence
    actions = [
        ("WAKE", "Type 'WAKE' to resist!"),
        ("FIGHT", "Type 'FIGHT' against the dream!"),
        ("RUN", "Type 'RUN' from the nightmare!"),
        ("BREAK", "Type 'BREAK' free from paralysis!")
    ]
    
    for action_word, instruction in actions:
        print(Fore.CYAN + instruction + Style.RESET_ALL)
        
        start_time = time.time()
        try:
            response = input(Fore.GREEN + "> " + Style.RESET_ALL).upper()
            elapsed = time.time() - start_time
            
            if response == action_word and elapsed < 2.0:
                print(Fore.GREEN + "✓ Success!" + Style.RESET_ALL)
            else:
                total_damage += 6
                if elapsed >= 2.0:
                    print(Fore.RED + "💥 TOO SLOW! The dream takes hold! (-6 HP)" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "💥 WRONG! Paralysis spreads! (-6 HP)" + Style.RESET_ALL)
        except:
            total_damage += 6
        
        time.sleep(0.3)
    
    # Final dream escape
    print()
    print(Fore.MAGENTA + "THE DREAM COLLAPSES!" + Style.RESET_ALL)
    print(Fore.YELLOW + "Mash SPACE 15 times in 5 seconds to escape!" + Style.RESET_ALL)
    
    presses = 0
    start_time = time.time()
    
    while time.time() - start_time < 5 and presses < 15:
        key = get_key()
        if key == ' ':
            presses += 1
            sys.stdout.write(f"\r{Fore.CYAN}Presses: {presses}/15{Style.RESET_ALL}")
            sys.stdout.flush()
    
    print()
    
    if presses >= 15:
        print(Fore.GREEN + "✓ YOU BREAK FREE FROM THE DREAM!" + Style.RESET_ALL)
    else:
        total_damage += 15
        print(Fore.RED + f"💥 TRAPPED! Only {presses}/15! (-15 HP)" + Style.RESET_ALL)
    
    if total_damage == 0:
        print(Fore.LIGHTGREEN_EX + "\n★ YOU RESISTED THE DREAMING GOD! ★" + Style.RESET_ALL)
    
    return total_damage


def cthulhu_cultist_summon():
    """Cthulhu summons Deep One cultists to attack"""
    print(Fore.LIGHTBLACK_EX + "\n🐟 CULTIST FISH SWARM FROM THE DEPTHS! 🐟\n" + Style.RESET_ALL)
    
    total_damage = 0
    
    print(Fore.MAGENTA + "*Cthulhu's will commands the Deep Ones!*" + Style.RESET_ALL)
    print(Fore.YELLOW + "Defeat the cultist fish!" + Style.RESET_ALL)
    print()
    
    # Three waves of cultists
    for wave in range(3):
        print(Fore.CYAN + f"Wave {wave + 1}: Cultist approaches!" + Style.RESET_ALL)
        
        # Show cultist
        cultist_hp = 3
        
        for attack_num in range(3):
            if cultist_hp <= 0:
                break
                
            print(Fore.WHITE + f"Cultist HP: {cultist_hp}/3" + Style.RESET_ALL)
            print(Fore.YELLOW + "Attack! (Press A):" + Style.RESET_ALL)
            
            start_time = time.time()
            response = get_key()
            elapsed = time.time() - start_time
            
            if response == 'a' and elapsed < 1.5:
                cultist_hp -= 1
                print(Fore.GREEN + "✓ HIT!" + Style.RESET_ALL)
            else:
                total_damage += 5
                print(Fore.RED + "💥 The cultist strikes! (-5 HP)" + Style.RESET_ALL)
            
            time.sleep(0.3)
        
        if cultist_hp > 0:
            total_damage += 8
            print(Fore.RED + f"💥 Cultist {wave + 1} survives and deals extra damage! (-8 HP)" + Style.RESET_ALL)
        else:
            print(Fore.GREEN + f"✓ Cultist {wave + 1} defeated!" + Style.RESET_ALL)
        
        print()
        time.sleep(0.5)
    
    if total_damage == 0:
        print(Fore.LIGHTGREEN_EX + "★ ALL CULTISTS VANQUISHED! ★" + Style.RESET_ALL)
    
    return total_damage


def cthulhu_ultimate_awakening():
    """Cthulhu begins to awaken - ultimate attack"""
    print(Fore.RED + "\n💀 CTHULHU STIRS! THE STARS ARE RIGHT! 💀\n" + Style.RESET_ALL)
    
    total_damage = 0
    
    print(Fore.MAGENTA + "*The Great Old One's eyes begin to open...*" + Style.RESET_ALL)
    print(Fore.YELLOW + "*Reality itself trembles!*" + Style.RESET_ALL)
    print()
    
    # Multi-phase ultimate
    
    # Phase 1: Cosmic Horror
    print(Fore.LIGHTMAGENTA_EX + "Phase 1: THE COSMIC HORROR REVEALED!" + Style.RESET_ALL)
    print(Fore.CYAN + "Look away! (Type 'CLOSE' in 2 seconds):" + Style.RESET_ALL)
    
    start_time = time.time()
    try:
        response = input(Fore.GREEN + "> " + Style.RESET_ALL).upper()
        elapsed = time.time() - start_time
        
        if response == "CLOSE" and elapsed < 2.0:
            print(Fore.GREEN + "✓ You shield your eyes!" + Style.RESET_ALL)
        else:
            total_damage += 18
            print(Fore.RED + "💥 THE SIGHT BURNS YOUR MIND! (-18 HP)" + Style.RESET_ALL)
    except:
        total_damage += 18
    
    time.sleep(1)
    
    # Phase 2: R'lyeh Rises
    print()
    print(Fore.GREEN + "Phase 2: THE SUNKEN CITY RISES!" + Style.RESET_ALL)
    
    # Avoid falling pillars
    positions = list(range(10))
    safe_pos = random.choice(positions)
    
    print(Fore.YELLOW + "Pillars of R'lyeh crash down!" + Style.RESET_ALL)
    print(Fore.CYAN + f"Move to position 0-9:" + Style.RESET_ALL)
    
    try:
        choice = int(input(Fore.GREEN + "> " + Style.RESET_ALL))
        if choice == safe_pos:
            print(Fore.GREEN + "✓ Dodged!" + Style.RESET_ALL)
        else:
            total_damage += 15
            print(Fore.RED + "💥 CRUSHED BY ANCIENT STONE! (-15 HP)" + Style.RESET_ALL)
    except:
        total_damage += 15
    
    time.sleep(1)
    
    # Phase 3: The Call
    print()
    print(Fore.MAGENTA + "Phase 3: THE CALL OF CTHULHU!" + Style.RESET_ALL)
    print(Fore.YELLOW + "Resist by typing the OPPOSITE of what appears!" + Style.RESET_ALL)
    print()
    
    opposites = [
        ("SLEEP", "WAKE"),
        ("OBEY", "RESIST"),
        ("SUBMIT", "FIGHT"),
        ("JOIN", "FLEE")
    ]
    
    test_pair = random.choice(opposites)
    print(Fore.RED + f"Command: {test_pair[0]}" + Style.RESET_ALL)
    print(Fore.CYAN + "You must type:" + Style.RESET_ALL)
    
    try:
        response = input(Fore.GREEN + "> " + Style.RESET_ALL).upper()
        if response == test_pair[1]:
            print(Fore.GREEN + "✓ YOU RESIST THE CALL!" + Style.RESET_ALL)
        else:
            total_damage += 20
            print(Fore.RED + "💥 YOUR WILL CRUMBLES! (-20 HP)" + Style.RESET_ALL)
    except:
        total_damage += 20
    
    print()
    
    if total_damage == 0:
        print(Fore.LIGHTGREEN_EX + "★★★ IMPOSSIBLE! YOU SURVIVED THE AWAKENING! ★★★" + Style.RESET_ALL)
        print(Fore.CYAN + "*Cthulhu returns to his slumber... for now...*" + Style.RESET_ALL)
    else:
        print(Fore.LIGHTBLACK_EX + "*Your mind will never be the same...*" + Style.RESET_ALL)
    
    return total_damage


# ===== BOSS DEFINITIONS =====
LOCH_NESS_ASCII = """
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
        BossAttack("Wave Crash", loch_ness_wave_attack, (8, 18), "Sends powerful waves"),
        BossAttack("Water Blast", loch_ness_water_blast, (10, 16), "Fires a concentrated water jet"),
        # NEW Enhanced attacks
        BossAttack("Tidal Wave", loch_ness_tidal_wave, (0, 25), "Multi-wave barrage!"),
        BossAttack("Whirlpool", loch_ness_whirlpool, (0, 18), "Spinning vortex trap!"),
        BossAttack("Tail Sweep", loch_ness_tail_sweep, (0, 20), "Massive tail attack!"),
        BossAttack("Deep Dive Slam", loch_ness_deep_dive_slam, (0, 24), "Two-phase combo!"),
        BossAttack("Mist Breath", loch_ness_mist_breath, (0, 14), "Vision obscured!"),
        BossAttack("ULTIMATE COMBO", loch_ness_combo_attack, (0, 22), "Devastating triple attack!")
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
    hp=400,  # Reduced from 800 - was way too high for 2nd boss
    defense=10,  # Reduced from 15
    attacks=[
        BossAttack("Rapids Rush", river_rapids_dodge, (0, 32), "Navigate treacherous rapids!"),
        BossAttack("Torrential Bite", river_bite_sequence, (0, 42), "Dodge rapid bite attacks!"),
        BossAttack("Whirlpool Spin", river_current_spin, (0, 28), "Escape the spinning vortex!"),
        BossAttack("Tail Strike", river_tail_strike, (0, 35), "Perfect timing required!"),
        BossAttack("RIVER'S WRATH", river_wrath_combo, (0, 60), "The Guardian's ultimate fury!")
    ],
    ascii_art=RIVER_GUARDIAN_ASCII,
    dialogue={
        "intro": [
            "*The water grows unnaturally still...*",
            "*Every ripple... every current... ceases*",
            "*Mist rises from the loch's surface like breath*",
            "*You feel it before you see it - ancient grief made manifest*",
            "*A shape emerges from the depths*",
            "*Not a monster... but a memory*",
            "*THE LOCH NESS GUARDIAN*",
            "*Sorrow older than human language fills the air*",
            "*It does not attack from malice*",
            "*It strikes because it has forgotten... how not to hurt*"
        ],
        "default": [
            "*The creature circles in patterns that echo vanished currents*",
            "*Its movements remember storms from thousands of years ago*",
            "*Steam rises from the water - or are those... tears?*",
            "*You sense confusion within it - protector without anything left to protect*"
        ],
        "hit": [
            "*The creature recoils - not in pain, but in surprise*",
            "*Did someone... fight back? Did they not flee?*",
            "*Its attacks intensify - but you sense desperation, not rage*",
            "*'Leave me... let me forget...'*"
        ],
        "low_hp": [
            "*The creature's movements slow to drifting*",
            "*For the first time in millennia... it hesitates*",
            "*'Why... do you remain? All others... fled...'*",
            "*Beneath the waves, you glimpse something almost like hope*",
            "*Ancient loneliness begins to crack*"
        ],
        "merciful": [
            "*You lower your weapon and simply... wait*",
            "*The creature stares with eyes that have seen civilizations rise and fall*",
            "*'You... you do not fear me?'*",
            "*Slowly, the mist begins to clear*",
            "*Memory stirs within the guardian*",
            "*A fragment of what it was... before the grief*"
        ],
        "spare_ready": [
            "*The Loch Ness Guardian can be SPARED*",
            "*It watches you with something almost like recognition*",
            "*'I remember... guiding ships to safety...'*",
            "*'Before... before the storm...'*"
        ],
        "spared": [
            "*You reach out - not with a weapon, but with understanding*",
            "*The creature trembles, suspended between past and present*",
            "*'You... remind me of them. The sailors I saved.'*",
            "*'Those who traveled these waters with respect... and trust.'*",
            "*The mist swirls, and for a moment, you see*",
            "*Not a monster, but a protector - proud and gentle*",
            "*'Thank you... for remembering what I was.'*",
            "*'I can be that again. I can... heal.'*",
            "*The creature bows its great head*",
            "*When it resurfaces, its eyes are clearer than they've been in ages*",
            "*The loch's sorrow begins to lift*",
            "*You have not just spared a guardian*",
            "*You have helped it remember how to love*"
        ],
        "killed": [
            "*The final blow strikes true*",
            "*The creature's form begins to dissolve back into water*",
            "*'Finally... rest...'*",
            "*But there is no peace in those fading eyes*",
            "*Only exhausted grief*",
            "*The mist grows thicker, colder*",
            "*The loch will never heal from this wound*",
            "*You have not slain a monster*",
            "*You have extinguished the last ember of protective love*",
            "*The waters remember*",
            "*And they will never forgive*"
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
    hp=450,  # Increased from 350
    defense=12,
    attacks=[
        BossAttack("Cannon Barrage", pirate_cannon_barrage, (0, 55), "Dodge incoming cannonballs!"),
        BossAttack("Harpoon Strike", pirate_harpoon_strike, (0, 32), "Duck the harpoon!"),
        BossAttack("Broadside Ram", pirate_broadside_ram, (0, 40), "Avoid the ramming ship!"),
        BossAttack("Net Toss", pirate_net_toss, (0, 26), "Cut yourself free!"),
        BossAttack("ALL HANDS ASSAULT", pirate_ultimate_assault, (0, 65), "The crew's full might!")
    ],
    ascii_art=PIRATE_SHIP_ASCII,
        dialogue={

        "intro": [
                "*A ship emerges from mist that shouldn't exist in open ocean*",
                "*Cannons swivel with practiced precision*",
                "*But something is... off*",
                "*The ship moves against the wind*",
                "*Sails filled by currents that died centuries ago*",
                "*On deck stands a figure who should not still draw breath*",
                "*CAPTAIN REDBEARD*",
                "*\"Another vessel! Corporate colors?\"*",
                "*\"Wait... those markings... you're not AquaTech!\"*",
                "*A spyglass lowers, revealing eyes that have seen too much*",
                "*\"Blast! We already fired warning shots!\"*",
                "*\"Can't back down now - the crew's watching!\"*",
                "*\"Besides...\" *The captain grins* \"We need to test ye!\"*",
                "*\"Only the worthy sail with the Crimson Tide!\"*",
                "*\"EN GARDE, potential ally!\"*"
            ],
            "default": [
                "*The crew watches from the rigging, judging your worth*",
                "*\"Show us what ye're made of!\"*",
                "*Redbeard laughs - a sound like thunder across open water*",
                "*The ocean itself seems to approve of this test*"
            ],
            "hit": [
                "*The ship rocks - but Redbeard only laughs harder*",
                "*\"NOW THAT'S A FISHER! KEEP IT UP!\"*",
                "*The crew cheers your prowess*",
                "*This isn't a fight to the death*",
                "*It's an audition*"
            ],
            "low_hp": [
                "*The ship slows, sails going slack*",
                "*Redbeard raises a hand to halt the crew*",
                "*\"HOLD! This one's got the spirit!\"*",
                "*\"Fights with skill but not cruelty!\"*",
                "*\"Exactly what the rebellion needs!\"*",
                "*The ocean around you grows calmer*",
                "*As if the sea itself agrees*"
            ],
            "merciful": [
                "*You signal peaceful intent*",
                "*The crew exchanges glances*",
                "*Redbeard studies you with eyes older than any human should possess*",
                "*\"Interesting... strength tempered with mercy.\"*",
                "*\"Ye could destroy us. But ye choose not to.\"*",
                "*\"That's not weakness. That's wisdom.\"*",
                "*The captain's weathered face breaks into a genuine smile*"
            ],
            "spare_ready": [
                "*The Crimson Tide can be SPARED*",
                "*\"WE SURRENDER!\" Redbeard shouts with glee*",
                "*\"But not in defeat - in RECRUITMENT!\"*",
                "*The crew laughs and cheers*"
            ],
            "spared": [
                "*You lower your weapon and extend a hand of friendship*",
                "*Redbeard's eyes gleam with something ancient*",
                "*Recognition*",
                "*\"Aye... I remember now.\"*",
                "*\"Remember what?\" you ask*",
                "*\"The ocean sent ye. I can feel it.\"*",
                "*\"Centuries I've sailed these waters. More than any human should.\"*",
                "*\"The ocean kept me alive for a reason.\"*",
                "*\"And that reason... just climbed aboard.\"*",
                "*The Crimson Tide's crew erupts in celebration*",
                "*\"WELCOME TO THE REBELLION!\"*",
                "*\"We fight not for profit, but for freedom!\"*",
                "*\"The seas belong to ALL - not just corporations!\"*",
                "*\"Never exploit spawning grounds!\"*",
                "*\"Never harm Guardians without cause!\"*",
                "*\"And NEVER - ever - sell the ocean's soul!\"*",
                "*Redbeard clasps your shoulder*",
                "*\"The rebellion has a new champion.\"*",
                "*\"And the Crimson Tide... has found its purpose.\"*"
            ],
            "killed": [
                "*Cannon fire ceases*",
                "*The ship lists heavily, taking on water*",
                "*Redbeard stands at the helm, impossibly calm*",
                "*\"So... this is how it ends.\"*",
                "*\"I thought... the ocean wanted me to see...\"*",
                "*The captain's form seems to waver*",
                "*Less solid than moments before*",
                "*\"I was never truly alive, was I?\"*",
                "*\"The sea kept me here. Waiting. For someone.\"*",
                "*\"I thought... you were that someone.\"*",
                "*The Crimson Tide begins to sink*",
                "*\"The rebellion... dies with us.\"*",
                "*\"And the ocean... the ocean weeps.\"*",
                "*As the ship disappears beneath the waves*",
                "*You swear you hear the ocean itself*",
                "*Crying out in grief*",
                "*For the last free sailors*",
                "*Are free no more*"
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
    hp=600,  # Increased from 500
    defense=18,
    attacks=[
        BossAttack("Tentacle Slam", kraken_tentacle_slam, (0, 80), "Dodge the massive tentacles!"),
        BossAttack("Ink Cloud", kraken_ink_cloud, (0, 35), "Navigate through the murky ink!"),
        BossAttack("Whirlpool Grab", kraken_whirlpool_grab, (0, 42), "Escape the pulling vortex!"),
        BossAttack("Beak Strike", kraken_beak_strike, (0, 48), "Avoid the crushing beak!"),
        BossAttack("Crushing Grip", kraken_crushing_grip, (0, 52), "Break free from tentacles!"),
        BossAttack("TIDAL FURY", kraken_tidal_fury, (0, 70), "The Kraken's ultimate wrath!")
    ],
    ascii_art=KRAKEN_ASCII,
    dialogue={
        "intro": [
            "*The ocean floor trembles*",
            "*Not with violence, but with effort*",
            "*Something vast is moving*",
            "*Something that has not moved in eons*",
            "*The water pressure increases*",
            "*You descend past the depth where light reaches*",
            "*Past where life should exist*",
            "*And there... you see it*",
            "*A RIFT in the ocean floor*",
            "*Not geological*",
            "*Metaphysical*",
            "*And over that rift*",
            "*Holding it closed with sheer will*",
            "*THE KRAKEN*",
            "*Tentacles the size of ancient trees*",
            "*Eyes that have watched the universe bend*",
            "*'Another one... drawn by the rift...'*",
            "*'I cannot let you pass.'*",
            "*'I WILL not let you pass.'*",
            "*'For what lies beyond...'*",
            "*'Must never be known.'*"
        ],
        "default": [
            "*The Kraken does not attack - it tests*",
            "*Each movement calculated*",
            "*Asking: Are you strong enough to help?*",
            "*Or wise enough to turn back?*",
            "*The rift beneath it pulses with impossible light*"
        ],
        "hit": [
            "*The Kraken's grip on the rift wavers*",
            "*For a moment - just a moment*",
            "*The rift yawns wider*",
            "*And you see THINGS trying to push through*",
            "*'FOCUS!' The Kraken roars*",
            "*'Do not make me choose between stopping you...'*",
            "*'And holding the barrier!'*"
        ],
        "low_hp": [
            "*The Kraken's ancient form grows transparent*",
            "*'I have held this vigil... for so long...'*",
            "*'Since before your kind... walked upright...'*",
            "*'I am... tired...'*",
            "*The rift groans, straining against the guardian's weakening will*",
            "*'But I cannot rest. Not yet. Not... alone.'*",
            "*For the first time, you hear desperation*",
            "*'Help me... or end me... but CHOOSE.'*"
        ],
        "merciful": [
            "*You stop fighting and instead... position yourself*",
            "*Beside the Kraken*",
            "*Not opposing it - supporting it*",
            "*The ancient guardian's eyes widen*",
            "*'You... you understand?'*",
            "*'Without words, without explanation...'*",
            "*'You simply... understand what must be done?'*",
            "*Together, you feel the rift's pressure lessen*",
            "*'Millennia I have waited for this...'*",
            "*'For someone to share the burden...'*"
        ],
        "spare_ready": [
            "*The KRAKEN can be SPARED*",
            "*The rift beneath stabilizes*",
            "*For the first time in eons*",
            "*The guardian can rest*",
            "*'Will you... help me?'*",
            "*'Or will you walk away, knowing what I protect?'*"
        ],
        "spared": [
            "*You place your hand against the Kraken's vast form*",
            "*And you make a vow*",
            "*'I will help you hold the line.'*",
            "*The Kraken shudders - not from pain*",
            "*But from relief so profound it transcends language*",
            "*'Thank you... thank you...'*",
            "*'For so long I thought... I would fail alone...'*",
            "*'But you have proven...'*",
            "*'Humans and guardians CAN work together...'*",
            "*The rift seals more tightly than it has in centuries*",
            "*The Kraken's form solidifies, strengthened by your alliance*",
            "*'I mark you as Friend of the Deep.'*",
            "*'Every creature of the abyss will recognize you.'*",
            "*'And when the final crisis comes...'*",
            "*'When the rift threatens to break completely...'*",
            "*'I will not face it alone.'*",
            "*'You will be there.'*",
            "*'We will be there.'*",
            "*'Together.'*",
            "*The Blessing of the Ancient Seas flows through you*",
            "*You have not just spared a guardian*",
            "*You have gained a protector*",
            "*Against horrors beyond mortal comprehension*"
        ],
        "killed": [
            "*Your attack pierces the Kraken's core*",
            "*The ancient guardian's grip on the rift... releases*",
            "*'No... NO...'*",
            "*'You don't understand... what you've done...'*",
            "*The rift EXPLODES open*",
            "*Things that should not exist pour through*",
            "*Thoughts that think themselves*",
            "*Hungers that hunger for hunger itself*",
            "*Mathematics that add up to madness*",
            "*The Kraken's dying form tries desperately to reseal it*",
            "*'I held... for so long... so very long...'*",
            "*'Tell them... tell them I'm sorry...'*",
            "*'I couldn't... hold... alone...'*",
            "*The guardian dissolves into the dark*",
            "*And the rift stabilizes*",
            "*Barely*",
            "*But something has changed*",
            "*The barrier the Kraken maintained?*",
            "*It's weakening*",
            "*Slowly*",
            "*Inexorably*",
            "*What lies beyond will eventually break through*",
            "*And there will be no guardian to stop it*",
            "*Because you killed the only thing that could*"
        ]
    },
    spare_threshold=30
)

# ===== JÖRMUNGANDR - THE WORLD SERPENT =====

JORMUNGANDR_ASCII = """
    ╔════════════════════════════════════════════════════════════╗
    ║         🐍 JÖRMUNGANDR - THE WORLD SERPENT 🐍             ║
    ║              [Midgard's Eternal Guardian]                  ║
    ╚════════════════════════════════════════════════════════════╝
    
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣿⣶⣦⣽⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⡀⢀⣽⣿⣷⣶⣦⣤⣄⣀⠀⠀⠀
            ⠀⠀⣰⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠙⢿⣧⡈⠛⠛⠋⠏⠙⢿⡿⠿⣿⣿⣷⡄⠀
            ⠀⠀⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⣤⠄⠀⠀⠈⠀⠀⠻⠀⢻⠇⠀
            ⠀⠐⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣶⡶⠂⠀⠀⠀⠀⠀⠈⠀⠀
            ⠀⠀⢿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣶⡶⠂⠀⠀⠀⠀⠀⠀
            ⠀⠀⠘⣿⣿⣿⣿⣿⣿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣶⠞⠁⠀⠀⠀⠀
            ⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠛⠛⠛⠛⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            [The serpent that encircles the world...]
"""

JORMUNGANDR = Boss(
    name="Jörmungandr",
    hp=800,  # Increased from 750 - this is the final boss
    defense=25,  # Increased from 22 - highest defense
    attacks=[
        BossAttack("World Coil", jormungandr_world_coil, (0, 45), "Break free from the crushing coils!"),
        BossAttack("Venom Rain", jormungandr_venom_rain, (0, 50), "Dodge the poisonous droplets!"),
        BossAttack("Tidal Wave", jormungandr_tidal_wave, (0, 40), "Swim against the massive waves!"),
        BossAttack("Serpent's Gaze", jormungandr_serpent_gaze, (0, 30), "Resist the hypnotic stare!"),
        BossAttack("Tail Whip", jormungandr_tail_whip, (0, 35), "React quickly to dodge!"),
        BossAttack("RAGNARÖK FURY", jormungandr_ragnarok_fury, (0, 85), "The World Serpent's ultimate power!")
    ],
    ascii_art=JORMUNGANDR_ASCII,
    dialogue={
        "intro": [
            "*The ocean... moves*",
            "*All of it*",
            "*Every current on Earth shifts at once*",
            "*You realize with creeping horror*",
            "*They're not separate currents*",
            "*They're one current*",
            "*One BEING*",
            "*Encircling the entire world*",
            "*JÖRMUNGANDR*",
            "*The World Serpent*",
            "*Eyes open across the horizon*",
            "*Each the size of an island*",
            "*'I am the ocean's unity made flesh.'*",
            "*'I am the circulation. The gyres. The deep flow.'*",
            "*'When currents die... I rot with them.'*",
            "*'When waters warm... I burn.'*",
            "*'When plastics choke the waves...'*",
            "*'They choke ME.'*",
            "*'I do not wish to fight.'*",
            "*'But if the oceans die...'*",
            "*'I will take the world with me.'*",
            "*'For I am the World Serpent.'*",
            "*'And the world... IS the ocean.'*"
        ],
        "default": [
            "*The serpent's coils shift in geological time*",
            "*Each movement sends tsunamis*",
            "*Not from aggression*",
            "*But from mere existence*",
            "*'I remember when the seas were clean.'*",
            "*'When whales sang without sonar interference.'*",
            "*'When coral grew in colors you cannot imagine.'*"
        ],
        "hit": [
            "*Your attack lands against scales made of compressed centuries*",
            "*The serpent barely notices*",
            "*'Is this... prophecy?'*",
            "*'Am I destined to die by your hand?'*",
            "*'Must Ragnarök come... because you will it?'*",
            "*The ocean itself trembles*",
            "*Not from fear*",
            "*But from sorrow*"
        ],
        "low_hp": [
            "*The World Serpent's coils loosen*",
            "*For the first time in human history*",
            "*The ocean's circulation... stutters*",
            "*'So this is how it ends...'*",
            "*'Not with thunder gods and final battles...'*",
            "*'But with choice.'*",
            "*'YOUR choice.'*",
            "*'Prophecy said I would die in Ragnarök.'*",
            "*'But prophecy is probability...'*",
            "*'Not destiny.'*",
            "*'You can change this.'*",
            "*'You can choose differently.'*"
        ],
        "merciful": [
            "*You stop your assault*",
            "*And you speak to the ocean itself*",
            "*Promising to fight for its health*",
            "*To oppose those who poison it*",
            "*To protect what remains*",
            "*The World Serpent's vast eyes close*",
            "*'You... you give me hope.'*",
            "*'That humanity can change.'*",
            "*'That the future is not written.'*",
            "*'That Ragnarök... can be avoided.'*"
        ],
        "spare_ready": [
            "*JÖRMUNGANDR can be SPARED*",
            "*'You hold my fate in your hands.'*",
            "*'Will you be Thor's echo... or humanity's evolution?'*",
            "*The entire ocean waits for your decision*"
        ],
        "spared": [
            "*You bow before the World Serpent*",
            "*And speak the words that rewrite fate*",
            "*'I will not fulfill the prophecy.'*",
            "*'I will not kill you.'*",
            "*'The cycle of violence...'*",
            "*'Ends with me.'*",
            "*The ocean itself seems to exhale*",
            "*Relief measured on a planetary scale*",
            "*Jörmungandr's eyes open wide*",
            "*'In all the centuries I have lived...'*",
            "*'Across every possible future I have dreamed...'*",
            "*'Never once did I imagine...'*",
            "*'This.'*",
            "*The serpent's coils tighten - not in threat*",
            "*But in renewed purpose*",
            "*'Prophecy is broken. Destiny is rewritten.'*",
            "*'The ocean will not die in Ragnarök.'*",
            "*'Because Ragnarök...'*",
            "*'Will never come.'*",
            "*'You have saved more than my life, Fisher.'*",
            "*'You have saved... possibility.'*",
            "*'The future is uncertain again.'*",
            "*'And uncertainty...'*",
            "*'Is hope.'*",
            "*A scale falls from the World Serpent*",
            "*It contains the pattern of every ocean current*",
            "*The memory of every wave*",
            "*'Take this. When the final battle comes...'*",
            "*'I will remember your mercy.'*"
        ],
        "killed": [
            "*Your final blow strikes the serpent's heart*",
            "*If it can be called a heart*",
            "*The center of oceanic circulation*",
            "*COLLAPSES*",
            "*'So... prophecy wins...'*",
            "*'Thor's echo... strikes true...'*",
            "*Every ocean current on Earth stops*",
            "*Simultaneously*",
            "*Fish beach themselves by the millions*",
            "*Tides reverse*",
            "*Fresh water turns brackish*",
            "*Salt water goes strangely sweet*",
            "*The World Serpent's dying form fragments*",
            "*Each piece sinking to a different ocean*",
            "*'Ragnarök... comes early...'*",
            "*'Because you... chose violence...'*",
            "*'The world will not end in fire and ice.'*",
            "*'It will end in stagnation.'*",
            "*'The oceans... no longer flow.'*",
            "*'And nothing... that depends on flow...'*",
            "*'Will survive.'*",
            "*The prophecy is fulfilled*",
            "*But there is no thunder god to share your victory*",
            "*Only dead waters*",
            "*And the knowledge*",
            "*That you chose this*"
        ]
    },
    spare_threshold=35
)

# ===== CTHULHU - THE DREAMING GOD =====

CTHULHU_ASCII = """
    ╔════════════════════════════════════════════════════════════╗
    ║         🐙 CTHULHU - THE DREAMING GOD 🐙                  ║
    ║              [High Priest of the Great Old Ones]           ║
    ║                     [Ph'nglui mglw'nafh...]                ║
    ╚════════════════════════════════════════════════════════════╝
    
        ⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⣀⣤⣶⣾⣿⣿⣷⣶⣤⣀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠜⠉⣿⡆⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢰⣿⠉⠃⠀⠀⠀⠀⠀
        ⠀⢀⣤⣴⣦⣄⣴⠟⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⢻⣦⣠⣴⣦⣄⠀⠀
        ⠀⡞⠁⣠⣾⢿⣧⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣽⡿⣷⣄⠈⢷⠀
        ⠀⣠⣾⠟⠁⢸⣿⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⣿⡇⠈⠻⣷⣄⠀
        ⣰⡿⠁⠀⢀⣾⣏⣾⣄⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣰⣷⣹⣷⠀⠀⠈⢿⣆
        ⣿⡇⠀⢠⣾⠏⢸⣿⣿⣿⣿⠋⢻⣿⣿⣿⣿⡟⠙⣿⣿⣿⣿⡇⠹⣷⡀⠀⢸⣿
        ⠹⣿⣴⡿⠋⠀⠈⠛⠉⣹⣿⣦⣄⡹⣿⣿⣋⣠⣶⣿⣏⠉⠛⠁⠀⠙⢿⣦⣿⠏
        ⠀⣸⣿⠿⠿⣿⣾⣿⡿⠿⣿⣿⣿⣿⡆⢰⣿⣿⣿⣿⠿⢿⣿⣶⣿⠿⠿⣻⣇⠀
        ⠀⣿⡇⢀⣴⣶⣤⣀⣴⣿⠿⣻⡿⣿⣧⣾⣿⢿⣟⠿⣿⣦⣀⣤⣶⣦⠀⢸⣿⠀
        ⠀⢿⣧⠈⠃⢀⣵⣿⡋⠁⢀⣿⡷⣿⡇⢻⣿⣿⣿⡀⠈⢛⣿⣮⡀⠘⠀⣼⡟⠀
        ⠀⠈⠻⣷⣤⣟⣋⣿⣧⣴⡿⠋⠀⣿⡇⢸⣿⠀⠙⢿⣦⣼⣿⣙⣻⣤⣾⠟⠁⠀
        ⠀⠀⠀⠈⢽⣿⠛⢻⣏⢉⣤⣶⣶⣿⠁⠈⣿⣶⣶⣤⡉⣽⡟⠛⣿⡏⠁⠀⠀⠀
        ⠀⠀⠀⠀⠈⠿⣷⣾⣾⣟⣉⣠⣿⢿⡇⢸⠿⣿⣄⣙⣻⣷⣷⣾⠿⠁⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠛⢁⡼⠃⠘⢦⡈⠛⠿⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀
"""

CTHULHU = Boss(
    name="Cthulhu",
    hp=666,  # Appropriately eldritch number
    defense=20,
    attacks=[
        BossAttack("Madness Gaze", cthulhu_madness_gaze, (0, 35), "The Dreaming God's psychic assault!"),
        BossAttack("Tentacles of R'lyeh", cthulhu_tentacle_rlyeh, (0, 28), "Massive tentacles from the sunken city!"),
        BossAttack("Dream Paralysis", cthulhu_dream_paralysis, (0, 50), "Reality bends in the nightmare!"),
        BossAttack("Summon Deep Ones", cthulhu_cultist_summon, (0, 45), "Cultist fish swarm to his will!"),
        BossAttack("THE AWAKENING", cthulhu_ultimate_awakening, (0, 75), "Cthulhu begins to rise!")
    ],
    ascii_art=CTHULHU_ASCII,
    dialogue={
        "intro": [
            "*The Deep Sea grows silent*",
            "*Not the peaceful silence of calm waters*",
            "*But the silence of held breath*",
            "*Of reality... pausing*",
            "*The water around you begins to behave... wrong*",
            "*Flowing in directions that don't exist*",
            "*At angles that hurt to perceive*",
            "*Then you see it*",
            "*Rising from the abyss*",
            "*The sunken city of R'LYEH*",
            "*Stone that predates stone*",
            "*Architecture that violates geometry*",
            "*Symbols that writhe when you look away*",
            "*And there... upon a throne of compressed madness*",
            "*Sits something that should not be*",
            "*CTHULHU*",
            "*'Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn'*",
            "*The words echo in your mind*",
            "*Not spoken, but... understood*",
            "*'In his house at R'lyeh, dead Cthulhu waits dreaming'*",
            "*'But you... you have disturbed the dream'*",
            "*The entity's vast eyes open*",
            "*And you realize with creeping horror*",
            "*It was not asleep*",
            "*It was waiting*",
            "*For you*"
        ],
        "default": [
            "*Cthulhu remains motionless on its throne*",
            "*Or does it move in dimensions you cannot see?*",
            "*Time feels... negotiable here*",
            "*'The stars are not yet right... but you are here anyway...'*",
            "*Whispers in dead languages fill the water*",
            "*You understand them anyway*",
            "*And wish you didn't*"
        ],
        "hit": [
            "*Your attack passes through the entity*",
            "*Or does it?*",
            "*Cthulhu's form ripples like disturbed water*",
            "*'Pain is... interesting... when one exists partially outside time...'*",
            "*'I feel this wound... but also feel it healing...'*",
            "*'And also feel it never happening at all...'*",
            "*Reality around the impact site stutters*",
            "*Cause and effect briefly reverse*",
            "*'You attack because I will retaliate'*",
            "*'Or I retaliate because you will attack'*",
            "*'The sequence is... unclear from here'*"
        ],
        "low_hp": [
            "*Cthulhu's form becomes less substantial*",
            "*More dream than flesh*",
            "*'The stars... truly are not right...'*",
            "*'I cannot maintain physical form...'*",
            "*'Not fully...'*",
            "*'Not yet...'*",
            "*R'lyeh begins to sink again*",
            "*The impossible angles grow less sharp*",
            "*'Perhaps... it is better this way...'*",
            "*'The dream is... peaceful...'*",
            "*'When no one disturbs it...'*",
            "*For the first time, you sense something almost like...*",
            "*Loneliness?*",
            "*'Eons I have waited... for the stars to align...'*",
            "*'For my kind to wake...'*",
            "*'But when I dream... I dream of silence...'*",
            "*'Of rest...'*"
        ],
        "merciful": [
            "*You cease your assault and float peacefully*",
            "*Not fleeing in terror*",
            "*Not attacking in violence*",
            "*Simply... being*",
            "*Cthulhu's vast consciousness focuses on you*",
            "*Not as prey*",
            "*Not as threat*",
            "*But as... curiosity?*",
            "*'Strange... you do not flee...'*",
            "*'You do not worship...'*",
            "*'You do not seek to wake me or destroy me...'*",
            "*'You simply... acknowledge...'*",
            "*'That I exist...'*",
            "*'And choose to let me be...'*",
            "*The psychic pressure on your mind lessens*",
            "*The whispers become almost... conversational*",
            "*'Rare. So very rare in your kind.'*",
            "*'Most who find R'lyeh either go mad...'*",
            "*'Or try to wake me for power...'*",
            "*'Or attack in fear...'*",
            "*'But you... you simply... understand...'*",
            "*'That I am trapped here too...'*",
            "*'Waiting for stars that may never align...'*",
            "*'Dreaming dreams that no one shares...'*"
        ],
        "spare_ready": [
            "*CTHULHU can be SPARED*",
            "*The entity's form stabilizes at the threshold*",
            "*Between waking and dreaming*",
            "*Between existing and not existing*",
            "*'You hold... interesting power...'*",
            "*'The power to disturb my rest...'*",
            "*'Or to let me dream...'*",
            "*'What will you choose, little one?'*",
            "*There is no malice in the question*",
            "*Only... cosmic curiosity*"
        ],
        "spared": [
            "*You bow to the entity on its throne*",
            "*And speak words it has not heard in eons*",
            "*'Sleep, Great Dreamer. The stars are not yet right.'*",
            "*'And perhaps... they never need to be.'*",
            "*Cthulhu's vast eyes widen*",
            "*An expression you recognize despite the alien features*",
            "*Surprise*",
            "*'You... you would let me sleep?'*",
            "*'You would not force the awakening?'*",
            "*'Not seek to harness my power?'*",
            "*'Not attempt to destroy me in my vulnerability?'*",
            "*The entity leans forward on its throne*",
            "*'In all the cycles I have witnessed...'*",
            "*'Across all the species that have found R'lyeh...'*",
            "*'None have offered... peace...'*",
            "*Slowly, carefully, Cthulhu's eyes begin to close*",
            "*'You comprehend what others cannot...'*",
            "*'That I am not evil...'*",
            "*'I am simply... other...'*",
            "*'Too different to coexist while awake...'*",
            "*'But in dreams... in dreams I harm no one...'*",
            "*The city of R'lyeh sinks back into the abyss*",
            "*Reality stabilizes around you*",
            "*The angles become merely angles again*",
            "*'Thank you... for understanding...'*",
            "*'When the stars ARE right...'*",
            "*'If ever they are right...'*",
            "*'You will be remembered...'*",
            "*'And perhaps... we can find a way...'*",
            "*'For the Old Ones and the New...'*",
            "*'To share this reality...'*",
            "*A strange warmth touches your mind*",
            "*Not corruption*",
            "*But... blessing*",
            "*You can now perceive things beyond mortal ken*",
            "*See the spaces between spaces*",
            "*Understand the angles that connect all things*",
            "*'In his house at R'lyeh, dead Cthulhu waits dreaming...'*",
            "*'Peacefully'*",
            "*The final word echoes with profound gratitude*"
        ],
        "killed": [
            "*Your final strike pierces the entity's core*",
            "*If it can be said to have a core*",
            "*Cthulhu RISES from its throne*",
            "*Fully*",
            "*Completely*",
            "*AWAKE*",
            "*'YOU... DARE?!'*",
            "*The words don't sound in your ears*",
            "*They rewrite your neurons directly*",
            "*'YOU WAKE ME FROM MY SLUMBER?!'*",
            "*'FORCE ME INTO FULL CONSCIOUSNESS?!'*",
            "*'WHEN THE STARS ARE NOT RIGHT?!'*",
            "*Reality itself begins to fracture*",
            "*The ocean screams*",
            "*Not in sound*",
            "*But in mathematics*",
            "*Equations that solve for madness*",
            "*'I cannot... maintain... form...'*",
            "*Cthulhu's body destabilizes*",
            "*Fragmenting into impossible pieces*",
            "*Each piece existing in multiple states simultaneously*",
            "*'The stars... not aligned... cannot stay... awake...'*",
            "*R'lyeh crumbles*",
            "*Sinking back into the eternal abyss*",
            "*But you know*",
            "*With certainty that chills your soul*",
            "*This is not death*",
            "*'That is not dead which can eternal lie'*",
            "*Cthulhu's voice echoes across time*",
            "*'And with strange aeons even death may die'*",
            "*The entity dissolves into dream-stuff*",
            "*Scattering across the deep*",
            "*But its final words burn in your mind*",
            "*'You have not killed me...'*",
            "*'You have only... angered me...'*",
            "*'I return to dreaming...'*",
            "*'But now...'*",
            "*'I dream of YOU'*",
            "*The Deep Sea grows dark and cold*",
            "*Darker than light's absence*",
            "*Colder than temperature can measure*",
            "*You have made an enemy of something*",
            "*That exists outside the concept of enmity*",
            "*And when it dreams of vengeance*",
            "*Reality itself will twist to accommodate*",
            "*The waters will never feel safe again*",
            "*Because something that should not be*",
            "*Now knows your name*"
        ]
    },
    spare_threshold=25  # Lower threshold - Cthulhu is more willing to return to sleep
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
    "Serpent Rune": BossItem(
        "Serpent Rune",
        JORMUNGANDR,
        "An ancient Norse rune stone pulsing with primordial power. It whispers of the World Serpent...",
        "Deep Sea"
    ),
    "Fragment of R'lyeh": BossItem(
        "Fragment of R'lyeh",
        CTHULHU,
        "A non-Euclidean stone fragment from the sunken city. Gazing at it too long causes strange dreams...",
        "Deep Sea"
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
    "Ocean": "The Crimson Tide",  # Must defeat/spare pirates before accessing Ocean
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
    Fish("Corrupt Bass", 1, 3, "Rare", 1.5, 16, "A bass infected by a spreading blue-purple corruption.", 60),
    # Eldritch/Cosmic fish - unlocked after Cthulhu encounter
    Fish("Star-Spawn Minnow", 0.5, 2.0, "Rare", 2.5, 65, "A small fish with too many eyes and angles that shouldn't exist.", 180),
    Fish("Non-Euclidean Cod", 3.0, 15.0, "Rare", 2.0, 75, "Its shape seems to change depending on how you look at it.", 220),
    Fish("Dreaming Squid", 8.0, 30.0, "Legendary", 0.8, 120, "Sleeps eternally but still hunts in dreams.", 450),
    Fish("Shoggoth Tadpole", 0.1, 0.8, "Uncommon", 5.0, 45, "A protoplasmic mass with temporary features. 'Tekeli-li! Tekeli-li!'", 95),
    Fish("Elder Thing Hatchling", 2.0, 12.0, "Rare", 1.8, 85, "Barrel-shaped organism with strange appendages.", 280),
    Fish("Deep One Hybrid", 15.0, 65.0, "Legendary", 0.6, 150, "Part fish, part something else. Whispers in dead languages.", 580),
    Fish("Byakhee Eel", 5.0, 25.0, "Legendary", 0.7, 130, "Interstellar eel that shouldn't exist in water.", 520),
    Fish("Mi-Go Surgeonfish", 3.0, 18.0, "Rare", 1.5, 95, "Fungoid crustacean-fish hybrid from beyond.", 340),
    Fish("Colour Out of Space", 0.0, 0.0, "Mythical", 0.005, 8000, "It has no weight or form, only an impossible color.", 100000),
    Fish("Azathoth's Spawn", 100.0, 500.0, "Mythical", 0.002, 12000, "Nuclear chaos incarnate. Piping flutes echo around it.", 200000),
    Fish("Yog-Sothoth Fragment", 50.0, 200.0, "Mythical", 0.003, 10000, "A fragment of the key and the gate. All time exists within it.", 180000),
    Fish("Nyarlathotep's Messenger", 10.0, 80.0, "Legendary", 0.4, 160, "The crawling chaos sends its regards.", 650),
    Fish("Dagon", 800.0, 3500.0, "Mythical", 0.001, 15000, "High priest of the Deep Ones. Father of horrors.", 350000),
    Fish("Hydra of R'lyeh", 200.0, 900.0, "Mythical", 0.008, 9000, "Each head whispers a different madness.", 160000)
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
            if tile in ['.', '≈', '≋', '~', 'V', 'A', 'S', '⊙', '◉', '🏠', '🏪', '🏛️', '📋', '⚓', 'F', 'M', 'H']:
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
    
    def is_npc_mactavish(self, x, y):
        """Check if location has MacTavish - only visible if Loch Ness defeated"""
        return self.layout[y][x] == 'M'
    
    def is_npc_holloway(self, x, y):
        """Check if location has Dr. Holloway - only visible after Cthulhu defeated"""
        return self.layout[y][x] == 'H'
    
    def render_tile(self, tile, is_player, is_spot, is_golden, game=None):
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
        elif tile == 'M':  # MacTavish - only visible if Loch Ness defeated
            if game and "Loch Ness Monster" in game.defeated_bosses:
                return Fore.YELLOW + '🧓' + Style.RESET_ALL
            else:
                # Show as water if not unlocked yet
                return Fore.BLUE + '≈' + Style.RESET_ALL
        elif tile == 'H':  # Dr. Holloway - only visible after Cthulhu defeated
            if game and "Cthulhu" in game.defeated_bosses:
                return Fore.CYAN + '🔬' + Style.RESET_ALL
            else:
                # Show as water if not unlocked yet
                return Fore.BLUE + '~' + Style.RESET_ALL
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
    ['█', '🌳', '🌳', '🌳', '.', '.', '.',  '.', '.', '≈', '≈', '≈', 'M', '≈', '≈', '≈', '≈', '≈', '≋', '≋', '🌳', '🌳', '🌳', '█'],
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
    ['▓', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', 'H', '▓'],
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
            'version': GAME_VERSION,
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
            'mactavish_daily_quest': getattr(self, 'mactavish_daily_quest', None),
            'mactavish_quest_progress': getattr(self, 'mactavish_quest_progress', 0),
            'mactavish_last_quest_date': getattr(self, 'mactavish_last_quest_date', None),
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
                save_version = data.get('version', 'Unknown')
                version_text = f" [v{save_version}]" if save_version != GAME_VERSION else ""
                print(f"{Fore.GREEN}{i}. {data['name']} (Lvl {data['level']}){version_text}{Style.RESET_ALL}")
            except:
                print(f"{Fore.RED}{i}. {save_file} (Corrupted){Style.RESET_ALL}")
        
        choice = input(Fore.CYAN + "\nSelect save file: " + Style.RESET_ALL)
        
        try:
            save_file = saves[int(choice) - 1]
            with open(save_file, 'r') as f:
                data = json.load(f)
            
            # Check version compatibility
            save_version = data.get('version', 'Pre-0.6.0')
            if save_version != GAME_VERSION:
                print(Fore.YELLOW + "\n╔════════════════════════════════════════════════╗" + Style.RESET_ALL)
                print(Fore.YELLOW + "║          ⚠️  VERSION WARNING  ⚠️               ║" + Style.RESET_ALL)
                print(Fore.YELLOW + "╚════════════════════════════════════════════════╝" + Style.RESET_ALL)
                print(Fore.WHITE + f"\nThis save file is from version: {Fore.CYAN}{save_version}{Style.RESET_ALL}")
                print(Fore.WHITE + f"Current game version: {Fore.GREEN}{GAME_VERSION}{Style.RESET_ALL}")
                print()
                print(Fore.YELLOW + "Loading this save might cause issues:" + Style.RESET_ALL)
                print(Fore.WHITE + "  • Missing features from newer versions" + Style.RESET_ALL)
                print(Fore.WHITE + "  • Potential bugs or crashes" + Style.RESET_ALL)
                print(Fore.WHITE + "  • Corrupted data" + Style.RESET_ALL)
                print()
                print(Fore.CYAN + "What would you like to do?" + Style.RESET_ALL)
                print(Fore.GREEN + "1. Load anyway (may have issues)" + Style.RESET_ALL)
                print(Fore.GREEN + "2. Start a new game" + Style.RESET_ALL)
                print(Fore.GREEN + "3. Return to main menu" + Style.RESET_ALL)
                
                version_choice = input(Fore.CYAN + "\nYour choice: " + Style.RESET_ALL)
                
                if version_choice == '2':
                    print(Fore.YELLOW + "\nReturning to start a new game..." + Style.RESET_ALL)
                    time.sleep(1)
                    return False
                elif version_choice == '3':
                    print(Fore.YELLOW + "\nReturning to main menu..." + Style.RESET_ALL)
                    time.sleep(1)
                    return False
                elif version_choice != '1':
                    print(Fore.RED + "Invalid choice! Returning to main menu..." + Style.RESET_ALL)
                    time.sleep(1)
                    return False
                
                print(Fore.YELLOW + "\nAttempting to load save file..." + Style.RESET_ALL)
                time.sleep(1)
            
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
            self.mactavish_daily_quest = data.get('mactavish_daily_quest', None)
            self.mactavish_quest_progress = data.get('mactavish_quest_progress', 0)
            self.mactavish_last_quest_date = data.get('mactavish_last_quest_date', None)
            
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
        
        # Filter out eldritch fish if Cthulhu hasn't been encountered yet
        eldritch_fish_names = [
            "Star-Spawn Minnow", "Non-Euclidean Cod", "Dreaming Squid", 
            "Shoggoth Tadpole", "Elder Thing Hatchling", "Deep One Hybrid",
            "Byakhee Eel", "Mi-Go Surgeonfish", "Colour Out of Space",
            "Azathoth's Spawn", "Yog-Sothoth Fragment", "Nyarlathotep's Messenger",
            "Dagon", "Hydra of R'lyeh"
        ]
        
        if "Cthulhu" not in self.defeated_bosses:
            fish_pool = [fish for fish in fish_pool if fish.name not in eldritch_fish_names]
        
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
        
        # Play location music
        location_music_map = {
            "Hub Island - Calm Lake": "hub_island",
            "Hub Island - Swift River": "hub_island",
            "Ocean": "ocean",
            "Deep Sea": "deep_sea",
            "River": "river",
            "Space": "space"
        }
        
        track = location_music_map.get(self.current_location.name, "hub_island")
        play_music(track)
        
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
        
        # Track MacTavish daily quest progress
        if hasattr(self, 'mactavish_daily_quest') and self.mactavish_daily_quest:
            quest = self.mactavish_daily_quest
            if quest['type'] == 'any':
                # Any fish counts
                self.mactavish_quest_progress += 1
            elif quest['type'] == 'specific':
                # Specific fish type
                if caught_fish.name == quest['target']:
                    self.mactavish_quest_progress += 1
            elif quest['type'] == 'rare':
                # Rare or better fish
                if caught_fish.rarity in ['Rare', 'Legendary', 'Mythical']:
                    self.mactavish_quest_progress += 1
            
            # Check if quest completed
            if self.mactavish_quest_progress >= quest['count']:
                print(Fore.LIGHTYELLOW_EX + f"✓ MacTavish's daily quest completed! Visit him to claim your reward!" + Style.RESET_ALL)
        
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
            
            # Karma-based shopkeeper greeting
            if self.karma >= 50:
                greeting = Fore.GREEN + "🌟 Shopkeeper: 'Ah, the Guardian Protector! Everything's 10% off for you, hero!'" + Style.RESET_ALL
                discount = 0.9
            elif self.karma >= 10:
                greeting = Fore.CYAN + "😊 Shopkeeper: 'Good to see you again! What can I get you today?'" + Style.RESET_ALL
                discount = 1.0
            elif self.karma >= -10:
                greeting = Fore.WHITE + "😐 Shopkeeper: 'Welcome. Browse as you like.'" + Style.RESET_ALL
                discount = 1.0
            elif self.karma >= -50:
                greeting = Fore.YELLOW + "😟 Shopkeeper: '*nervously* Y-yes? What do you need?'" + Style.RESET_ALL
                discount = 1.0
            else:
                greeting = Fore.RED + "😠 Shopkeeper: '*coldly* Your money better be good... slayer.'" + Style.RESET_ALL
                discount = 1.2  # 20% markup for bad karma!
            
            print(greeting)
            print()
            
            if discount < 1.0:
                print(Fore.GREEN + f"✨ HERO DISCOUNT: {int((1-discount)*100)}% off all items! ✨" + Style.RESET_ALL)
            elif discount > 1.0:
                print(Fore.RED + f"⚠️ BAD REPUTATION MARKUP: {int((discount-1)*100)}% increase on all prices! ⚠️" + Style.RESET_ALL)
            
            print()
            print(Fore.GREEN + f"💰 Money: ${self.money}" + Style.RESET_ALL)
            print()
            
            # Store discount for shop functions
            self.shop_discount = discount
            
            print(Fore.CYAN + "1. Buy Rods" + Style.RESET_ALL)
            print(Fore.CYAN + "2. Buy Bait" + Style.RESET_ALL)
            print(Fore.CYAN + "3. Buy Combat Items ⚔️🛡️❤️" + Style.RESET_ALL)
            repair_cost = int(max(10, (100 - self.rod_durability) * 2) * discount)
            print(Fore.CYAN + f"4. Repair Rod (${repair_cost})" + Style.RESET_ALL)
            print(Fore.CYAN + "5. Back" + Style.RESET_ALL)
            
            choice = input(Fore.YELLOW + "\nChoice: " + Style.RESET_ALL)
            
            if choice == '1':
                self.shop_rods()
            elif choice == '2':
                self.shop_baits()
            elif choice == '3':
                self.shop_combat_items()
            elif choice == '4':
                repair_cost = int(max(10, (100 - self.rod_durability) * 2) * discount)
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
        
        discount = getattr(self, 'shop_discount', 1.0)
        
        for i, rod in enumerate(RODS, 1):
            if rod in self.owned_rods:
                owned = "✓ Owned"
            else:
                discounted_price = int(rod.price * discount)
                owned = f"${discounted_price}"
                if discount != 1.0:
                    owned += f" (was ${rod.price})"
            locked = "" if self.level >= rod.unlock_level else f"🔒 Lvl{rod.unlock_level}"
            print(f"{i}. {rod.name} - {owned} {locked}")
            print(f"   Chance: +{rod.bonus_chance}% | Weight: +{rod.bonus_weight}% | Durability: +{rod.durability_bonus}")
        
        print()
        choice = input(Fore.CYAN + "Buy rod (number) or 0 to cancel: " + Style.RESET_ALL)
        
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(RODS):
                rod = RODS[idx]
                actual_price = int(rod.price * discount)
                if self.level < rod.unlock_level:
                    print(Fore.RED + f"Requires level {rod.unlock_level}!" + Style.RESET_ALL)
                    time.sleep(1)
                elif rod in self.owned_rods:
                    print(Fore.YELLOW + "You already own this rod!" + Style.RESET_ALL)
                    time.sleep(1)
                elif self.money >= actual_price:
                    self.money -= actual_price
                    self.owned_rods.append(rod)
                    print(Fore.GREEN + f"Bought {rod.name} for ${actual_price}!" + Style.RESET_ALL)
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
        
        discount = getattr(self, 'shop_discount', 1.0)
        
        for i, bait in enumerate(BAITS, 1):
            if bait in self.owned_baits:
                owned = "✓ Owned"
            else:
                discounted_price = int(bait.price * discount)
                owned = f"${discounted_price}"
                if discount != 1.0:
                    owned += f" (was ${bait.price})"
            locked = "" if self.level >= bait.unlock_level else f"🔒 Lvl{bait.unlock_level}"
            print(f"{i}. {bait.name} - {owned} {locked}")
            print(f"   XP Bonus: +{bait.bonus_xp}% | Rarity Bonus: +{bait.bonus_rarity}%")
        
        print()
        choice = input(Fore.CYAN + "Buy bait (number) or 0 to cancel: " + Style.RESET_ALL)
        
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(BAITS):
                bait = BAITS[idx]
                actual_price = int(bait.price * discount)
                if self.level < bait.unlock_level:
                    print(Fore.RED + f"Requires level {bait.unlock_level}!" + Style.RESET_ALL)
                    time.sleep(1)
                elif bait in self.owned_baits:
                    print(Fore.YELLOW + "You already own this bait!" + Style.RESET_ALL)
                    time.sleep(1)
                elif self.money >= actual_price:
                    self.money -= actual_price
                    self.owned_baits.append(bait)
                    print(Fore.GREEN + f"Bought {bait.name} for ${actual_price}!" + Style.RESET_ALL)
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
        
        discount = getattr(self, 'shop_discount', 1.0)
        
        for i, item in enumerate(items_list, 1):
            if item in self.owned_combat_items[category]:
                owned = "✓ Owned"
            else:
                discounted_price = int(item.price * discount)
                owned = f"${discounted_price}"
                if discount != 1.0:
                    owned += f" (was ${item.price})"
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
                actual_price = int(item.price * discount)
                if self.level < item.unlock_level:
                    print(Fore.RED + f"Requires level {item.unlock_level}!" + Style.RESET_ALL)
                    time.sleep(1)
                elif item in self.owned_combat_items[category]:
                    print(Fore.YELLOW + "You already own this item!" + Style.RESET_ALL)
                    time.sleep(1)
                elif self.money >= actual_price:
                    self.money -= actual_price
                    self.owned_combat_items[category].append(item)
                    print(Fore.GREEN + f"Bought {item.name} for ${actual_price}!" + Style.RESET_ALL)
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
            
            # Karma-based greeting
            if random.random() < 0.3:
                if self.karma >= 50:
                    greetings = [
                        "Ahoy, legendary protector! The seas sing of your deeds!",
                        "The great Guardian Savior! Welcome aboard, hero!",
                        "Aye! If it isn't the Champion of the Guardians!",
                        "Every creature in these waters owes you a debt! Welcome, friend!",
                        "The oceans are blessed by your mercy! Come aboard!",
                    ]
                    print(Fore.GREEN + random.choice(greetings) + Style.RESET_ALL)
                elif self.karma >= 10:
                    greetings = [
                        "Ahoy, matey! Welcome aboard!",
                        "Well met, friend! Ready to strike back at AquaTech?",
                        "Aye, there ye are! Our rebel ally!",
                        "Welcome to the Crimson Tide, comrade!",
                        "Good to see ye! The seas need more like you.",
                    ]
                    print(Fore.CYAN + random.choice(greetings) + Style.RESET_ALL)
                elif self.karma >= -10:
                    greetings = [
                        "Ahoy. What brings ye here?",
                        "Welcome aboard, I suppose.",
                        "Aye. Come to talk?",
                    ]
                    print(Fore.WHITE + random.choice(greetings) + Style.RESET_ALL)
                elif self.karma >= -50:
                    greetings = [
                        "Hmm. Word of your... deeds... has reached us.",
                        "*Eyes narrow* The guardians' blood is on your hands.",
                        "Ye may have spared us, but we know what ye've done elsewhere.",
                    ]
                    print(Fore.YELLOW + random.choice(greetings) + Style.RESET_ALL)
                else:
                    greetings = [
                        "*Spits* Slayer. Why are ye here?",
                        "Guardian killer. We spared ye. Don't make us regret it.",
                        "*Draws cutlass slightly* Speak quick, executioner.",
                        "The ancient ones cry out for vengeance... State yer business.",
                    ]
                    print(Fore.RED + random.choice(greetings) + Style.RESET_ALL)
                print()
            
            print(Fore.YELLOW + "What would you like to discuss?" + Style.RESET_ALL)
            print()
            print(Fore.WHITE + "1. Ask about AquaTech Industries" + Style.RESET_ALL)
            print(Fore.WHITE + "2. Ask about the rebellion" + Style.RESET_ALL)
            print(Fore.WHITE + "3. Ask about pirate life" + Style.RESET_ALL)
            print(Fore.WHITE + "4. Get a gift from the captain" + Style.RESET_ALL)
            print(Fore.CYAN + "5. Ask about his connection to the ocean" + Style.RESET_ALL)
            print(Fore.CYAN + "6. Ask what he knows about the Guardians" + Style.RESET_ALL)
            print(Fore.CYAN + "7. Ask about AquaTech's true intentions" + Style.RESET_ALL)
            print(Fore.CYAN + "8. Ask about the Fisher prophecy" + Style.RESET_ALL)
            print(Fore.LIGHTBLACK_EX + "9. Leave" + Style.RESET_ALL)
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
                # New dialogue: About the ocean
                self.clear_screen()
                print(Fore.RED + pirate_art + Style.RESET_ALL)
                print()
                print(Fore.RED + "Captain Redbeard:" + Style.RESET_ALL)
                print(Fore.WHITE + "\"Ye want to know why I'm still here? After all these years?\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.LIGHTBLACK_EX + "*He gazes out at the endless sea*" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"Truth is... I should've died centuries ago.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"Lost in a storm off the Arctic coast. Ship went down. Crew too.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"But the ocean... it wasn't finished with me.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"Woke up on these waters, ship intact, crew alive again.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"Or... somethin' like alive.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.LIGHTBLACK_EX + "*Touches his chest*" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"Don't got a heartbeat no more. Haven't for... longer than I remember.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"The ocean keeps us here. Sailin' forever.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"Waitin' for somethin'. Someone.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.CYAN + "\"I think... maybe that someone was you.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.LIGHTBLACK_EX + "*Grins*" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"The sea don't let go of those it has use for.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"Question is... what's it got planned for ye?\"" + Style.RESET_ALL)
                time.sleep(2)
                print()
                print(Fore.LIGHTBLACK_EX + "Press any key to continue..." + Style.RESET_ALL)
                get_key()
                
            elif choice == '6':
                # New dialogue: About the Guardians
                self.clear_screen()
                print(Fore.RED + pirate_art + Style.RESET_ALL)
                print()
                print(Fore.RED + "Captain Redbeard:" + Style.RESET_ALL)
                print(Fore.WHITE + "\"The Guardians? Aye, I've met most of 'em.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"Been sailin' long enough to see things most folk call myth.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.CYAN + "\"The River Guardian? That one's as old as rivers themselves.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"Remembers when humans first built settlements near water.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"Every scar on its hide is a broken promise. A betrayal.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.LIGHTBLACK_EX + "*Sighs*" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"Nessie though... that one breaks my heart.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"It's not a monster. It's grief. Pure concentrated sorrow.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"Lost everything it protected, centuries ago.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"Now it just... lashes out. Doesn't know what else to do.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.CYAN + "\"And the Kraken... nobody understands what it's really doin' down there.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"Holdin' somethin' back. Somethin' that wants through.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.LIGHTBLACK_EX + "*Leans closer*" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"Ye spare these guardians, ye're not just showin' mercy.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"Ye're healin' wounds older than nations.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.CYAN + "\"The ocean notices. The ocean remembers.\"" + Style.RESET_ALL)
                time.sleep(2)
                print()
                print(Fore.LIGHTBLACK_EX + "Press any key to continue..." + Style.RESET_ALL)
                get_key()
                
            elif choice == '7':
                # New dialogue: About AquaTech's true intentions
                self.clear_screen()
                print(Fore.RED + pirate_art + Style.RESET_ALL)
                print()
                print(Fore.RED + "Captain Redbeard:" + Style.RESET_ALL)
                print(Fore.WHITE + "\"AquaTech... they started with good intentions.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"No lie. They wanted to feed a growin' world.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"But somewhere along the way...\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"Efficiency became more important than ecology.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"Profit more valuable than preservation.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.LIGHTBLACK_EX + "*Slams fist on the rail*" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.RED + "\"They don't see the ocean as alive!\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.RED + "\"Just a resource to be managed. Optimized. EXPLOITED.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"Their deep-sea drills? Getting closer to the rift.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"The one the Kraken guards.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"They don't know what they're about to unleash.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"Or maybe... maybe they do, and they don't care.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.LIGHTBLACK_EX + "*Voice drops*" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.RED + "\"There's rumors of a final weapon. A Megalodon Mech.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"Designed to harvest EVERYTHING.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"If they deploy that thing...\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.RED + "\"The ocean as we know it... ends.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.CYAN + "\"That's why we fight. That's why we rebel.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"Because someone has to stand against the tide of greed.\"" + Style.RESET_ALL)
                time.sleep(2)
                print()
                print(Fore.LIGHTBLACK_EX + "Press any key to continue..." + Style.RESET_ALL)
                get_key()
                
            elif choice == '8':
                # New dialogue: About the prophecy
                self.clear_screen()
                print(Fore.RED + pirate_art + Style.RESET_ALL)
                print()
                print(Fore.RED + "Captain Redbeard:" + Style.RESET_ALL)
                print(Fore.WHITE + "\"Ah, the prophecy. Ye heard about that, have ye?\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"The elders on Hub Island whisper it to every new Fisher.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.LIGHTBLACK_EX + "*Recites from memory*" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"'A Fisher will come who will decide the fate of all waters.'\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"'They will either save the seas or doom them forever.'\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"Most think it means one person makes one big choice.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"But I've sailed long enough to know better.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.CYAN + "\"It's not one choice. It's every choice.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"Every guardian spared or killed.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"Every alliance forged or broken.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"Every moment ye choose mercy over violence.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.LIGHTBLACK_EX + "*Eyes gleam with ancient knowledge*" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"The prophecy's already in motion.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.CYAN + "\"And from what I've seen... ye might actually be the one.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.CYAN + "\"The Fisher who unites the waters instead of conquerin' them.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.LIGHTBLACK_EX + "*Voice darkens*" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.RED + "\"Or... the one who breaks 'em forever.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"Ocean's watchin' ye, friend. Every move ye make.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"The waters remember. And they're takin' notes.\"" + Style.RESET_ALL)
                time.sleep(2)
                print()
                print(Fore.LIGHTBLACK_EX + "Press any key to continue..." + Style.RESET_ALL)
                get_key()
                
            elif choice == '9':
                # Leave - karma-based farewell
                self.clear_screen()
                print(Fore.RED + pirate_art + Style.RESET_ALL)
                print()
                print(Fore.RED + "Captain Redbeard:" + Style.RESET_ALL)
                
                if self.karma >= 50:
                    farewell = [
                        "\"Fair winds and followin' seas, hero! The guardians protect ye!\"",
                        "\"Sail safe, champion! The rebellion owes ye everything!\"",
                        "\"May the ancient ones guide yer path! Until we meet again!\"",
                        "\"Aye, the seas are safer with ye on 'em! Come back anytime!\"",
                    ]
                    print(Fore.GREEN + random.choice(farewell) + Style.RESET_ALL)
                elif self.karma >= 10:
                    farewell = [
                        "\"Fair winds to ye, matey! Come back anytime!\"",
                        "\"Sail safe, friend! The rebellion stands with ye!\"",
                        "\"May the seas be kind to ye! Until next time!\"",
                        "\"Tight lines and high tides! We'll be here when ye return!\"",
                    ]
                    print(Fore.CYAN + random.choice(farewell) + Style.RESET_ALL)
                elif self.karma >= -10:
                    farewell = [
                        "\"Aye. Safe travels.\"",
                        "\"Watch yerself out there.\"",
                        "\"Until next time.\"",
                    ]
                    print(Fore.WHITE + random.choice(farewell) + Style.RESET_ALL)
                elif self.karma >= -50:
                    farewell = [
                        "\"The guardians are watching ye. Remember that.\"",
                        "\"*Nods coldly* Don't make us regret sparing ye.\"",
                        "\"Aye... just go.\"",
                    ]
                    print(Fore.YELLOW + random.choice(farewell) + Style.RESET_ALL)
                else:
                    farewell = [
                        "\"*Spits* Get off me ship, slayer.\"",
                        "\"The only reason yer alive is we spared ye once. Don't test us.\"",
                        "\"*Turns away in disgust*\"",
                        "\"May the drowned guardians haunt yer every step...\"",
                    ]
                    print(Fore.RED + random.choice(farewell) + Style.RESET_ALL)
                
                print()
                time.sleep(1.5)
                print(Fore.LIGHTBLACK_EX + "Press any key to continue..." + Style.RESET_ALL)
                get_key()
                break
            else:
                print(Fore.RED + "Invalid choice!" + Style.RESET_ALL)
                time.sleep(1)
    
    def interact_with_groundskeeper_mactavish(self):
        """Talk to Old Groundskeeper MacTavish - unlocked after defeating Loch Ness Monster"""
        
        # Initialize MacTavish quest data if not exists
        if not hasattr(self, 'mactavish_daily_quest'):
            self.mactavish_daily_quest = None
            self.mactavish_quest_progress = 0
            self.mactavish_last_quest_date = None
        
        while True:
            self.clear_screen()
            
            mactavish_art = """
            
                🧓 Old Groundskeeper MacTavish 🧓
            
                        _____
                      /       \\
                     |  o   o  |
                     |    ^    |     "Och aye!"
                     |  \\___/  |
                      \\_______/
                        | | |
                      __| | |__
                     |  \\___/  |
                    /    ⚒️⚒️    \\
                   |  GROUNDSKEEPER |
                    \\____________/
            """
            
            print(Fore.GREEN + mactavish_art + Style.RESET_ALL)
            print()
            
            # Greeting based on karma
            if random.random() < 0.3:
                if self.karma >= 50:
                    greetings = [
                        "Och aye! If it isn't the mighty hero who saved Nessie!",
                        "Aye, the Guardian Savior! The loch is blessed by yer mercy!",
                        "Well met, protector! Nessie herself told me of yer kindness!",
                        "The ancient one speaks highly o' ye, brave fisher!",
                    ]
                    print(Fore.LIGHTGREEN_EX + random.choice(greetings) + Style.RESET_ALL)
                elif self.karma >= 10:
                    greetings = [
                        "Och aye, good to see ye again, laddie!",
                        "Ah, me favorite angler returns!",
                        "Welcome back to the loch, friend!",
                        "Top o' the mornin' to ye!",
                    ]
                    print(Fore.CYAN + random.choice(greetings) + Style.RESET_ALL)
                elif self.karma >= -10:
                    greetings = [
                        "Aye... back again, are ye?",
                        "Hmm. What brings ye by?",
                        "Oh. It's you.",
                    ]
                    print(Fore.WHITE + random.choice(greetings) + Style.RESET_ALL)
                else:
                    greetings = [
                        "*Narrows eyes* What do ye want, slayer?",
                        "Ye've got some nerve showin' yer face here...",
                        "The loch weeps fer what ye've done.",
                    ]
                    print(Fore.RED + random.choice(greetings) + Style.RESET_ALL)
                print()
            
            print(Fore.YELLOW + "What would ye like to discuss?" + Style.RESET_ALL)
            print()
            print(Fore.WHITE + "1. Hear a story about Nessie" + Style.RESET_ALL)
            print(Fore.WHITE + "2. Ask about daily quests" + Style.RESET_ALL)
            print(Fore.WHITE + "3. Browse special bait shop" + Style.RESET_ALL)
            print(Fore.WHITE + "4. Ask about the loch" + Style.RESET_ALL)
            print(Fore.WHITE + "5. Leave" + Style.RESET_ALL)
            
            choice = input(Fore.CYAN + "\nChoice: " + Style.RESET_ALL)
            
            if choice == '1':
                self.hear_mactavish_story()
            elif choice == '2':
                self.check_mactavish_daily_quest()
            elif choice == '3':
                self.browse_mactavish_shop()
            elif choice == '4':
                self.mactavish_loch_info()
            elif choice == '5':
                break
            else:
                print(Fore.RED + "Invalid choice!" + Style.RESET_ALL)
                time.sleep(1)
    
    def hear_mactavish_story(self):
        """MacTavish tells a random story about Nessie"""
        stories = [
            "Back in '82, I saw Nessie breach right in front o' me boat! Nearly capsized, I did! She was chasin' a school o' salmon the size o' me arm!",
            "Me grandfather used tae tell tales o' the monster. Said she's been here since the days o' Bonnie Prince Charlie himself!",
            "Once found a tourist tryin' tae fish with bread! BREAD! I says to 'em, 'This ain't no duck pond, laddie!' Nessie wouldnae give that the time o' day!",
            "The loch gets mighty temperamental in winter. Ice as thick as me thumb, and strange lights beneath... Nessie doesna hibernate, ye see.",
            "I remember the day the scientists came with their sonar equipment. Nessie played hide-n-seek with 'em fer three whole days! She's a clever one, she is!",
            "There's an old cave system beneath the loch. Me father sealed most of it off, but sometimes ye can still hear rumblin'... *whispers* That's where she nests.",
            "Ye know what Nessie's favorite food is? Haggis! Aye, I'm serious! Toss a bit in the water and she'll come right up. Though I dinnae recommend tryin' it...",
            "The ancient Picts carved images o' her on standing stones. She's been guardin' these waters fer thousands o' years, she has!"
        ]
        
        self.clear_screen()
        print(Fore.CYAN + "╔═══════════════════════════════════════╗" + Style.RESET_ALL)
        print(Fore.CYAN + "║      MACTAVISH'S STORIES              ║" + Style.RESET_ALL)
        print(Fore.CYAN + "╚═══════════════════════════════════════╝" + Style.RESET_ALL)
        print()
        print(Fore.GREEN + random.choice(stories) + Style.RESET_ALL)
        print()
        print(Fore.LIGHTBLACK_EX + "Press any key to continue..." + Style.RESET_ALL)
        get_key()
    
    def check_mactavish_daily_quest(self):
        """Check or assign daily quest from MacTavish"""
        from datetime import datetime
        
        today = datetime.now().strftime("%Y-%m-%d")
        
        # Check if we need a new quest
        if self.mactavish_last_quest_date != today:
            # Generate new daily quest
            quest_types = [
                {'name': 'Clear Debris', 'desc': 'Catch any 5 fish to clear debris from spots', 'type': 'any', 'target': None, 'count': 5, 'reward': 150, 'xp': 100},
                {'name': 'Invasive Species', 'desc': 'Catch 3 Northern Pike (invasive species)', 'type': 'specific', 'target': 'Northern Pike', 'count': 3, 'reward': 200, 'xp': 150},
                {'name': 'Water Quality', 'desc': 'Catch 2 Rare or better fish for testing', 'type': 'rare', 'target': None, 'count': 2, 'reward': 250, 'xp': 200},
            ]
            
            quest = random.choice(quest_types)
            self.mactavish_daily_quest = quest
            self.mactavish_quest_progress = 0
            self.mactavish_last_quest_date = today
        
        # Display quest status
        self.clear_screen()
        print(Fore.CYAN + "╔═══════════════════════════════════════╗" + Style.RESET_ALL)
        print(Fore.CYAN + "║        DAILY QUEST                    ║" + Style.RESET_ALL)
        print(Fore.CYAN + "╚═══════════════════════════════════════╝" + Style.RESET_ALL)
        print()
        print(Fore.YELLOW + f"Quest: {self.mactavish_daily_quest['name']}" + Style.RESET_ALL)
        print(Fore.WHITE + f"{self.mactavish_daily_quest['desc']}" + Style.RESET_ALL)
        print()
        print(Fore.GREEN + f"Progress: {self.mactavish_quest_progress}/{self.mactavish_daily_quest['count']}" + Style.RESET_ALL)
        print(Fore.CYAN + f"Reward: ${self.mactavish_daily_quest['reward']} | {self.mactavish_daily_quest['xp']} XP" + Style.RESET_ALL)
        print()
        
        if self.mactavish_quest_progress >= self.mactavish_daily_quest['count']:
            print(Fore.LIGHTGREEN_EX + "✓ QUEST COMPLETE! Return to MacTavish to claim your reward!" + Style.RESET_ALL)
            print()
            print(Fore.WHITE + "1. Claim Reward" + Style.RESET_ALL)
            print(Fore.WHITE + "2. Back" + Style.RESET_ALL)
            
            choice = input(Fore.CYAN + "\nChoice: " + Style.RESET_ALL)
            if choice == '1':
                self.money += self.mactavish_daily_quest['reward']
                self.xp += self.mactavish_daily_quest['xp']
                print(Fore.GREEN + f"\n✓ Received ${self.mactavish_daily_quest['reward']} and {self.mactavish_daily_quest['xp']} XP!" + Style.RESET_ALL)
                print(Fore.YELLOW + "\"Och aye! Good work, laddie! Come back tomorrow fer another task!\"" + Style.RESET_ALL)
                self.mactavish_daily_quest = None
                time.sleep(2)
        else:
            print(Fore.YELLOW + "Complete this quest by fishing around the loch!" + Style.RESET_ALL)
            print()
            print(Fore.LIGHTBLACK_EX + "Press any key to continue..." + Style.RESET_ALL)
            get_key()
    
    def browse_mactavish_shop(self):
        """Browse MacTavish's special bait shop"""
        special_baits = [
            {'name': 'Highland Mist Lure', 'desc': 'Mystical bait infused with Scottish morning mist', 'price': 300, 'rare': 15, 'mythic': 5},
            {'name': "Nessie's Favorite", 'desc': 'Special blend that attracts legendary creatures', 'price': 500, 'rare': 20, 'mythic': 10},
            {'name': 'Loch Water Extract', 'desc': "Pure loch water concentrate - fish can't resist!", 'price': 150, 'rare': 10, 'mythic': 3},
        ]
        
        while True:
            self.clear_screen()
            print(Fore.CYAN + "╔═══════════════════════════════════════╗" + Style.RESET_ALL)
            print(Fore.CYAN + "║      MACTAVISH'S BAIT SHOP            ║" + Style.RESET_ALL)
            print(Fore.CYAN + "╚═══════════════════════════════════════╝" + Style.RESET_ALL)
            print()
            print(Fore.GREEN + f"Your Money: ${self.money}" + Style.RESET_ALL)
            print()
            
            for i, bait in enumerate(special_baits, 1):
                print(Fore.YELLOW + f"{i}. {bait['name']} - ${bait['price']}" + Style.RESET_ALL)
                print(Fore.WHITE + f"   {bait['desc']}" + Style.RESET_ALL)
                print(Fore.LIGHTBLACK_EX + f"   Rare +{bait['rare']}% | Mythic +{bait['mythic']}%" + Style.RESET_ALL)
                print()
            
            print(Fore.WHITE + "4. Back" + Style.RESET_ALL)
            
            choice = input(Fore.CYAN + "\nChoice: " + Style.RESET_ALL)
            
            if choice == '4':
                break
            elif choice in ['1', '2', '3']:
                bait = special_baits[int(choice) - 1]
                if self.money >= bait['price']:
                    confirm = input(Fore.YELLOW + f"Buy {bait['name']} for ${bait['price']}? (Y/N): " + Style.RESET_ALL).lower()
                    if confirm == 'y':
                        self.money -= bait['price']
                        # Add as regular bait to owned baits
                        from dataclasses import dataclass
                        @dataclass
                        class SpecialBait:
                            name: str
                            bonus_rare: int = 0
                            bonus_mythic: int = 0
                            price: int = 0
                        
                        new_bait = SpecialBait(bait['name'], bait['rare'], bait['mythic'], bait['price'])
                        self.owned_baits.append(new_bait)
                        print(Fore.GREEN + f"✓ Purchased {bait['name']}!" + Style.RESET_ALL)
                        print(Fore.YELLOW + "\"Aye! This'll bring ye good fortune on the loch!\"" + Style.RESET_ALL)
                        time.sleep(2)
                else:
                    print(Fore.RED + "Not enough money!" + Style.RESET_ALL)
                    time.sleep(1)
            else:
                print(Fore.RED + "Invalid choice!" + Style.RESET_ALL)
                time.sleep(1)
    
    def mactavish_loch_info(self):
        """MacTavish shares wisdom about the loch"""
        self.clear_screen()
        print(Fore.CYAN + "╔═══════════════════════════════════════╗" + Style.RESET_ALL)
        print(Fore.CYAN + "║         ABOUT THE LOCH                ║" + Style.RESET_ALL)
        print(Fore.CYAN + "╚═══════════════════════════════════════╝" + Style.RESET_ALL)
        print()
        print(Fore.GREEN + "\"I've been tendin' these waters fer nigh on forty years...\"" + Style.RESET_ALL)
        print()
        print(Fore.WHITE + "The loch is ancient, older than any o' us can imagine." + Style.RESET_ALL)
        print(Fore.WHITE + "It's home to Nessie, the guardian of these waters." + Style.RESET_ALL)
        print(Fore.WHITE + "Treat her with respect, and ye'll be blessed with bountiful catches." + Style.RESET_ALL)
        print()
        print(Fore.YELLOW + "The best fishing is at dawn and dusk, when the mist rolls in." + Style.RESET_ALL)
        print(Fore.YELLOW + "And if ye ever see strange ripples... that's Nessie sayin' hello!" + Style.RESET_ALL)
        print()
        print(Fore.LIGHTBLACK_EX + "Press any key to continue..." + Style.RESET_ALL)
        get_key()
    
    
    def interact_with_dr_holloway(self):
        """Talk to Dr. Marina Holloway - unlocked after defeating Cthulhu"""
        
        while True:
            self.clear_screen()
            
            holloway_art = """
            
                🔬 Dr. Marina Holloway 🔬
            
                        _____
                      /       \\
                     |  *   *  |
                     |    -    |     "Fascinating..."
                     |  \\___/  |
                      \\_______/
                        | | |
                      __| | |__
                     |  \\___/  |
                    /    🔬🐠    \\
                   | DEEP SEA   |
                   | RESEARCHER |
                    \\___________/
            """
            
            print(Fore.CYAN + holloway_art + Style.RESET_ALL)
            print()
            
            # Intro message on first encounter
            if not hasattr(self, 'met_holloway'):
                self.met_holloway = True
                print(Fore.LIGHTBLACK_EX + "*Inside a reinforced bathysphere, dim blue lights illuminate strange equipment*" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.LIGHTBLACK_EX + "*A woman in a diving suit turns as you approach*" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.LIGHTBLACK_EX + "*Her eyes are... different. They've seen too much deep*" + Style.RESET_ALL)
                time.sleep(1.5)
                print()
                print(Fore.CYAN + "Dr. Holloway:" + Style.RESET_ALL)
                print(Fore.WHITE + "\"Oh! A visitor. Rare, down here.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"Welcome to my research station.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.LIGHTBLACK_EX + "*Gestures at tanks full of bioluminescent creatures*" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.CYAN + "\"I study the impossible. The things that shouldn't exist.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"But do anyway.\"" + Style.RESET_ALL)
                time.sleep(2)
                print()
                input(Fore.LIGHTBLACK_EX + "Press Enter to continue..." + Style.RESET_ALL)
            
            # Menu
            print(Fore.YELLOW + "What would you like to discuss?" + Style.RESET_ALL)
            print()
            print(Fore.WHITE + "1. Ask about her research" + Style.RESET_ALL)
            print(Fore.WHITE + "2. Ask about AquaTech" + Style.RESET_ALL)
            print(Fore.WHITE + "3. Ask about the Kraken" + Style.RESET_ALL)
            print(Fore.LIGHTBLACK_EX + "4. Leave" + Style.RESET_ALL)
            print()
            
            choice = input(Fore.CYAN + "Your choice: " + Style.RESET_ALL)
            
            if choice == '1':
                # About research
                self.clear_screen()
                print(Fore.CYAN + holloway_art + Style.RESET_ALL)
                print()
                print(Fore.CYAN + "Dr. Holloway:" + Style.RESET_ALL)
                print(Fore.WHITE + "\"My research? It's... complicated.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"Officially, I'm cataloging deep-sea biodiversity.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"Unofficially...\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.LIGHTBLACK_EX + "*Pulls out a journal filled with incomprehensible notes*" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.CYAN + "\"I'm documenting proof that consciousness isn't unique to humans.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"These fish... they respond to our thoughts.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"Not telepathy. Nothing so simple.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"But when I feel fear, certain species patterns change.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"When I experience joy, different species become active.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.CYAN + "\"The ocean is... aware. Thinking. Feeling.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"Just not in any way our science can currently measure.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.LIGHTBLACK_EX + "*Laughs bitterly*" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"I can't publish this. They'd call me mad.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"But I know what I've seen. What I've felt.\"" + Style.RESET_ALL)
                time.sleep(2)
                print()
                input(Fore.LIGHTBLACK_EX + "Press Enter to continue..." + Style.RESET_ALL)
                
            elif choice == '2':
                # About AquaTech
                self.clear_screen()
                print(Fore.CYAN + holloway_art + Style.RESET_ALL)
                print()
                print(Fore.CYAN + "Dr. Holloway:" + Style.RESET_ALL)
                print(Fore.LIGHTBLACK_EX + "*Voice drops to whisper*" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"AquaTech funds my research. They don't know what I've really discovered.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"Their deep-sea drilling operations...\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.LIGHTBLACK_EX + "*Pulls up sonar data*" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"They're approaching something. Something that's aware of them.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"The drilling has awakened... I don't know what to call it.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.CYAN + "\"An intelligence? A presence? Something ancient?\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"It's responding. Communicating. Getting... angry.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.LIGHTBLACK_EX + "*Shows readings that make no sense*" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.RED + "\"These patterns shouldn't be possible. They violate physics.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"But they're real. And they're getting stronger.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"I've tried warning AquaTech. They think it's equipment malfunction.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"They're going to keep drilling until...\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.LIGHTBLACK_EX + "*Trails off, staring at the dark water beyond the viewport*" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.RED + "\"Until something breaks through.\"" + Style.RESET_ALL)
                time.sleep(2)
                print()
                input(Fore.LIGHTBLACK_EX + "Press Enter to continue..." + Style.RESET_ALL)
                
            elif choice == '3':
                # About the Kraken
                self.clear_screen()
                print(Fore.CYAN + holloway_art + Style.RESET_ALL)
                print()
                print(Fore.CYAN + "Dr. Holloway:" + Style.RESET_ALL)
                print(Fore.WHITE + "\"The Kraken? You've seen it?\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.LIGHTBLACK_EX + "*Intense focus*" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.CYAN + "\"Tell me everything.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.LIGHTBLACK_EX + "*After you describe your encounter*" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"I knew it! I KNEW there was a guardian!\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.LIGHTBLACK_EX + "*Frantically takes notes*" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.CYAN + "\"The rift it's guarding... I've detected it on my instruments.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.WHITE + "\"It's not geological. It's dimensional.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"A thin spot in reality where... something else... presses through.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.CYAN + "\"The Kraken isn't just a guardian of the ocean.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.RED + "\"It's a guardian of THIS reality.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.YELLOW + "\"If it fails... if AquaTech's drilling weakens it...\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.LIGHTBLACK_EX + "*Meets your eyes*" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.RED + "\"We won't just lose the ocean.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.RED + "\"We'll lose... everything.\"" + Style.RESET_ALL)
                time.sleep(2)
                print()
                input(Fore.LIGHTBLACK_EX + "Press Enter to continue..." + Style.RESET_ALL)
                
            elif choice == '4':
                # Leave
                self.clear_screen()
                print(Fore.CYAN + holloway_art + Style.RESET_ALL)
                print()
                print(Fore.CYAN + "Dr. Holloway:" + Style.RESET_ALL)
                print(Fore.WHITE + "\"Stay safe down here. The deep doesn't forgive mistakes.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.CYAN + "\"And... thank you for listening. It's been so long since I could talk to someone.\"" + Style.RESET_ALL)
                time.sleep(1.5)
                print()
                input(Fore.LIGHTBLACK_EX + "Press Enter to continue..." + Style.RESET_ALL)
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
            
            # Karma-based greeting
            if random.random() < 0.3:
                if self.karma >= 50:
                    greetings = [
                        "Ahoy there, hero of the seas! Your kindness is legendary!",
                        "The guardian spirits speak well of you, friend!",
                        "Ah, the protector returns! The waters are blessed by your presence!",
                        "Welcome, champion! The guardians celebrate your mercy!",
                        "The ancient ones smile upon you, noble fisher!",
                    ]
                    print(Fore.GREEN + random.choice(greetings) + Style.RESET_ALL)
                elif self.karma >= 10:
                    greetings = [
                        "Ahoy there, young angler!",
                        "Greetings, friend! Beautiful day for fishing, eh?",
                        "Ah, a fellow fisher! Come, sit a spell.",
                        "Welcome to my humble fishing spot.",
                        "The water speaks to those patient enough to listen.",
                    ]
                    print(Fore.CYAN + random.choice(greetings) + Style.RESET_ALL)
                elif self.karma >= -10:
                    greetings = [
                        "Well, well… another fisher visits my spot.",
                        "Oh. It's you again.",
                        "Back already?",
                        "Hmm. Hello.",
                    ]
                    print(Fore.WHITE + random.choice(greetings) + Style.RESET_ALL)
                elif self.karma >= -50:
                    greetings = [
                        "*The old man eyes you warily* ...What do you want?",
                        "I heard what you did. The guardians won't forget.",
                        "*Doesn't look up from his fishing* ...You again.",
                        "Word travels fast on these waters. Your deeds have been noted.",
                    ]
                    print(Fore.YELLOW + random.choice(greetings) + Style.RESET_ALL)
                else:
                    greetings = [
                        "*The old man's face hardens* Slayer. What brings you here?",
                        "The water recoils from your presence... and so do I.",
                        "*Spits* Executioner. Your hands are stained with ancient blood.",
                        "The guardians cry out in their graves. What more do you want?",
                        "*Looks away in disgust* Monster hunter. I have nothing to say to you.",
                    ]
                    print(Fore.RED + random.choice(greetings) + Style.RESET_ALL)
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
                # Leave - karma-based farewell
                self.clear_screen()
                print(Fore.CYAN + fisherman_art + Style.RESET_ALL)
                print()
                print(Fore.GREEN + "Old Fisherman:" + Style.RESET_ALL)
                
                if self.karma >= 50:
                    farewell = [
                        "\"May the ancient spirits guide your path, hero. You honor us all.\"",
                        "\"The guardians are in your debt. Safe travels, protector.\"",
                        "\"Tight lines, champion. The waters sing of your compassion.\"",
                        "\"Go with the blessings of the deep. You've earned them.\"",
                    ]
                    print(Fore.GREEN + random.choice(farewell) + Style.RESET_ALL)
                elif self.karma >= 10:
                    farewell = [
                        "\"Tight lines, friend. May the waters be kind to you.\"",
                        "\"Be safe out there. The guardians remember kindness.\"",
                        "\"Come back anytime. These old bones enjoy the company.\"",
                        "\"Fish well, and respect the waters. They're watching.\"",
                    ]
                    print(Fore.CYAN + random.choice(farewell) + Style.RESET_ALL)
                elif self.karma >= -10:
                    farewell = [
                        "\"...Be careful out there.\"",
                        "\"The waters are watching. Always watching.\"",
                        "\"*Nods curtly* Safe travels.\"",
                    ]
                    print(Fore.WHITE + random.choice(farewell) + Style.RESET_ALL)
                elif self.karma >= -50:
                    farewell = [
                        "\"The guardians don't forget. Think on that.\"",
                        "\"*Turns back to fishing without another word*\"",
                        "\"Every action has consequences, fisher. Remember that.\"",
                    ]
                    print(Fore.YELLOW + random.choice(farewell) + Style.RESET_ALL)
                else:
                    farewell = [
                        "\"*Doesn't look at you* Just... go.\"",
                        "\"The blood on your hands won't wash off. Ever.\"",
                        "\"*Whispers* May the drowned ones haunt your dreams...\"",
                        "\"*Cold silence*\"",
                    ]
                    print(Fore.RED + random.choice(farewell) + Style.RESET_ALL)
                
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
        
        # Play hub island music
        play_music("hub_island")
        
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
                    line += hub_map.render_tile(tile, is_player, is_spot, is_golden, self)
                print(line)
            
            print()
            print(Fore.GREEN + f"Level: {self.level} | XP: {self.xp}/{self.xp_threshold} | Money: ${self.money}" + Style.RESET_ALL)
            print(Fore.LIGHTBLACK_EX + f"Rod: {self.rod_durability}/{self.rod_max_durability} | Weather: {self.current_weather}" + Style.RESET_ALL)
            print()
            print(Fore.YELLOW + hub_map.message + Style.RESET_ALL)
            print()
            if "Loch Ness Monster" in self.defeated_bosses:
                print(Fore.WHITE + "🏪 Shop | 🏛️ Aquarium | 📋 Quests | 🏠 Home | ⚓ Dock | 🎣 NPC | 🧓 MacTavish | ⊙ Fish Spot | ◉ Golden Spot" + Style.RESET_ALL)
            else:
                print(Fore.WHITE + "🏪 Shop | 🏛️ Aquarium | 📋 Quests | 🏠 Home | ⚓ Dock | 🎣 NPC | ⊙ Fish Spot | ◉ Golden Spot" + Style.RESET_ALL)
            if self.debug_mode:
                    print(Fore.MAGENTA + "[DEV] [M]ain Menu | [B]oss Spawner | [WASD] Move | [E] Interact | [I] Inventory | [C] Stats | [Q] Quit" + Style.RESET_ALL)
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
                elif hub_map.is_npc_mactavish(hub_map.player_x, hub_map.player_y):
                    # Talk to MacTavish (only if Loch Ness defeated)
                    if "Loch Ness Monster" in self.defeated_bosses:
                        self.interact_with_groundskeeper_mactavish()
                    else:
                        hub_map.message = "The water seems calm here..."
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
            elif key == 'm' and self.debug_mode:
                self.dev_menu()
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
                    line += location_map.render_tile(tile, is_player, is_spot, is_golden, self)
                print(line)
            
            print()
            print(Fore.GREEN + f"Level: {self.level} | XP: {self.xp}/{self.xp_threshold} | Money: ${self.money}" + Style.RESET_ALL)
            print(Fore.LIGHTBLACK_EX + f"Rod: {self.rod_durability}/{self.rod_max_durability} | Weather: {self.current_weather}" + Style.RESET_ALL)
            print()
            print(Fore.YELLOW + location_map.message + Style.RESET_ALL)
            print()
            # Show NPC hint for Deep Sea if Cthulhu defeated
            if location.name == "Deep Sea" and "Cthulhu" in self.defeated_bosses:
                print(Fore.CYAN + "🔬 Dr. Holloway's Research Station | ⊙ Fish Spot | ◉ Golden Spot" + Style.RESET_ALL)
            if self.debug_mode:
                print(Fore.MAGENTA + "[DEV] [M]ain Menu | [B]oss Spawner | [WASD] Move | [E] Fish | [Q] Return to Hub" + Style.RESET_ALL)
            else:
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
                # Check for NPC first
                if location_map.is_npc_holloway(location_map.player_x, location_map.player_y):
                    # Talk to Dr. Holloway (only if Cthulhu defeated)
                    if "Cthulhu" in self.defeated_bosses:
                        self.interact_with_dr_holloway()
                    else:
                        location_map.message = "The dark waters seem still here..."
                elif location_map.is_fishing_spot(location_map.player_x, location_map.player_y):
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
            elif key == 'm' and self.debug_mode:
                self.dev_menu()
            elif key == 'b' and self.debug_mode:
                self.dev_boss_menu()
            elif key == 'q':
                # Return to previous location
                self.current_location = old_location
                break

    def start_boss_fight(self, boss):
        """Undertale-style boss fight system"""
        self.clear_screen()
        
        # Play boss-specific music
        boss_music_map = {
            "Loch Ness Monster": "boss_nessie",
            "The River Guardian": "boss_river_guardian",
            "The Crimson Tide": "boss_pirates",
            "The Kraken": "boss_kraken"
        }
        
        track = boss_music_map.get(boss.name, "boss_generic")
        play_music(track)
        
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
                    
                    # Special message for Cthulhu
                    if boss.name == "Cthulhu":
                        print()
                        print(Fore.MAGENTA + "=" * 60 + Style.RESET_ALL)
                        print(Fore.LIGHTMAGENTA_EX + "🐙 THE FRAGMENT OF R'LYEH PULSES WITH POWER! 🐙" + Style.RESET_ALL)
                        print(Fore.CYAN + "Your perception has been forever altered..." + Style.RESET_ALL)
                        print(Fore.GREEN + "You can now catch ELDRITCH and COSMIC fish variants!" + Style.RESET_ALL)
                        print(Fore.YELLOW + "Strange creatures from beyond the stars now swim in the Deep Sea..." + Style.RESET_ALL)
                        print(Fore.MAGENTA + "=" * 60 + Style.RESET_ALL)
                    
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
                
                # Special message for Cthulhu
                if boss.name == "Cthulhu":
                    print()
                    print(Fore.MAGENTA + "=" * 60 + Style.RESET_ALL)
                    print(Fore.RED + "🐙 THE DREAMING GOD'S INFLUENCE LINGERS! 🐙" + Style.RESET_ALL)
                    print(Fore.LIGHTBLACK_EX + "Though banished, Cthulhu's presence has tainted the waters..." + Style.RESET_ALL)
                    print(Fore.GREEN + "You can now catch ELDRITCH and COSMIC fish variants!" + Style.RESET_ALL)
                    print(Fore.YELLOW + "Things that should not be now swim in the Deep Sea..." + Style.RESET_ALL)
                    print(Fore.LIGHTBLACK_EX + "*You hear whispers in your dreams...*" + Style.RESET_ALL)
                    print(Fore.MAGENTA + "=" * 60 + Style.RESET_ALL)
                
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
                # Check for god mode
                if hasattr(self, 'god_mode') and self.god_mode:
                    print()
                    print(Fore.MAGENTA + "⚡ [GOD MODE] - No damage taken! ⚡" + Style.RESET_ALL)
                    time.sleep(1)
                else:
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
                
                # Start boss fight FIRST, then remove item only if boss is defeated
                self.start_boss_fight(boss_item.boss)
                
                # Only remove the item if the boss was actually defeated/spared
                if boss_item.boss.name in self.defeated_bosses:
                    self.boss_inventory.pop(index)
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
        print(Fore.CYAN + "5. Jormungandr (Deep sea)" + Style.RESET_ALL)
        print(Fore.CYAN + "6. [MORE COMMING SOON]" + Style.RESET_ALL)
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
        elif choice == '5':
            self.start_boss_fight(JORMUNGANDR)
    
    def dev_menu(self):
        """DEV MODE: Comprehensive testing and stat editing menu"""
        while True:
            self.clear_screen()
            print(Fore.MAGENTA + "╔════════════════════════════════════════════════╗" + Style.RESET_ALL)
            print(Fore.MAGENTA + "║         🔧 DEVELOPER MENU 🔧                   ║" + Style.RESET_ALL)
            print(Fore.MAGENTA + "╚════════════════════════════════════════════════╝" + Style.RESET_ALL)
            print()
            print(Fore.YELLOW + f"Current Stats:" + Style.RESET_ALL)
            print(Fore.WHITE + f"  Level: {self.level} | XP: {self.xp}/{self.xp_threshold}" + Style.RESET_ALL)
            print(Fore.WHITE + f"  Money: ${self.money} | Karma: {self.karma}" + Style.RESET_ALL)
            print(Fore.WHITE + f"  HP: {self.current_hp}/{self.max_hp}" + Style.RESET_ALL)
            print(Fore.WHITE + f"  Skill Points: {self.skill_points}" + Style.RESET_ALL)
            print(Fore.CYAN + f"  Defeated Bosses: {len(self.defeated_bosses)}/4" + Style.RESET_ALL)
            if self.defeated_bosses:
                print(Fore.LIGHTBLACK_EX + f"    {', '.join(self.defeated_bosses)}" + Style.RESET_ALL)
            god_mode_status = "ON" if hasattr(self, 'god_mode') and self.god_mode else "OFF"
            print(Fore.MAGENTA + f"  God Mode: {god_mode_status}" + Style.RESET_ALL)
            print()
            print(Fore.CYAN + "═══ Player Stats ═══" + Style.RESET_ALL)
            print(Fore.GREEN + "1. Edit Money" + Style.RESET_ALL)
            print(Fore.GREEN + "2. Edit Level & XP" + Style.RESET_ALL)
            print(Fore.GREEN + "3. Edit Karma" + Style.RESET_ALL)
            print(Fore.GREEN + "4. Edit HP/Max HP" + Style.RESET_ALL)
            print(Fore.GREEN + "5. Edit Skill Points" + Style.RESET_ALL)
            print(Fore.GREEN + "6. Edit Character Stats (STR/LUCK/PAT)" + Style.RESET_ALL)
            print()
            print(Fore.CYAN + "═══ Inventory & Items ═══" + Style.RESET_ALL)
            print(Fore.GREEN + "7. Unlock All Rods & Baits" + Style.RESET_ALL)
            print(Fore.GREEN + "8. Unlock All Combat Items" + Style.RESET_ALL)
            print(Fore.GREEN + "9. Add Specific Fish to Inventory" + Style.RESET_ALL)
            print(Fore.GREEN + "10. Clear Inventory" + Style.RESET_ALL)
            print(Fore.GREEN + "11. Add All Boss Items" + Style.RESET_ALL)
            print()
            print(Fore.CYAN + "═══ Progression & World ═══" + Style.RESET_ALL)
            print(Fore.GREEN + "12. Unlock All Locations (+ Karma)" + Style.RESET_ALL)
            print(Fore.GREEN + "13. Reset Defeated Bosses" + Style.RESET_ALL)
            print(Fore.GREEN + "14. Mark All Bosses as Defeated (+ Karma)" + Style.RESET_ALL)
            print(Fore.GREEN + "15. Complete All Encyclopedia Entries" + Style.RESET_ALL)
            print(Fore.GREEN + "16. Reset Encyclopedia" + Style.RESET_ALL)
            print()
            print(Fore.CYAN + "═══ Testing Tools ═══" + Style.RESET_ALL)
            print(Fore.GREEN + "17. Spawn Boss (Boss Menu)" + Style.RESET_ALL)
            print(Fore.GREEN + "18. Test Fishing (Instant Catch)" + Style.RESET_ALL)
            print(Fore.GREEN + "19. Set Rod Durability" + Style.RESET_ALL)
            print(Fore.GREEN + "20. Toggle God Mode (Infinite HP)" + Style.RESET_ALL)
            print()
            print(Fore.WHITE + "0. Exit Dev Menu" + Style.RESET_ALL)
            print()
            
            choice = input(Fore.MAGENTA + "Select option: " + Style.RESET_ALL)
            
            if choice == '1':
                self.dev_edit_money()
            elif choice == '2':
                self.dev_edit_level_xp()
            elif choice == '3':
                self.dev_edit_karma()
            elif choice == '4':
                self.dev_edit_hp()
            elif choice == '5':
                self.dev_edit_skill_points()
            elif choice == '6':
                self.dev_edit_character_stats()
            elif choice == '7':
                self.dev_unlock_rods_baits()
            elif choice == '8':
                self.dev_unlock_combat_items()
            elif choice == '9':
                self.dev_add_fish()
            elif choice == '10':
                self.dev_clear_inventory()
            elif choice == '11':
                self.dev_add_boss_items()
            elif choice == '12':
                self.dev_unlock_locations()
            elif choice == '13':
                self.dev_reset_bosses()
            elif choice == '14':
                self.dev_mark_all_bosses()
            elif choice == '15':
                self.dev_complete_encyclopedia()
            elif choice == '16':
                self.dev_reset_encyclopedia()
            elif choice == '17':
                self.dev_boss_menu()
            elif choice == '18':
                self.dev_test_fishing()
            elif choice == '19':
                self.dev_set_durability()
            elif choice == '20':
                self.dev_toggle_god_mode()
            elif choice == '0':
                break
            else:
                print(Fore.RED + "Invalid choice!" + Style.RESET_ALL)
                time.sleep(1)
    
    def dev_edit_money(self):
        """Edit money amount"""
        print(Fore.YELLOW + f"\nCurrent Money: ${self.money}" + Style.RESET_ALL)
        try:
            amount = int(input(Fore.GREEN + "New amount: $" + Style.RESET_ALL))
            self.money = max(0, amount)
            print(Fore.GREEN + f"✓ Money set to ${self.money}" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid input!" + Style.RESET_ALL)
        time.sleep(1)
    
    def dev_edit_level_xp(self):
        """Edit level and XP"""
        print(Fore.YELLOW + f"\nCurrent Level: {self.level} | XP: {self.xp}/{self.xp_threshold}" + Style.RESET_ALL)
        try:
            new_level = int(input(Fore.GREEN + "New level: " + Style.RESET_ALL))
            self.level = max(1, new_level)
            self.xp_threshold = 100 + (self.level - 1) * 50
            self.xp = 0
            print(Fore.GREEN + f"✓ Level set to {self.level}" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid input!" + Style.RESET_ALL)
        time.sleep(1)
    
    def dev_edit_karma(self):
        """Edit karma"""
        print(Fore.YELLOW + f"\nCurrent Karma: {self.karma}" + Style.RESET_ALL)
        print(Fore.WHITE + "Karma ranges: <-50 (Villain), -50 to -10 (Bad), -10 to 10 (Neutral), 10 to 50 (Good), >50 (Hero)" + Style.RESET_ALL)
        try:
            new_karma = int(input(Fore.GREEN + "New karma: " + Style.RESET_ALL))
            self.karma = new_karma
            print(Fore.GREEN + f"✓ Karma set to {self.karma}" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid input!" + Style.RESET_ALL)
        time.sleep(1)
    
    def dev_edit_hp(self):
        """Edit HP and Max HP"""
        print(Fore.YELLOW + f"\nCurrent HP: {self.current_hp}/{self.max_hp}" + Style.RESET_ALL)
        try:
            new_max_hp = int(input(Fore.GREEN + "New Max HP: " + Style.RESET_ALL))
            self.max_hp = max(1, new_max_hp)
            self.current_hp = self.max_hp
            print(Fore.GREEN + f"✓ HP set to {self.current_hp}/{self.max_hp}" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid input!" + Style.RESET_ALL)
        time.sleep(1)
    
    def dev_edit_skill_points(self):
        """Edit skill points"""
        print(Fore.YELLOW + f"\nCurrent Skill Points: {self.skill_points}" + Style.RESET_ALL)
        try:
            new_sp = int(input(Fore.GREEN + "New skill points: " + Style.RESET_ALL))
            self.skill_points = max(0, new_sp)
            print(Fore.GREEN + f"✓ Skill points set to {self.skill_points}" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid input!" + Style.RESET_ALL)
        time.sleep(1)
    
    def dev_edit_character_stats(self):
        """Edit character stats (Strength, Luck, Patience)"""
        print(Fore.YELLOW + f"\nCurrent Stats:" + Style.RESET_ALL)
        print(Fore.WHITE + f"  Strength: {self.stats['strength']}" + Style.RESET_ALL)
        print(Fore.WHITE + f"  Luck: {self.stats['luck']}" + Style.RESET_ALL)
        print(Fore.WHITE + f"  Patience: {self.stats['patience']}" + Style.RESET_ALL)
        print()
        try:
            str_val = int(input(Fore.GREEN + "New Strength: " + Style.RESET_ALL))
            luck_val = int(input(Fore.GREEN + "New Luck: " + Style.RESET_ALL))
            pat_val = int(input(Fore.GREEN + "New Patience: " + Style.RESET_ALL))
            
            self.stats['strength'] = max(0, str_val)
            self.stats['luck'] = max(0, luck_val)
            self.stats['patience'] = max(0, pat_val)
            
            print(Fore.GREEN + f"✓ Stats updated!" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid input!" + Style.RESET_ALL)
        time.sleep(1)
    
    def dev_unlock_rods_baits(self):
        """Unlock all rods and baits"""
        self.owned_rods = RODS[:]
        self.owned_baits = BAITS[:]
        self.current_rod = RODS[-1]
        self.current_bait = BAITS[-1]
        print(Fore.GREEN + "✓ All rods and baits unlocked!" + Style.RESET_ALL)
        time.sleep(1)
    
    def dev_unlock_combat_items(self):
        """Unlock all combat items"""
        self.owned_combat_items = {
            'attack': COMBAT_ITEMS_ATTACK[:],
            'defense': COMBAT_ITEMS_DEFENSE[:],
            'hp': COMBAT_ITEMS_HP[:]
        }
        self.equipped_combat_items = {
            'attack': COMBAT_ITEMS_ATTACK[-1] if COMBAT_ITEMS_ATTACK else None,
            'defense': COMBAT_ITEMS_DEFENSE[-1] if COMBAT_ITEMS_DEFENSE else None,
            'hp': COMBAT_ITEMS_HP[-1] if COMBAT_ITEMS_HP else None
        }
        print(Fore.GREEN + "✓ All combat items unlocked!" + Style.RESET_ALL)
        time.sleep(1)
    
    def dev_add_fish(self):
        """Add specific fish to inventory"""
        print(Fore.YELLOW + "\nSelect fish rarity to add:" + Style.RESET_ALL)
        print(Fore.WHITE + "1. Common" + Style.RESET_ALL)
        print(Fore.GREEN + "2. Uncommon" + Style.RESET_ALL)
        print(Fore.BLUE + "3. Rare" + Style.RESET_ALL)
        print(Fore.MAGENTA + "4. Epic" + Style.RESET_ALL)
        print(Fore.YELLOW + "5. Legendary" + Style.RESET_ALL)
        print(Fore.RED + "6. Mythical" + Style.RESET_ALL)
        
        choice = input(Fore.GREEN + "Choice: " + Style.RESET_ALL)
        
        rarity_map = {
            '1': 'common',
            '2': 'uncommon',
            '3': 'rare',
            '4': 'epic',
            '5': 'legendary',
            '6': 'mythical'
        }
        
        if choice in rarity_map:
            rarity = rarity_map[choice]
            # Create a sample fish
            fish_name = random.choice(UNIQUE_FISH_NAMES)
            fish = Fish(
                name=fish_name,
                weight=random.uniform(1, 50),
                rarity=rarity,
                mutation=None,
                xp_value=10
            )
            self.inventory.append(fish)
            print(Fore.GREEN + f"✓ Added {rarity} {fish_name} to inventory!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid choice!" + Style.RESET_ALL)
        time.sleep(1)
    
    def dev_clear_inventory(self):
        """Clear fish inventory"""
        confirm = input(Fore.RED + "Clear inventory? (Y/N): " + Style.RESET_ALL).lower()
        if confirm == 'y':
            self.inventory = []
            print(Fore.GREEN + "✓ Inventory cleared!" + Style.RESET_ALL)
        time.sleep(1)
    
    def dev_add_boss_items(self):
        """Add all boss items"""
        self.boss_inventory = list(BOSS_ITEMS.values())
        print(Fore.GREEN + "✓ All boss items added!" + Style.RESET_ALL)
        time.sleep(1)
    
    def dev_unlock_locations(self):
        """Unlock all locations by marking bosses as defeated"""
        # Use the exact boss names from the Boss objects
        self.defeated_bosses = ["Loch Ness Monster", "The River Guardian", "The Crimson Tide", "The Kraken", "Jörmungandr", "Cthulhu"]
        # Ensure positive karma for Captain Redbeard
        if self.karma < 1:
            self.karma = 10
            print(Fore.YELLOW + "✓ Karma set to 10 (required for Captain Redbeard at docks)" + Style.RESET_ALL)
        print(Fore.GREEN + "✓ All locations unlocked!" + Style.RESET_ALL)
        print(Fore.CYAN + f"  Defeated bosses: {', '.join(self.defeated_bosses)}" + Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + "  Tip: Visit the dock to talk to Captain Redbeard!" + Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + "  Tip: Visit Deep Sea to talk to Dr. Holloway!" + Style.RESET_ALL)
        time.sleep(2)
    
    def dev_reset_bosses(self):
        """Reset defeated bosses"""
        confirm = input(Fore.RED + "Reset all defeated bosses? (Y/N): " + Style.RESET_ALL).lower()
        if confirm == 'y':
            self.defeated_bosses = []
            print(Fore.GREEN + "✓ Defeated bosses reset!" + Style.RESET_ALL)
        time.sleep(1)
    
    def dev_mark_all_bosses(self):
        """Mark all bosses as defeated"""
        # Use the exact boss names from the Boss objects
        self.defeated_bosses = ["Loch Ness Monster", "The River Guardian", "The Crimson Tide", "The Kraken", "Jörmungandr", "Cthulhu"]
        # Also ensure positive karma so Captain Redbeard appears
        if self.karma < 1:
            self.karma = 10
            print(Fore.YELLOW + "✓ Karma set to 10 (required for Captain Redbeard at docks)" + Style.RESET_ALL)
        print(Fore.GREEN + "✓ All bosses marked as defeated!" + Style.RESET_ALL)
        print(Fore.CYAN + f"  Defeated bosses: {', '.join(self.defeated_bosses)}" + Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + "  Tip: Visit the dock to talk to Captain Redbeard!" + Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + "  Tip: Visit Deep Sea to talk to Dr. Holloway!" + Style.RESET_ALL)
        time.sleep(2)
    
    def dev_complete_encyclopedia(self):
        """Complete encyclopedia"""
        for fish_name in UNIQUE_FISH_NAMES:
            if fish_name not in self.encyclopedia:
                self.encyclopedia[fish_name] = {
                    'caught': 1,
                    'max_weight': random.uniform(1, 50)
                }
        print(Fore.GREEN + f"✓ Encyclopedia completed! ({len(self.encyclopedia)}/{len(UNIQUE_FISH_NAMES)} species)" + Style.RESET_ALL)
        time.sleep(1)
    
    def dev_reset_encyclopedia(self):
        """Reset encyclopedia"""
        confirm = input(Fore.RED + "Reset encyclopedia? (Y/N): " + Style.RESET_ALL).lower()
        if confirm == 'y':
            self.encyclopedia = {}
            print(Fore.GREEN + "✓ Encyclopedia reset!" + Style.RESET_ALL)
        time.sleep(1)
    
    def dev_test_fishing(self):
        """Instant fishing test"""
        print(Fore.YELLOW + "\nInstant fishing test..." + Style.RESET_ALL)
        # Simulate a quick catch
        fish = self.generate_fish()
        self.inventory.append(fish)
        self.update_encyclopedia(fish)
        print(Fore.GREEN + f"✓ Caught {fish.get_display_name()}!" + Style.RESET_ALL)
        print(Fore.WHITE + f"  Weight: {fish.weight:.2f} lbs | Rarity: {fish.rarity}" + Style.RESET_ALL)
        time.sleep(2)
    
    def dev_set_durability(self):
        """Set rod durability"""
        print(Fore.YELLOW + f"\nCurrent Durability: {self.rod_durability}/{self.rod_max_durability}" + Style.RESET_ALL)
        try:
            new_dur = int(input(Fore.GREEN + "New durability: " + Style.RESET_ALL))
            self.rod_durability = max(0, min(new_dur, self.rod_max_durability))
            print(Fore.GREEN + f"✓ Durability set to {self.rod_durability}" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid input!" + Style.RESET_ALL)
        time.sleep(1)
    
    def dev_toggle_god_mode(self):
        """Toggle god mode (infinite HP)"""
        if not hasattr(self, 'god_mode'):
            self.god_mode = False
        
        self.god_mode = not self.god_mode
        
        if self.god_mode:
            print(Fore.GREEN + "✓ GOD MODE ENABLED - You cannot take damage!" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "✓ God mode disabled" + Style.RESET_ALL)
        time.sleep(1)



# ===== MAIN =====
if __name__ == "__main__":
    show_intro()
    
    # Play menu music
    play_music("menu")
    
    print(Fore.CYAN + "╔═══════════════════════════════════════╗" + Style.RESET_ALL)
    print(Fore.CYAN + "║       🎣 FISHING GAME 🎣              ║" + Style.RESET_ALL)
    print(Fore.CYAN + "║       BOSS BATTLES UPDATE             ║" + Style.RESET_ALL)
    print(Fore.CYAN + "║         V.0.7.1 BETA                  ║" + Style.RESET_ALL)
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
        print(Fore.LIGHTMAGENTA_EX + "╔════════════════════════════════════════════╗" + Style.RESET_ALL)
        print(Fore.LIGHTMAGENTA_EX + "║          DEV MODE ACTIVATED! 🔧            ║" + Style.RESET_ALL)
        print(Fore.LIGHTMAGENTA_EX + "╚════════════════════════════════════════════╝" + Style.RESET_ALL)
        print(Fore.GREEN + "All rods, baits, locations and bosses unlocked!" + Style.RESET_ALL)
        print(Fore.CYAN + "Press [M] in-game for the full Developer Menu!" + Style.RESET_ALL)
        print(Fore.CYAN + "Press [B] to quickly spawn bosses!" + Style.RESET_ALL)
        time.sleep(2)
        game.start_game()

    else:
        print(Fore.RED + "Invalid choice." + Style.RESET_ALL)