from django.urls import path
from .views_front import (
    ThriveCreateView,
    ThriveDeleteView,
    ThriveDetailView,
    ThriveListView,
    ThriveUpdateView,
)
from .views import get_zen

urlpatterns = [
    path("", ThriveListView.as_view(), name="thrive_list"),
    path("<int:pk>/", ThriveDetailView.as_view(), name="thrive_detail"),
    path("create/", ThriveCreateView.as_view(), name="thrive_create"),
    path("<int:pk>/update/", ThriveUpdateView.as_view(), name="thrive_update"),
    path("<int:pk>/delete/", ThriveDeleteView.as_view(), name="thrive_delete"),
    path("zen/", get_zen, name="get_zen"),
]
