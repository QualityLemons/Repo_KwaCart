"""Published case studies — real facilitation outputs turned into walkthroughs."""

CASE_STUDIES = {
    'supporting-positive-behaviour': {
        'slug': 'supporting-positive-behaviour',
        'title': 'Supporting positive behaviour',
        'subtitle': (
            'A coaching conversation after a health wake-up call — using '
            'Helping Heuristics to explore habits without rushing to fix.'
        ),
        'tool_slug': 'helping-heuristics',
        'tool_title': 'Helping Heuristics',
        'use_case_icon': '🤝',
        'date': '23 August 2026',
        'context': (
            'T received a prognosis of very high cholesterol and borderline type 2 diabetes. '
            'He had always believed he could manage his health despite being overweight — '
            'but the results showed that some patterns had caught up with him. '
            'A coach used Helping Heuristics to walk through four ways of helping, '
            'so T could reflect at his own pace and agree small, deliberate next steps.'
        ),
        'steps': [
            {
                'key': 'challenge',
                'title': 'The challenge',
                'phase': 'Client sets the scene',
                'content': (
                    'T had been given a prognosis of very high cholesterol and borderline '
                    'type 2 diabetes. He always thought he could take care of himself despite '
                    'being overweight. He now knows his health decisions have caught up with him '
                    'and he needs to make a number of changes — some immediate, some gradual.'
                ),
            },
            {
                'key': 'quiet_presence',
                'title': 'Quiet Presence',
                'phase': 'Round 1 — listen without fixing',
                'content': (
                    'T knew his cholesterol was going up but had not connected that to eating '
                    'too much and developing insulin resistance. He cooks for his family and '
                    'is also cooked for, and does a lot of grazing because he works at home — '
                    'disordered eating patterns, sometimes barely eating and sometimes snacking '
                    'throughout the day. He has been roughly the same weight for ten years.'
                ),
            },
            {
                'key': 'guided_discovery',
                'title': 'Guided Discovery',
                'phase': 'Round 2 — inquiry, not advice',
                'content': (
                    'T agrees he needs to make progress to lose weight and is comforted that '
                    'he can do the process slowly and deliberately. The advice he got was to '
                    'stop eating when the sun begins to set — a window for eating and a window '
                    'to recover. He thinks this is a good place to start and will work on '
                    'improving his food intake through that rhythm.'
                ),
            },
            {
                'key': 'loving_provocation',
                'title': 'Loving Provocation',
                'phase': 'Round 3 — gentle challenge',
                'content': (
                    'T said he previously got conflicting advice from friends and does not know '
                    'how to deal with people who tell him he looks good — he was not used to '
                    'being told he is handsome. Most of the time people see his face and '
                    'compliment him, then see the rest of his body and the conversation stops '
                    'unless they really get to know him.'
                ),
            },
            {
                'key': 'process_mindfulness',
                'title': 'Process Mindfulness',
                'phase': 'Round 4 — accept offers, notice possibilities',
                'content': (
                    'T accepts that he wants to change and it will take time. He admits he '
                    'smokes socially and drinks a few nights each week — something he will '
                    'need to stop. He has quit for periods before and would like to think about '
                    'healthy habits and hobbies instead of going to the pub, or alternatives '
                    'to drinking and smoking when he is there.'
                ),
            },
            {
                'key': 'debrief',
                'title': 'Debrief',
                'phase': 'What shifted?',
                'content': (
                    'T is happy reflecting on the progress he made since receiving his prognosis '
                    'a week ago. He can see possibilities for slow weight loss and behaviour change. '
                    'As the coach, I feel confident I can patiently help T take steps without '
                    'triggering his anxiety.'
                ),
            },
        ],
    },
}


def get_case_study(slug):
    return CASE_STUDIES.get(slug)


def list_case_studies():
    return list(CASE_STUDIES.values())
