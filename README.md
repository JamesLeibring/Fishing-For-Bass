# Fishing For Bass
**Note:** This game is still a work in progress and is not fully functional. Features are being developed and tested.

A risk-like strategy game for 3-6 players!

## Description

### Basics

In *Fishing For Bass*, there are four core resources: Food, Wood, Metal, and Oil. These resources are accrued by your territories and spent to grow your armies. During your turn, move each unit to attack or defend territories as you choose. If you own every territory, you win! Some units occupy the seas or the skies of your territories, but if you run out of boots on the ground, you lose.

To learn more about each territory, unit, or player, hover over them on the map or in the shop (player boxes are color-coded at the top left of the map) and check the info box at the bottom right of your screen! You should see a variety of stats, including who claims ownership, yields/costs, or total power.

### Gameplay

To start the game, each player receives one free Warrior (the simplest unit) in their chosen starting territory. Turn order is first come, first serve, so act fast and good luck!

At the start of your turn, territories you own will accrue resources. Buy and move units as you please, but be careful—moving units into enemy territory is an attack that will trade power until the unit dies or the territory is left undefended. Each unit can make moves or attacks until their movement is spent.

It's worth noting that a territory's coast can be occupied by a different player than the territory itself. Dominating the seas is a great way to take control of many of the less landlocked territories and influence the flow of your opponent's armies.

### Units

In Fishing For Bass, there are 20 unique units, each available for purchase in the shop (located mid-right of the screen) for a unique resource cost. Units make up your army and have two essential stats: Power (Star) and Movement (Arrow). One movement is spent to move from a territory to an adjacent one—meaning one that shares a border.

Each unit can move an amount of times each turn equal to their movement stat. If a unit moves into an opposing player's territory, it is considered an attack. When this occurs, the unit will trade its power with the units in the opponent's territory until it dies or all units in the territory are defeated. Power reduction is permanent, and a unit is destroyed if its power is reduced to 0. See the following examples:

- A 10-power unit attacks a 2-power territory containing a single 2-power unit → The 10-power unit will be reduced to 8 power but will defeat all units in the defending territory, claiming the territory for the attacking player with an 8-power unit moving there.

- A 3-power unit attacks a 5-power territory containing a 1-power unit and a 4-power unit → The 3-power unit is reduced to 2 power after defeating the 1-power unit. The now 2-power unit is then defeated by the 4-power unit, reducing the defending unit's power (and the territory’s total power) to 2. The territory remains under the control of the defending player.

- A 1-power unit attacks a 1-power territory containing a 1-power unit → Both units die, and the defending territory is left unclaimed.

**Defender:** Units with the defender (Shield) keyword often have very high power but cannot use the attack action. They have priority to defend your territories. Use these units to keep your territories safe!

**Naval:** Naval units (Anchor) do not operate on land but rather on the coast of each territory. Movement is used to go to adjacent coasts (territories that share a border over water) or across the pinned lines on the map. A player can only place Naval units on the coast of a territory they own that does not contain enemy Naval units. Naval units trade power much like land units, although they attack the coasts of territories rather than the territory itself.

**Capacity:** Typically a stat bound to Naval units, a unit with capacity (Plus) can board and carry land units, so long as the total power does not exceed the unit’s capacity. It takes one movement to embark a unit with capacity, but it will move with the boarding unit free of charge once embarked. Units can also use one movement to disembark the unit boarded from the coast, potentially as an attack towards the territory disembarked onto, if it is owned by another player. If a unit with capacity is destroyed, all units currently embarked are also destroyed.

**Aerial & Range:** Aerial Units (Plane) operate in the air. Rather than attacking in the standard fashion, they perform aerial strikes, which only diminish the power of the defending territory's units, not the aerial unit itself. Aerial units can perform an aerial attack against any territory or coast within range (Bullseye). A territory or coast is in range if a land or naval unit could move there with movement equal to the aerial unit's range category, ignoring attacking and land ownership rules.

**Special Abilities:** The following units have unique special abilities.
* **Anti-Air Gun:** Defensive special unit. Anti-Air Guns, unlike other units, trade power with aerial units during aerial attacks.
* **Aircraft Carrier:** Naval special unit. Aircraft Carriers, unlike other units with capacity, can hold aerial units. Aerial units can make aerial attacks from Carriers as they would from a territory.
* **Helicopter:** Aerial special unit. Helicopters are the only non-Naval unit with capacity. Units that embark are automatically disembarked without spending movement during aerial strikes against territories.

## Getting Started

### Dependencies

* Python 3.12
* Pygame 2.5.2

### Installing

* Clone the repository onto your machine and ensure Pygame is installed by running the command below:
```
pip3 install pygame
```

### Running the Rrogram

1. Navigate to the `Fishing-For-Bass` folder and run the command below.
2. If you're the host, run the game first.
3. The host should start a server automatically after querying player count.
4. Enter your name, and you should connect to the server automatically once complete.
5. Once all players have connected, the game begins! Look for the Pygame window.
```
python .\src\fishinferbass.py
```

## Acknowledgments

Created and Developed by James Leibring with inspiration from a board game created by Matthew Pusateri and Alan Lingle.