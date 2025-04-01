Welcome to Fishing For Bass! A turn based strategy game similar to Risk that has literally nothing to do with fishing, or bass...

**How to Use:**
To run Fishing For Bass, the host of your game first runs server.py (located within the src folder). Once running, this file will query how many players are in this game and create a server to run upon. Once complete, each player
runs fishinferbass.py (also located within the src folder). This will automatically create a client and once all players connect, beginning the game.

**How To Win:**
The world is divided into 42 territories spread amongst 6 continents. Each territory grants resources to feul your armies. Grow your army and take control of all 42 territories to win!

**How to Play:**

**Territories & Resources:**
In Fishing For Bass, there are four major resources you can acrue. Food, Wood, Metal, and Oil. These resources can be used to purchase units and conquer your opponents. Resources are gained from territories you own each turn, and can be
spent on units. Your resource totals are displayed in the top right just under your name and turn number. Feel free also to hover over a territory to see how many of each resource it yields per turn. You should see these stats in the
bottom right below its name. Similarly, if you hover over a player box (top left of the screen, color coordinated per player), a players total resources per turn, as well as their total power should appear in the same location. Each
turn, you may spend resources to place units on territories you own. Naval units can only be placed on coasts of territories and coasts you own. More on these later.

The more territories you control, the more resources per turn you acrue, the more powerful (or plentiful) the units you can afford. To control a territory, simply have units there. Only one player can own a territory.

**Units:**
In Fishing For Bass, there are 20 unique units. Each unit has a unique resource coast. Units make up your army and have two essential stats. Power (Star) and Movement (Arrow). One movement is spent to move from a territory to an adjacent one.
That is to say, one that shares a land border. Each unit can move an amount of times each turn equal to their movement. If the unit moves into an opposing players territory, it is considered an attack. When this occurs, the unit will trade its power
with the units within the opponents territory until it dies, or all units in the territory do. Units of a territory defend in order of the most recently moved/placed there. So the longest standing units in a territory defend last. A unit is
destroyed if its power is reduced to 0. To view a units statistics, hover over the item in the shop on the right hand panel of the screen.

Examples:
- A 10 power unit attacks a 2 power territory -> The 10 power unit will be reduced to 8 power, but will defeat all units in the defending territory, claiming the territory for the attacking player with an 8 power unit there.
- A 3 power unit attacks a 5 power territoy (a 2 power unit and 3 power unit, where the 2 power was placed more recently) -> The 3 power unit is reduced to 1 after defeating the 2 power unit, and hen defeated itself by the 3 power defending
  unit, reducing its power (and the territories total power) to 2.
- A 1 power unit attacks a 1 power territory (another 1 power unit) -> Both units die, and the defending territory is left unclaimed.

**Defender:**
Units with defender (Denoted by a shield) often have very high power, but cannot use the attack action and have priority to defend your territories. Use these units to keep your territories safe!

**Naval:**
These units do not operate on land, but rather on the coast of each territory. Movement can be used to go to adjacent coasts (territories that share adjacent water) or across the pinned lines on map. Only one player can occupy a given coast, but
not necassarily the player who ones the territory associated with it. Naval units trade power much like land ones do, although they cannot directly attack land.

**Capacity:**
Typically a stat bound to Naval units, a unit with capacity can board and carry land units so long as the total power does not exceed the units capacity (Denoted by a plus symbol) and they are on the same territory as the coast the unit with
capacity is on. It takes the land unit 1 movement to embark a unit with capacity, but it will move with the unit once embarked. Units can also use one movement to disembark the unit boarded from the coast, potentially as an attack towards the territory
being disembarked onto, if it is owned by another player. If a unit with capacity is destroyed, all units currently embarked are destroyed as well.

**Arial & Range:**
These units operate in the air. Rather than attacking in standard fashion, they perform ariel strikes. Ariel strikes only diminish ONLY the power of the defending territories units, but do not cause the ariel unit to move into the territory formally. Ariel units
can also attack coasts if they are in range. A territory (or coast) is in range if a land or naval unit could move there with movement equal to the Ariel units range category (Denoted by a target).

**Special Abilities:**
Some units have special abilities unique to themselves.

Anti-Air Gun:
Defensive special unit. Anti-Air Guns, unlike other units, trade power with ariel units during ariel attacks. They have the lowest priority amongst to defend territories, but the highest priority for defending ariel attacks.

Aircraft Carrier:
Naval special unit. Aircraft Carriers, unlike other units with capacity, can hold Ariel units. Ariel units can also make ariel attacks from Carriers as they would a territory.

Helicopter:
Ariel special unit. Helicopters are the only non-Naval unit with a capacity. Units the embark are automatically disembarked attacking during ariel strikes against territories.

**Start of Game:**
Each player receives one Warrior (the simplest land unit) and chooses their starting territory.

**Gameplay:**
At the start of your turn, acrue resources from each territory you own and units you own regain movement. On your turn, you may choose to buy any amount of units you can afford, and each unit you own may make moves or attacks until their movement is spent.

Turn order is first come first serve, so act fast and good luck!
