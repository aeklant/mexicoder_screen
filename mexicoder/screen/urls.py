from django.conf.urls import url, include
from rest_framework import routers
from screen import views

router = routers.DefaultRouter()
router.register(r'leagues', views.LeagueViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'players', views.PlayerViewSet)
router.register(r'coaches', views.CoachViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
]
