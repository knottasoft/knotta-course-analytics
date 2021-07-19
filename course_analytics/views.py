from django.shortcuts import render
from common.djangoapps.edxmako.paths import add_lookup, lookup_template
from rest_framework.generics import GenericAPIView
from opaque_keys.edx.keys import CourseKey
from lms.djangoapps.courseware.courses import get_course_with_access

class CourseAnalyticsView(GenericAPIView):

    def get(self, request, course_id):

        course_key = CourseKey.from_string(course_id)
        course = get_course_with_access(request.user, "load", course_key)
        user = request.user

        context = {
            "course": course,
            "user_info": {
                "username": user.username,
            },
            "user": user
        }
        return render(request, "course_analytics/course_analytics.html", context)