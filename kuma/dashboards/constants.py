from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext_lazy as _

KNOWN_AUTHORS_GROUP = 'Known Authors'

# Rounded to nearby 7-day period for weekly cycles
SPAM_PERIODS = (
    (1, 'period_daily'),
    (7, 'period_weekly'),
    (28, 'period_monthly'),
    (91, 'period_quarterly'),
)
SPAM_STAT_CATEGORY_OPTIONS = (
    ('group', ('staff', 'known', 'other')),
    ('published', ('published', 'blocked')),
    ('content', ('spam', 'ham', 'unknown')),
    ('fresh', ('new', 'edit')),
    ('lang', ('en', 'other')),
)
SPAM_STAT_CATEGORIES = set(name for name, opts in SPAM_STAT_CATEGORY_OPTIONS)
SPAM_DASHBOARD_DERIVED_STATS = [
    {
        'id': 'total',
        'derived': {},
    }, {
        'id': 'published_ham',
        'derived': {'content': 'ham', 'published': 'published'},
    }, {
        'id': 'blocked_spam',
        'derived': {'content': 'spam', 'published': 'blocked'},
        'rate_denominiator': 'total',
    }, {
        'id': 'published_spam',
        'derived': {'content': 'spam', 'published': 'published'},
        'rate_denominiator': 'total',
    }, {
        'id': 'blocked_ham',
        'derived': {'content': 'ham', 'published': 'blocked'},
        'rate_denominiator': 'total',
    }, {
        'id': 'spam',
        'derived': {'content': 'spam'},
        'rate_denominiator': 'total',
    }, {
        'id': 'spam_blocked',
        'derived': {'content': 'spam', 'published': 'blocked'},
        'rate_denominiator': 'spam',
    }
]
SPAM_RATE_ID_SUFFIX = '_rate'
SPAM_DASHBOARD_NAMES = {
    'date': pgettext_lazy('a heading for a column of days', 'Date'),
    # Periods for trends over time
    'period_daily': _('Daily'),
    'period_weekly': _('Weekly'),
    'period_monthly': _('Monthly'),
    'period_quarterly': _('Quarterly'),
    # Statistics, all users
    'total': _('Total Edits'),
    'published_ham': _('Published Ham'),
    'blocked_spam': _('Blocked Spam'),
    'published_spam': _('Published Spam'),
    'blocked_ham': _('Blocked Ham'),
    'published_ham_rate': _('Published Ham Rate'),
    'blocked_spam_rate': _('Blocked Spam Rate'),
    'published_spam_rate': _('Published Spam Rate'),
    'blocked_ham_rate': _('Blocked Ham Rate'),
    'spam_rate': _('Spam Rate'),
    'spam_blocked_rate': _('Spam Blocked Rate'),
    # Groups
    'group_staff': _('MDN Staff'),
    'group_known': _('Known Authors'),
    'group_other': _('Other Users'),
    # Change types
    'changetype_new': _('New Page'),
    'changetype_edit': _('Page Edit'),
    'changetype_newtrans': _('New Translation'),
    'changetype_edittrans': _('Translation Update'),
}
