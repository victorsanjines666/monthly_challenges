
from django.urls import path
from . import views

"""

urlpatterns = [
    path("january", views.january),
    path("february", views.february),
    path("march", views.march),
    path("<month>", views.monthly_challenge),
]
"""
urlpatterns = [
    path("<month>", views.monthly_challenge),
]

