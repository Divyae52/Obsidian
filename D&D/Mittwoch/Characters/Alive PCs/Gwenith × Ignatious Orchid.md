https://www.dndbeyond.com/characters/xxx

| Species                                 | Class                | Alignment    | Experience Points |
| --------------------------------------- | -------------------- | ------------ | ----------------- |
| [[centaur\|Centaur]] (Add Species Ver.) | [[paladin\|Paladin]] | True Neutral | Milestone (3)     |
## Appearance

Wearing a Helmet emitting fire
Wearing [[plate-armor|Plate Armor]] w/ orange highlights, fiery motif
![[Gwenith Drawing.png]]
## Characteristics
[[ability-scores-and-modifiers|Ability Scores and Modifiers]]

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
| Passive Stealth       |       |
| Passive Investigation |       |
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
* [[plate-armor|Plate Armor]]

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
