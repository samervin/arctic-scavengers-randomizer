# Fields
NAME = 'name'
NUMBER = 'number'
TYPE = 'type'
FOOD_COST = 'food-cost'
MED_COST = 'med-cost'
VARIABLE_COST = 'variable-cost'
DRAW = 'draw'
DIG = 'dig'
HUNT = 'hunt'
FIGHT = 'fight'
MEDICINE = 'medicine'
TRIBE_MEMBERS = 'tribe-members'
PLUS_DRAW = 'plus-draw'
PLUS_DIG = 'plus-dig'
PLUS_HUNT = 'plus-hunt'
PLUS_FIGHT = 'plus-fight'
IS_REFUGEE = 'is-refugee'

# Abilities -- forthcoming

# Values
FOR_HIRE = "for-hire"
CONTESTED = "contested-resource"


class Mercenaries:
    ALL_MERCENARIES = [
        {
            NAME: "Refugee",
            NUMBER: 20,
            TYPE: FOR_HIRE,
            FOOD_COST: 0,
            DIG: 0,
            HUNT: 0,
            TRIBE_MEMBERS: 1,
            IS_REFUGEE: True
        },
        {
            NAME: "Scavenger",
            NUMBER: 20,
            TYPE: FOR_HIRE,
            FOOD_COST: 1,
            DRAW: 1,
            DIG: 1,
            HUNT: 1,
            FIGHT: 1,
            TRIBE_MEMBERS: 1,
        },
        {
            NAME: "Brawler",
            NUMBER: 10,
            TYPE: FOR_HIRE,
            FOOD_COST: 2,
            DIG: 1,
            FIGHT: 2,
            TRIBE_MEMBERS: 1,
        },
        {
            NAME: "Hunter",
            NUMBER: 8,
            TYPE: FOR_HIRE,
            MED_COST: 1,
            HUNT: 2,
            FIGHT: 1,
            TRIBE_MEMBERS: 1
        }
    ]
