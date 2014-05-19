# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MonsterAttack.isRandom'
        db.add_column('main_monsterattack', 'isRandom',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MonsterAttack.isRandom'
        db.delete_column('main_monsterattack', 'isRandom')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.aptitude': {
            'Meta': {'object_name': 'Aptitude'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '20', 'blank': 'True'})
        },
        'main.baseitem': {
            'Meta': {'object_name': 'BaseItem'},
            'armour': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'availability': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cost': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'damageAttribute': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '3', 'blank': 'True'}),
            'damageDieCount': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '10', 'blank': 'True'}),
            'damageDieSize': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '10', 'blank': 'True'}),
            'damageScale': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'evasion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemSlot': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '2', 'blank': 'True'}),
            'itemType': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['main.ItemCategory']"}),
            'magicalArmour': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'magicalEvasion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'target': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'tier': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['auth.User']"})
        },
        'main.baseitemability': {
            'Meta': {'object_name': 'BaseItemAbility'},
            'baseItem': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'abilities'", 'symmetrical': 'False', 'to': "orm['main.BaseItem']"}),
            'craftPoints': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'equippableTo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tier': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'usedInCrafting': ('django.db.models.fields.BooleanField', [], {})
        },
        'main.baseskill': {
            'Meta': {'object_name': 'BaseSkill'},
            'aptitude': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['main.Aptitude']"}),
            'attribute': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '20', 'blank': 'True'}),
            'halfRate': ('django.db.models.fields.BooleanField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isMonsterSkill': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '20', 'blank': 'True'}),
            'skillType': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '20', 'blank': 'True'}),
            'specialized': ('django.db.models.fields.BooleanField', [], {})
        },
        'main.character': {
            'Meta': {'object_name': 'Character'},
            'accessorySlot': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'equippedAccessories'", 'on_delete': 'models.SET_NULL', 'to': "orm['main.Item']"}),
            'accessorySlot2': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'equippedAccessories2'", 'on_delete': 'models.SET_NULL', 'to': "orm['main.Item']"}),
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '4', 'blank': 'True'}),
            'agility': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '3', 'blank': 'True'}),
            'armourBase': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'baseHP': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '3', 'blank': 'True'}),
            'baseMP': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '3', 'blank': 'True'}),
            'blurb': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '1000', 'blank': 'True'}),
            'bodySlot': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'equippedBodies'", 'on_delete': 'models.SET_NULL', 'to': "orm['main.Item']"}),
            'bonusAptitudes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.Aptitude']"}),
            'category': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'characterImage': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'characterImages'", 'on_delete': 'models.SET_NULL', 'to': "orm['main.ImageFile']"}),
            'encounterSizeMonsters': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encounterSizePCs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'family': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'frequency': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gil': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '10', 'blank': 'True'}),
            'handSlot': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'equippedHands'", 'on_delete': 'models.SET_NULL', 'to': "orm['main.Item']"}),
            'headSlot': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'equippedHeads'", 'on_delete': 'models.SET_NULL', 'to': "orm['main.Item']"}),
            'hitBase': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intelligence': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'isMonster': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'characters'", 'on_delete': 'models.SET_NULL', 'to': "orm['main.Job']"}),
            'level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '3', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'magic': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '3', 'blank': 'True'}),
            'magicArmourBase': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'magicBase': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'monsterType': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'characters'", 'on_delete': 'models.SET_NULL', 'to': "orm['main.Race']"}),
            'reaction': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'secondWeaponSlot': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'equippedSecondaryWeapons'", 'on_delete': 'models.SET_NULL', 'to': "orm['main.Item']"}),
            'speed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '3', 'blank': 'True'}),
            'spirit': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '3', 'blank': 'True'}),
            'strength': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '3', 'blank': 'True'}),
            'traits': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.Trait']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'characters'", 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'vitality': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '3', 'blank': 'True'}),
            'weaponSlot': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'equippedWeapons'", 'on_delete': 'models.SET_NULL', 'to': "orm['main.Item']"}),
            'xp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '10', 'blank': 'True'})
        },
        'main.imagefile': {
            'Meta': {'object_name': 'ImageFile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '254'})
        },
        'main.item': {
            'Meta': {'object_name': 'Item'},
            'baseItem': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['main.BaseItem']"}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'items'", 'to': "orm['main.Character']"}),
            'damageAttribute': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '3', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'main.itemcategory': {
            'Meta': {'object_name': 'ItemCategory'},
            'baseSkill': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['main.BaseSkill']"}),
            'craftPoints': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '3'}),
            'defaultItemSlot': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'subCategory': ('django.db.models.fields.IntegerField', [], {'max_length': '2'})
        },
        'main.job': {
            'Meta': {'object_name': 'Job'},
            'accuracyBonus': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'aptitude': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['main.Aptitude']"}),
            'expertiseAttribute': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '20', 'blank': 'True'}),
            'expertiseSkill': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['main.BaseSkill']"}),
            'hasMP': ('django.db.models.fields.BooleanField', [], {}),
            'hpDie': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.ItemCategory']"}),
            'maxAgility': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'maxMagic': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'maxSpeed': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'maxSpirit': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'maxStrength': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'maxVitality': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'mpDie': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '20', 'blank': 'True'}),
            'skillPoints': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
        },
        'main.monsterattack': {
            'Meta': {'object_name': 'MonsterAttack'},
            'actionType': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'attackType': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'bonusDamage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'bonusDamagePercent': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'combatStat': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '3', 'blank': 'True'}),
            'combatStatModifier': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '3', 'blank': 'True'}),
            'damageAttribute': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '3', 'blank': 'True'}),
            'damageType': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '4', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isRandom': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modifiers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.MonsterAttackModifier']"}),
            'monster': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'monsterAttacks'", 'to': "orm['main.Character']"}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True'}),
            'statusStat': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '3', 'blank': 'True'}),
            'statusStatModifier': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '3', 'blank': 'True'}),
            'target': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'main.monsterattackmodifier': {
            'Meta': {'object_name': 'MonsterAttackModifier'},
            'cos': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'gilModifier': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isMultiplier': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True'}),
            'xpModifier': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '4'})
        },
        'main.overviewbox': {
            'Meta': {'object_name': 'OverviewBox'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'viewName': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.overviewboxsetting': {
            'Meta': {'object_name': 'OverviewBoxSetting'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'overviewBoxSettings'", 'to': "orm['main.Character']"}),
            'enabled': ('django.db.models.fields.BooleanField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'overviewBox': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.OverviewBox']"}),
            'sortOrder': ('django.db.models.fields.IntegerField', [], {}),
            'spanFull': ('django.db.models.fields.BooleanField', [], {})
        },
        'main.race': {
            'Meta': {'object_name': 'Race'},
            'dayVision': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'hearing': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lifeSense': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'magicSense': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'maxAgility': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'maxMagic': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'maxSpeed': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'maxSpirit': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'maxStrength': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'maxVitality': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '20', 'blank': 'True'}),
            'nightVision': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'smell': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
        },
        'main.skill': {
            'Meta': {'object_name': 'Skill'},
            'baseSkill': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['main.BaseSkill']"}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'skills'", 'to': "orm['main.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'specialization': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '20', 'blank': 'True'})
        },
        'main.trait': {
            'Meta': {'object_name': 'Trait'},
            'cost': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'traitType': ('django.db.models.fields.IntegerField', [], {})
        },
        'main.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'canCreateMonsters': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'currentCharacter': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['main.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['main']