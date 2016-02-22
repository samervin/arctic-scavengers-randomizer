# Fields
NAME = 'name'
SET = 'set'
NUMBER = 'number'
BUILD_TIME = 'build-time'
HOLD_TYPE = 'hold-type'
HOLD_QUANTITY = 'hold-quantity'
ABILITY = 'ability'
TEXT = 'text'

# Set values
HQ_EXP = 'hq'
RECON_EXP = 'recon'

# Ability values
RECON = 'recon'


class Buildings:
    ALL_BUILDINGS = [
        {
            NAME: 'Pharmacy',
            SET: HQ_EXP,
            NUMBER: 3,
            BUILD_TIME: 2,
            HOLD_TYPE: 'medicine',
            HOLD_QUANTITY: 2,
            TEXT: 'Allows medicine cards to be stored and then retrieved prior to the skirmish.'
        },
        {
            NAME: 'Hydroponic Garden',
            SET: HQ_EXP,
            NUMBER: 3,
            BUILD_TIME: 4,
            TEXT: 'Generates 1 food each round to assist with hiring mercenaries. Food does not accumulate.'
        },
        {
            NAME: 'Armory',
            SET: HQ_EXP,
            NUMBER: 3,
            BUILD_TIME: 3,
            HOLD_TYPE: 'tool',
            HOLD_QUANTITY: 2,
            TEXT: 'Allows tool cards to be stored and then retrieved prior to the skirmish.'
        },
        {
            NAME: 'Bunker',
            SET: HQ_EXP,
            NUMBER: 3,
            BUILD_TIME: 5,
            HOLD_TYPE: 'tribe-members',
            HOLD_QUANTITY: 3,
            TEXT: 'Allows tribe members to be stored and then retrieved prior to the skirmish.'
        },
        {
            NAME: 'Portable Decoys',
            SET: RECON_EXP,
            NUMBER: 3,
            BUILD_TIME: 2,
            TEXT: 'Treat your skirmish force as being larger by 1 for every 2 cards you bring to the skirmish (round down).'
        },
        {
            NAME: 'Scout Tower',
            SET: RECON_EXP,
            NUMBER: 3,
            BUILD_TIME: 3,
            ABILITY: RECON,
            TEXT: 'Discard 1 card from hand to activate. '
                  'Peek at top 2 cards from any 2 piles in play.'
        }
    ]
