# Fields
NAME = 'name'
NUMBER = 'number'
TYPE = 'type'
MEDICINE = 'medicine'
PLUS_DIG = 'plus-dig'
PLUS_HUNT = 'plus-hunt'
PLUS_FIGHT = 'plus-fight'

# Values for selected fields
JUNKYARD = 'junkyard'
CONTESTED_RESOURCE = 'contested-resource'


class Items:
    ALL_ITEMS = [
        {
            NAME: 'Junk',
            NUMBER: 7,
            TYPE: JUNKYARD
        },
        {
            NAME: 'Pills',
            NUMBER: 9,
            TYPE: JUNKYARD,
            MEDICINE: 1
        },
        {
            NAME: 'Medkit',
            NUMBER: 6,
            TYPE: JUNKYARD,
            MEDICINE: 2
        },
        {
            NAME: 'Net',
            NUMBER: 4,
            TYPE: JUNKYARD,
            PLUS_HUNT: 2,
            PLUS_FIGHT: 1
        },
        {
            NAME: 'Pickaxe',
            NUMBER: 4,
            TYPE: JUNKYARD,
            PLUS_DIG: 1,
            PLUS_FIGHT: 2
        },
        {
            NAME: 'Multitool',
            NUMBER: 4,
            TYPE: JUNKYARD,
            PLUS_DIG: 1,
            PLUS_HUNT: 1,
            PLUS_FIGHT: 1
        },
        {
            NAME: 'Shovel',
            NUMBER: 6,
            TYPE: JUNKYARD,
            PLUS_DIG: 1,
            PLUS_FIGHT: 1
        },
        {
            NAME: 'Spear',
            NUMBER: 6,
            TYPE: JUNKYARD,
            PLUS_HUNT: 1,
            PLUS_FIGHT: 2
        },
        {
            NAME: 'Grenade',
            NUMBER: 2,
            TYPE: CONTESTED_RESOURCE,
            PLUS_FIGHT: 3
        },
        {
            NAME: 'Wolf Pack',
            NUMBER: 2,
            TYPE: CONTESTED_RESOURCE,
            PLUS_HUNT: 3,
            PLUS_FIGHT: 2
        }
    ]
