# Fields
NAME = 'name'
NUMBER = 'number'
SET = 'set'
TYPE = 'type'
MEDICINE = 'medicine'
PLUS_DIG = 'plus-dig'
PLUS_HUNT = 'plus-hunt'
PLUS_FIGHT = 'plus-fight'
TEXT = 'text'

# Set values
BASE = 'base'
HQ_EXP = 'hq'
RECON_EXP = 'recon'

# Type values
JUNKYARD = 'junkyard'
CONTESTED_RESOURCE = 'contested-resource'


class Items:
    ALL_ITEMS = [
        {
            NAME: 'Junk',
            SET: BASE,
            NUMBER: 7,
            TYPE: JUNKYARD
        },
        {
            NAME: 'Pills',
            SET: BASE,
            NUMBER: 9,
            TYPE: JUNKYARD,
            MEDICINE: 1
        },
        {
            NAME: 'Medkit',
            SET: BASE,
            NUMBER: 6,
            TYPE: JUNKYARD,
            MEDICINE: 2
        },
        {
            NAME: 'Net',
            SET: BASE,
            NUMBER: 4,
            TYPE: JUNKYARD,
            PLUS_HUNT: 2,
            PLUS_FIGHT: 1
        },
        {
            NAME: 'Pickaxe',
            SET: BASE,
            NUMBER: 4,
            TYPE: JUNKYARD,
            PLUS_DIG: 1,
            PLUS_FIGHT: 2
        },
        {
            NAME: 'Multitool',
            SET: BASE,
            NUMBER: 4,
            TYPE: JUNKYARD,
            PLUS_DIG: 1,
            PLUS_HUNT: 1,
            PLUS_FIGHT: 1
        },
        {
            NAME: 'Shovel',
            SET: BASE,
            NUMBER: 6,
            TYPE: JUNKYARD,
            PLUS_DIG: 1,
            PLUS_FIGHT: 1
        },
        {
            NAME: 'Spear',
            SET: BASE,
            NUMBER: 6,
            TYPE: JUNKYARD,
            PLUS_HUNT: 1,
            PLUS_FIGHT: 2
        },
        {
            NAME: 'Grenade',
            SET: BASE,
            NUMBER: 2,
            TYPE: CONTESTED_RESOURCE,
            PLUS_FIGHT: 3
        },
        {
            NAME: 'Wolf Pack',
            SET: BASE,
            NUMBER: 2,
            TYPE: CONTESTED_RESOURCE,
            PLUS_HUNT: 3,
            PLUS_FIGHT: 2
        },
        {
            NAME: 'Rifle',
            SET: HQ_EXP,
            NUMBER: 4,
            TYPE: JUNKYARD,
            PLUS_HUNT: 2,
            PLUS_FIGHT: 2
        },
        {
            NAME: 'Toolkit',
            SET: HQ_EXP,
            NUMBER: 4,
            TYPE: JUNKYARD,
            PLUS_DIG: 2,
            TEXT: 'Increases a tribe member\'s build by +2 cards.'
        }
    ]
