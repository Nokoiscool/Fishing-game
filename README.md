# 🎣 Very Cool Fishing Game

A feature-rich terminal-based fishing game with RPG elements, written in Python.

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Version](https://img.shields.io/badge/version-0.4.1-orange.svg)

## 🌟 Features

### Core Gameplay
- **7 Unique Locations** - Lake, River, Ocean, Deep Sea, Volcanic Lake, Arctic, and Space!
- **150+ Fish Species** - From common Trout to mythical creatures like the Kraken and Leviathan
- **7 Mutation Types** - Normal, Albino, Glowing, Spotted, Golden, Shadow, and the ultra-rare Magical
- **Dynamic Weather System** - 4 weather types (Sunny, Cloudy, Rainy, Stormy) that affect catch rates
- **Day/Night Cycle** - 4 times of day (Dawn, Day, Dusk, Night) with different fish spawns
- **Character Creation** - Customize your name, distribute 10 stat points, and choose difficulty

### Progression Systems
- **RPG Leveling** - Gain XP, level up, unlock new locations (up to level 12 for Space)
- **Skill Tree** - 6 upgradeable skills with up to 5 levels each
- **Equipment Shop** - 14 rods (Bamboo to Godly) and 15 bait types
- **Rod Durability** - Rods wear down and need repairs
- **Quest System** - Dynamic quests with monetary rewards
- **Trophy Room** - Preserve your most memorable catches

### Collection & Tracking
- **Encyclopedia** - Detailed tracking of all discovered species with real-world info
- **33+ Achievements** - Unlock rewards for reaching milestones
- **Statistics Page** - Track total catches, species discovered, and more
- **Save/Load System** - JSON-based saves stored in Documents folder

### Mini-Games
- **Reaction Test** - Quick reflexes determine success
- **Memory Sequence** - Memorize and repeat symbol patterns
- **Pattern Matching** - Follow directional movement patterns
- Difficulty scales with fish rarity and player level

### Special Features
- **Easter Eggs** - Hidden video game-themed fish (Minecraft, Portal, Dark Souls, and more!)
- **Difficulty Modes** - Easy, Normal, Hard, and Legendary with XP/challenge modifiers
- **Dev Mode** - Debug menu accessible with code '99' at main menu

## 📋 Requirements

- Python 3.7 or higher
- colorama library
- Windows, macOS, or Linux

## 🚀 Quick Start

### Option 1: Automatic Installation (Windows Only)

**PowerShell:**
```powershell
powershell -ExecutionPolicy Bypass -File install_fishing_game.ps1
```

The installer will automatically:
- Check/install Python if needed
- Download the game from GitHub
- Install colorama dependency
- Create desktop launcher
- Set up update script

### Option 2: Manual Installation

1. **Install Python** (if not already installed)
   - Download from [python.org](https://www.python.org/downloads/)
   - ✅ Check "Add Python to PATH" during installation

2. **Install colorama**
   ```bash
   pip install colorama
   ```

3. **Download the game**
   ```bash
   curl -O https://raw.githubusercontent.com/Nokoiscool/Fishing-game/main/fishgame.py
   ```

4. **Run the Game**
   ```bash
   python fishgame.py
   ```

## 🎮 How to Play

### Starting Your Journey
1. **Character Creation**
   - Choose your fisherman's name
   - Distribute 10 stat points:
     - **Strength**: Increases catch rate (reduces escape chance)
     - **Luck**: Increases rare fish spawn chance
     - **Patience**: Makes mini-games easier
   - Select difficulty (affects XP gain and challenge)

2. **Main Menu Navigation**
   - `1` - Fish (choose location)
   - `2` - View Inventory
   - `3` - Sell Fish
   - `4` - Shop (rods, bait, upgrades)
   - `5` - View Encyclopedia
   - `6` - Quests
   - `7` - Trophy Room
   - `8` - View Achievements
   - `9` - Stats
   - `10` - Skill Tree
   - `11` - Save Game
   - `12` - Load Game
   - `13` - Exit

3. **Fishing Mechanics**
   - Choose an unlocked location
   - Complete the mini-game to catch the fish
   - Success depends on rod quality, stats, and skills
   - Rod durability decreases with each catch

4. **Economy & Progression**
   - Sell fish for money (mutations boost value significantly)
   - Buy better rods and bait
   - Upgrade esky capacity (starts at 50)
   - Level up to unlock new locations
   - Spend skill points on permanent upgrades

### Controls
- Navigate all menus using number keys
- Mini-games use keyboard input (Enter, letters)
- Type `99` at main menu for dev mode (if creating new game)

## 🎯 Tips for Success

### Essential Strategies
- 🎣 **Upgrade Early** - Better rods = more catches, less escapes
- 🪱 **Use Premium Bait** - Master Bait (+50% rarity) is worth the investment
- 🌩️ **Storm Fishing** - Rare/Legendary fish spawn 1.5x more during storms
- 🌙 **Night & Dawn/Dusk** - Best times for Legendary and Mythical fish
- 💰 **Don't Sell Everything** - Keep special mutations and rare fish for trophy room

### Stat Allocation
- **Balanced Build**: 3/3/4 (good for beginners)
- **Lucky Fisher**: 2/6/2 (maximize rare catches)
- **Skilled Angler**: 5/2/3 (never miss a catch)
- **Patient Master**: 2/2/6 (easiest mini-games)

### Skill Tree Priority
1. **Master Angler** (catch rate) - Prevents fish from escaping before mini-game
2. **Rare Finder** (rare spawn) - More legendary/mythical encounters
3. **Quick Reflexes** (mini-game ease) - Easier to actually catch fish
4. **Iron Grip** (XP gain) - Faster leveling
5. **Lucky Fisherman** (mutations) - Golden/Magical fish worth 5-10x more
6. **Bargain Hunter** (sell price) - Extra profit

### Money Making
- Focus on Rare+ fish (100+ coins)
- Golden mutations = 5x base value
- Magical mutations = 10x base value
- Don't sell until esky is full for efficiency
- Complete quests for bonus income

## 🐟 Fish System

### Rarity Tiers

| Rarity | Spawn Weight | Examples | Avg Value |
|--------|--------------|----------|-----------|
| **Common** | 70-80% | Trout, Cod, Perch, Sunfish | $10-50 |
| **Uncommon** | 15-20% | Bass, Tuna, Pike, Catfish | $50-150 |
| **Rare** | 5-8% | Sturgeon, Shark, Muskie, Crystal Salmon | $100-400 |
| **Legendary** | 1-3% | Arapaima, Coelacanth, Giant Grouper, Phoenix Tuna | $600-1,500 |
| **Mythical** | <0.1% | Kraken, Leviathan, Dragon, Blobfish | $10,000-300,000 |

### Mutation System

| Mutation | Rarity | Value Multiplier | Visual |
|----------|--------|------------------|--------|
| Normal | 79.99% | 1x | White text |
| Albino | 5% | 2x | Bright white |
| Glowing | 5% | 2.5x | Green |
| Spotted | 5% | 1.5x | Yellow |
| Golden | 3% | 5x | Light yellow |
| Shadow | 2% | 3x | Dark gray |
| **Magical** | 0.01% | **10x** | Magenta |

### Location Unlock Levels

1. **Lake** - Level 1 (Starting location)
2. **River** - Level 2
3. **Ocean** - Level 3
4. **Deep Sea** - Level 5
5. **Volcanic Lake** - Level 7
6. **Arctic** - Level 9
7. **Space** - Level 12

## 🏆 Achievements (33 Total)

### Fishing Achievements
- ✅ **First Catch** - Catch your first fish
- ✅ **First Rare** - Catch a rare fish
- ✅ **First Legendary** - Catch a legendary fish
- ✅ **First Mythical** - Catch a mythical fish
- ✅ **Fisherman** - Catch 50 fish total
- ✅ **Master Fisherman** - Catch 200 fish total
- ✅ **Legendary Angler** - Catch 1000 fish total
- ✅ **Speed Fisher** - Complete minigame in under 3 seconds
- ✅ **Perfect Reflexes** - Complete 10 minigames perfectly
- ✅ **Lucky Streak** - Catch 5 rare+ fish in a row

### Wealth Achievements
- ✅ **Millionaire** - Earn $1,000,000
- ✅ **Billionaire** - Earn $1,000,000,000 (Awards 5 skill points!)

### Discovery Achievements
- ✅ **Encyclopedia 25%** - Discover 25% of all species (+$1,000)
- ✅ **Encyclopedia 50%** - Discover 50% of all species (+$3,000)
- ✅ **Encyclopedia 75%** - Discover 75% of all species (+$7,500)
- ✅ **Encyclopedia Master** - 100% completion (+$50,000 + 10 skill points!)

### Mutation Achievements
- ✅ **Mutation Hunter** - Find all 6 mutation types (+$5,000)
- ✅ **Golden Catch** - Catch a golden mutation
- ✅ **Magical Encounter** - Catch a magical mutation (+2 skill points!)

### Size Achievements
- ✅ **Heavyweight** - Catch 100kg+ fish
- ✅ **Titan Hunter** - Catch 1,000kg+ fish (+$5,000)
- ✅ **Leviathan Slayer** - Catch 10,000kg+ fish (+$25,000 + 3 skill points!)

### Exploration Achievements
- ✅ **Explorer** - Fish in 3 different locations
- ✅ **Master Explorer** - Fish in all 7 locations (+$10,000)
- ✅ **Deep Diver** - Catch a deep sea fish
- ✅ **Cosmic Fisher** - Catch a fish in space (+$15,000)

### Condition Achievements
- ✅ **Night Owl** - Fish at night
- ✅ **Storm Chaser** - Fish during a storm

### Progress Achievements
- ✅ **Trophy Collector** - Collect 10 trophies
- ✅ **Quest Master** - Complete 20 quests (+3 skill points)
- ✅ **Skill Master** - Reach 20+ total skill levels

## 🛠️ Equipment System

### Fishing Rods (14 Total)

| Rod | Cost | Catch Rate | Unlock |
|-----|------|------------|--------|
| Bamboo Rod | $0 | 70% | Starting |
| Wooden Rod | $150 | 73% | Shop |
| Fiberglass Rod | $400 | 76% | Shop |
| Composite Rod | $800 | 80% | Shop |
| Carbon Rod | $1,500 | 84% | Shop |
| Graphite Rod | $2,500 | 88% | Shop |
| Titanium Rod | $4,000 | 92% | Shop |
| Reinforced Rod | $6,500 | 95% | Shop |
| Legendary Rod | $10,000 | 98% | Shop |
| Mythic Rod | $20,000 | 102% | Shop |
| Abyssal Rod | $35,000 | 105% | Shop |
| Quantum Rod | $60,000 | 108% | Shop |
| Godly Rod | $100,000 | 112% | Shop |
| Blobfish Rod | $2,000,000 | 500% | Special |

### Bait Types (15 Total)

| Bait | Cost | Rarity Boost | Notes |
|------|------|--------------|-------|
| Worm | Free | 0% | Starting bait |
| Bread | $50 | +5% | Basic upgrade |
| Cricket | $120 | +8% | Insect type |
| Corn | $180 | +10% | Versatile |
| Minnow | $250 | +12% | Live bait |
| Nightcrawler | $400 | +14% | Premium worm |
| Shrimp | $500 | +15% | Ocean bait |
| Cut Bait | $650 | +16% | Fresh chunks |
| Squid | $800 | +18% | Deep sea |
| Artificial Lure | $1,200 | +22% | Mimics prey |
| Live Bait | $1,500 | +25% | Real deal |
| Special Lure | $2,500 | +30% | Hand-crafted |
| Premium Lure | $4,000 | +35% | Professional |
| Exotic Bait | $6,500 | +40% | Rare ingredients |
| **Master Bait** | $50,000 | **+50%** | Ultimate |

### Rod Durability
- Rods start at 100% durability
- Lose 1-3% per catch
- Below 20% = warning message
- At 0% = breaks and reverts to Bamboo Rod
- Repair at shop: $5 per 1% restored

### Esky Capacity
- Starts at 50 fish
- Upgrade cost: Current Capacity × $10
- Each upgrade adds +10 capacity
- No maximum limit

## 🌳 Skill Tree System

### Available Skills

| Skill | Max Level | Effect per Level | Total Investment |
|-------|-----------|------------------|------------------|
| **Rare Finder** | 5 | +2% rare fish chance | +10% at max |
| **Quick Reflexes** | 5 | -5% minigame difficulty | -25% at max |
| **Master Angler** | 5 | +5% catch rate | +25% at max |
| **Lucky Fisherman** | 5 | +10% mutation chance | +50% at max |
| **Bargain Hunter** | 3 | +10% sell price | +30% at max |
| **Iron Grip** | 3 | +15% XP gain | +45% at max |

### Earning Skill Points
- 1 point per level up
- 2 points from Magical Encounter achievement
- 3 points from Leviathan Slayer achievement
- 3 points from Quest Master achievement
- 5 points from Billionaire achievement
- 10 points from Encyclopedia Master achievement

## 🎲 Quest System

### Quest Types
1. **Catch Species** - Catch a specific fish (Reward: $500)
2. **Catch Weight** - Catch a fish over X kg (Reward: $300)
3. **Catch Rarity** - Catch X fish of specific rarity (Reward: $800)

### Quest Features
- One active quest at a time
- Auto-generates new quest when completed
- Tracks progress automatically
- Completion awards shown immediately
- Counts toward Quest Master achievement

## 💾 Save System

### Save File Location
- **Windows:** `C:\Users\[YourName]\Documents\FiskeSpill\game_save.json`
- **macOS/Linux:** `~/Documents/FiskeSpill/game_save.json`

### What's Saved
- Character name, stats, difficulty
- Level, XP, and money
- Current equipment and owned items
- All fish in esky
- Encyclopedia progress
- Achievement status
- Skill points and skill levels
- Rod durability
- Time of day and weather
- Trophy room
- Active quests
- Quest completion count

### Save Tips
- Save frequently (option 11 in main menu)
- Game auto-saves on major milestones
- Backup save file before updates
- Save file is human-readable JSON

## 🔄 Updating the Game

### Windows (Automatic Installer)
1. Navigate to your game folder
2. Double-click `Update Game.bat`
3. Wait for download to complete
4. Your saves are preserved!

### Manual Update
```bash
# Backup your save first!
curl -O https://raw.githubusercontent.com/Nokoiscool/Fishing-game/main/fishgame.py
```

### Version History
- **v0.4.1** (Current) - Bug fixes, balance adjustments
- **v0.4.0** - Skill tree, quests, trophy room
- **v0.3.0** - Day/night cycle, rod durability
- **v0.2.0** - Achievement system, encyclopedia
- **v0.1.0** - Initial release

## 🎨 Easter Eggs & Hidden Fish

The game contains numerous references to popular video games:

### Gaming References
- **Minecraft** - Blockfish Creeper, Redstone Katten
- **Portal** - Portal Eel, Vault Carp
- **Dark Souls** - Abyss Watcher, Ashen Knight Carp, Hollow Pike
- **Halo** - Warp Stalker, Fallen Starfish
- **Half-Life** - Headcrab Eel, Lambda Salmon, Resonance Catfish
- **Zelda** - Hylian Pike
- **Mario** - Plumber's Tuna
- **Skyrim** - Nordic Dragon Salmon
- **Undertale** - Determined Eel, Mountain Spirit Trout
- **Terraria** - Corrupt Bass
- **And many more!**

### Ultra-Rare Discoveries
- **Blobfish** - 0.00001% chance in Deep Sea (requires Blobfish Rod!)
- **Magical Mutations** - 0.01% chance on any fish
- **Redstone Katten** - Mythical Space fish tribute

## 🐛 Known Issues

- None currently reported in v0.4.1

## 🗺️ Roadmap

### Planned Features
- [ ] Fishing tournaments with leaderboards
- [ ] Seasonal events with limited-time fish
- [ ] Crafting system for custom lures
- [ ] Pet companions that provide bonuses
- [ ] More locations (Swamp, Kelp Forest, Alien Ocean)
- [ ] Weather forecast system
- [ ] Fish breeding mechanics
- [ ] Multiplayer trading

### Under Consideration
- [ ] Mobile version
- [ ] GUI interface option
- [ ] Steam Workshop integration
- [ ] Mod support

## 🤝 Contributing

Contributions welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Ideas
- New fish species with real-world info
- Additional mini-game types
- Balance adjustments
- Bug fixes
- Achievement ideas
- Easter egg suggestions

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👏 Credits

- **Developer:** Nokoiscool
- **Engine:** Python 3.7+
- **Library:** colorama (terminal colors)
- **Inspired by:** Stardew Valley, Terraria fishing mechanics

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/Nokoiscool/Fishing-game/issues)
- **Updates:** Check GitHub for latest version
- **Community:** Share your catches and strategies!

---

## 📸 Sample Gameplay

```
╔══════════════════════════════════════╗
║    🎣 Angler's FISHING GAME 🎣       ║
╚══════════════════════════════════════╝
Level: 5 | XP: 150/500 | 💰: $2,450
Weather: Stormy
Difficulty: Normal
Rod: Carbon Rod | Bait: Squid
Esky: 23/50

You hooked a Megalodon!
Get ready... Wait for the signal!
>>> NOW! Press Enter!
Perfect! (0.243s)

Caught: Megalodon (Shadow) (Weight: 15234.56 kg, Rarity: Mythical, Size: Gigantic)
Sell value: $150,000
You gained 5000 XP! (+60% difficulty bonus)
🏆 Achievement Unlocked: First Mythical!
```

---

**Happy Fishing! 🎣**

*Remember: The biggest fish are always the ones that got away... unless you're using Master Bait!*