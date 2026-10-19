Mebahel's Draugr Creatures - Configuration Guide
================================================

This file explains what each field in the configuration JSON files does.
All configs are located in this folder.


1) entity_health_config.json
--------------------------------
Controls the FINAL max health (HP) of each entity.
If a value is set to 0, the entity keeps its vanilla/default modded health.

  - draugrEntityHealth
    Max health for basic Draugr melee units.

  - draugrArcherEntityHealth
    Max health for Draugr Archers.

  - draugrWightEntityHealth
    Max health for Draugr Wights (elite melee + magic).

  - draugrScourgeEntityHealth
    Max health for Draugr Scourges (stronger spellcaster).

  - draugrOverlordEntityHealth
    Max health for the Draugr Overlord boss.

  - skeletonWarriorEntityHealth
    Max health for Skeleton Warriors.

  - flameAtronachEntityHealth
    Max health for Flame Atronachs.

  - infernalDraugrEntityHealth
    Max health for Infernal Draugrs.


2) entity_armor_config.json
--------------------------------
Controls the FINAL armor value of each entity.
Armor reduces incoming damage. Higher values = more tanky.
If a value is set to 0, the entity keeps its vanilla/default modded armor.

  - draugrEntityArmor
    Armor for basic Draugr melee units.

  - draugrArcherEntityArmor
    Armor for Draugr Archers.

  - draugrWightEntityArmor
    Armor for Draugr Wights.

  - draugrScourgeEntityArmor
    Armor for Draugr Scourges.

  - draugrOverlordEntityArmor
    Armor for the Draugr Overlord boss.

  - skeletonWarriorEntityArmor
    Armor for Skeleton Warriors.

  - flameAtronachEntityArmor
    Armor for Flame Atronachs.

  - infernalDraugrEntityArmor
    Armor for Infernal Draugrs.


3) entity_damage_config.json
--------------------------------
Controls damage values used by custom attacks.
These values do NOT automatically affect vanilla damage unless your code applies them.
Recommended range: 0 to 100.

  - draugrEntityMeleeDamage
    Melee damage for basic Draugr units.

  - draugrArcherEntityBonusArrowDamage
    Extra damage added on top of normal arrow damage for Draugr Archers.
    Example: 2.0 => arrow damage + 2.0.

  - draugrWightEntityMeleeDamage
    Melee damage for Draugr Wights.

  - draugrWightEntityFrostbiteDamage
    Bonus / special damage dealt by the Wight frostbite attack.

  - draugrScourgeEntityFrostbiteDamage
    Damage dealt by the Scourge frostbite magic.

  - draugrScourgeEntityIceSpikeDamage
    Damage dealt by the Scourge ice spike projectile.

  - draugrOverlordEntityMeleeDamage
    Melee damage for the Draugr Overlord.

  - draugrOverlordEntitySpinDamage
    Damage dealt by the Overlord spin attack.

  - draugrOverlordEntityGroundStrikeDamage
    Damage dealt by the Overlord ground strike / slam attack.

  - skeletonWarriorEntityMeleeDamage
    Melee damage for Skeleton Warriors.

  - flameAtronachEntityDamage
    Damage dealt by Flame Atronach attacks.

  - infernalDraugrEntityMeleeDamage
    Melee damage for Infernal Draugrs.

  - infernalDraugrEntityFireBoltDamage
    Damage dealt by the Infernal Draugr fire bolt projectile.


4) combat_balancing_config.json
--------------------------------------
Controls combat-related behaviours and probabilities for Draugr entities.

  - draugrMinBlockProbability (float, default 8.0)
    Minimum chance (in %) for a Draugr to decide to block after an attack
    when its health is relatively high.
    Example: 8.0 => at high HP, ~8% chance to block.

  - draugrMaxBlockProbability (float, default 16.0)
    Maximum chance (in %) for a Draugr to block when its HP is low.
    The actual block chance interpolates between min and max based on current HP.
    Higher values => more defensive behaviour at low HP.

  - draugrSpawnWithPotionProbability (float, default 5.0)
    Chance (in %) for a Draugr to spawn with a potion (heal/strength/resistance/etc.).
    Valid range: 0 < value <= 100 (outside this range => reset to 5).
    Example: 5.0 => roughly 1 Draugr out of 20 spawns with a potion.

  - draugrRaidScalingDifficulty (boolean, default true)
    If true, Draugr raids scale with difficulty / wave progression.
    Typically used to make later waves stronger (more mobs).
    true  => raids become harder as if a player as entered the nether in your world.
    false => raids stay at a flat difficulty.


5) spawn_rate_config.json
---------------------------------
Controls the relative rarity / spawn frequency of each custom mob.
All values must be between 0 and 10.
These are NOT direct percentages but weights used in spawn checks.
Higher value => more likely to spawn when conditions are met.

  - draugrSpawnRate (int, default 10)
    Spawn weight for basic Draugr melee mobs.
    0 => effectively never spawns.
    10 => maximum spawn frequency for this mob type.

  - draugrArcherSpawnRate (int, default 10)
    Spawn weight for Draugr Archers.

  - draugrWightSpawnRate (int, default 10)
    Spawn weight for Draugr Wights (stronger unit).

  - draugrScourgeSpawnRate (int, default 10)
    Spawn weight for Draugr Scourges (rare/elite unit).

  - skeletonWarriorSpawnRate (int, default 10)
    Spawn weight for Skeleton Warriors.

Notes on spawn rates:
  - All these values are combined with vanilla spawn conditions (light level, biome, etc.).
  - Setting a value to 0 is a simple way to completely disable a mob type.
  - Values > 10 are automatically reset to defaults when the config loads.

