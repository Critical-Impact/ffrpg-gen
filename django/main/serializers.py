from django.contrib.auth.models import User, Group
from main.fields import Base64ImageField
from main.models import *
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        resource_name = 'userProfile'
        fields = ('id', 'currentCharacter','user','canCreateMonsters')

class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField('get_profile')
    class Meta:
        model = User
        resource_name = 'user'
        fields = ('id', 'username','password', 'email', 'groups', 'characters','profile')
    def get_profile(self, obj):
        return obj.get_profile().id

    def restore_object(self, attrs, instance=None):
            user = super(UserSerializer, self).restore_object(attrs, instance)
            user.set_password(attrs['password'])
            return user

    def to_native(self, obj):
        ret = super(UserSerializer, self).to_native(obj)
        del ret['password']
        return ret

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        resource_name = 'group'
        fields = ('id', 'name')

class CharacterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Character
        resource_name = 'character'
        fields = ('id', 'user', 'name','age','isMonster','strength', 'vitality', 'agility', 'speed','magic','spirit','baseHP','baseMP','level','xp','gil','job','job2','race','user','overviewBoxSettings','skills', 'accessorySlot','bodySlot','handSlot','headSlot','weaponSlot','secondWeaponSlot','items','bonusAptitudes','characterImage','category','family','location','intelligence','reaction','frequency','encounterSizeMonsters','encounterSizePCs','monsterType','hitBase','magicBase','armourBase','magicArmourBase','monsterAttacks')

class OverviewBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverviewBox
        resource_name = 'overviewBox'
        fields = ('id', 'name','viewName')

class OverviewBoxSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverviewBoxSetting
        resource_name = 'overviewBoxSetting'
        fields = ('id', 'overviewBox','spanFull','enabled','sortOrder', 'character')

class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        resource_name = 'race'
        fields = ('id', 'name','maxStrength', 'maxVitality', 'maxAgility', 'maxSpeed','maxMagic','maxSpirit','dayVision','nightVision','smell','hearing','lifeSense','magicSense')

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        resource_name = 'job'
        fields = ('id', 'name','hpDie','mpDie','hasMP','maxStrength', 'maxVitality', 'maxAgility', 'maxSpeed','maxMagic','maxSpirit','accuracyBonus','skillPoints','aptitude','items','expertiseSkill','expertiseAttribute')

class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        resource_name = 'itemCategory'
        fields = ('id', 'name','baseSkill','defaultItemSlot', 'craftPoints','subCategory')

class AptitudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aptitude
        resource_name = 'aptitude'
        fields = ('id', 'name')

class BaseSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseSkill
        resource_name = 'baseSkill'
        fields = ('id', 'name','skillType','attribute','aptitude','specialized','halfRate','isMonsterSkill')

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        resource_name = 'skill'
        fields = ('id','baseSkill','level','character','specialization')

class BaseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseItem
        resource_name = 'baseItem'
        fields = ('id','abilities', 'damageScale','damageAttribute','damageDieCount','damageDieSize','armour','magicalArmour','evasion','magicalEvasion','name','cost','availability','tier','itemType','itemSlot','user')

class BaseItemAbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseItemAbility
        resource_name = 'baseItemAbility'
        fields = ('id', 'name', 'usedInCrafting','craftPoints','tier','equippableTo')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        resource_name = 'item'
        fields = ('id','baseItem','character','quantity','damageAttribute')

class TraitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trait
        resource_name = 'trait'
        fields = ('id', 'name','description','cost','traitType')

class ImageFileSerializer(serializers.ModelSerializer):
    image = Base64ImageField(source='image')
    class Meta:
        model = ImageFile
        resource_name = 'imageFile'
        fields = ('id', 'image')

class MonsterAttackSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonsterAttack
        resource_name = 'monsterAttack'
        fields = ('id','isRandom', 'monster','name','actionType','attackType','target','modifiers','damageAttribute','damageType','combatStat','combatStatModifier','statusStat','statusStatModifier','bonusDamage','bonusDamagePercent')

class MonsterAttackModifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonsterAttackModifier
        resource_name = 'monsterAttackModifier'
        fields = ('id', 'option','option2','modifier','monsterAttack')

class BaseMonsterAttackModifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseMonsterAttackModifier
        resource_name = 'baseMonsterAttackModifier'
        fields = ('id', 'name','description','xpModifier','gilModifier','isMultiplier','cos','attackType','attackSubType')