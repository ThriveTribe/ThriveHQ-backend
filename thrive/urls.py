from django.urls import path
from .views import ThriveList, ThriveDetail

urlpatterns = [
    path("", ThriveList.as_view(), name="thrive_list"),
    # path("zen/", get_zen, name="get_zen"),
    path("<int:pk>/", ThriveDetail.as_view(), name="thrive_detail"),
]
