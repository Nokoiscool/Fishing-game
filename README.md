# 🎣 Very Cool Fishing Game

A feature-rich terminal-based fishing RPG with beautiful Unicode graphics, exploration mechanics, and dynamic progression systems.

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Version](https://img.shields.io/badge/version-0.4.3-orange.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)
![Code Size](https://img.shields.io/badge/code%20size-~55KB-informational.svg)
![Fish Species](https://img.shields.io/badge/fish%20species-150+-success.svg)
![Locations](https://img.shields.io/badge/locations-7-blueviolet.svg)
![Achievements](https://img.shields.io/badge/achievements-33+-yellow.svg)
![Status](https://img.shields.io/badge/status-open%20beta-brightgreen.svg)
![Game Type](https://img.shields.io/badge/type-RPG%20%2F%20Exploration-ff69b4.svg)
![Terminal](https://img.shields.io/badge/interface-terminal%20Unicode-black.svg)
![Dependencies](https://img.shields.io/badge/dependencies-colorama-red.svg)
![Save System](https://img.shields.io/badge/save%20system-JSON-blue.svg)
![Updates](https://img.shields.io/badge/updates-active-success.svg)
![Made With](https://img.shields.io/badge/made%20with-%E2%9D%A4%EF%B8%8F-red.svg)

## 🌟 What's New in v0.4.3

### 🗺️ Overworld Exploration System
- **Zelda-style overworld map** with WASD navigation
- **Visual location discovery** - walk to locations and enter them with E
- **Level-based unlocking** - locked locations appear dimmed on the map
- **Beautiful Unicode graphics** - gorgeous symbols for water, trees, mountains, and more

### ✨ Dynamic Fishing Spots
- **Randomized spot generation** - every location visit has different fishing spot layouts
- **Golden Fishing Spots** - 10% chance for spots with 2.5x rare fish multiplier
- **Visual distinction** - Golden spots (◉) vs Regular spots (⊙)
- **Stay-on-tile fishing** - fish repeatedly without leaving the location

### 🎨 Enhanced Visuals
- **Unicode terrain** - ≈ water, ♠ forests, ♨ volcanoes, ⌬ space stations
- **Colorful maps** - distinct colors for each location type
- **Smooth borders** - elegant box-drawing characters (┏━┓)
- **Player character** - friendly ☻ instead of boring @

---

## 📋 Requirements

- **Python 3.7 or higher**
- **colorama library** - for terminal colors
- **Terminal with Unicode support** - for beautiful graphics
- **Windows, macOS, or Linux**

## 🚀 Quick Start

### Installation

1. **Install Python** (if not already installed)
   ```bash
   # Download from python.org
   # ✅ Check "Add Python to PATH" during installation
   ```

2. **Install colorama**
   ```bash
   pip install colorama
   ```

3. **Download and Run**
   ```bash
   # Download the game
   curl -O https://raw.githubusercontent.com/Nokoiscool/Fishing-game/main/fishgame.py
   
   # Run it!
   python fishgame.py
   ```

### First Launch

1. **Enjoy the animated intro** 🌈
2. **Choose "New Game"** and create your character:
   - Pick a cool fishing name
   - Distribute 10 stat points wisely
   - Select your difficulty
3. **Start exploring the overworld!**

---

## 🎮 How to Play

### Overworld Navigation

The game now features a **beautiful overworld map** where you explore to find fishing locations:

```
╔════════════════════════╗
║         Level 5 Angler             ║
╚════════════════════════╝

╔════════════════════════╗
║···♠♠♠··················║
║··♠♠♠♠♠·················║
║···♠♠♠··················║  ☻ You
║························║
║·≈≈≈≈·····≋≋≋≋··········║  ≈ Lake (Unlocked)
║≈≈≈≈≈≈···≋≋≋≋≋≋·········║  ≋ River (Unlocked)
║·≈≈≈≈·····≋≋≋≋··········║  ~ Ocean (Locked)
║························║  ♨ Volcanic (Locked)
║········~~~~~~~~~~······║  ⌬ Space (Locked)
║·······~~~~~~~~~~~~·····║
║······~~~~~~~~~~~~~~····║
║······~~~~~~~~~~~~~~·♨♨♨║
║·······~~~~~~~~~~~~·♨♨♨♨║
║········~~~~~~~~~~···♨♨♨║
╚════════════════════════╝

Locations:
  ≈ Freshwater Lake      ✓
  ≋ River                ✓
  ~ Deep Ocean           🔒 Lvl3
  ♨ Volcanic Waters      🔒 Lvl7
  ⌬ Space Station        🔒 Lvl12

[WASD] Move | [E] Enter Location | [Q] Exit
```

**Controls:**
- **W/A/S/D** - Move around the overworld
- **E** - Enter a location when standing on it
- **Q** - Return to main menu

### Inside Locations

Once you enter a location, explore to find fishing spots:

```
┏━━━━━━━━━━━━━━━━━━━━┓
║  Freshwater Lake     ║
┗━━━━━━━━━━━━━━━━━━━━┛
A peaceful lake surrounded by trees

┏━━━━━━━━━━━━━━━━━━━━┓
┃··········≈≈≈≈≈≈····┃
┃·······⊙·≈≈≈≈≈≈≈≈··◉┃  ◉ Golden Spot!
┃♣♣♣♣··⊙·≈≈≈≈≈≈≈≈≈≈··┃  ⊙ Regular Spot
┃♣♣♣♣····≈≈≈≈≈≈≈≈≈≈·⊙┃  ☻ You
┃······⊙·≈≈≈≈≈≈≈≈≈≈··┃  ≈ Lake Water
┃·········≈≈≈≈≈≈≈≈···┃  ♣ Trees
┃··········≈≈≈≈≈≈····┃
┗━━━━━━━━━━━━━━━━━━━━┛

⊙ Regular Spot | ◉ Golden Spot (Better loot!)
[WASD] Move | [E] Fish at spot | [Q] Return to overworld
```

**Location Controls:**
- **W/A/S/D** - Move around to find fishing spots
- **E** - Fish when standing on a spot (⊙ or ◉)
- **Q** - Return to overworld

### Fishing Mechanics

1. **Find a fishing spot** - look for ⊙ or ◉ symbols
2. **Stand on the spot** and press **E**
3. **Complete the mini-game** - quick reflexes!
4. **Catch the fish** - stays in your esky
5. **Fish again!** - Press E to cast again at the same spot

#### Golden Spots ✨
- **10% spawn chance** for any fishing spot
- **Bright golden color** - can't miss them!
- **2.5x rare fish multiplier** - Legendary & Mythical fish much more common
- **Special message** - "✨ Fishing at a GOLDEN SPOT! Better odds for rare fish! ✨"

### Progression Loop

```
Explore Overworld → Enter Location → Find Spots → Fish
       ↑                                            ↓
   Level Up  ← Gain XP ← Sell Fish ← Catch Fish ←
```

1. **Fish** to catch species and earn XP
2. **Level up** to unlock new locations
3. **Sell fish** to buy better equipment
4. **Upgrade skills** to improve your abilities
5. **Complete encyclopedia** to discover all species
6. **Hunt achievements** for bonus rewards

---

## 🌍 Locations & Unlocking

### Location Unlock Progression

| Level | Location | Symbol | Fish Rarity | Special Features |
|-------|----------|--------|-------------|------------------|
| **1** | Freshwater Lake | ≈ | Common-Rare | Starting zone, peaceful |
| **2** | River | ≋ | Common-Rare | Flowing water, Pike |
| **3** | Deep Ocean | ~ | Uncommon-Legendary | Sharks and big game |
| **5** | Deep Sea | 🌊 | Rare-Mythical | Deepest waters, Kraken |
| **7** | Volcanic Waters | ♨ | Rare-Legendary | Dangerous heat, unique species |
| **9** | Arctic | ❄️ | Rare-Mythical | Frozen waters, polar fish |
| **12** | Space Station | ⌬ | Legendary-Godly | Zero gravity, alien fish |

### Visual Lock System

Locked locations appear **dimmed/gray** on the overworld map. When you reach the required level, they light up in full color and become accessible!

**Walking onto a locked location:**
```
🔒 Volcanic Waters - Unlocks at level 7 (You: Lvl 3)
```

**Walking onto an unlocked location:**
```
📍 River - Press E to enter!
```

---

## 🎯 Core Gameplay Features

### Character Creation
- **Name your angler** - choose your fishing identity
- **Distribute 10 stat points:**
  - **Strength** - Increases catch rate (less fish escape)
  - **Luck** - Better chance for rare fish
  - **Patience** - Makes mini-games easier
- **Choose difficulty** - Easy, Normal, Hard, or Legendary

### RPG Progression
- **Level up** from catching fish and earning XP
- **Unlock locations** as you reach level thresholds
- **Skill tree** with 6 upgradeable skills (5 levels each)
- **Equipment shop** - 14 rods and 15 bait types
- **Dynamic weather** - 4 weather types affecting spawns
- **Day/Night cycle** - 4 times affecting rare fish

### Collection Systems
- **150+ fish species** from Common to Mythical
- **7 mutation types** including ultra-rare Magical (10x value!)
- **Encyclopedia** tracking with real-world fish facts
- **33+ achievements** with rewards
- **Trophy Room** to preserve special catches
- **Statistics tracking** for total catches, species, etc.

### Economic System
- **Sell fish** for money based on rarity and mutations
- **Buy equipment** - better rods = better success rates
- **Upgrade esky** capacity (starts at 50 fish)
- **Repair rods** when durability gets low
- **Quest rewards** for completing objectives

---

## 🐟 Fish & Rarity System

### Rarity Tiers

| Rarity | Spawn Weight | Value Range | Examples |
|--------|--------------|-------------|----------|
| **Common** | 70-80% | $10-50 | Trout, Cod, Perch, Sunfish |
| **Uncommon** | 15-20% | $50-150 | Bass, Tuna, Pike, Catfish |
| **Rare** | 5-8% | $100-400 | Sturgeon, Shark, Crystal Salmon |
| **Legendary** | 1-3% | $600-1,500 | Arapaima, Coelacanth, Phoenix Tuna |
| **Mythical** | <0.1% | $10,000-300,000 | Kraken, Leviathan, Dragon, Blobfish |
| **Godly** | <0.01% | $500,000+ | Ultra-rare endgame fish |

### Mutation System

Mutations dramatically increase fish value:

| Mutation | Spawn Chance | Value Multiplier | Color |
|----------|--------------|------------------|-------|
| Normal | 79.99% | 1x | White |
| Albino | 5% | 2x | Bright white |
| Glowing | 5% | 2.5x | Green |
| Spotted | 5% | 1.5x | Yellow |
| Golden | 3% | **5x** | Light yellow |
| Shadow | 2% | 3x | Dark gray |
| **Magical** | **0.01%** | **10x** | Magenta |

**Example:** A Legendary fish worth $1,000 with a Golden mutation = $5,000!

---

## 💰 Equipment & Upgrades

### Fishing Rods (14 Total)

| Rod Name | Cost | Catch Bonus | Notes |
|----------|------|-------------|-------|
| Bamboo Rod | Free | 60% | Starting rod |
| Basic Rod | $500 | 70% | First upgrade |
| Sturdy Rod | $1,500 | 80% | Reliable |
| Carbon Rod | $3,500 | 90% | Lightweight |
| Reinforced Rod | $6,500 | 95% | Durable |
| Legendary Rod | $10,000 | 98% | High performance |
| Mythic Rod | $20,000 | 102% | Mythical tech |
| Abyssal Rod | $35,000 | 105% | Deep sea specialist |
| Quantum Rod | $60,000 | 108% | Advanced physics |
| Godly Rod | $100,000 | 112% | Divine power |
| Blobfish Rod | $2,000,000 | **500%** | Ultra-rare special rod |

### Bait Types (15 Total)

Higher-tier bait significantly increases rare fish spawn rates:

| Bait | Cost | Rarity Boost |
|------|------|--------------|
| Worm | Free | 0% |
| Bread | $50 | +5% |
| Cricket | $120 | +8% |
| Corn | $180 | +10% |
| Minnow | $250 | +12% |
| Nightcrawler | $400 | +14% |
| Shrimp | $500 | +15% |
| Cut Bait | $650 | +16% |
| Squid | $800 | +18% |
| Artificial Lure | $1,200 | +22% |
| Live Bait | $1,500 | +25% |
| Special Lure | $2,500 | +30% |
| Premium Lure | $4,000 | +35% |
| Exotic Bait | $6,500 | +40% |
| **Master Bait** | **$50,000** | **+50%** |

### Rod Durability
- All rods start at **100% durability**
- Lose **1-3% per catch**
- **Warning at 20%** - time to repair!
- **Breaks at 0%** - reverts to Bamboo Rod
- **Repair cost:** $5 per 1% restored

---

## 🌳 Skill Tree System

Earn skill points by leveling up and completing achievements!

### Available Skills

| Skill | Max Level | Effect per Level | Total at Max | Cost |
|-------|-----------|------------------|--------------|------|
| **Rare Finder** | 5 | +2% rare spawn | +10% | 1 pt/lvl |
| **Quick Reflexes** | 5 | -5% mini-game difficulty | -25% | 1 pt/lvl |
| **Master Angler** | 5 | +5% catch rate | +25% | 1 pt/lvl |
| **Lucky Fisherman** | 5 | +10% mutation chance | +50% | 1 pt/lvl |
| **Bargain Hunter** | 3 | +10% sell price | +30% | 1 pt/lvl |
| **Iron Grip** | 3 | +15% XP gain | +45% | 1 pt/lvl |

### Earning Skill Points

- **1 point per level up** (natural progression)
- **2 points** - Magical Encounter achievement
- **3 points** - Leviathan Slayer achievement
- **3 points** - Quest Master achievement
- **5 points** - Billionaire achievement
- **10 points** - Encyclopedia Master achievement

### Recommended Build Order

**Early Game (Levels 1-5):**
1. Master Angler 1-2 (prevent escapes)
2. Quick Reflexes 1-2 (easier catches)

**Mid Game (Levels 6-10):**
3. Rare Finder 1-3 (better fish)
4. Master Angler 3-5 (max catch rate)
5. Iron Grip 1-2 (faster leveling)

**Late Game (Level 11+):**
6. Lucky Fisherman 1-5 (golden/magical mutations)
7. Bargain Hunter 1-3 (more profit)
8. Complete remaining skills

---

## 🏆 Achievements (33+ Total)

### Fishing Milestones
- ✅ **First Catch** - Catch your very first fish
- ✅ **First Rare** - Catch a rare-tier fish
- ✅ **First Legendary** - Catch a legendary fish
- ✅ **First Mythical** - Catch a mythical fish
- ✅ **Fisherman** - Catch 50 fish total
- ✅ **Master Fisherman** - Catch 200 fish
- ✅ **Legendary Angler** - Catch 1,000 fish
- ✅ **Speed Fisher** - Complete mini-game in under 3 seconds
- ✅ **Perfect Reflexes** - 10 perfect mini-game completions
- ✅ **Lucky Streak** - Catch 5 rare+ fish in a row

### Wealth Achievements
- ✅ **Millionaire** - Earn $1,000,000 total
- ✅ **Billionaire** - Earn $1,000,000,000 (+5 skill points!)

### Discovery Achievements
- ✅ **Encyclopedia 25%** - Discover 25% of species (+$1,000)
- ✅ **Encyclopedia 50%** - Discover 50% of species (+$3,000)
- ✅ **Encyclopedia 75%** - Discover 75% of species (+$7,500)
- ✅ **Encyclopedia Master** - 100% completion (+$50,000 + 10 skill points!)

### Mutation Achievements
- ✅ **Mutation Hunter** - Catch all 6 mutation types (+$5,000)
- ✅ **Golden Catch** - Catch a golden mutation
- ✅ **Magical Encounter** - Catch the ultra-rare magical mutation (+2 skill points!)

### Special Achievements
- ✅ **Blobfish Bonanza** - Catch the legendary Blobfish
- ✅ **Leviathan Slayer** - Defeat the Leviathan (+3 skill points!)
- ✅ **Kraken's Demise** - Catch the Kraken
- ✅ **Rod Master** - Own all rod types
- ✅ **Bait Collector** - Own all bait types
- ✅ **Location Master** - Unlock all locations
- ✅ **Quest Master** - Complete 50 quests (+3 skill points!)

---

## 🎲 Quest System

Dynamic quests provide extra income and objectives!

### Quest Types

1. **Catch Specific Species**
   - Example: "Catch a Pike"
   - Reward: $500

2. **Catch Minimum Weight**
   - Example: "Catch a fish over 50kg"
   - Reward: $300

3. **Catch Rarity Targets**
   - Example: "Catch 3 Rare fish"
   - Reward: $800

### Quest Features
- **One active quest** at a time
- **Auto-generation** when completed
- **Automatic tracking** during fishing
- **Immediate rewards** on completion
- **Progress toward Quest Master** achievement

---

## 🎨 Visual Design

### Beautiful Unicode Symbols

The game uses elegant Unicode characters for stunning visuals:

**Terrain:**
- `≈` - Lake water (calm waves)
- `≋` - River water (flowing)
- `~` - Ocean water
- `♨` - Volcanic water (hot springs)
- `⌬` - Space station tiles
- `♠` - Forests/trees
- `▲` - Mountains
- `·` - Ground/land
- `█` - Walls/borders

**Map Elements:**
- `☻` - Your character (friendly face!)
- `⊙` - Regular fishing spot (target)
- `◉` - Golden fishing spot (enhanced)
- `✦` - Special objects/stars

**Borders:**
- `┏━━┓` - Top border
- `┃  ┃` - Side borders
- `┗━━┛` - Bottom border
- `╔══╗` - Menu borders
- `║  ║` - Menu sides

### Color System

**Locations:**
- **Light Blue** - Lake waters
- **Cyan** - Rivers
- **Blue** - Ocean
- **Red** - Volcanic
- **Magenta** - Space Station
- **Green** - Forests

**Fishing Spots:**
- **Cyan** - Regular spots
- **Bright Yellow** - Golden spots

**UI:**
- **Green** - Success messages
- **Red** - Warnings/errors
- **Yellow** - Important info
- **Cyan** - Headers

---

## 💡 Pro Tips & Strategies

### General Strategy
1. 🎯 **Always scout for golden spots** before fishing
2. ⚡ **Fish at golden spots during storms** for maximum rare fish
3. 🌙 **Night fishing at golden spots** = best Legendary/Mythical odds
4. 💰 **Save golden mutations** for when you need emergency cash
5. 📚 **Complete encyclopedia** early for 10 skill points

### Stat Allocation Guide

**Balanced Build (Recommended):**
- Strength: 3 | Luck: 3 | Patience: 4
- Good all-around for beginners

**Lucky Hunter:**
- Strength: 2 | Luck: 6 | Patience: 2
- Maximize rare fish encounters

**Skill Master:**
- Strength: 5 | Luck: 2 | Patience: 3
- Never miss a catch, consistent income

**Patient Angler:**
- Strength: 2 | Luck: 2 | Patience: 6
- Easiest mini-games, stress-free

### Money Making Strategies

**Early Game (Levels 1-3):**
- Fish at Lake and River
- Sell everything except special mutations
- Save for Carbon Rod ($3,500)
- Buy Squid bait ($800)

**Mid Game (Levels 4-7):**
- Unlock Ocean at Level 3
- Hunt for Rare+ fish
- Upgrade to Legendary Rod ($10,000)
- Buy Premium Lure ($4,000)
- Start completing encyclopedia

**Late Game (Level 8+):**
- Farm Volcanic Waters and Space Station
- Focus on golden spots
- Hunt Mythical fish during storms
- Complete quests for extra income
- Max out skill tree

**Endgame Farming:**
- Space Station + Golden Spots + Stormy Weather + Night
- Use Godly Rod + Master Bait
- Max Lucky Fisherman skill
- Sell Magical/Golden Mythicals for millions

### Golden Spot Optimization

1. **Enter location**
2. **Scan entire map** for golden spots (◉)
3. **Mark positions** mentally
4. **Start with furthest spot** and work back
5. **Fish until esky is 90% full**
6. **Return to sell**
7. **Repeat!**

**Golden Spot Math:**
- 10% spawn chance per spot
- Average 1-2 golden spots per location
- 2.5x multiplier to rare fish weights
- Stacks with weather, time, bait, and skills!

---

## 🎮 Mini-Game System

### Mini-Game Types

1. **Reaction Test**
   - Wait for "NOW!" signal
   - Press Enter as fast as possible
   - Perfect timing: < 0.5 seconds

2. **Memory Sequence**
   - Memorize symbol pattern
   - Repeat it correctly
   - Length increases with fish rarity

3. **Pattern Matching**
   - Follow directional movements
   - Input correct sequence
   - Speed and accuracy matter

### Difficulty Scaling

Mini-game difficulty depends on:
- Fish rarity (Mythical = hardest)
- Player level (scales up gradually)
- Patience stat (higher = easier)
- Quick Reflexes skill (reduces difficulty)
- Game difficulty setting

**Pro Tip:** Max Patience stat + Quick Reflexes skill = easiest mini-games!

---

## 🌦️ Weather & Time System

### Weather Types

| Weather | Spawn Rate | Effect |
|---------|-----------|---------|
| **Sunny** | 40% | Normal spawn rates |
| **Cloudy** | 30% | Slightly increased activity |
| **Rainy** | 20% | +20% to all fish weights |
| **Stormy** | 10% | +50% to Rare/Legendary/Mythical! |

**Weather changes randomly** with 15% chance when fishing.

### Time of Day

| Time | Effect |
|------|--------|
| **Dawn** | 2x Mythical spawn rate |
| **Day** | Normal rates |
| **Dusk** | 2x Mythical spawn rate |
| **Night** | 1.3x Rare & Legendary spawn rate |

**Best combo:** Dawn/Dusk + Stormy + Golden Spot = Maximum Mythical odds!

---

## 💾 Save System

### Save File Location

- **Windows:** `C:\Users\[YourName]\Documents\FiskeSpill\game_save.json`
- **macOS/Linux:** `~/Documents/FiskeSpill/game_save.json`

### What Gets Saved

**Character Data:**
- Name, stats, difficulty
- Level, XP, money
- Current rod and bait

**Inventory:**
- All fish in esky
- Owned rods and baits
- Trophy room contents

**Progress:**
- Encyclopedia discoveries
- Achievement completion
- Skill tree levels
- Quest status
- Rod durability
- Weather & time

### Save Tips

- **Save frequently** (option 11 in main menu)
- **Auto-save** on major achievements
- **Backup** before updates
- **Human-readable** JSON format
- **Can edit** for debugging (don't cheat!)

---

## 🎨 Easter Eggs & References

The game is packed with video game references!

### Gaming Easter Eggs

**Minecraft:**
- Blockfish Creeper
- Redstone Katten (Mythical tribute)

**Portal:**
- Portal Eel
- Vault Carp

**Dark Souls:**
- Abyss Watcher
- Ashen Knight Carp
- Hollow Pike

**Halo:**
- Warp Stalker
- Fallen Starfish

**Half-Life:**
- Headcrab Eel
- Lambda Salmon
- Resonance Catfish

**The Legend of Zelda:**
- Hylian Pike

**Super Mario:**
- Plumber's Tuna

**Skyrim:**
- Nordic Dragon Salmon

**Undertale:**
- Determined Eel
- Mountain Spirit Trout

**Terraria:**
- Corrupt Bass

**Plus many more hidden references to discover!**

### Ultra-Rare Finds

- **Blobfish** - 0.00001% chance (requires Blobfish Rod!)
- **Magical Mutations** - 0.01% on any fish
- **Redstone Katten** - Mythical Space tribute fish

---

## 🗺️ Roadmap & Future Plans

### Confirmed Upcoming Features

- [ ] **More locations** - Swamp, Kelp Forest, Alien Ocean
- [ ] **Seasonal events** - Limited-time fish
- [ ] **Crafting system** - Make custom lures
- [ ] **Weather forecast** - Plan your fishing trips
- [ ] **Tournaments** - Compete for prizes

### Under Consideration

- [ ] **Pet companions** - Bonus effects
- [ ] **Fish breeding** - Genetics system
- [ ] **Multiplayer trading** - Share your catches
- [ ] **Mobile version** - Fish on the go
- [ ] **GUI option** - Graphical interface
- [ ] **Mod support** - Community content

---

## 🐛 Known Issues

Currently **no major bugs** in v0.4.3!

If you encounter issues:
1. Update to latest version
2. Check your Python version (3.7+ required)
3. Verify colorama is installed
4. Report on GitHub Issues

---

## 🤝 Contributing

Want to help improve the game? Contributions welcome!

### How to Contribute

1. **Fork** the repository
2. **Create** a feature branch
3. **Make** your changes
4. **Test** thoroughly
5. **Submit** a pull request

### Contribution Ideas

- New fish species with real-world info
- Additional mini-game types
- Balance adjustments
- Bug fixes
- Achievement suggestions
- Easter egg ideas
- Location designs
- UI improvements

---

## 📜 License

This project is licensed under the **MIT License**.

You're free to:
- ✅ Use commercially
- ✅ Modify
- ✅ Distribute
- ✅ Private use

Just include the original license!

---

## 👏 Credits

**Developer:** Nokoiscool  
**Engine:** Python 3.7+  
**Library:** colorama (terminal colors)  
**Inspired by:** Stardew Valley, Terraria fishing, The Legend of Zelda exploration  

**Special Thanks:**
- The Python community
- Everyone who suggested features
- Players who found bugs
- You, for playing! 🎣

---

## 📞 Support & Community

- **Issues:** [GitHub Issues](https://github.com/Nokoiscool/Fishing-game/issues)
- **Updates:** Check GitHub for latest release
- **Community:** Share your legendary catches!

---

## 📸 Sample Gameplay

### Overworld Exploration
```
╔════════════════════════╗
║  FISHING WORLD MAP     ║
║  Level 5 Angler        ║
╚════════════════════════╝

╔════════════════════════╗
║···♠♠♠··················║
║··♠♠♠♠♠·················║
║·≈≈≈≈·····≋≋≋≋··········║
║≈≈≈≈≈≈···≋≋≋≋≋≋·········║
║·≈≈≈≈·····≋≋≋≋······☻···║
║········~~~~~~~~~~······║
║·······~~~~~~~~~~~~·····║
╚════════════════════════╝

📍 River - Press E to enter!
```

### Location Fishing
```
┏━━━━━━━━━━━━━━━━━━━━┓
┃  Freshwater Lake     ┃
┗━━━━━━━━━━━━━━━━━━━━┛

┏━━━━━━━━━━━━━━━━━━━━┓
┃·······⊙·≈≈≈≈≈≈≈≈··◉┃
┃♣♣♣♣··☻·≈≈≈≈≈≈≈≈≈≈··┃
┃♣♣♣♣····≈≈≈≈≈≈≈≈≈≈·⊙┃
┗━━━━━━━━━━━━━━━━━━━━┛

✨ GOLDEN SPOT! ✨ Rare fish more likely!
```

### Successful Catch
```
✨ Fishing at a GOLDEN SPOT! Better odds! ✨

You hooked a Kraken!
Get ready... Wait for the signal!
>>> NOW! Press Enter!
Perfect! (0.189s)

Caught: Kraken (Golden) 
Weight: 52,341.23 kg | Rarity: Mythical
Sell value: $750,000
You gained 8,000 XP!

🏆 Achievement Unlocked: Kraken's Demise!
🎣 Cast your line again, or move to explore!
```

---

**Happy Fishing! 🎣**

*"The best fishing spots are the golden ones you discover yourself!"*

---


**Version 0.4.3 | Open Beta | Active Development**











wow du leste gjennom
