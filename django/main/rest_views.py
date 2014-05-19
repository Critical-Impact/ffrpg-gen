import django_filters
from django.contrib.auth.models import User, Group
from rest_framework.viewsets import GenericViewSet
from main.filters import IdsFilterBackend, NullableNumberFilter, MultipleNumberFilter
from main.models import Character
from rest_framework import viewsets, generics, filters, mixins
from main.serializers import *


#Custom Viewsets
class NoDeleteModelViewSet(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.ListModelMixin,GenericViewSet):
    pass

class UserViewSet(NoDeleteModelViewSet):

    queryset = User.objects.all()
    filter_backends = (filters.DjangoFilterBackend,IdsFilterBackend)
    serializer_class = UserSerializer

class UserProfileViewSet(NoDeleteModelViewSet):

    queryset = UserProfile.objects.all()
    filter_backends = (filters.DjangoFilterBackend,IdsFilterBackend)
    serializer_class = UserProfileSerializer

class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    filter_backends = (filters.DjangoFilterBackend,IdsFilterBackend)
    serializer_class = GroupSerializer

class CharacterViewSet(NoDeleteModelViewSet):

    model = Character
    serializer_class = CharacterSerializer
    filter_backends = (filters.DjangoFilterBackend,IdsFilterBackend)
    def get_queryset(self):
        if self.request.user.is_authenticated():
            return Character.objects.filter(user = self.request.user)
        else:
            return Character.objects.all()

class OverviewBoxViewSet(viewsets.ModelViewSet):
    model = OverviewBox
    serializer_class = OverviewBoxSerializer
    filter_backends = (filters.DjangoFilterBackend,IdsFilterBackend)
    def get_queryset(self):
        return OverviewBox.objects.all()

class OverviewBoxSettingViewSet(viewsets.ModelViewSet):
    model = OverviewBoxSetting
    serializer_class = OverviewBoxSettingSerializer
    filter_backends = (filters.DjangoFilterBackend,IdsFilterBackend)
    def get_queryset(self):
        ids = self.request.QUERY_PARAMS.get('ids', None)
        if ids is not None:
            return OverviewBoxSetting.objects.filter(id = ids)
        if self.request.user.is_authenticated():
            return OverviewBoxSetting.objects.filter(character = self.request.user.userProfile.character)
        else:
            return OverviewBoxSetting.objects.all()

class RaceViewSet(viewsets.ModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer
    filter_backends = (filters.DjangoFilterBackend,IdsFilterBackend)

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = (filters.DjangoFilterBackend,IdsFilterBackend)

class ItemCategoryFilter(django_filters.FilterSet):
    subCategory = django_filters.CharFilter(name="subCategory")
    craftPoints = NullableNumberFilter(name="craftPoints")
    class Meta:
        model = ItemCategory
        fields = ['subCategory']

class ItemCategoryViewSet(viewsets.ModelViewSet):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
    filter_backends = (filters.DjangoFilterBackend,IdsFilterBackend)
    filter_class = ItemCategoryFilter
    filter_fields = ('subCategory', 'craftPoints')

class AptitudeViewSet(viewsets.ModelViewSet):
    queryset = Aptitude.objects.all()
    filter_backends = (filters.DjangoFilterBackend,IdsFilterBackend)
    serializer_class = AptitudeSerializer

class BaseSkillFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(name="id")
    isMonsterSkill = django_filters.BooleanFilter(name="isMonsterSkill")
    class Meta:
        model = BaseSkill
        fields = ['id','isMonsterSkill']

class BaseSkillViewSet(viewsets.ModelViewSet):
    queryset = BaseSkill.objects.all()
    filter_backends = (filters.DjangoFilterBackend,IdsFilterBackend)
    filter_class = BaseSkillFilter
    serializer_class = BaseSkillSerializer



class SkillViewSet(viewsets.ModelViewSet):
    model = Skill
    filter_backends = (filters.DjangoFilterBackend,IdsFilterBackend)
    serializer_class = SkillSerializer
    def get_queryset(self):
        if self.request.user.is_authenticated():
            return Skill.objects.filter(character = self.request.user.userProfile.currentCharacter)
        else:
            return Skill.objects.all()

class BaseItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(name="name")
    filter_backends = (filters.DjangoFilterBackend,IdsFilterBackend)
    itemType = django_filters.ModelChoiceFilter(name="itemType",queryset=ItemCategory.objects.all())

    class Meta:
        model = BaseItem
        fields = ['name','itemType']


class BaseItemAbilityFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(name="id")
    usedInCrafting = django_filters.CharFilter(name="usedInCrafting")
    equippableTo = MultipleNumberFilter(name="equippableTo")
    class Meta:
        model = BaseItemAbility
        fields = ['id','usedInCrafting','equippableTo']

class BaseItemViewSet(viewsets.ModelViewSet):
    queryset = BaseItem.objects.all()
    serializer_class = BaseItemSerializer
    filter_backends = (filters.DjangoFilterBackend,IdsFilterBackend)
    filter_class = BaseItemFilter

class BaseItemAbilityViewSet(viewsets.ModelViewSet):
    queryset = BaseItemAbility.objects.all()
    serializer_class = BaseItemAbilitySerializer
    filter_backends = (filters.DjangoFilterBackend,IdsFilterBackend)
    filter_class = BaseItemAbilityFilter

class ItemViewSet(viewsets.ModelViewSet):
    model = Item
    serializer_class = ItemSerializer
    filter_backends = (filters.DjangoFilterBackend,IdsFilterBackend)
    def get_queryset(self):
        if self.request.user.is_authenticated():
            return Item.objects.filter(character = self.request.user.userProfile.currentCharacter)
        else:
            return Item.objects.all()

class TraitViewSet(viewsets.ModelViewSet):
    model = Trait
    filter_backends = (filters.DjangoFilterBackend,IdsFilterBackend)
    serializer_class = TraitSerializer

class ImageFileViewSet(viewsets.ModelViewSet):
    queryset = ImageFile.objects.all()
    filter_backends = (filters.DjangoFilterBackend,IdsFilterBackend)
    serializer_class = ImageFileSerializer

class MonsterAttackViewSet(viewsets.ModelViewSet):
    model = MonsterAttack
    filter_backends = (filters.DjangoFilterBackend,IdsFilterBackend)
    serializer_class = MonsterAttackSerializer
    def get_queryset(self):
        if self.request.user.is_authenticated():
            return MonsterAttack.objects.filter(monster = self.request.user.userProfile.currentCharacter)
        else:
            return MonsterAttack.objects.all()

class MonsterAttackModifierViewSet(viewsets.ModelViewSet):
    model = MonsterAttackModifier
    filter_backends = (filters.DjangoFilterBackend,IdsFilterBackend)
    serializer_class = MonsterAttackModifierSerializer
    def get_queryset(self):
        if self.request.user.is_authenticated():
            return MonsterAttackModifier.objects.filter(monster = self.request.user.userProfile.currentCharacter)
        else:
            return MonsterAttackModifier.objects.all()

class BaseMonsterAttackModifierViewSet(viewsets.ModelViewSet):
    model = BaseMonsterAttackModifier
    filter_backends = (filters.DjangoFilterBackend,IdsFilterBackend)
    serializer_class = BaseMonsterAttackModifierSerializer
    def get_queryset(self):
        return BaseMonsterAttackModifier.objects.all()