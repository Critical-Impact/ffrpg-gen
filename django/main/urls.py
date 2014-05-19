from django.conf.urls import patterns, include, url
from rest_framework import routers, generics
from main import rest_views
from django.contrib import admin
from security import urls as security_urls

admin.autodiscover()

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', rest_views.UserViewSet)
router.register(r'userProfiles', rest_views.UserProfileViewSet)
router.register(r'groups', rest_views.GroupViewSet)
router.register(r'characters', rest_views.CharacterViewSet)
router.register(r'overviewBoxes', rest_views.OverviewBoxViewSet)
router.register(r'overviewBoxSettings', rest_views.OverviewBoxSettingViewSet)
router.register(r'races', rest_views.RaceViewSet)
router.register(r'jobs', rest_views.JobViewSet)
router.register(r'itemCategories', rest_views.ItemCategoryViewSet)
router.register(r'aptitudes', rest_views.AptitudeViewSet)
router.register(r'skills', rest_views.SkillViewSet)
router.register(r'baseSkills', rest_views.BaseSkillViewSet)
router.register(r'items', rest_views.ItemViewSet)
router.register(r'baseItems', rest_views.BaseItemViewSet)
router.register(r'traits', rest_views.TraitViewSet)
router.register(r'imageFiles', rest_views.ImageFileViewSet)
router.register(r'baseItemAbilities', rest_views.BaseItemAbilityViewSet)
router.register(r'monsterAttacks', rest_views.MonsterAttackViewSet)
router.register(r'monsterAttackModifiers', rest_views.MonsterAttackModifierViewSet)
router.register(r'baseMonsterAttackModifiers', rest_views.BaseMonsterAttackModifierViewSet)

urlpatterns = patterns('',
    url(r'^data/', include(router.urls)),
    url(r'^', include(security_urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
