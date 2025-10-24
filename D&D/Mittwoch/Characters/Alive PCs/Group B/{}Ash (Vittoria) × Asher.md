---
{}
---
https://www.dndbeyond.com/characters/xxx

| Species                          | Class              | Alignment    | Experience Points |
| -------------------------------- | ------------------ | ------------ | ----------------- |
| [[goblin\|Goblin]] (Add Species) | [[ranger\|Ranger]] | True Neutral | Milestone (3)     |
## Appearance

Red eyes
4'
greyish green skin
Studded bracelets jewelry
sharp teeth
## Characteristics

| STR | DEX | CON | INT | WIS | CHA |
| --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |

### Derived Stats

| Derived Stat          | Value |
| --------------------- | ----- |
| Hit Points            | /     |
| Temp HP               | 0     |
| Hit Dice              | 3d    |
| Proficiency Bonus     | 2     |
| Passive Perception    |       |
| Passive Investigation |       |
| Passive Stealth       |       |
| Passive Insight       |       |
| Speed                 | 30ft  |
| Amor Class (AC)       |       |
| Initiative            |       |

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

| Name           | Hit / DC | Damage | Type        | Other |
| -------------- | -------- | ------ | ----------- | ----- |
| Unarmed Strike | +4       | 1+STR  | Bludgeoning |       |
|                |          |        |             |       |
|                |          |        |             |       |
|                |          |        |             |       |
|                |          |        |             |       |

## Equipment

| Copper | Silver | Electrum | Gold | Platinum |
| ------ | ------ | -------- | ---- | -------- |
| 0      | 0      | 0        | 0    | 0        |

* [[travelers-clothes|Traveler's Clothes]]

## Languages and Proficiencies

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
