# 🎣 FISHING GAME

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Version](https://img.shields.io/badge/version-1.0.0%20FULL%20RELEASE-orange.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)
![Code Size](https://img.shields.io/badge/code%20size-~690KB-informational.svg)
![Fish Species](https://img.shields.io/badge/fish%20species-150+-success.svg)
![Locations](https://img.shields.io/badge/locations-6-blueviolet.svg)
![Boss Battles](https://img.shields.io/badge/boss%20battles-10-red.svg)
![Status](https://img.shields.io/badge/status-full%20release-brightgreen.svg)
![Game Type](https://img.shields.io/badge/type-RPG%20%2F%20Story%20Rich-ff69b4.svg)
![Terminal](https://img.shields.io/badge/interface-terminal%20Unicode-black.svg)
![Dependencies](https://img.shields.io/badge/dependencies-colorama-red.svg)
![Save System](https://img.shields.io/badge/save%20system-JSON-blue.svg)
![Updates](https://img.shields.io/badge/updates-active-success.svg)
![Made With](https://img.shields.io/badge/made%20with-%E2%9D%A4%EF%B8%8F-red.svg)
![Music System](https://img.shields.io/badge/music-dynamic%20soundtrack-purple.svg)
![Endings](https://img.shields.io/badge/endings-3%20unique-yellow.svg)



```
╔══════════════════════════════════════════════════════════════╗
║                  🌊 FISHING GAME 🌊                         ║
║                                                              ║
║              A Terminal-Based Fishing RPG Adventure          ║
║                   Where Every Choice Ripples                 ║
╚══════════════════════════════════════════════════════════════╝
```

*Not everyone who casts a line is a Fisher.*

</div>

---

## 📖 Table of Contents

- [About](#-about)
- [Key Features](#-key-features)
- [Installation](#-installation)
- [How to Play](#-how-to-play)
- [Game Systems](#-game-systems)
- [New Game+](#-new-game)
- [Credits](#-credits)
- [License](#-license)

---

## 🌊 About

**Fishing game** is a narrative-driven terminal RPG combining fishing mechanics with boss battles and moral choices. Set on the mysterious Hub Island, embark on a journey to discover ancient Guardians and your destiny as a Fisher.

Every Guardian can be fought or spared. Every choice matters.

### Key Features

- 🎭 **Story-Driven**: Mythology, environmentalism, and cosmic horror themes
- 🐉 **10 Boss Battles**: Ancient Guardians from world mythology
- 🎣 **150+ Fish Species**: Complete your encyclopedia
- 🌍 **10 Locations**: Explore diverse environments
- ⚔️ **Morality System**: Your choices determine the ending
- 🎵 **Dynamic Music**: Cross-platform soundtrack (optional)
- 💾 **Save System**: Save anywhere, New Game+ mode
- 🎨 **Terminal Art**: Colorful ASCII art and Unicode UI

---

## 🎮 Installation

### Requirements
- **Python 3.7 or higher**
- **colorama** library (for colored terminal output)
- Terminal with Unicode support (most modern terminals)
- Approximately 1 MB of disk space

### Quick Start

1. **Clone or download the game**
   ```bash
   git clone https://github.com/yourusername/fishing-game.git
   cd fishing-game
   ```

2. **Install dependencies**
   ```bash
   pip install colorama
   ```

3. **Run the game**
   ```bash
   python fishgame.py
   ```

### Optional: Music Setup (music is not done yet, but do this when it is)

The game includes a music system! To enable:

**Windows:**
- Place `.wav` files in a `music/` folder next to `fishgame.py`
- The game uses Windows Media Player to play tracks

**macOS:**
- Place `.wav` files in a `music/` folder
- The game uses `afplay` (built into macOS)

**Linux:**
- Install `mpg123`: `sudo apt-get install mpg123`
- Place `.wav` files in a `music/` folder

Music files should be named:
- `menu.wav` - Main menu theme
- `hub_island.wav` - Hub Island theme
- `river.wav`, `lake.wav`, etc. - Location themes
- `boss_battle.wav` - Boss encounter theme
- `ending_good.wav`, `ending_bad.wav`, etc. - Ending themes

**Note**: Music is optional. The game will play perfectly without it!

---

## 🎯 How to Play

### Getting Started

1. Choose **New Game** or **Load Game**
2. Create your character (name, difficulty, allocate stats)
3. Begin your journey on Hub Island

### Controls

```
[F] - Fish          [M] - Map/Travel    [I] - Inventory
[S] - Shop          [E] - Encyclopedia  [T] - Talk
[Q] - Quick Save    [L] - Load          [X] - Exit
```

### Basic Gameplay Loop

1. **Fish** at locations to catch species and earn money
2. **Upgrade** your rod and bait at the shop
3. **Explore** new locations as you progress
4. **Battle** Guardians - choose to defeat or spare them
5. **Complete** your encyclopedia and discover the story

---

## ⚙️ Game Systems

### Character Stats

- **Strength** 💪 - Catch success rate, combat damage
- **Luck** 🍀 - Rare fish chance, critical hits
- **Patience** ⏳ - Bite frequency, stamina regeneration

### Equipment

**Rods**: 12 types from Basic Rod to Poseidon's Trident  
**Bait**: 15 varieties, each attracts different fish  
**Boss Items**: Powerful artifacts from Guardian encounters

### Progression

- Level up through fishing and combat
- Unlock new locations by progressing the story
- Complete your encyclopedia with 150+ fish species
- Karma system tracks your choices

---

## 🔄 New Game+

After completing any ending, start **New Game+** with:

**Carries Over**: Encyclopedia, 50% money, character stats  
**Resets**: Bosses, inventory, locations, story  
**Increased Difficulty**: Boss HP +50%, damage +25%, harder catches, higher prices

---

## 👥 Credits

### Development
- **Noko** - Lead Developer, Story Writer, Game Design

### Linux Support
- **Beff** - Linux Port & Cross-Platform Testing

### Story & Lore
- **Noko** - Original narrative, worldbuilding, Guardian lore

### Art & ASCII
- **[ASCII Art](https://www.asciiart.eu/)** - Community ASCII art resources
- **Noko** - Custom terminal art and UI design

### Music & Sound
- **Ismagmais** - Original soundtrack composition
- **Noko** - Additional tracks and audio implementation

### Technology
- **Python** - Programming language
- **colorama** - Terminal color support
- **JSON** - Save system storage

---



## 🐛 Support

**Found a bug?** Include your OS, Python version, error message, and steps to reproduce.

**Common Issues:**
- Music won't play? Check `music/` folder and required player installation
- Colors wrong? Try a different terminal or disable colors
- Unicode boxes? Update your terminal font

---



**🎣 Cast Your Line With Care 🎣**

*Made with ❤️ by Noko*

![Fish](https://img.shields.io/badge/🐟-Catch%20Them%20All-blue)
![Boss](https://img.shields.io/badge/⚔️-Face%20The%20Guardians-red)
![Story](https://img.shields.io/badge/📖-Discover%20Your%20Path-purple)

