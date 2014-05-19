# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'MonsterAttackModifier.xpModifier'
        db.alter_column('main_monsterattackmodifier', 'xpModifier', self.gf('django.db.models.fields.DecimalField')(decimal_places=4, max_digits=4))

        # Changing field 'MonsterAttackModifier.gilModifier'
        db.alter_column('main_monsterattackmodifier', 'gilModifier', self.gf('django.db.models.fields.DecimalField')(decimal_places=4, max_digits=4))

    def backwards(self, orm):

        # Changing field 'MonsterAttackModifier.xpModifier'
        db.alter_column('main_monsterattackmodifier', 'xpModifier', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'MonsterAttackModifier.gilModifier'
        db.alter_column('main_monsterattackmodifier', 'gilModifier', self.gf('django.db.models.fields.IntegerField')())

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Group']", 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']", 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.aptitude': {
            'Meta': {'object_name': 'Aptitude'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'})
        },
        'main.baseitem': {
            'Meta': {'object_name': 'BaseItem'},
            'armour': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'availability': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'cost': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'damageAttribute': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'damageDieCount': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '10'}),
            'damageDieSize': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '10'}),
            'damageScale': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'effect': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'evasion': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemSlot': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '2'}),
            'itemType': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.PROTECT', 'to': "orm['main.ItemCategory']", 'null': 'True'}),
            'magicalArmour': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'magicalEvasion': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'target': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'tier': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'})
        },
        'main.baseitemability': {
            'Meta': {'object_name': 'BaseItemAbility'},
            'baseItem': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.BaseItem']", 'related_name': "'abilities'"}),
            'craftPoints': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'equippableTo': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tier': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'usedInCrafting': ('django.db.models.fields.BooleanField', [], {})
        },
        'main.baseskill': {
            'Meta': {'object_name': 'BaseSkill'},
            'aptitude': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.PROTECT', 'to': "orm['main.Aptitude']", 'null': 'True'}),
            'attribute': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'halfRate': ('django.db.models.fields.BooleanField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isMonsterSkill': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'skillType': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'specialized': ('django.db.models.fields.BooleanField', [], {})
        },
        'main.character': {
            'Meta': {'object_name': 'Character'},
            'accessorySlot': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'to': "orm['main.Item']", 'null': 'True', 'related_name': "'equippedAccessories'"}),
            'accessorySlot2': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'to': "orm['main.Item']", 'null': 'True', 'related_name': "'equippedAccessories2'"}),
            'age': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '4'}),
            'agility': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'armourBase': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'baseHP': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'baseMP': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'blurb': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '1000'}),
            'bodySlot': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'to': "orm['main.Item']", 'null': 'True', 'related_name': "'equippedBodies'"}),
            'bonusAptitudes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.Aptitude']"}),
            'category': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'characterImage': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'to': "orm['main.ImageFile']", 'null': 'True', 'related_name': "'characterImages'"}),
            'encounterSizeMonsters': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'encounterSizePCs': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'family': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'frequency': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'gil': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '10'}),
            'handSlot': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'to': "orm['main.Item']", 'null': 'True', 'related_name': "'equippedHands'"}),
            'headSlot': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'to': "orm['main.Item']", 'null': 'True', 'related_name': "'equippedHeads'"}),
            'hitBase': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intelligence': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'to': "orm['main.Job']", 'null': 'True', 'related_name': "'characters'"}),
            'level': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'location': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'magic': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'magicArmourBase': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'magicBase': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'monsterType': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'to': "orm['main.Race']", 'null': 'True', 'related_name': "'characters'"}),
            'reaction': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'secondWeaponSlot': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'to': "orm['main.Item']", 'null': 'True', 'related_name': "'equippedSecondaryWeapons'"}),
            'speed': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'spirit': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'strength': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'traits': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.Trait']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']", 'null': 'True', 'related_name': "'characters'"}),
            'vitality': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'weaponSlot': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'to': "orm['main.Item']", 'null': 'True', 'related_name': "'equippedWeapons'"}),
            'xp': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '10'})
        },
        'main.imagefile': {
            'Meta': {'object_name': 'ImageFile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '254'})
        },
        'main.item': {
            'Meta': {'object_name': 'Item'},
            'baseItem': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.PROTECT', 'to': "orm['main.BaseItem']", 'null': 'True'}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Character']", 'null': 'True', 'related_name': "'items'"}),
            'damageAttribute': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'main.itemcategory': {
            'Meta': {'object_name': 'ItemCategory'},
            'baseSkill': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.PROTECT', 'to': "orm['main.BaseSkill']", 'null': 'True'}),
            'craftPoints': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '3'}),
            'defaultItemSlot': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'subCategory': ('django.db.models.fields.IntegerField', [], {'max_length': '2'})
        },
        'main.job': {
            'Meta': {'object_name': 'Job'},
            'accuracyBonus': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'aptitude': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.PROTECT', 'blank': 'True', 'to': "orm['main.Aptitude']", 'null': 'True'}),
            'expertiseAttribute': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'expertiseSkill': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.PROTECT', 'blank': 'True', 'to': "orm['main.BaseSkill']", 'null': 'True'}),
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
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'skillPoints': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
        },
        'main.monsterattack': {
            'Meta': {'object_name': 'MonsterAttack'},
            'actionType': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'attackType': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'bonusDamage': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'bonusDamagePercent': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'combatStat': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'combatStatModifier': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'damageAttribute': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'damageType': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modifiers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.MonsterAttackModifier']"}),
            'monster': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Character']"}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'statusStat': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'statusStatModifier': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'target': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'main.monsterattackmodifier': {
            'Meta': {'object_name': 'MonsterAttackModifier'},
            'cos': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'gilModifier': ('django.db.models.fields.DecimalField', [], {'decimal_places': '4', 'max_digits': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isMultiplier': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'xpModifier': ('django.db.models.fields.DecimalField', [], {'decimal_places': '4', 'max_digits': '4'})
        },
        'main.overviewbox': {
            'Meta': {'object_name': 'OverviewBox'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'viewName': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.overviewboxsetting': {
            'Meta': {'object_name': 'OverviewBoxSetting'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Character']", 'related_name': "'overviewBoxSettings'"}),
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
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'nightVision': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'smell': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
        },
        'main.skill': {
            'Meta': {'object_name': 'Skill'},
            'baseSkill': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.PROTECT', 'to': "orm['main.BaseSkill']", 'null': 'True'}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Character']", 'null': 'True', 'related_name': "'skills'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'specialization': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'})
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
            'currentCharacter': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'to': "orm['main.Character']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['main']