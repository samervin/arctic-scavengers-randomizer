# Fields
NAME = 'name'
SET = 'set'
TRIBE_MEMBERS = 'tribe-members'
VICTORY_CONDITION = 'victory-condition'
TIE_BREAKER = 'tie-breaker'
TEXT = 'text'
COMMENT = 'comment'

# Set values
HQ_EXP = 'hq'
RECON_EXP = 'recon'

# Information not strictly contained on the card
COMMENT = 'comment'


class Gangs:
    ALL_GANGS = [
        {
            NAME: 'The Gearheads',
            SET: HQ_EXP,
            TRIBE_MEMBERS: 5,
            VICTORY_CONDITION: 'tools',
            TIE_BREAKER: 'contested-resources',
            TEXT: 'At game end this gang joins whichever tribe has accumulated the most tools.',
            COMMENT: 'From the manual: '
                     'Most tool is determined by adding up the quantity of cards with a tool icon. '
                     'Ties are broken by counting the total number of tools that are contested resources.'
        },
        {
            NAME: 'The Pharmers',
            SET: HQ_EXP,
            TRIBE_MEMBERS: 5,
            VICTORY_CONDITION: 'medicine',
            TIE_BREAKER: 'medics',
            TEXT: 'At game end this gang joins whichever tribe has accumulated the most meds.',
            COMMENT: 'From the manual: '
                     'Most meds is determined by adding the total meds VALUE of all medicine cards (based on card type). '
                     'Ties are broken by counting the total number of medics.'
        },
        {
            NAME: 'The Masons',
            SET: HQ_EXP,
            TRIBE_MEMBERS: 5,
            VICTORY_CONDITION: 'buildings',
            TIE_BREAKER: 'engineers',
            TEXT: 'At game end this gang joins whichever tribe has accumulated the most buildings.',
            COMMENT: 'From the manual: '
                     'Most buildings is determined by adding the total number of completed and enabled buildings. '
                     'Ties are broken by adding up the total number of engineers.'
        },
        {
            NAME: 'Humanitarians',
            SET: RECON_EXP,
            TRIBE_MEMBERS: 5,
            VICTORY_CONDITION: 'refugees',
            TEXT: 'At game end, this gang joins whichever tribe has accumulated the most Refugees.',
            COMMENT: 'From the manual: '
                     'Awarded based upon number of cards with the "refugee" keyword in the title. '
                     'There is no tie-breaker. In the event of a tie, this gang is not awarded.'
        }
    ]
