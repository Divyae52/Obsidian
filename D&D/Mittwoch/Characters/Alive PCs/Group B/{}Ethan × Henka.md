---
{}
---
	https://www.dndbeyond.com/characters/xxx

| Species    | Class                                                           | Alignment    | Experience Points |
| ---------- | --------------------------------------------------------------- | ------------ | ----------------- |
| Changeling | [[artificer\|Artificer]] [[artificer-artillerist\|Artillerist]] | True Neutral | Milestone (3)     |
## Appearance


[[breastplate|Breastplate]]
Cloth Pants
Boots
Looks like Ethan in cloak
## Characteristics
[[ability-scores-and-modifiers|Ability Scores and Modifiers]]

| STR     | DEX     | CON    | INT    | WIS    | CHA    |
| ------- | ------- | ------ | ------ | ------ | ------ |
| +2 (15) | +1 (12) | 0 (10) | 0 (10) | 0 (11) | -1 (8) |

### Derived Stats

| Derived Stat          | Value   |
| --------------------- | ------- |
| Hit Points            | 16 / 16 |
| Temp HP               | 0       |
| Hit Dice              | 3d8     |
| Proficiency Bonus     | 2       |
| Passive Perception    | 12      |
| Passive Stealth       | 11      |
| Passive Investigation | 12      |
| Passive Insight       | 12      |
| Speed                 | 30ft    |
| Amor Class (AC)       | 18      |
| Initiative            | +1      |

## Skills
[**P**] is Proficent

| Skill                         | Stat | Bonus | Total |
| ----------------------------- | ---- | ----- | ----- |
| Acrobatics (DEX)              | +1   | 0     |       |
| Animal Handling (WIS)         | 0    | 0     |       |
| Arcana (INT) [**P**]          | 0    |       |       |
| Athletics (STR)               | +2   | 0     |       |
| Deception (CHA)               | -1   | 0     |       |
| History (INT)                 | 0    | 0     |       |
| Insight (WIS) [**P**]         | 0    |       |       |
| Intimidation (CHA) [**P**]    | -1   |       |       |
| Investigation (INT) [**P**]   | 0    |       |       |
| Medicine (WIS)                | 0    | 0     |       |
| Nature (INT)                  | 0    | 0     |       |
| Perception (WIS) [**P**]      | 0    |       |       |
| Performance (CHA)             | -1   | 0     |       |
| Persuasion (CHA) [**P**]      | -1   |       |       |
| Religion (INT)                | 0    | 0     |       |
| Sleight of Hand (DEX) [**P**] | +1   |       |       |
| Stealth (DEX)                 | +1   | 0     |       |
| Survival (WIS)                | 0    | 0     |       |

## Saving Throws
[**P**]

| Save Type    | Stat | Bonus | Total |
| ------------ | ---- | ----- | ----- |
| Strength     |      |       |       |
| Dexterity    |      |       |       |
| Constitution |      |       |       |
| Intelligence |      |       |       |
| Wisdom       |      |       |       |
| Charisma     |      |       |       |

## Actions (NO Spells Needed (Optional))
[**P**]

| Name           | Hit / DC | Damage  | Type        | Other |
| -------------- | -------- | ------- | ----------- | ----- |
| Unarmed Strike | +4       | 1d8 + 2 | Bludgeoning |       |
|                |          |         |             |       |
|                |          |         |             |       |
|                |          |         |             |       |
|                |          |         |             |       |

## Equipment

| Copper | Silver | Electrum | Gold | Platinum |
| ------ | ------ | -------- | ---- | -------- |
| 0      | 0      | 0        | 0    | 0        |

* [[travelers-clothes|Traveler's Clothes]]
* [[breastplate|Breastplate]]

## Languages, Proficiencies, and Speed

* `Instruments`: None
* `Languages`: Common, 
* `Weapon Proficiencies`: Simple Weapons
* `Armor Proficencies`: XXX Armor / Shields
* `Tool Proficiencies`: None
* `Land Speed`: 30 feet

## Features

* 

## Spell Casting
(**U**) is Upcastable

| Cast Skill | Spell Save DC | Spell Modifier | Spell Attack |
| ---------- | ------------- | -------------- | ------------ |
|            |               |                |              |

### Cantrips

* [[guidance|Guidance]] - Touch a creature to grant them a **bonus d4 to one ability check** of their choice.

### First Level

* [ ] Spell Slot 1
* Spell

### Second Level

* [ ] Spell Slot 1
* Spell

## Background

*Insert traumatic experiences here*


D&D Beyond Puller: change char id
```dataviewjs
	const character_id = "char_id_here"

const headers = {}
const url = "https://character-service.dndbeyond.com/character/v5/character/" + character_id
const character_sheet_json = await requestUrl({url: url, headers})
const data = character_sheet_json.json.data
dv.paragraph(data)
```
