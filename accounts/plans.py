"""Subscription plan labels shown on signup (intent only — billing later)."""

PLANS = {
    'individual': {
        'key': 'individual',
        'name': 'Individual',
        'price_month': '£12',
        'price_year': '£100',
        'summary': 'One host login — run live sessions with your groups.',
    },
    'organisation': {
        'key': 'organisation',
        'name': 'Organisation',
        'price_month': '£36',
        'price_year': '£300',
        'summary': 'Additional host logins when more than one person needs to host.',
    },
}


def resolve_plan(plan_key):
    """Return a plan dict for a valid key, otherwise None."""
    if not plan_key:
        return None
    return PLANS.get(str(plan_key).strip().lower())
