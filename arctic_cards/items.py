# Fields
NAME = 'name'
NUMBER = 'number'
SET = 'set'
TYPE = 'type'
IS_INSTANT = 'is-instant'
MEDICINE = 'medicine'
PLUS_DIG = 'plus-dig'
PLUS_HUNT = 'plus-hunt'
PLUS_FIGHT = 'plus-fight'
ABILITY = 'ability'
TEXT = 'text'

# Set values
BASE = 'base'
HQ_EXP = 'hq'
RECON_EXP = 'recon'

# Type values
JUNKYARD = 'junkyard'
CONTESTED_RESOURCE = 'contested-resource'

# Ability values
RECON = 'recon'


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
        },
        {
            NAME: 'Map',
            SET: RECON_EXP,
            NUMBER: 4,
            TYPE: JUNKYARD,
            IS_INSTANT: True,
            TEXT: 'Return 1 tribe member to your hand after performing a non-skirmish action.'
        },
        {
            NAME: 'Binoculars',
            SET: RECON_EXP,
            NUMBER: 4,
            TYPE: JUNKYARD,
            IS_INSTANT: True,
            ABILITY: RECON,
            TEXT: 'May peek at the top card from all piles in play, OR, recon +2'
        },
        {
            NAME: 'Cargo Sled',
            SET: RECON_EXP,
            NUMBER: 2,
            TYPE: CONTESTED_RESOURCE,
            PLUS_DIG: 2,
            PLUS_HUNT: 2,
            TEXT: 'When digging in the Junkyard, you may keep 1 additional tool or medicine.'
        },
        {
            NAME: 'Tear Gas',
            SET: RECON_EXP,
            NUMBER: 2,
            TYPE: CONTESTED_RESOURCE,
            IS_INSTANT: True,
            TEXT: 'Select 1 opponent tribe member and reduce its fight (or bonus to fight) to 0.'
        }
    ]
