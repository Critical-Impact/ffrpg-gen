# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'BaseMonsterAttackModifier.xpModifier'
        db.alter_column('main_basemonsterattackmodifier', 'xpModifier', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2))

        # Changing field 'BaseMonsterAttackModifier.gilModifier'
        db.alter_column('main_basemonsterattackmodifier', 'gilModifier', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2))

    def backwards(self, orm):

        # Changing field 'BaseMonsterAttackModifier.xpModifier'
        db.alter_column('main_basemonsterattackmodifier', 'xpModifier', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2))

        # Changing field 'BaseMonsterAttackModifier.gilModifier'
        db.alter_column('main_basemonsterattackmodifier', 'gilModifier', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Group']", 'symmetrical': 'False', 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False', 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'", 'object_name': 'ContentType'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.aptitude': {
            'Meta': {'object_name': 'Aptitude'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'})
        },
        'main.baseitem': {
            'Meta': {'object_name': 'BaseItem'},
            'armour': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'availability': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'cost': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'damageAttribute': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'damageDieCount': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '10', 'null': 'True'}),
            'damageDieSize': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '10', 'null': 'True'}),
            'damageScale': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'effect': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'evasion': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemSlot': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '2', 'null': 'True'}),
            'itemType': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.ItemCategory']", 'on_delete': 'models.PROTECT', 'null': 'True'}),
            'magicalArmour': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'magicalEvasion': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'target': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'tier': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'})
        },
        'main.baseitemability': {
            'Meta': {'object_name': 'BaseItemAbility'},
            'baseItem': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.BaseItem']", 'symmetrical': 'False', 'related_name': "'abilities'"}),
            'craftPoints': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'equippableTo': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tier': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'usedInCrafting': ('django.db.models.fields.BooleanField', [], {})
        },
        'main.basemonsterattackmodifier': {
            'Meta': {'object_name': 'BaseMonsterAttackModifier'},
            'attackSubType': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'attackType': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'cos': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'gilModifier': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isMultiplier': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'xpModifier': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
        },
        'main.baseskill': {
            'Meta': {'object_name': 'BaseSkill'},
            'aptitude': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Aptitude']", 'on_delete': 'models.PROTECT', 'null': 'True'}),
            'attribute': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'halfRate': ('django.db.models.fields.BooleanField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isMonsterSkill': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'skillType': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'specialized': ('django.db.models.fields.BooleanField', [], {})
        },
        'main.character': {
            'Meta': {'object_name': 'Character'},
            'accessorySlot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Item']", 'on_delete': 'models.SET_NULL', 'related_name': "'equippedAccessories'", 'null': 'True'}),
            'accessorySlot2': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Item']", 'on_delete': 'models.SET_NULL', 'related_name': "'equippedAccessories2'", 'null': 'True'}),
            'age': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '4', 'null': 'True'}),
            'agility': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'armourBase': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'baseHP': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'baseMP': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'blurb': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '1000', 'null': 'True'}),
            'bodySlot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Item']", 'on_delete': 'models.SET_NULL', 'related_name': "'equippedBodies'", 'null': 'True'}),
            'bonusAptitudes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.Aptitude']", 'symmetrical': 'False'}),
            'category': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'characterImage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.ImageFile']", 'on_delete': 'models.SET_NULL', 'related_name': "'characterImages'", 'null': 'True'}),
            'encounterSizeMonsters': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'encounterSizePCs': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'family': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'frequency': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'gil': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '10', 'null': 'True'}),
            'handSlot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Item']", 'on_delete': 'models.SET_NULL', 'related_name': "'equippedHands'", 'null': 'True'}),
            'headSlot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Item']", 'on_delete': 'models.SET_NULL', 'related_name': "'equippedHeads'", 'null': 'True'}),
            'hitBase': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intelligence': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'isMonster': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Job']", 'on_delete': 'models.SET_NULL', 'related_name': "'characters'", 'null': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'magic': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'magicArmourBase': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'magicBase': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'monsterType': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Race']", 'on_delete': 'models.SET_NULL', 'related_name': "'characters'", 'null': 'True'}),
            'reaction': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'secondWeaponSlot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Item']", 'on_delete': 'models.SET_NULL', 'related_name': "'equippedSecondaryWeapons'", 'null': 'True'}),
            'speed': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'spirit': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'strength': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'traits': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.Trait']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'on_delete': 'models.SET_NULL', 'related_name': "'characters'", 'null': 'True'}),
            'vitality': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'weaponSlot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Item']", 'on_delete': 'models.SET_NULL', 'related_name': "'equippedWeapons'", 'null': 'True'}),
            'xp': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '10', 'null': 'True'})
        },
        'main.imagefile': {
            'Meta': {'object_name': 'ImageFile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '254'})
        },
        'main.item': {
            'Meta': {'object_name': 'Item'},
            'baseItem': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BaseItem']", 'on_delete': 'models.PROTECT', 'null': 'True'}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Character']", 'related_name': "'items'", 'null': 'True'}),
            'damageAttribute': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'main.itemcategory': {
            'Meta': {'object_name': 'ItemCategory'},
            'baseSkill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BaseSkill']", 'on_delete': 'models.PROTECT', 'null': 'True'}),
            'craftPoints': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True'}),
            'defaultItemSlot': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'subCategory': ('django.db.models.fields.IntegerField', [], {'max_length': '2'})
        },
        'main.job': {
            'Meta': {'object_name': 'Job'},
            'accuracyBonus': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'aptitude': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['main.Aptitude']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'expertiseAttribute': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'expertiseSkill': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['main.BaseSkill']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'hasMP': ('django.db.models.fields.BooleanField', [], {}),
            'hpDie': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.ItemCategory']", 'symmetrical': 'False'}),
            'maxAgility': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'maxMagic': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'maxSpeed': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'maxSpirit': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'maxStrength': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'maxVitality': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'mpDie': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'skillPoints': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
        },
        'main.monsterattack': {
            'Meta': {'object_name': 'MonsterAttack'},
            'actionType': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'attackType': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'bonusDamage': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'bonusDamagePercent': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'combatStat': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'combatStatModifier': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'damageAttribute': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'damageType': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '4', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isRandom': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'monster': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Character']", 'related_name': "'monsterAttacks'"}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'statusStat': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'statusStatModifier': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'target': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'main.monsterattackmodifier': {
            'Meta': {'object_name': 'MonsterAttackModifier'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BaseMonsterAttackModifier']", 'on_delete': 'models.SET_NULL', 'null': 'True'}),
            'monsterAttack': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.MonsterAttack']", 'related_name': "'modifiers'", 'null': 'True'}),
            'option': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'})
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
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'nightVision': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'smell': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
        },
        'main.skill': {
            'Meta': {'object_name': 'Skill'},
            'baseSkill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BaseSkill']", 'on_delete': 'models.PROTECT', 'null': 'True'}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Character']", 'related_name': "'skills'", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'specialization': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'})
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
            'currentCharacter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Character']", 'on_delete': 'models.SET_NULL', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['main']