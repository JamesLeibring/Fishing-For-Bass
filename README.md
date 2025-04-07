# Fishing For Bass

A risk-like strategy game played with 3-6 friends!

## Description

### Basics

In Fishing For Bass, there are four core resources. Food, Wood, Metal, and Oil. These resources are acrued by your territories and spent to grow your armies. During your turn, move each unit to attack or defend territories as you choose. If you own every territory, you win! Some units occupy the seas or the skies of your territories, but if you run out of boots on the ground, you lose.

To learn more about each territory, unit, or player, hover over them on the map or in the shop (player boxes are color coded at the top left of the map) and check the info box on the bottom right of your screen! You should see a variety of stats like who claims ownership, yields/cost, or total power.

### Gameplay

To start the game, each player receives one free Warrior (the simplest unit) in their chosen starting territory. Turn order is first come first serve, so act fast and good luck!

At the start of your turn, territories you own will acrue resources. Buy and move units as you please, but be careful, moving units into enemy territory is an attack that will trade power until the unit dies or the territory is left undefended. Each unit you own may make moves or attacks until their movement is spent. Its worth noting that a territories coast can be occupied by
a different player than on the territory itself. Dominating the seas is a great way to take control of many of the less land-locked territories and control the flow of your opponents armies.

### Units

In Fishing For Bass, there are 20 unique units, each available for purchase in the shop (midright of the screen) for a unique resource coast. Units make up your army and have two essential stats. Power (Star) and Movement (Arrow). One movement is spent to move from a territory to an adjacent one. That is to say, one that shares a border. Each unit can move an amount of times each turn equal to their movement. If the unit moves into an opposing players territory, it is considered an attack. When this occurs, the unit will trade its power with the units in the opponents territory until it dies, or all units in the territory do. Power reduction is permanent, and a unit is destroyed if its power is reduced to 0. See the following example below...

- A 10 power unit attacks a 2 power territory containing a single 2 power unit -> The 10 power unit will be reduced to 8 power, but will defeat all units in the defending territory, claiming the territory for the attacking player with an 8 power unit moving there.
- A 3 power unit attacks a 5 power territoy containing a 1 power unit and 4 power unit -> The 3 power unit is reduced to 2 power after defeating the 1 power unit defending. Next, the now 2 power unit is defeated by the 4 power unit defending, reducing the defending units power (and the territories total power) to 2. It remains under control of the defending player.
- A 1 power unit attacks a 1 power territory containing a 1 power unit -> Both units die, and the defending territory is left unclaimed.

**Defender:** Units with defender (Shield) often have very high power, but cannot use the attack action and have priority to defend your territories. Use these units to keep your territories safe!

**Naval:** Naval units (Anchor) do not operate on land, but rather on the coast of each territory. Movement is used to go to adjacent coasts (territories that share a border over water water) or across the pinned lines on map. A player can only place Naval units on the coast of a territory they own not containing enemy Naval units. Naval units trade power much like land units, although they attack the coasts of territories rather than the territory itself.

**Capacity:** Typically a stat bound to Naval units, a unit with capacity (Plus) can board and carry land units so long as the total power does not exceed the units capacity. It takes the embarking unit 1 movement to board a unit with capacity, but it will move with the boarding unit free of charge once embarked. Units can also use one movement to disembark the unit boarded from the coast, potentially as an attack towards the territory disembarked onto, if it is owned by another player. If a unit with capacity is destroyed, all units currently embarked are destroyed as well.

**Aerial & Range:** Aerial Units (Plane) operate in the air. Rather than attacking in standard fashion, they perform aeriel strikes, which diminish ONLY the power of the defending territories units, not itself. Aeriel units can perform an aerial attack against any territory or coast within range (Bullseye). A territory or coast is in range if a land or naval unit could move there with movement equal to the aeriel units range category, ignoring attacking and land ownership rules.

**Special Abilities:** The following units have unique special abilities.
* **Anti-Air Gun:** Defensive special unit. Anti-Air Guns, unlike other units, trade power with aeriel units during aeriel attacks.
* **Aircraft Carrier:** Naval special unit. Aircraft Carriers, unlike other units with capacity, can hold aeriel units. Aeriel units can make aeriel attacks from Carriers as they would a territory.
* **Helicopter:** Ariel special unit. Helicopters are the only non-Naval unit with a capacity. Units that embark are automatically disembarked without spending movement during aeriel strikes against territories.

## Getting Started

### Dependencies

* Python 3.12
* Pygame 2.5.2

### Installing

* Clone the repository onto your machine and ensure pygame is installed by running the command below.
```
pip3 install pygame
```

### Executing program

* Navigate to the 'Fishing-For-Bass' folder and run the command below.
* Enter if you are the host machine. The host should run their game before other players.  
  * If you are hosting, a server should start automatically after querying player count.
* Enter your name. You should connect to the server automatically once complete.
* Once all players have connected, the game begins! Look for a pygame window.
```
python .\src\fishinferbass.py
```

## Acknowledgments

Created and Developed by James Leibring with inspiration from a board game created by Matthew Pusateri and Alan Lingle.