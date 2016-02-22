# Fields
NAME = 'name'
NUMBER = 'number'
SET = 'set'
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
ABILITY = 'ability'
TEXT = 'text'

# Set values
BASE = 'base'
HQ_EXP = 'hq'
RECON_EXP = 'recon'

# Card type values
FOR_HIRE = 'for-hire'
CONTESTED_RESOURCE = 'contested-resource'

# Abilities
DISARM = 'disarm'
SNIPE = 'snipe'
SAVE = 'save'
BUILD = 'build'
BUILD_RELATED = 'build-related'
CANCEL = 'cancel'
CANCEL_RECON = 'cancel-recon'
DRAW_RELATED = 'draw-related'
RECON = 'recon'

# Information not strictly contained on the card
COMMENT = 'comment'


class Mercenaries:
    ALL_MERCENARIES = [
        {
            NAME: 'Refugee',
            SET: BASE,
            NUMBER: 20,
            TYPE: FOR_HIRE,
            FOOD_COST: 0,
            DIG: 0,
            HUNT: 0,
            TRIBE_MEMBERS: 1,
            IS_REFUGEE: True
        },
        {
            NAME: 'Scavenger',
            SET: BASE,
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
            NAME: 'Brawler',
            SET: BASE,
            NUMBER: 10,
            TYPE: FOR_HIRE,
            FOOD_COST: 2,
            DIG: 1,
            FIGHT: 2,
            TRIBE_MEMBERS: 1,
        },
        {
            NAME: 'Hunter',
            SET: BASE,
            NUMBER: 8,
            TYPE: FOR_HIRE,
            MED_COST: 1,
            HUNT: 2,
            FIGHT: 1,
            TRIBE_MEMBERS: 1
        },
        {
            NAME: 'Saboteur',
            SET: BASE,
            NUMBER: 8,
            TYPE: FOR_HIRE,
            FOOD_COST: 1,
            MED_COST: 1,
            DIG: 1,
            FIGHT: 1,
            TRIBE_MEMBERS: 1,
            ABILITY: DISARM,
            TEXT: 'Disarm one tool card, forcing it to be discarded.'
        },
        {
            NAME: 'Scout',
            SET: BASE,
            NUMBER: 8,
            TYPE: FOR_HIRE,
            FOOD_COST: 2,
            MED_COST: 1,
            DRAW: 2,
            FIGHT: 2,
            TRIBE_MEMBERS: 1
        },
        {
            NAME: 'Group Leaders',
            SET: BASE,
            NUMBER: 5,
            TYPE: FOR_HIRE,
            FOOD_COST: 2,
            MED_COST: 2,
            PLUS_DRAW: 2,
            PLUS_DIG: 2,
            PLUS_HUNT: 2,
            PLUS_FIGHT: 2,
            TRIBE_MEMBERS: 2,
            TEXT: 'Any action may be enhanced by both Group Leaders and a tool.'
        },
        {
            NAME: 'Sniper Team',
            SET: BASE,
            NUMBER: 5,
            TYPE: FOR_HIRE,
            FOOD_COST: 2,
            MED_COST: 2,
            TRIBE_MEMBERS: 2,
            ABILITY: SNIPE,
            TEXT: 'Snipe one tribe member, forcing it to be discarded.'
        },
        {
            NAME: 'Thugs',
            SET: BASE,
            NUMBER: 5,
            TYPE: FOR_HIRE,
            VARIABLE_COST: 6,
            DIG: 1,
            FIGHT: 3,
            TRIBE_MEMBERS: 3
        },
        {
            NAME: 'Sled Team',
            SET: BASE,
            NUMBER: 2,
            TYPE: CONTESTED_RESOURCE,
            DRAW: 2,
            FIGHT: 1,
            TRIBE_MEMBERS: 2
        },
        {
            NAME: 'Field Crew',
            SET: BASE,
            NUMBER: 2,
            TYPE: CONTESTED_RESOURCE,
            DIG: 2,
            HUNT: 2,
            FIGHT: 2,
            TRIBE_MEMBERS: 4
        },
        {
            NAME: 'Tribe Family (3)',
            SET: BASE,
            NUMBER: 2,
            TYPE: CONTESTED_RESOURCE,
            HUNT: 0,
            FIGHT: 0,
            TRIBE_MEMBERS: 3,
            COMMENT: 'The actual name of this card is just "Tribe Family"; '
                     'parentheses are added to distinguish the different tribe family cards'
        },
        {
            NAME: 'Tribe Family (4)',
            SET: BASE,
            NUMBER: 2,
            TYPE: CONTESTED_RESOURCE,
            HUNT: 0,
            FIGHT: 0,
            TRIBE_MEMBERS: 4,
            COMMENT: 'The actual name of this card is just "Tribe Family"; '
                     'parentheses are added to distinguish the different tribe family cards'
        },
        {
            NAME: 'Tribe Family (5)',
            SET: BASE,
            NUMBER: 2,
            TYPE: CONTESTED_RESOURCE,
            HUNT: 0,
            FIGHT: 0,
            TRIBE_MEMBERS: 5,
            COMMENT: 'The actual name of this card is just "Tribe Family"; '
                     'parentheses are added to distinguish the different tribe family cards'
        },
        {
            NAME: 'Medic',
            SET: HQ_EXP,
            NUMBER: 8,
            TYPE: FOR_HIRE,
            FOOD_COST: 3,
            DRAW: 1,
            MEDICINE: 1,
            TRIBE_MEMBERS: 1,
            ABILITY: SAVE,
            TEXT: 'Saves one tribe member from the effect of a snipe.'
        },
        {
            NAME: 'Engineer',
            SET: HQ_EXP,
            NUMBER: 8,
            TYPE: FOR_HIRE,
            FOOD_COST: 2,
            MED_COST: 1,
            DRAW: 1,
            DIG: 2,
            TRIBE_MEMBERS: 1,
            ABILITY: BUILD,
            TEXT: 'Builds one building by digging in the schematics pile.'
        },
        {
            NAME: 'Scouting Refugee',
            SET: RECON_EXP,
            NUMBER: 20,
            TYPE: FOR_HIRE,
            FOOD_COST: 1,
            PLUS_DIG: 1,
            PLUS_HUNT: 1,
            PLUS_FIGHT: 1,
            TRIBE_MEMBERS: 1,
            ABILITY: CANCEL_RECON,
            TEXT: 'May cancel a recon action. Then, draw 1 card.'
        },
        {
            NAME: 'Hardy Scavenger',
            SET: RECON_EXP,
            NUMBER: 20,
            TYPE: FOR_HIRE,
            FOOD_COST: 1,
            DRAW: 0,
            DIG: 1,
            HUNT: 1,
            FIGHT: 0,
            TRIBE_MEMBERS: 1,
            TEXT: 'If you don\'t win the Skirmish, return any Hardy Scavengers back to your hand. '
                  'You still draw a normal starting hand.'
        },
        {
            NAME: 'Assassin',
            SET: RECON_EXP,
            NUMBER: 8,
            TYPE: FOR_HIRE,
            MED_COST: 2,
            DRAW: 1,
            TRIBE_MEMBERS: 1,
            ABILITY: SNIPE,
            TEXT: 'Snipe any single-unit tribe member.'
        },
        {
            NAME: 'Courier',
            SET: RECON_EXP,
            NUMBER: 8,
            TYPE: FOR_HIRE,
            FOOD_COST: 1,
            MED_COST: 1,
            DRAW: 3,
            PLUS_FIGHT: 1,
            TRIBE_MEMBERS: 1,
            ABILITY: DRAW_RELATED,
            TEXT: 'When you perform a draw, you must discard 2 of the drawn cards per Courier played.'
        },
        {
            NAME: 'Drill Sergeant',
            SET: RECON_EXP,
            NUMBER: 8,
            TYPE: FOR_HIRE,
            FOOD_COST: 2,
            MED_COST: 1,
            DIG: 2,
            FIGHT: 1,
            TRIBE_MEMBERS: 1,
            ABILITY: DRAW_RELATED,
            TEXT: 'May choose up to 2 cards from your discard pile and shuffle them into your deck. '
                  'Then draw 2 cards.'
        },
        {
            NAME: 'Guard',
            SET: RECON_EXP,
            NUMBER: 8,
            TYPE: FOR_HIRE,
            FOOD_COST: 2,
            FIGHT: 2,
            TRIBE_MEMBERS: 1,
            ABILITY: CANCEL,
            TEXT: 'May cancel 1 pre-skirmish action targeting your card(s). '
                  'Then, draw 1 card.'
        },
        {
            NAME: 'Provocateur',
            SET: RECON_EXP,
            NUMBER: 8,
            TYPE: FOR_HIRE,
            MED_COST: 1,
            DRAW: 1,
            FIGHT: 1,
            TRIBE_MEMBERS: 1,
            TEXT: 'May use your tribe member count in place of your fight score.'
        },
        {
            NAME: 'Rogue',
            SET: RECON_EXP,
            NUMBER: 8,
            TYPE: FOR_HIRE,
            MED_COST: 1,
            DRAW: 1,
            FIGHT: 1,
            TRIBE_MEMBERS: 1,
            TEXT: 'If there is a tie for the highest fight score, you win the skirmish. '
                  'The first Rogue played in a tied skirmish wins.'
        },
        {
            NAME: 'Tinker',
            SET: RECON_EXP,
            NUMBER: 8,
            TYPE: FOR_HIRE,
            FOOD_COST: 3,
            PLUS_DIG: 1,
            PLUS_HUNT: 1,
            PLUS_FIGHT: 1,
            TRIBE_MEMBERS: 1,
            ABILITY: BUILD,
            TEXT: 'Builds 1 building by digging in the schematics pile.'
        },
        {
            NAME: 'Spy',
            SET: RECON_EXP,
            NUMBER: 8,
            TYPE: FOR_HIRE,
            VARIABLE_COST: 3,
            PLUS_FIGHT: 2,
            TRIBE_MEMBERS: 1,
            ABILITY: RECON,
            TEXT: 'May peek at up to 4 cards from 1 player. Then, draw 1 card.'
        },
        {
            NAME: 'Scrappers',
            SET: RECON_EXP,
            NUMBER: 5,
            TYPE: FOR_HIRE,
            VARIABLE_COST: 4,
            DIG: 3,
            FIGHT: 2,
            TRIBE_MEMBERS: 2,
            TEXT: 'When you dig, you may pull from the top or bottom of a pile. '
                  'You may return cards to the top or bottom of a pile.'
        },
        {
            NAME: 'Demolition Team',
            SET: RECON_EXP,
            NUMBER: 2,
            TYPE: CONTESTED_RESOURCE,
            DIG: 2,
            FIGHT: 2,
            TRIBE_MEMBERS: 2,
            ABILITY: BUILD_RELATED,
            TEXT: 'May reset a building\'s build timer. If you do, then draw 2 cards.'
        },
        {
            NAME: 'Combat Medics',
            SET: RECON_EXP,
            NUMBER: 2,
            TYPE: CONTESTED_RESOURCE,
            DRAW: 1,
            MEDICINE: 2,
            FIGHT: 1,
            TRIBE_MEMBERS: 4,
            ABILITY: SAVE,
            TEXT: 'When fighting, can perform a save action to block 1 snipe attack. '
                  'Combat Medics still contribute to fight.'
        },
        {
            NAME: 'Tribal Hunters (2)',
            SET: RECON_EXP,
            NUMBER: 2,
            TYPE: CONTESTED_RESOURCE,
            HUNT: 1,
            FIGHT: 0,
            TRIBE_MEMBERS: 2,
            COMMENT: 'The actual name of this card is just "Tribal Hunters"; '
                     'parentheses are added to distinguish the different tribal hunters cards'
        },
        {
            NAME: 'Tribal Hunters (3)',
            SET: RECON_EXP,
            NUMBER: 2,
            TYPE: CONTESTED_RESOURCE,
            HUNT: 1,
            FIGHT: 1,
            TRIBE_MEMBERS: 3,
            COMMENT: 'The actual name of this card is just "Tribal Hunters"; '
                     'parentheses are added to distinguish the different tribal hunters cards'
        },
        {
            NAME: 'Tribal Hunters (4)',
            SET: RECON_EXP,
            NUMBER: 2,
            TYPE: CONTESTED_RESOURCE,
            HUNT: 2,
            FIGHT: 1,
            TRIBE_MEMBERS: 4,
            COMMENT: 'The actual name of this card is just "Tribal Hunters"; '
                     'parentheses are added to distinguish the different tribal hunters cards'
        }
    ]
