from lms.djangoapps.courseware.tabs import CourseTab
from django.utils.translation import ugettext_noop


class CourseAnalyticsTab(CourseTab):
    """A new course tab."""

    name = "course_analytics"
    title = ugettext_noop("Analytics")
    view_name = "course_analytics"
    tab_id = "course_analytics"
    priority = 50
    type = "course_analytics"
    is_dynamic = True

    @classmethod
    def is_enabled(cls, course, user=None):
        """Returns true if this tab is enabled."""
        return bool(user and user.is_authenticated)
        #return True

    @classmethod
    def validate(cls, tab_dict, raise_error=True):
        return True
