# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MonsterAttackModifier.description'
        db.add_column('main_monsterattackmodifier', 'description',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'MonsterAttackModifier.isMultiplier'
        db.add_column('main_monsterattackmodifier', 'isMultiplier',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'MonsterAttackModifier.cos'
        db.add_column('main_monsterattackmodifier', 'cos',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'MonsterAttack.bonusDamage'
        db.add_column('main_monsterattack', 'bonusDamage',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'MonsterAttack.bonusDamagePercent'
        db.add_column('main_monsterattack', 'bonusDamagePercent',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MonsterAttackModifier.description'
        db.delete_column('main_monsterattackmodifier', 'description')

        # Deleting field 'MonsterAttackModifier.isMultiplier'
        db.delete_column('main_monsterattackmodifier', 'isMultiplier')

        # Deleting field 'MonsterAttackModifier.cos'
        db.delete_column('main_monsterattackmodifier', 'cos')

        # Deleting field 'MonsterAttack.bonusDamage'
        db.delete_column('main_monsterattack', 'bonusDamage')

        # Deleting field 'MonsterAttack.bonusDamagePercent'
        db.delete_column('main_monsterattack', 'bonusDamagePercent')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission'},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.aptitude': {
            'Meta': {'object_name': 'Aptitude'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True', 'null': 'True'})
        },
        'main.baseitem': {
            'Meta': {'object_name': 'BaseItem'},
            'armour': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'availability': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'cost': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'damageAttribute': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'}),
            'damageDieCount': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True', 'null': 'True'}),
            'damageDieSize': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True', 'null': 'True'}),
            'damageScale': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'effect': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'evasion': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemSlot': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'blank': 'True', 'null': 'True'}),
            'itemType': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.ItemCategory']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'magicalArmour': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'magicalEvasion': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'target': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'tier': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'})
        },
        'main.baseitemability': {
            'Meta': {'object_name': 'BaseItemAbility'},
            'baseItem': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'abilities'", 'to': "orm['main.BaseItem']"}),
            'craftPoints': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'equippableTo': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tier': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'usedInCrafting': ('django.db.models.fields.BooleanField', [], {})
        },
        'main.baseskill': {
            'Meta': {'object_name': 'BaseSkill'},
            'aptitude': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Aptitude']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'attribute': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True', 'null': 'True'}),
            'halfRate': ('django.db.models.fields.BooleanField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isMonsterSkill': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True', 'null': 'True'}),
            'skillType': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True', 'null': 'True'}),
            'specialized': ('django.db.models.fields.BooleanField', [], {})
        },
        'main.character': {
            'Meta': {'object_name': 'Character'},
            'accessorySlot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedAccessories'", 'to': "orm['main.Item']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'accessorySlot2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedAccessories2'", 'to': "orm['main.Item']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'age': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'blank': 'True', 'null': 'True'}),
            'agility': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'}),
            'armourBase': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'baseHP': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'}),
            'baseMP': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'}),
            'blurb': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True', 'null': 'True'}),
            'bodySlot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedBodies'", 'to': "orm['main.Item']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'bonusAptitudes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.Aptitude']"}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'characterImage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'characterImages'", 'to': "orm['main.ImageFile']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'encounterSizeMonsters': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'encounterSizePCs': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'family': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'frequency': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'gil': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'blank': 'True', 'null': 'True'}),
            'handSlot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedHands'", 'to': "orm['main.Item']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'headSlot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedHeads'", 'to': "orm['main.Item']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'hitBase': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intelligence': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'characters'", 'to': "orm['main.Job']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'level': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'magic': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'}),
            'magicArmourBase': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'magicBase': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'monsterType': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'characters'", 'to': "orm['main.Race']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'reaction': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'secondWeaponSlot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedSecondaryWeapons'", 'to': "orm['main.Item']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'speed': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'}),
            'spirit': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'}),
            'strength': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'}),
            'traits': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.Trait']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'characters'", 'to': "orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'vitality': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'}),
            'weaponSlot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedWeapons'", 'to': "orm['main.Item']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'xp': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'blank': 'True', 'null': 'True'})
        },
        'main.imagefile': {
            'Meta': {'object_name': 'ImageFile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '254'})
        },
        'main.item': {
            'Meta': {'object_name': 'Item'},
            'baseItem': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BaseItem']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': "orm['main.Character']", 'null': 'True'}),
            'damageAttribute': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'main.itemcategory': {
            'Meta': {'object_name': 'ItemCategory'},
            'baseSkill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BaseSkill']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'craftPoints': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True'}),
            'defaultItemSlot': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'subCategory': ('django.db.models.fields.IntegerField', [], {'max_length': '2'})
        },
        'main.job': {
            'Meta': {'object_name': 'Job'},
            'accuracyBonus': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'aptitude': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Aptitude']", 'blank': 'True', 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'expertiseAttribute': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True', 'null': 'True'}),
            'expertiseSkill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BaseSkill']", 'blank': 'True', 'null': 'True', 'on_delete': 'models.PROTECT'}),
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True', 'null': 'True'}),
            'skillPoints': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
        },
        'main.monsterattack': {
            'Meta': {'object_name': 'MonsterAttack'},
            'actionType': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'attackType': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'bonusDamage': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'bonusDamagePercent': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'combatStat': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'}),
            'combatStatModifier': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'}),
            'damageAttribute': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'}),
            'damageType': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modifiers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.MonsterAttackModifier']"}),
            'monster': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Character']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True', 'null': 'True'}),
            'statusStat': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'}),
            'statusStatModifier': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'}),
            'target': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'main.monsterattackmodifier': {
            'Meta': {'object_name': 'MonsterAttackModifier'},
            'cos': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'gilModifier': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isMultiplier': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True', 'null': 'True'}),
            'xpModifier': ('django.db.models.fields.IntegerField', [], {})
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True', 'null': 'True'}),
            'nightVision': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'smell': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
        },
        'main.skill': {
            'Meta': {'object_name': 'Skill'},
            'baseSkill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BaseSkill']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'skills'", 'to': "orm['main.Character']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'specialization': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True', 'null': 'True'})
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
            'currentCharacter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Character']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['main']