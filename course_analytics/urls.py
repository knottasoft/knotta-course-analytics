"""Defines the URL routes for this app."""

from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import CourseAnalyticsView

urlpatterns = [
    url(r'^$', login_required(CourseAnalyticsView.as_view()), name="course_analytics")
]