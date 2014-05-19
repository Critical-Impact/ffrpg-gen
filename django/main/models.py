from django.conf import settings
from django.db import models
from django.contrib.auth import models as AuthModels
from rest_framework.relations import RelatedField
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.db.models.signals import post_save

ItemSlots = (
    ('1', '1 Handed Weapon'),
    ('2', '2 Handed Weapon'),
    ('3', 'Accessory'),
    ('4', 'Head'),
    ('5', 'Body'),
    ('6', 'Hand'),
    ('7', 'Shield'),
    ('8', 'Item'),
)

SubCategories = (
    ('2', 'Weapon'),
    ('1', 'Armour'),
    ('3', 'Accessory'),
    ('4', 'Item'),
)

AttributeCodes = (
    ('STR', 'Strength'),
    ('VIT', 'Vitality'),
    ('AGI', 'Agility'),
    ('SPD', 'Speed'),
    ('MAG', 'Magic'),
    ('SPR', 'Spirit'),
)

DamageTypes = (
    ('PHY', 'Physical'),
    ('MAG', 'Magical')
)

CombatStats = (
    ('ACC', 'Accuracy'),
    ('M.ACC', 'M. Accuracy'),
    ('MIND', 'Mind'),
    ('DEX', 'Dexterity'),
)

CombatStatModifiers = (
    ('EVA', 'Evasion'),
    ('M.EVA', 'M. Evasion'),
)

statusStats = (
    ('M.ACC', '(M. Accuracy - 50)'),
    ('MIND', 'Mind'),
    ('DEX', 'Dexterity'),
)

TraitTypes = (
    (1, 'Advantage'),
    (2, 'Disadvantage'),
)

EquippableTypes = (
    (1, 'Armour'),
    (2, 'Weapon'),
    (3, 'Either')
)

Reaction = (
    (1, 'Friendly'),
    (2, 'Neutral'),
    (3, 'Wary'),
    (4, 'Hostile')
)

Frequency = (
    (1, 'Common'),
    (2, 'Uncommon'),
    (3, 'Rare'),
    (4, 'Very Rare'),
    (5, 'Unique')
)

MonsterTypes = (
    (1, 'Regular'),
    (2, 'Notorious'),
    (3, 'Boss'),
    (4, 'End Bosses')
)

HitBases = (
    (1,1),
    (1.5,1.5),
    (2,2),
    (4,4),
    (6,6),
    (8,8)
)

MagicBases = (
    (0.5,0.5),
    (1,1),
    (1.5,1.5),
    (2,2),
    (4,4)
)

ArmourBases = (
    (0.5,0.5),
    (1,1),
    (2,2),
    (4,4),
    (6,6)
)

MagicArmourBases = (
    (0.5,0.5),
    (1,1),
    (2,2),
    (4,4),
    (6,6)
)

ActionTypes = (
    (1, 'Attack'),
    (2, 'Ability'),
    (3, 'Magic')
)

AttackTypes = (
    (0, 'No Attack'),
    (1, 'D6'),
    (2, 'D8'),
    (3, 'D10'),
    (4, 'D12')
)

Targets = (
    (1, 'Single'),
    (2, 'Group'),
    (4, 'Unfocused(Vulnerable to Attack'),
    (5, 'Unfocused(Invulnerable to Attack'),
)

class Character(models.Model):
    name = models.CharField("Name", max_length=100, blank=True, null=True)
    age = models.IntegerField("Age", max_length=4, blank=True, null=True)
    blurb = models.CharField("Blurb", max_length=1000, blank=True, null=True)
    strength = models.IntegerField("Strength", max_length=3, blank=True, null=True)
    vitality = models.IntegerField("Vitality", max_length=3, blank=True, null=True)
    agility = models.IntegerField("Agility", max_length=3, blank=True, null=True)
    speed = models.IntegerField("Speed", max_length=3, blank=True, null=True)
    magic = models.IntegerField("Magic", max_length=3, blank=True, null=True)
    spirit = models.IntegerField("Spirit", max_length=3, blank=True, null=True)
    baseHP = models.IntegerField("Base HP", max_length=3, blank=True, null=True)
    baseMP = models.IntegerField("Base MP", max_length=3, blank=True, null=True)
    level = models.IntegerField("Level", max_length=3, blank=True, null=True)
    xp = models.IntegerField("XP", max_length=10, blank=True, null=True)
    gil = models.IntegerField("Gil", max_length=10, blank=True, null=True)
    job = models.ForeignKey("Job", related_name='characters', on_delete=models.SET_NULL, null=True)
    job2 = models.ForeignKey("Job", related_name='characters2', on_delete=models.SET_NULL, null=True)
    race = models.ForeignKey("Race", related_name='characters', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="characters",editable=False, null=True, on_delete=models.SET_NULL)
    overviewBoxSettings = RelatedField(many=True)
    accessorySlot = models.ForeignKey("Item", related_name="equippedAccessories", null=True, on_delete=models.SET_NULL)
    accessorySlot2 = models.ForeignKey("Item", related_name="equippedAccessories2", null=True, on_delete=models.SET_NULL)
    bodySlot = models.ForeignKey("Item", related_name="equippedBodies", null=True, on_delete=models.SET_NULL)
    handSlot = models.ForeignKey("Item", related_name="equippedHands", null=True, on_delete=models.SET_NULL)
    headSlot = models.ForeignKey("Item", related_name="equippedHeads", null=True, on_delete=models.SET_NULL)
    weaponSlot = models.ForeignKey("Item", related_name="equippedWeapons", null=True, on_delete=models.SET_NULL)
    secondWeaponSlot = models.ForeignKey("Item", related_name="equippedSecondaryWeapons", null=True, on_delete=models.SET_NULL)
    characterImage = models.ForeignKey("ImageFile", related_name="characterImages", null=True, on_delete=models.SET_NULL)
    traits = models.ManyToManyField("Trait")
    bonusAptitudes = models.ManyToManyField("Aptitude")
    items = RelatedField(many=True)
    skills = RelatedField(many=True)

    #Monster
    isMonster = models.BooleanField("Is Monster", default=False)
    category = models.CharField("Category", max_length=200, blank=True, null=True)
    family = models.CharField("Family", max_length=200, blank=True, null=True)
    location = models.CharField("Location", max_length=200, blank=True, null=True)
    intelligence = models.CharField("Intelligence", max_length=200,null=True,blank=True)
    reaction = models.IntegerField("Reaction",choices=Reaction,null=True,blank=True)
    frequency = models.IntegerField("Frequency",choices=Frequency,null=True,blank=True)
    encounterSizeMonsters = models.IntegerField("Encounter Size Monsters", null=True, blank=True)
    encounterSizePCs = models.IntegerField("Encounter Size PCs", null=True, blank=True)
    monsterType = models.IntegerField("Type", choices=MonsterTypes, null=True, blank=True)
    hitBase = models.IntegerField("Hit Base",choices=HitBases, null=True, blank=True)
    magicBase = models.IntegerField("Magic Base",choices=MagicBases, null=True, blank=True)
    armourBase = models.IntegerField("Armour Base",choices=ArmourBases, null=True, blank=True)
    magicArmourBase = models.IntegerField("Magic Armour Base",choices=MagicArmourBases, null=True, blank=True)
    monsterAttacks = RelatedField(many=True)

class MonsterAttack(models.Model):
    monster = models.ForeignKey("Character", on_delete=models.CASCADE, related_name='monsterAttacks')
    name = models.CharField("Name", max_length=255,blank=True, null=True)
    actionType = models.IntegerField("Action Type",choices=ActionTypes,blank=True, null=True)
    attackType = models.IntegerField("Attack Type",choices=AttackTypes,blank=True, null=True)
    target = models.IntegerField("Target",choices=Targets, blank=True, null=True)
    isRandom = models.BooleanField("Is Random",default=False)
    modifiers = RelatedField(many=True)
    damageAttribute = models.CharField("Damage Attribute",choices=AttributeCodes, max_length=3,blank=True, null=True)
    damageType = models.CharField("Damage Type",choices=DamageTypes, max_length=4,blank=True, null=True)
    combatStat = models.CharField("COS Combat Stat",choices=CombatStats, max_length=3,blank=True, null=True)
    combatStatModifier = models.CharField("COS Combat Stat Modifier",choices=CombatStatModifiers, max_length=3,blank=True, null=True)
    statusStat = models.CharField("COS Status Stat",choices=statusStats, max_length=3,blank=True, null=True)
    statusStatModifier = models.CharField("COS Status Stat Modifier",choices=CombatStatModifiers, max_length=3,blank=True, null=True)
    bonusDamage = models.IntegerField("Bonus Damage",blank=True, null=True)
    bonusDamagePercent = models.IntegerField("Bonus Damage Prcent",blank=True,null=True)
    def __unicode__(self):
        return '%s' % self.name

class MonsterAttackModifier(models.Model):
    option = models.CharField("Option", max_length=255, blank=True, null=True)
    option2 = models.CharField("Option2", max_length=255, blank=True, null=True)
    modifier = models.ForeignKey("BaseMonsterAttackModifier",null=True, on_delete=models.SET_NULL)
    monsterAttack = models.ForeignKey("MonsterAttack",null=True, on_delete=models.CASCADE,related_name="modifiers")
    def __unicode__(self):
        return '%s' % self.modifier.name

class BaseMonsterAttackModifier(models.Model):
    name = models.CharField("Name", max_length=255,blank=True, null=True)
    description = models.TextField("Description", blank=True, null=True)
    attackType = models.TextField("Attack Type", blank=True, null=True)
    attackSubType = models.TextField("Attack Sub Type", blank=True, null=True)
    xpModifier = models.DecimalField("XP Modifier",max_digits=6,decimal_places=2)
    gilModifier = models.DecimalField("Gil Modifier",max_digits=6 ,decimal_places=2)
    isMultiplier = models.BooleanField("Is Multiplier",default=False)
    cos = models.IntegerField("Chance of Success",null=True)
    def __unicode__(self):
        return '%s' % self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    currentCharacter = models.ForeignKey("Character",editable=False, null=True, on_delete=models.SET_NULL)
    canCreateMonsters = models.BooleanField("Can Create Monsters?",default=False)

User.userProfile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class OverviewBox(models.Model):
    name = models.CharField("Name", max_length=100)
    viewName = models.CharField("View Name", max_length=100)

class OverviewBoxSetting(models.Model):
    overviewBox = models.ForeignKey("OverviewBox")
    spanFull = models.BooleanField("Span full page?", blank=True)
    enabled = models.BooleanField("Enabled?", blank=True)
    sortOrder = models.IntegerField("Sort Order")
    character = models.ForeignKey("Character", related_name='overviewBoxSettings')

class Trait(models.Model):
    name = models.CharField("Name", max_length=100)
    description = models.TextField("Description")
    traitType = models.IntegerField("Trait Type", choices=TraitTypes)
    cost = models.IntegerField("Cost")

class Race(models.Model):
    name = models.CharField("Name", max_length=20,blank=True, null=True)
    maxStrength = models.IntegerField("Max Strength", max_length=3)
    maxVitality = models.IntegerField("Max Vitality", max_length=3)
    maxAgility = models.IntegerField("Max Agility", max_length=3)
    maxSpeed = models.IntegerField("Max Speed", max_length=3)
    maxMagic = models.IntegerField("Max Magic", max_length=3)
    maxSpirit = models.IntegerField("Max Spirit", max_length=3)
    dayVision = models.IntegerField("Day Vision", max_length=3)
    nightVision = models.IntegerField("Night Vision", max_length=3)
    smell = models.IntegerField("Smell", max_length=3)
    hearing = models.IntegerField("Hearing", max_length=3)
    lifeSense = models.IntegerField("Life Sense", max_length=3)
    magicSense = models.IntegerField("Magic Sense", max_length=3)
    characters = RelatedField(many=True)
    def __unicode__(self):
        return '%s' % self.name

class Job(models.Model):
    name = models.CharField("Name", max_length=20,blank=True, null=True)
    hpDie = models.IntegerField("Hit Die", max_length=3)
    mpDie = models.IntegerField("Magic Die", max_length=3)
    hasMP = models.BooleanField("Has MP?", blank=True)
    maxStrength = models.IntegerField("Strength", max_length=3)
    maxVitality = models.IntegerField("Vitality", max_length=3)
    maxAgility = models.IntegerField("Agility", max_length=3)
    maxSpeed = models.IntegerField("Speed", max_length=3)
    maxMagic = models.IntegerField("Magic", max_length=3)
    maxSpirit = models.IntegerField("Spirit", max_length=3)
    accuracyBonus = models.IntegerField("Accuracy Bonus", max_length=3)
    skillPoints = models.IntegerField("Skill Points", max_length=3)
    aptitude = models.ForeignKey("Aptitude",blank=True, null=True, on_delete=models.PROTECT)
    items = models.ManyToManyField('ItemCategory')
    characters = RelatedField(many=True)
    characters2 = RelatedField(many=True)
    expertiseSkill = models.ForeignKey("BaseSkill",blank=True, null=True, on_delete=models.PROTECT)
    expertiseAttribute = models.CharField("Expertise Attribute",choices=AttributeCodes, max_length=20,blank=True, null=True)
    def __unicode__(self):
        return '%s' % self.name



class ItemCategory(models.Model):
    name = models.CharField("Name", max_length=20)
    baseSkill = models.ForeignKey("BaseSkill", null=True, on_delete=models.PROTECT)
    subCategory = models.IntegerField("Subcategory",choices=SubCategories, max_length=2)
    defaultItemSlot = models.IntegerField("Default Item Slot",choices=ItemSlots, max_length=2)
    craftPoints = models.IntegerField("Craft Points", max_length=3, null=True)
    def __unicode__(self):
        return '%s' % self.name

class Aptitude(models.Model):
    name = models.CharField("Name", max_length=20,blank=True, null=True)
    def __unicode__(self):
        return '%s' % self.name

class BaseSkill(models.Model):
    aptitude = models.ForeignKey("Aptitude", on_delete=models.PROTECT, null=True)
    name = models.CharField("Name", max_length=20,blank=True, null=True)
    attribute = models.CharField("Attribute",choices=AttributeCodes, max_length=20,blank=True, null=True)
    skillType = models.CharField("Type", max_length=20,blank=True, null=True)
    specialized = models.BooleanField("Requires Specialization?", blank=True)
    halfRate = models.BooleanField("Raises at Half Rate?", blank=True)
    isMonsterSkill = models.BooleanField("Is Monster Skill?", blank=True, default=False)
    def __unicode__(self):
        return '%s' % self.name

class Skill(models.Model):
    baseSkill = models.ForeignKey("BaseSkill", on_delete=models.PROTECT, null=True)
    character = models.ForeignKey("Character", related_name='skills', on_delete=models.CASCADE, null=True)
    specialization = models.CharField("Specialization", max_length=20,blank=True, null=True)
    level = models.IntegerField("Level")
    def __unicode__(self):
        return '%s' % self.baseSkill.name

class Item(models.Model):
    baseItem = models.ForeignKey("BaseItem", on_delete=models.PROTECT, null=True)
    character = models.ForeignKey("Character", related_name='items', on_delete=models.CASCADE, null=True)
    damageAttribute = models.CharField("Damage Attribute",choices=AttributeCodes, max_length=3,blank=True, null=True)
    quantity = models.IntegerField("Damage Scale",blank=True, null=True)
    def __unicode__(self):
        return '%s' % self.baseItem.name

class BaseItem(models.Model):
    damageScale = models.IntegerField("Damage Scale",blank=True, null=True)
    damageAttribute = models.CharField("Damage Attribute",choices=AttributeCodes, max_length=3,blank=True, null=True)
    damageDieCount = models.CharField("Damage Die Count", max_length=10,blank=True, null=True)
    damageDieSize = models.CharField("Damage Die Size", max_length=10,blank=True, null=True)

    #Armour Related
    armour = models.IntegerField("Armour",blank=True, null=True)
    magicalArmour = models.IntegerField("Magical Armour",blank=True, null=True)
    evasion = models.IntegerField("Evasion",blank=True, null=True)
    magicalEvasion = models.IntegerField("Magical Evasion",blank=True, null=True)

    #Shared
    itemType = models.ForeignKey("ItemCategory", on_delete=models.PROTECT, null=True)
    name = models.CharField("Name", max_length=100,blank=True, null=True)
    cost = models.IntegerField("Cost",blank=True, null=True)
    availability = models.IntegerField("Availability",blank=True, null=True)
    tier = models.IntegerField("Tier",blank=True, null=True)
    itemSlot = models.IntegerField("Slot",max_length=2,blank=True, null=True)

    #Misc
    effect = models.CharField("Effect", max_length=100,blank=True, null=True)
    target = models.CharField("Target", max_length=100,blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    abilities = RelatedField(many=True)
    def __unicode__(self):
        return '%s' % self.name

class BaseItemAbility(models.Model):
    name = models.CharField("Name", max_length=100)
    baseItem = models.ManyToManyField("BaseItem",related_name='abilities')
    usedInCrafting = models.BooleanField("Used in Crafting?", blank=True)
    craftPoints = models.IntegerField("Craft Points", null=True, blank=True)
    tier = models.IntegerField("Tier", null=True, blank=True)
    equippableTo = models.IntegerField("Equippable To",choices=EquippableTypes, null=True, blank=True)
    def __unicode__(self):
        return '%s' % self.name

class ImageFile(models.Model):
    image = models.ImageField(upload_to='photos', max_length=254)

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        UserProfile.objects.create(user=instance)