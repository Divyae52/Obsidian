---
{}
---
https://www.dndbeyond.com/characters/xxx

| Species                    | Class                                            | Alignment    | Experience Points |
| -------------------------- | ------------------------------------------------ | ------------ | ----------------- |
| [[dragonborn\|Dragonborn]] | [[Cleric]] [[cleric-death-domain\|Death Domain]] | True Neutral | Milestone (3)     |
## Appearance


## Characteristics
[[ability-scores-and-modifiers|Ability Scores and Modifiers]]

| STR     | DEX    | CON     | INT    | WIS     | CHA     |
| ------- | ------ | ------- | ------ | ------- | ------- |
| +2 (14) | 0 (11) | +4 (18) | 0 (11) | +4 (19) | +1 (12) |

### Derived Stats

| Derived Stat          | Value   |
| --------------------- | ------- |
| Hit Points            | 30 / 30 |
| Temp HP               | 0       |
| Hit Dice              | 3d8     |
| Proficiency Bonus     | 2       |
| Passive Perception    | 14      |
| Passive Stealth       | 10      |
| Passive Investigation | 10      |
| Passive Insight       | 16      |
| Speed                 | 30ft    |
| Amor Class (AC)       |         |
| Initiative            |         |

## Skills
[**P**] is Proficent

| Skill                 | Stat | Bonus | Total |
| --------------------- | ---- | ----- | ----- |
| Acrobatics (DEX)      |      |       |       |
| Animal Handling (WIS) |      |       |       |
| Arcana (INT)          |      |       |       |
| Athletics (STR)       |      |       |       |
| Deception (CHA)       |      |       |       |
| History (INT)         |      |       |       |
| Insight (WIS)         |      |       |       |
| Intimidation (CHA)    |      |       |       |
| Investigation (INT)   |      |       |       |
| Medicine (WIS)        |      |       |       |
| Nature (INT)          |      |       |       |
| Perception (WIS)      |      |       |       |
| Performance (CHA)     |      |       |       |
| Persuasion (CHA)      |      |       |       |
| Religion (INT)        |      |       |       |
| Sleight of Hand (DEX) |      |       |       |
| Stealth (DEX)         |      |       |       |
| Survival (WIS)        |      |       |       |

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
