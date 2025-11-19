---
{}
---
https://www.dndbeyond.com/characters/xxx
Merth - sigh - und - eer

| Species | Class          | Alignment    | Experience Points |
| ------- | -------------- | ------------ | ----------------- |
| [[Elf]] | [[bard\|Bard]] | True Neutral | Milestone (3)     |
## Appearance

![[Merdh Drawing A.png]]
![[Merdh Drawing B.png]]
Elf


## Characteristics
[[ability-scores-and-modifiers|Ability Scores and Modifiers]]

| STR     | DEX     | CON     | INT     | WIS     | CHA     |
| ------- | ------- | ------- | ------- | ------- | ------- |
| +1 (12) | +2 (15) | +1 (13) | +1 (12) | +2 (14) | +3 (17) |

### Derived Stats

| Derived Stat          | Value    |
| --------------------- | -------- |
| Hit Points            | 21 / 21  |
| Temp HP               | 0        |
| Hit Dice              | 3d8      |
| Proficiency Bonus     | 2        |
| Passive Perception    | 14       |
| Passive Stealth       | 12       |
| Passive Investigation | 11       |
| Passive Insight       | 14       |
| Speed                 | 30ft     |
| Amor Class (AC)       | 13 or 14 |
| Initiative            | +2       |

## Skills
[**P**] is Proficent

| Skill                         | Stat | Bonus | Total |
| ----------------------------- | ---- | ----- | ----- |
| Acrobatics (DEX) [**P**]      | +2   | +2    | +4    |
| Animal Handling (WIS)         | +2   | 0     | +2    |
| Arcana (INT)                  | +1   | 0     | +1    |
| Athletics (STR)               | +1   | 0     | +1    |
| Deception (CHA) [**P**]       | +3   | +2    | +5    |
| History (INT)                 | +1   | 0     | +1    |
| Insight (WIS) [**P**]         | +2   | +2    | +4    |
| Intimidation (CHA) [**P**]    | +3   | +2    | +5    |
| Investigation (INT)           | +1   | 0     | +1    |
| Medicine (WIS)                | +2   | 0     | +2    |
| Nature (INT)                  | +1   | 0     | +1    |
| Perception (WIS) [**P**]      | +2   | +2    | +4    |
| Performance (CHA) [**P**]     | +3   | +2    | +5    |
| Persuasion (CHA) [**P**]      | +3   | +2    | +5    |
| Religion (INT)                | +1   | 0     | +1    |
| Sleight of Hand (DEX) [**P**] | +2   | +2    | +4    |
| Stealth (DEX)                 | +2   | 0     | +2    |
| Survival (WIS)                | +2   | 0     | +2    |

## Saving Throws
[**P**]

| Save Type         | Stat | Bonus | Total |
| ----------------- | ---- | ----- | ----- |
| Strength          | +1   | 0     | +1    |
| Dexterity [**P**] | +2   | +2    | +4    |
| Constitution      | +1   | 0     | +1    |
| Intelligence      | +1   | 0     | +1    |
| Wisdom            | +2   | 0     | +2    |
| Charisma [**P**]  | +3   | +2    | +5    |

## Actions (NO Spells Needed (Optional))
[**P**]

| Name                             | Hit / DC | Damage | Type        | Other        |
| -------------------------------- | -------- | ------ | ----------- | ------------ |
| Unarmed Strike                   | +3       | 2      | Bludgeoning |              |
| [[shortsword\|Shortsword]]       | +0       | 1d6    | Piercing    |              |
| [[hand-crossbow\|Hand Crossbow]] | +0       | 1d6    | Piercing    | Range 30/120 |
|                                  |          |        |             |              |
|                                  |          |        |             |              |

## Equipment

| Copper | Silver | Electrum | Gold | Platinum |
| ------ | ------ | -------- | ---- | -------- |
| 0      | 0      | 0        | 0    | 0        |

* [[travelers-clothes|Traveler's Clothes]]
* [[Lute]]
* [[Flute]]
* [[shortsword|Shortsword]]
* [[hand-crossbow|Hand Crossbow]]
* [[leather-armor|Leather Armor]] (13) or [[padded-armor|Padded Armor]] (13) or [[studded-leather-armor|Studded Leather Armor]] (14)

## Languages, Proficiencies, and Speed

* `Instruments`: None
* `Languages`: Common, Elvish
* `Weapon Proficiencies`: Simple Weapons
* `Armor Proficencies`: Light Armor
* `Tool Proficiencies`: One Simple Instrument of your choice
* `Land Speed`: 30 feet

## Features

* Fey Ancestry
	* You have advantage on saving throws against being [charmed](rules/conditions.md#charmed), and magic can't put you to sleep.
* Trance
	* Elves don't need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. (The Common word for such meditation is "trance.") While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep.


## Spell Casting
(**U**) is Upcastable

| Cast Skill | Spell Save DC | Spell Modifier | Spell Attack |
| ---------- | ------------- | -------------- | ------------ |
| CHA        | 13            | +5             |              |

### Cantrips

* [[Lay on Hands]]

### Third Level

* [ ] 
* [[Oath of Conquest]]

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
