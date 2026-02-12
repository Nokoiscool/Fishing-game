# 🎣 Very Cool Fishing Game

A feature-rich terminal-based fishing RPG with beautiful Unicode graphics, exploration mechanics, dynamic progression systems, and **epic boss battles!**

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Version](https://img.shields.io/badge/version-0.6.0%20BETA-orange.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)
![Code Size](https://img.shields.io/badge/code%20size-~65KB-informational.svg)
![Fish Species](https://img.shields.io/badge/fish%20species-150+-success.svg)
![Locations](https://img.shields.io/badge/locations-7-blueviolet.svg)
![Boss Battles](https://img.shields.io/badge/boss%20battles-NEW!-red.svg)
![Status](https://img.shields.io/badge/status-open%20beta-brightgreen.svg)
![Game Type](https://img.shields.io/badge/type-RPG%20%2F%20Exploration-ff69b4.svg)
![Terminal](https://img.shields.io/badge/interface-terminal%20Unicode-black.svg)
![Dependencies](https://img.shields.io/badge/dependencies-colorama-red.svg)
![Save System](https://img.shields.io/badge/save%20system-JSON-blue.svg)
![Updates](https://img.shields.io/badge/updates-active-success.svg)
![Made With](https://img.shields.io/badge/made%20with-%E2%9D%A4%EF%B8%8F-red.svg)

## 🌟 What's New in v0.6.0 - BOSS BATTLES UPDATE!

### ⚔️ Undertale-Style Boss Battle System
- **Epic Boss Encounters** - Find special items while fishing to trigger boss fights!
- **Strategic Combat** - Fight, Act, Spare, or Run in turn-based battles
- **8+ Unique Attack Patterns** - Dodge tidal waves, whirlpools, tail sweeps, and devastating combos
- **Attack Minigames** - Time your strikes for critical hits using rhythm-based mechanics
- **Multiple Outcomes** - Spare bosses for positive karma or defeat them for loot

### 💫 Karma System
- **Moral Choices Matter** - Sparing gives +10 karma, killing gives -15 karma
- **Track Your Path** - Your karma affects future encounters (more features coming!)
- **Two Playstyles** - Pacifist or Warrior? You choose!

### 🐉 Current Boss: Loch Ness Monster
- **200 HP Epic Battle** - Face the legendary lake monster
- **Dynamic Fight Phases** - Boss gets more aggressive below 30% HP
- **Mercy Mechanics** - Use ACT to build mercy, then SPARE at low HP
- **Dramatic Animations** - Screen effects, ASCII art, and cinematic moments
- **Special Rewards** - Unique rewards based on how you end the fight

### 📦 Boss Item Collection
- **5% Drop Chance** - Find rare boss items while fishing in specific locations
- **Special Inventory** - Boss items stored separately from regular fish
- **Location-Specific** - Each location has its own unique boss to discover

### 🗺️ Hub Island Exploration
- **Detailed Hub Map** - Navigate the expanded Hub Island with multiple locations
Dev mode (option 99) unlocks everything instantly
- **Interactive Buildings**:
  - 🏪 **Shop** - Buy rods, bait, and repair equipment
  - 🏛️ **Aquarium** - View your trophy collection
  - 📋 **Quest Board** - Accept and complete challenges
  - 🏠 **Home** - Save your game and rest
  - ⚓ **Dock** - Travel to remote locations via world map

### 🌊 Dual Fishing Areas on Hub Island
- **Calm Lake** (≈) - Peaceful waters with lake fish
- **Swift River** (≋) - Fast-flowing river with salmon and trout
- **Golden Spots** (◉) - Rare 1.5x bonus spots on both areas

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

1. **Enjoy the animated rainbow intro** 🌈
2. **Choose "New Game"** and create your character:
   - Pick a cool fishing name
   - Distribute 15 stat points wisely (Strength, Luck, Patience)
   - Select your difficulty (Easy, Normal, or Hard)
3. **Start exploring Hub Island!**

---

## 🎮 How to Play

### Hub Island Navigation

Start your journey on the beautiful Hub Island:

```
╔═══════════════════════════════════════╗
║        🏝️ HUB ISLAND 🏝️               ║
╚═══════════════════════════════════════╝

█████████████████████████████
█🌳🌳▓▓▓▓🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳█
█🌳🏛️..▓▓▓🌳≋≋≋≋≋≋🌳🌳🌳🌳🌳█
█🌳...▓▓🌳≋⊙≋≋⊙≋◉🌳🌳🌳🌳🌳█
█🌳🏠..☻..🌳🌳≋≋≋≋≋≋≋🌳🌳🌳🌳█
█🌳......🌳≈≈≈≋≋≋🌳🌳🌳🌳🌳█
█🌳...🏪..≈≈⊙≈≈≋≋≋🌳🌳🌳🌳🌳█
█🌳🌳....≈≈≈≈≈≈≈≋≋≋🌳🌳🌳🌳🌳█
█🌳🌳.📋..≈⊙≈≈◉≈≈≈≋≋≋🌳🌳🌳🌳█
█🌳🌳....≈≈≈≈≈≈≈≈≈≋≋≋🌳🌳🌳🌳█
█████████████████████████████

🏪 Shop | 🏛️ Aquarium | 📋 Quests | 🏠 Home | ⚓ Dock
⊙ Fish Spot | ◉ Golden Spot

[WASD] Move | [E] Interact | [I] Inventory | [Q] Quit
```

**Controls:**
- **W/A/S/D** - Move around Hub Island
- **E** - Interact with buildings or fish at spots
- **I** - Open inventory
- **C** - View character stats
- **Q** - Quit game

### World Map & Remote Locations

Visit the **Dock (⚓)** to access the world map and travel to distant fishing grounds:

```
╔════════════════════════════════════════════╗
║            🗺️  WORLD MAP 🗺️               ║
╚════════════════════════════════════════════╝

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~🌊O~~~~~~~~~❄️A~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~🏝️H~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~🌋V~~~~~~~🌊D~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~🚀S~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Locations:
  🌊 Ocean           ✓ Lvl 5
  🌊 Deep Sea        ✓ Lvl 10
  🌋 Volcanic Lake   🔒 Lvl 20
  ❄️ Arctic Waters   🔒 Lvl 25
  🚀 Space Station   🔒 Lvl 30

[WASD] Move | [E] Enter Location | [Q] Return
```

### Fishing Mechanics

1. **Find a fishing spot** - look for ⊙ or ◉ symbols
2. **Stand on the spot** and press **E**
3. **Complete the mini-game** - button mashing, timing, or pattern matching
4. **Catch the fish** - added to your inventory
5. **Fish again!** - Press E to cast again at the same spot

#### Golden Spots ✨
- **Bright golden color (◉)** - easy to spot!
- **1.5x sell price and XP** - better rewards
- **Scattered across Hub Island** - explore to find them all!

### Boss Battle System ⚔️

#### Finding Boss Items
While fishing, you have a **5% chance** to find a special boss item:
```
⚡ You found a special item: Ancient Scale! ⚡
A shimmering scale from an ancient creature. Using it might summon something...
```

#### Starting a Boss Fight
1. Open your **Inventory** with [I]
2. Select **[U]se Boss Item**
3. Choose which boss item to use
4. **The battle begins!**

#### Boss Battle Controls
```
╔═══════════════════════════════════════╗
║   ⚔️  BOSS BATTLE: Loch Ness Monster  ║
╚═══════════════════════════════════════╝

Boss HP: ❤❤❤❤❤❤❤❤❤❤❤❤♡♡♡♡♡♡♡♡ 120/200
Your HP: ❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤ 100/100

What do you do?
[F]ight | [A]ct | [S]pare | [R]un
```

**Action Breakdown:**

- **[F]ight** - Attack the boss with a timing minigame
  - Perfect timing = **2x damage (CRITICAL HIT!)**
  - Good timing = **1.5x damage**
  - Weak timing = **0.8x damage**
  - Miss = **0.5x damage**

- **[A]ct** - Show mercy to calm the boss
  - Increases mercy level
  - Makes boss spareable when combined with low HP
  - Required multiple times before sparing works

- **[S]pare** - End the fight peacefully
  - Only works when boss is **below 40% HP** AND **mercy level ≥ 3**
  - Grants **+10 karma** and special rewards
  - Boss becomes permanently peaceful

- **[R]un** - Attempt to flee
  - 50% success chance
  - No penalties if successful

#### Boss Attack Patterns

The Loch Ness Monster has **8 unique attacks**:

1. **Wave Crash** - Dodge moving wave patterns
2. **Water Blast** - Choose correct dodge direction
3. **Tidal Wave** - Multi-wave barrage with safe zones
4. **Whirlpool** - Button mashing to escape
5. **Tail Sweep** - Read tells and predict direction
6. **Deep Dive Slam** - Two-phase dive and slam attack
7. **Mist Breath** - Memory test with obscured vision
8. **ULTIMATE COMBO** - Triple attack (only when HP < 30%)

Each attack is a unique minigame you must complete to avoid damage!

#### Boss Rewards

**Sparing (Peaceful):**
- ✨ +10 Karma
- 💰 $1,000
- 🎯 500 XP
- 💚 Feel good about showing mercy

**Defeating (Combat):**
- ⚔️ -15 Karma
- 💰 $500
- 🎯 300 XP
- 😔 Weight on your conscience

**Death:**
- 💀 Lose 15% of your money
- 🐟 Lose up to 3 random fish from inventory
- ❤️ HP restored, can try again

### Progression Loop

```
Explore Hub Island → Find Boss Item → Boss Battle!
       ↑                    ↓                ↓
   Level Up  ← Gain XP ← Sell Fish ← Catch Fish
       ↑                                     ↓
Travel via Dock → Explore Remote Locations →
```

1. **Fish** on Hub Island and remote locations
2. **Level up** to unlock new areas
3. **Collect boss items** for epic encounters
4. **Battle or spare** legendary creatures
5. **Build karma** through your choices
6. **Sell fish** to buy better equipment
7. **Complete encyclopedia** with all species

---

## 🌍 Locations & Unlocking

### Location Unlock Progression

| Level | Location | Symbol | Fish Rarity | Special Features |
|-------|----------|--------|-------------|------------------|
| **1** | Hub Island - Calm Lake | ≈ | Common-Rare | Starting zone, peaceful |
| **1** | Hub Island - Swift River | ≋ | Common-Rare | Flowing water, salmon |
| **5** | Ocean | 🌊 | Uncommon-Legendary | Sharks and big game |
| **10** | Deep Sea | 🌊 | Rare-Mythical | Deepest waters, Kraken |
| **20** | Volcanic Lake | 🌋 | Rare-Legendary | Dangerous heat, fire fish |
| **25** | Arctic Waters | ❄️ | Rare-Mythical | Frozen waters, ice fish |
| **30** | Space Station | 🚀 | Legendary-Godly | Zero gravity, alien fish |

### Boss Locations

| Boss | Location | Item Required | Difficulty |
|------|----------|---------------|------------|
| **Loch Ness Monster** | Hub Island - Calm Lake | Ancient Scale | ⭐⭐⭐ |
| **[MORE COMING SOON]** | Various | Various | TBA |

---

## 🎯 Core Gameplay Features

### Character Creation
- **Name your angler** - choose your fishing identity
- **Distribute 15 stat points:**
  - **Strength** - More damage in boss fights, heavier fish
  - **Luck** - Better chance for rare fish and boss items
  - **Patience** - Makes mini-games easier (fishing & bosses)
- **Choose difficulty:**
  - **Easy** - 1.5x XP & Money, slower boss attacks
  - **Normal** - 1x XP & Money, standard difficulty
  - **Hard** - 0.75x XP & Money, 2x Rarity Chance, faster boss attacks

### RPG Progression
- **Level up** from catching fish and defeating bosses
- **Unlock locations** as you reach level thresholds
- **Skill points** to upgrade stats (earn 3 per level)
- **Equipment shop** - 14 rods and 15 bait types
- **Dynamic weather** - 5 weather types affecting spawns
- **Rod durability** - maintain your equipment

### Collection Systems
- **150+ fish species** from Common to Mythical
- **7 mutation types** including ultra-rare Magical (10x value!)
- **Encyclopedia** tracking with real-world fish facts
- **Trophy Room** to preserve special catches
- **Boss Item Collection** - find all special items
- **Defeated Bosses Log** - track your victories

### Economic System
- **Sell fish** for money based on rarity and mutations
- **Buy equipment** - better rods = better success rates
- **Repair rods** when durability gets low
- **Boss rewards** for completing encounters
- **Difficulty multipliers** affect earnings

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
| **Godly** | <0.01% | $500,000+ | Noko the Blobfish (ultra-rare) |

### Mutation System

Mutations dramatically increase fish value:

| Mutation | Spawn Chance | Value Multiplier | Color |
|----------|--------------|------------------|-------|
| Normal | 94.99% | 1x | White |
| Albino | 5% | 2x | Bright white |
| Golden | 1% | 5x | Light yellow |
| Shiny | 0.1% | 3x | Cyan |
| **Magical** | **0.01%** | **10x** | Magenta |

**Example:** A Legendary fish worth $1,000 with a Magical mutation = $10,000!

---

## 💰 Equipment & Upgrades

### Fishing Rods (14 Total)

| Rod Name | Cost | Bonus | Notes |
|----------|------|-------|-------|
| Bamboo Rod | Free | 0% | Starting rod |
| Wooden Rod | $150 | 0.73x | First upgrade |
| Fiberglass Rod | $400 | 0.76x | Decent |
| Composite Rod | $800 | 0.80x | Balanced |
| Carbon Rod | $1,500 | 0.84x | Professional |
| Graphite Rod | $2,500 | 0.88x | Lightweight |
| Titanium Rod | $4,000 | 0.92x | Top tier |
| Reinforced Rod | $6,500 | 0.95x | Durable |
| Legendary Rod | $10,000 | 0.98x | Elite |
| Mythic Rod | $20,000 | 1.02x | Mythical tech |
| Abyssal Rod | $35,000 | 1.05x | Deep sea |
| Quantum Rod | $60,000 | 1.08x | Time tech |
| Godly Rod | $100,000 | 1.12x | Divine |
| **Blobfish Rod** | **$2,000,000** | **5.0x** | Ultimate rod |

### Bait Types (15 Total)

| Bait Name | Cost | XP Bonus | Rarity Bonus |
|-----------|------|----------|--------------|
| Worm | Free | 0% | 0% |
| Bread | $50 | 0% | 0.05% |
| Cricket | $120 | 0% | 0.08% |
| Minnow | $250 | 0% | 0.12% |
| Corn | $180 | 0% | 0.10% |
| Shrimp | $500 | 0% | 0.15% |
| Nightcrawler | $400 | 0% | 0.14% |
| Squid | $800 | 0% | 0.18% |
| Cut Bait | $650 | 0% | 0.16% |
| Artificial Lure | $1,200 | 0% | 0.22% |
| Live Bait | $1,500 | 0% | 0.25% |
| Special Lure | $2,500 | 0% | 0.30% |
| Premium Lure | $4,000 | 0% | 0.35% |
| Exotic Bait | $6,500 | 0% | 0.40% |
| **Master Bait** | **$50,000** | **0%** | **0.50%** |

---

## 🌟 Tips & Strategies

### Fishing Tips
1. **Golden Spots (◉)** - Always prioritize! 1.5x rewards
2. **Weather Matters** - Stormy weather = +30% rarity, +50 XP
3. **Upgrade Rods First** - Better rods = higher catch rates
4. **Save Trophies** - Keep rare catches in aquarium
5. **Patience Stat** - Makes ALL minigames easier
6. **Explore Thoroughly** - Hub Island has hidden golden spots

### Boss Battle Tips
1. **Learn Patterns** - Each attack has tells and strategies
2. **Build Mercy First** - Use ACT 3+ times before sparing
3. **Perfect Timing** - Practice the attack minigame for critical hits
4. **Spare at 40% HP** - Boss becomes spareable at low health with high mercy
5. **Strength Matters** - Higher strength = more damage to bosses
6. **Patience Helps** - Makes boss attack dodges easier
7. **Save Before Fighting** - Visit Home to save your progress
8. **Karma Path** - Decide early: peaceful or warrior playthrough

### Progression Tips
1. **Complete Quests** - Easy money and XP boosts
2. **Level 5 First Goal** - Unlock Ocean for better fish
3. **Save Boss Items** - Use when you're strong enough
4. **Repair Often** - Don't let rod durability hit 0
5. **Difficulty Choice** - Hard mode = 2x rare fish spawns!
6. **Invest in Bait** - Better rarity bonuses = more legendaries

### Money Making Tips
1. **Hunt Mutations** - Golden/Magical = 5-10x value
2. **Storm Fishing** - Best weather for valuable catches
3. **Golden Spots** - 1.5x sell prices
4. **Deep Sea** - Highest concentration of expensive fish
5. **Boss Sparing** - Better rewards than killing
6. **Trophy Selectively** - Only keep the rarest for aquarium

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
- Reaper Levi-Minnow

**Halo:**
- Warp Stalker
- Fallen Starfish

**Half-Life:**
- Headcrab Eel
- Lambda Salmon
- Resonance Catfish

**The Legend of Zelda:**
- Hylian Pike
- (Overworld inspired by Zelda exploration!)

**Super Mario:**
- Plumber's Tuna

**Skyrim:**
- Nordic Dragon Salmon

**Undertale:**
- Determined Eel
- Mountain Spirit Trout
- (Boss battle system inspired by Undertale!)

**Terraria:**
- Corrupt Bass

**Hollow Knight:**
- Pale King Mackerel

**Celeste:**
- Strawberry Koi

**Slime Rancher:**
- Slimey Gloopfish

**Fallout:**
- Vault Carp

**Cyberpunk:**
- Cyberpunk Neon Koi

**Plus many more hidden references to discover!**

### Ultra-Rare Finds

- **Blobfish** - 0.00001% chance (requires Blobfish Rod!)
- **Noko the Blobfish** - 0.0000001% chance (Godly rarity!)
- **Magical Mutations** - 0.01% on any fish
- **Redstone Katten** - Mythical Space tribute fish

---

## 🗺️ Roadmap & Future Plans

### Confirmed Upcoming Features

- [ ] **More Boss Battles** - Ocean Kraken, Deep Sea Horror, Volcanic Phoenix
- [ ] **Advanced Karma System** - Special dialogue and endings based on choices
- [ ] **Boss Respawns** - Rechallenge defeated bosses
- [ ] **More Locations** - Swamp, Kelp Forest, Alien Ocean
- [ ] **Crafting System** - Create custom lures
- [ ] **Tournaments** - Compete for prizes

### Under Consideration

- [ ] **Pet Companions** - Fishing buddies with bonuses
- [ ] **Boss Rush Mode** - Fight all bosses back-to-back
- [ ] **Multiplayer Trading** - Share catches with friends
- [ ] **Mobile Version** - Fish on the go
- [ ] **GUI Option** - Graphical interface
- [ ] **Mod Support** - Community content

---

## 🐛 Known Issues

### Current Known Issues
- Boss battles are currently limited to one boss (more coming!)
- Some terminal emulators may have input lag during minigames
- Emoji rendering varies by system

### Reporting Issues
If you encounter issues:
1. Update to latest version
2. Check your Python version (3.7+ required)
3. Verify colorama is installed
4. Report on GitHub Issues with details

---

## 💾 Save System

### Save File Location

Saves are stored with unique hash-based filenames:
- **Format:** `save_[hash].json`
- **Location:** Same directory as game

### What Gets Saved

**Character Data:**
- Name, stats, difficulty
- Level, XP, money, skill points
- Current rod and bait
- HP (current and max)

**Inventory:**
- All fish in inventory
- **Boss items** (separate collection)
- Owned rods and baits
- Trophy room contents

**Progress:**
- Encyclopedia discoveries
- **Defeated bosses list**
- **Karma score**
- Current location and weather
- Rod durability

### Save Tips

- **Save frequently** at Home building
- **Backup** before boss fights
- **Human-readable** JSON format
- **Multiple saves** supported (character-specific)

---

## 🤝 Contributing

Want to help improve the game? Contributions welcome!

### How to Contribute

1. **Fork** the repository
2. **Create** a feature branch
3. **Make** your changes
4. **Test** thoroughly (especially boss battles!)
5. **Submit** a pull request

### Contribution Ideas

- New boss designs with unique attacks
- Additional fish species with real-world info
- New mini-game types
- Balance adjustments (boss difficulty, fish values)
- Achievement suggestions
- Easter egg ideas
- Location designs
- UI improvements
- Bug fixes

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
**Inspired by:**
- Stardew Valley (fishing mechanics)
- Undertale (boss battle system)
- The Legend of Zelda (exploration)
- Animal Crossing (collection & progression)

**Special Thanks:**
- The Python community
- Everyone who suggested features (especially boss battles!)
- Players who found bugs
- You, for playing! 🎣

---

## 📞 Support & Community

- **Issues:** [GitHub Issues](https://github.com/Nokoiscool/Fishing-game/issues)
- **Updates:** Check GitHub for latest release
- **Community:** Share your legendary catches and boss victories!

---

## 📸 Sample Gameplay

### Hub Island Exploration
```
╔═══════════════════════════════════════╗
║        🏝️ HUB ISLAND 🏝️               ║
╚═══════════════════════════════════════╝

█🌳🌳▓▓▓▓🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳█
█🌳🏛️..▓▓▓🌳≋≋≋≋≋≋🌳🌳🌳🌳🌳█
█🌳...▓▓🌳≋⊙≋≋⊙≋◉🌳🌳🌳🌳🌳█
█🌳🏠..☻..🌳🌳≋≋≋≋≋≋≋🌳🌳🌳🌳█
█🌳......🌳≈≈≈≋≋≋🌳🌳🌳🌳🌳█

📍 Standing at Home - Press E to enter!
```

### Boss Battle Start
```
╔═══════════════════════════════════════╗
║     ⚡ BOSS ITEM ACTIVATED ⚡          ║
╚═══════════════════════════════════════╝

Using: Ancient Scale
Location: Hub Island - Calm Lake

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                _..--+~/@-@--.
        _-=~      (  .    )
        _-~     _.--=.\ \''''
    _~      _-       \ \_\
    =      _=          '--'
    '      =                    
    :      :              
... Loch Ness Monster!

*The water trembles...*
*A massive shape rises from the depths!*
*The Loch Ness Monster emerges!*

Press Enter to begin battle...
```

### Epic Combat
```
════════════════════════════════════
Loch Ness Monster
HP: ❤❤❤❤❤❤❤❤❤❤❤❤♡♡♡♡♡♡♡♡ 120/200

You
HP: ❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤ 100/100
════════════════════════════════════

What do you do?
[F]ight | [A]ct | [S]pare | [R]un
> F

⚔️  ATTACK! Press SPACE at the right moment! ⚔️

[──────────────█████──────────────]

★★★ CRITICAL HIT! ★★★
You dealt 40 damage!

*It roars in pain!*
```

### Peaceful Resolution
```
════════════════════════════════════
⭐ * The monster can be SPARED *

You choose to spare the monster...

    ✨              
  ✨  ✨            
✨  💚  ✨          
✨  MERCY  ✨        
  ✨  💚  ✨         
    ✨  ✨           

════════════════════════════════════
*The monster nods gratefully*
*It sinks back into the depths peacefully*
*You feel warmth in your heart*
════════════════════════════════════

You gained 500 XP and $1,000!
Karma +10 (Total: 10)
```

---

**Happy Fishing! 🎣⚔️**

*"May your lines be tight, your catches legendary, and your heart merciful!"*

---

**Version 0.6.0 BETA | Boss Battles Update | Active Development**







wow du leste gjennom

