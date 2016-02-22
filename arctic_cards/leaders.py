# Fields
NAME = 'name'
SET = 'set'
USES_REFUGEES = 'uses-refugees'
TEXT = 'text'

# Set values
HQ_EXP = 'hq'
RECON_EXP = 'recon'

# Information not strictly contained on the card
COMMENT = 'comment'


class Leaders:
    ALL_LEADERS = [
        {
            NAME: 'The Peacemaker',
            SET: HQ_EXP,
            USES_REFUGEES: True,
            TEXT: 'Each round you may play 1 Refugee to increase the power of another tribe member\s hunt or dig actions by +2.'
        },
        {
            NAME: 'The Gangster',
            SET: HQ_EXP,
            USES_REFUGEES: True,
            TEXT: 'Your Refugees have a fight of 0 and they count as 2 people for the purpose of breaking tied skirmishes.'
        },
        {
            NAME: 'The Butcher',
            SET: HQ_EXP,
            TEXT: 'Each round you may kill 1 of your tribe members (remove the card permanently from play) and sell his/her internal organs for 1 food and 1 med.'
        },
        {
            NAME: 'The Fanatic',
            SET: HQ_EXP,
            USES_REFUGEES: True,
            TEXT: 'Each round you may use 1 Refugee from your hand as a suicide bomber against an opponent. '
                  'Discard 1 of your opponent\'s revealed cards (your choice), the Refugee dies in the process (remove card from play).'
        },
        {
            NAME: 'The Organizer',
            SET: HQ_EXP,
            USES_REFUGEES: True,
            TEXT: 'Each round you may play 1 Refugee to perform a draw of 2, but only keep 1. '
                  'No other cards may be played to modify this draw and you may not perform another draw this round.'
        },
        {
            NAME: 'The Cannibal',
            SET: HQ_EXP,
            TEXT: 'Each round you may cannibalize 1 tribe member for 3 food (and subsequently remove that card from play). '
                  'You may not combine food from hunting or a garden when hiring with cannibalized food.'
        },
        {
            NAME: 'The Sergent at Arms',
            SET: HQ_EXP,
            TEXT: 'You are immune to the disarm action, preventing saboteurs from discarding your tools. '
                  'When hiring saboteurs, you pay no food (cost for you is 1 med).',
            COMMENT: 'This card is misspelled as printed: the correct spelling is Sergeant.'
        },
        {
            NAME: 'The Mentor',
            SET: HQ_EXP,
            USES_REFUGEES: True,
            TEXT: 'Each round you may play 1 Refugee card to grant another tribe member a +1 to any action.'
        },
        {
            NAME: 'The Excavator',
            SET: HQ_EXP,
            USES_REFUGEES: True,
            TEXT: 'All of your Refugees have a dig of 1. '
                  'If a Refugee uses a digging tool (i.e. shovel or a pick axe), ignore the tool\'s normal bonus and add +1 to the score.'
        },
        {
            NAME: 'The Ranger',
            SET: HQ_EXP,
            USES_REFUGEES: True,
            TEXT: 'All of your Refugees and Tribe Families have a hunt of 1.'
        },
        {
            NAME: 'The Swindler',
            SET: RECON_EXP,
            USES_REFUGEES: True,
            TEXT: 'Once per turn, you may discard 1 Refugee to persuade a mercenary into joining your tribe for 1 less food '
                  'or discard two Refugees to reduce the price by 1 med.'
        },
        {
            NAME: 'The Yardmaster',
            SET: RECON_EXP,
            TEXT: 'Once per turn, you may peek at the top 2 cards of the Junkyard. '
                  'Return both of them to the top or bottom of the Junkyard.'
        }
    ]
