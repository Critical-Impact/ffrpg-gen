# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BaseItem.effect'
        db.add_column('main_baseitem', 'effect',
                      self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=100),
                      keep_default=False)

        # Adding field 'BaseItem.target'
        db.add_column('main_baseitem', 'target',
                      self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BaseItem.effect'
        db.delete_column('main_baseitem', 'effect')

        # Deleting field 'BaseItem.target'
        db.delete_column('main_baseitem', 'target')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
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
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'object_name': 'ContentType'},
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
            'itemType': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.ItemCategory']"}),
            'magicalArmour': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'magicalEvasion': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'target': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'tier': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'main.baseitemability': {
            'Meta': {'object_name': 'BaseItemAbility'},
            'baseItem': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.BaseItem']", 'related_name': "'abilities'", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.baseskill': {
            'Meta': {'object_name': 'BaseSkill'},
            'aptitude': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Aptitude']"}),
            'attribute': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'halfRate': ('django.db.models.fields.BooleanField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'skillType': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'specialized': ('django.db.models.fields.BooleanField', [], {})
        },
        'main.character': {
            'Meta': {'object_name': 'Character'},
            'accessorySlot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Item']", 'null': 'True', 'related_name': "'equippedAccessories'"}),
            'age': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '4'}),
            'agility': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'baseHP': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'baseMP': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'blurb': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '1000'}),
            'bodySlot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Item']", 'null': 'True', 'related_name': "'equippedBodies'"}),
            'gil': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '10'}),
            'handSlot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Item']", 'null': 'True', 'related_name': "'equippedHands'"}),
            'headSlot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Item']", 'null': 'True', 'related_name': "'equippedHeads'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Job']", 'related_name': "'characters'"}),
            'level': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'magic': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Race']", 'related_name': "'characters'"}),
            'secondWeaponSlot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Item']", 'null': 'True', 'related_name': "'equippedSecondaryWeapons'"}),
            'speed': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'spirit': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'strength': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'characters'"}),
            'vitality': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'weaponSlot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Item']", 'null': 'True', 'related_name': "'equippedWeapons'"}),
            'xp': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '10'})
        },
        'main.item': {
            'Meta': {'object_name': 'Item'},
            'baseItem': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BaseItem']"}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Character']", 'related_name': "'items'"}),
            'damageAttribute': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'main.itemcategory': {
            'Meta': {'object_name': 'ItemCategory'},
            'baseSkill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BaseSkill']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'subCategory': ('django.db.models.fields.IntegerField', [], {'max_length': '2'})
        },
        'main.job': {
            'Meta': {'object_name': 'Job'},
            'accuracyBonus': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'agility': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'aptitude': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Aptitude']", 'blank': 'True', 'null': 'True'}),
            'expertiseAttribute': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'expertiseSkill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BaseSkill']", 'blank': 'True', 'null': 'True'}),
            'hasMP': ('django.db.models.fields.BooleanField', [], {}),
            'hpDie': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.ItemCategory']", 'symmetrical': 'False'}),
            'magic': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'mpDie': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'skillPoints': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'speed': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'spirit': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'strength': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'vitality': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
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
            'baseSkill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BaseSkill']"}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Character']", 'related_name': "'skills'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'specialization': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'})
        },
        'main.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'currentCharacter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Character']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['main']