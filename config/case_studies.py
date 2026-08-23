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
    'shape-a-communication-plan': {
        'slug': 'shape-a-communication-plan',
        'title': 'Shaping a communication plan',
        'subtitle': (
            'A support team uses 1-2-4-All to find a workable way for D — who is mute '
            'and still learning to spell — to express everyday needs.'
        ),
        'tool_slug': '1-2-4-all',
        'tool_title': '1-2-4-All',
        'use_case_icon': '💬',
        'date': '23 August 2026',
        'context': (
            'D cannot speak and uses a letter board, but cannot yet spell many words. '
            'A support team ran 1-2-4-All to surface what already works, who can help teach, '
            'and what would make communication less stressful — so everyone could agree '
            'a shared plan rather than leaving it to one person.'
        ),
        'steps': [
            {
                'key': 'challenge',
                'title': 'The challenge',
                'phase': 'What needs a plan?',
                'content': (
                    'D is mute and cannot speak. She can use a letter board, but she is not '
                    'able to spell a lot of words yet. The team needs a communication plan '
                    'that meets her needs now — without waiting until spelling catches up — '
                    'and that more than one supporter can help with.'
                ),
            },
            {
                'key': 'self_reflection',
                'title': 'Self Reflection',
                'phase': 'Phase 1 — alone (1 min)',
                'content': (
                    'I am now able to use my keyboard to type words, but I know that I am '
                    'alone in my area for being able to do this. D is not able to speak and '
                    'is mute. D can use a letter board but is not able to spell a lot of words.'
                ),
            },
            {
                'key': 'pair_ideas',
                'title': 'Pair Ideas',
                'phase': 'Phase 2 — in pairs (2 min)',
                'content': (
                    'When I learned to use a letter board I was able to learn with Lorraine. '
                    'Lorraine left a few years ago and has not come back. Trudy says that she '
                    'will teach D and maybe R could help? I could help and maybe D could have '
                    'a picture board instead.'
                ),
            },
            {
                'key': 'foursome_ideas',
                'title': 'Foursome Ideas',
                'phase': 'Phase 3 — in fours (4 min)',
                'content': (
                    'R and Trudy agreed to share with Timothee and D that they will help D '
                    'learn to use a letterboard and help to make a picture board of their '
                    'favourite things if they don\'t know how to spell them.'
                ),
            },
            {
                'key': 'standout_idea',
                'title': 'Standout Idea',
                'phase': 'Phase 4 — share with all (5 min)',
                'content': (
                    'A picture board would be easier for D to be able to communicate her needs '
                    'without being stressed about spelling.'
                ),
            },
        ],
    },
}


def get_case_study(slug):
    return CASE_STUDIES.get(slug)


def list_case_studies():
    return list(CASE_STUDIES.values())
