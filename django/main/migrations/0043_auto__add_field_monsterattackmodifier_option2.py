# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MonsterAttackModifier.option2'
        db.add_column('main_monsterattackmodifier', 'option2',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MonsterAttackModifier.option2'
        db.delete_column('main_monsterattackmodifier', 'option2')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'db_table': "'django_content_type'", 'object_name': 'ContentType'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.aptitude': {
            'Meta': {'object_name': 'Aptitude'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        'main.baseitem': {
            'Meta': {'object_name': 'BaseItem'},
            'armour': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'availability': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cost': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'damageAttribute': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'damageDieCount': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'damageDieSize': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'damageScale': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'evasion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemSlot': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'itemType': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.ItemCategory']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'magicalArmour': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'magicalEvasion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'target': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tier': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'})
        },
        'main.baseitemability': {
            'Meta': {'object_name': 'BaseItemAbility'},
            'baseItem': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'abilities'", 'to': "orm['main.BaseItem']", 'symmetrical': 'False'}),
            'craftPoints': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'equippableTo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tier': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'usedInCrafting': ('django.db.models.fields.BooleanField', [], {})
        },
        'main.basemonsterattackmodifier': {
            'Meta': {'object_name': 'BaseMonsterAttackModifier'},
            'attackSubType': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'attackType': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'cos': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'gilModifier': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isMultiplier': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'xpModifier': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
        },
        'main.baseskill': {
            'Meta': {'object_name': 'BaseSkill'},
            'aptitude': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Aptitude']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'attribute': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'halfRate': ('django.db.models.fields.BooleanField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isMonsterSkill': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'skillType': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'specialized': ('django.db.models.fields.BooleanField', [], {})
        },
        'main.character': {
            'Meta': {'object_name': 'Character'},
            'accessorySlot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedAccessories'", 'to': "orm['main.Item']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'accessorySlot2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedAccessories2'", 'to': "orm['main.Item']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'age': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'agility': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'armourBase': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'baseHP': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'baseMP': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'blurb': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'bodySlot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedBodies'", 'to': "orm['main.Item']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'bonusAptitudes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.Aptitude']", 'symmetrical': 'False'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'characterImage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'characterImages'", 'to': "orm['main.ImageFile']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'encounterSizeMonsters': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encounterSizePCs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'family': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'frequency': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gil': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'handSlot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedHands'", 'to': "orm['main.Item']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'headSlot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedHeads'", 'to': "orm['main.Item']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'hitBase': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intelligence': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'isMonster': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'characters'", 'to': "orm['main.Job']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'level': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'magic': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'magicArmourBase': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'magicBase': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'monsterType': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'characters'", 'to': "orm['main.Race']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'reaction': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'secondWeaponSlot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedSecondaryWeapons'", 'to': "orm['main.Item']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'speed': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'spirit': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'strength': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'traits': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.Trait']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'characters'", 'to': "orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'vitality': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'weaponSlot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedWeapons'", 'to': "orm['main.Item']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'xp': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
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
            'damageAttribute': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
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
            'aptitude': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Aptitude']", 'null': 'True', 'blank': 'True', 'on_delete': 'models.PROTECT'}),
            'expertiseAttribute': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'expertiseSkill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BaseSkill']", 'null': 'True', 'blank': 'True', 'on_delete': 'models.PROTECT'}),
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'skillPoints': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
        },
        'main.monsterattack': {
            'Meta': {'object_name': 'MonsterAttack'},
            'actionType': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'attackType': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'bonusDamage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'bonusDamagePercent': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'combatStat': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'combatStatModifier': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'damageAttribute': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'damageType': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isRandom': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'monster': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'monsterAttacks'", 'to': "orm['main.Character']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'statusStat': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'statusStatModifier': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'target': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'main.monsterattackmodifier': {
            'Meta': {'object_name': 'MonsterAttackModifier'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BaseMonsterAttackModifier']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'monsterAttack': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'modifiers'", 'to': "orm['main.MonsterAttack']", 'null': 'True'}),
            'option': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'option2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'nightVision': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'smell': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
        },
        'main.skill': {
            'Meta': {'object_name': 'Skill'},
            'baseSkill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BaseSkill']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'skills'", 'to': "orm['main.Character']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'specialization': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
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
            'currentCharacter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Character']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['main']