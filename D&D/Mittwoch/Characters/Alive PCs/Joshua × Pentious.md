https://www.dndbeyond.com/characters/xxx

| Species              | Class                | Alignment    | Experience Points |
| -------------------- | -------------------- | ------------ | ----------------- |
| [[yuan-ti\|Yuan-ti]] | [[fighter\|Fighter]] | True Neutral | Milestone (3)     |
## Appearance

Lower body is snake tail
Humanoid upper body
[[breastplate|Breastplate]]
Standing 5'11"
Holding spear, has javelin

## Characteristics
[[ability-scores-and-modifiers|Ability Scores and Modifiers]]

| STR     | DEX     | CON    | INT    | WIS     | CHA    |
| ------- | ------- | ------ | ------ | ------- | ------ |
| +3 (16) | +2 (15) | 0 (10) | -2 (7) | +1 (13) | -1 (9) |

### Derived Stats

| Derived Stat          | Value   |
| --------------------- | ------- |
| Hit Points            | 22 / 22 |
| Temp HP               | 0       |
| Hit Dice              | 3d10    |
| Proficiency Bonus     | 2       |
| Passive Perception    | 13      |
| Passive Stealth       | 12      |
| Passive Investigation | 8       |
| Passive Insight       | 11      |
| Speed                 | 30ft    |
| Amor Class (AC)       | 16      |
| Initiative            | +2      |

## Skills
[**P**] is Proficent

| Skill                    | Stat | Bonus | Total |
| ------------------------ | ---- | ----- | ----- |
| Acrobatics (DEX)         | +2   | 0     | +2    |
| Animal Handling (WIS)    | +1   | 0     | +1    |
| Arcana (INT)             | -2   | 0     | -2    |
| Athletics (STR) [**P**]  | +3   | +2    | +5    |
| Deception (CHA)          | -1   | 0     | -1    |
| History (INT)            | -2   | 0     | -2    |
| Insight (WIS)            | +1   | 0     | +1    |
| Intimidation (CHA)       | -1   | 0     | -1    |
| Investigation (INT)      | -2   | 0     | -2    |
| Medicine (WIS)           | +1   | 0     | +1    |
| Nature (INT)             | -2   | 0     | -2    |
| Perception (WIS) [**P**] | +1   | +2    | +3    |
| Performance (CHA)        | -1   | 0     | -1    |
| Persuasion (CHA)         | -1   | 0     | -1    |
| Religion (INT)           | -2   | 0     | -2    |
| Sleight of Hand (DEX)    | +2   | 0     | +2    |
| Stealth (DEX)            | +2   | 0     | +2    |
| Survival (WIS)           | +1   | 0     | +1    |

## Saving Throws
[**P**]

| Save Type    | Stat | Bonus | Total |
| ------------ | ---- | ----- | ----- |
| Strength     | +3   | +2    | +5    |
| Dexterity    | +2   | 0     | +2    |
| Constitution | 0    | +2    | +2    |
| Intelligence | -2   | 0     | -2    |
| Wisdom       | +1   | 0     | +1    |
| Charisma     | -1   | 0     | -1    |

## Actions (NO Spells Needed (Optional))
[**P**]

| Name                 | Hit / DC | Damage    | Type        | Other |
| -------------------- | -------- | --------- | ----------- | ----- |
| Unarmed Strike       | +5       | 4         | Bludgeoning |       |
| [[spear\|Spear]]     | +2       | 1d6 / 1d8 | Piercing    |       |
| [[javelin\|Javelin]] | +2       | 1d6       | Piercing    |       |
|                      |          |           |             |       |
|                      |          |           |             |       |

## Equipment

| Copper | Silver | Electrum | Gold | Platinum |
| ------ | ------ | -------- | ---- | -------- |
| 0      | 0      | 0        | 0    | 0        |

* [[travelers-clothes|Traveler's Clothes]]
* [[breastplate|Breastplate]]
* [[spear|Spear]]
* [[javelin|Javelin]]

## Languages, Proficiencies, and Speed

* `Instruments`: None
* `Languages`: Common, 
* `Weapon Proficiencies`: Simple Weapons, Martial Weapons
* `Armor Proficencies`: Light Armor, Medium Armor, Heavy Armor, Shields
* `Tool Proficiencies`: None
* `Land Speed`: 30 feet

## Features

* 

## Spell Casting
N/A

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
