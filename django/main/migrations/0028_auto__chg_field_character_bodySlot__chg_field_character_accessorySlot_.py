# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Character.bodySlot'
        db.alter_column('main_character', 'bodySlot_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, null=True, to=orm['main.Item']))

        # Changing field 'Character.accessorySlot'
        db.alter_column('main_character', 'accessorySlot_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, null=True, to=orm['main.Item']))

        # Changing field 'Character.secondWeaponSlot'
        db.alter_column('main_character', 'secondWeaponSlot_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, null=True, to=orm['main.Item']))

        # Changing field 'Character.weaponSlot'
        db.alter_column('main_character', 'weaponSlot_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, null=True, to=orm['main.Item']))

        # Changing field 'Character.job'
        db.alter_column('main_character', 'job_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, null=True, to=orm['main.Job']))

        # Changing field 'Character.user'
        db.alter_column('main_character', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, null=True, to=orm['auth.User']))

        # Changing field 'Character.headSlot'
        db.alter_column('main_character', 'headSlot_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, null=True, to=orm['main.Item']))

        # Changing field 'Character.handSlot'
        db.alter_column('main_character', 'handSlot_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, null=True, to=orm['main.Item']))

        # Changing field 'Character.accessorySlot2'
        db.alter_column('main_character', 'accessorySlot2_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, null=True, to=orm['main.Item']))

        # Changing field 'Character.race'
        db.alter_column('main_character', 'race_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, null=True, to=orm['main.Race']))

        # Changing field 'Skill.baseSkill'
        db.alter_column('main_skill', 'baseSkill_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, null=True, to=orm['main.BaseSkill']))

        # Changing field 'ItemCategory.baseSkill'
        db.alter_column('main_itemcategory', 'baseSkill_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, null=True, to=orm['main.BaseSkill']))

        # Changing field 'Job.aptitude'
        db.alter_column('main_job', 'aptitude_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.DO_NOTHING, to=orm['main.Aptitude']))

        # Changing field 'Job.expertiseSkill'
        db.alter_column('main_job', 'expertiseSkill_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.DO_NOTHING, to=orm['main.BaseSkill']))

        # Changing field 'BaseSkill.aptitude'
        db.alter_column('main_baseskill', 'aptitude_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, null=True, to=orm['main.Aptitude']))

        # Changing field 'Item.baseItem'
        db.alter_column('main_item', 'baseItem_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, null=True, to=orm['main.BaseItem']))

        # Changing field 'Item.character'
        db.alter_column('main_item', 'character_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, null=True, to=orm['main.Character']))

        # Changing field 'UserProfile.currentCharacter'
        db.alter_column('main_userprofile', 'currentCharacter_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, null=True, to=orm['main.Character']))

        # Changing field 'BaseItem.itemType'
        db.alter_column('main_baseitem', 'itemType_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, null=True, to=orm['main.ItemCategory']))

    def backwards(self, orm):

        # Changing field 'Character.bodySlot'
        db.alter_column('main_character', 'bodySlot_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, null=True, to=orm['main.Item']))

        # Changing field 'Character.accessorySlot'
        db.alter_column('main_character', 'accessorySlot_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, null=True, to=orm['main.Item']))

        # Changing field 'Character.secondWeaponSlot'
        db.alter_column('main_character', 'secondWeaponSlot_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, null=True, to=orm['main.Item']))

        # Changing field 'Character.weaponSlot'
        db.alter_column('main_character', 'weaponSlot_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, null=True, to=orm['main.Item']))

        # Changing field 'Character.job'
        db.alter_column('main_character', 'job_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, null=True, to=orm['main.Job']))

        # Changing field 'Character.user'
        db.alter_column('main_character', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

        # Changing field 'Character.headSlot'
        db.alter_column('main_character', 'headSlot_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, null=True, to=orm['main.Item']))

        # Changing field 'Character.handSlot'
        db.alter_column('main_character', 'handSlot_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, null=True, to=orm['main.Item']))

        # Changing field 'Character.accessorySlot2'
        db.alter_column('main_character', 'accessorySlot2_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, null=True, to=orm['main.Item']))

        # Changing field 'Character.race'
        db.alter_column('main_character', 'race_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, null=True, to=orm['main.Race']))

        # Changing field 'Skill.baseSkill'
        db.alter_column('main_skill', 'baseSkill_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, null=True, to=orm['main.BaseSkill']))

        # Changing field 'ItemCategory.baseSkill'
        db.alter_column('main_itemcategory', 'baseSkill_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, null=True, to=orm['main.BaseSkill']))

        # Changing field 'Job.aptitude'
        db.alter_column('main_job', 'aptitude_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, null=True, to=orm['main.Aptitude']))

        # Changing field 'Job.expertiseSkill'
        db.alter_column('main_job', 'expertiseSkill_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, null=True, to=orm['main.BaseSkill']))

        # Changing field 'BaseSkill.aptitude'
        db.alter_column('main_baseskill', 'aptitude_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, null=True, to=orm['main.Aptitude']))

        # Changing field 'Item.baseItem'
        db.alter_column('main_item', 'baseItem_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, null=True, to=orm['main.BaseItem']))

        # Changing field 'Item.character'
        db.alter_column('main_item', 'character_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, null=True, to=orm['main.Character']))

        # Changing field 'UserProfile.currentCharacter'
        db.alter_column('main_userprofile', 'currentCharacter_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, null=True, to=orm['main.Character']))

        # Changing field 'BaseItem.itemType'
        db.alter_column('main_baseitem', 'itemType_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, null=True, to=orm['main.ItemCategory']))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)"},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
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
            'itemType': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.DO_NOTHING', 'null': 'True', 'to': "orm['main.ItemCategory']"}),
            'magicalArmour': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'magicalEvasion': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'target': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'tier': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'main.baseitemability': {
            'Meta': {'object_name': 'BaseItemAbility'},
            'baseItem': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'abilities'", 'symmetrical': 'False', 'to': "orm['main.BaseItem']"}),
            'craftPoints': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'equippableTo': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tier': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'usedInCrafting': ('django.db.models.fields.BooleanField', [], {})
        },
        'main.baseskill': {
            'Meta': {'object_name': 'BaseSkill'},
            'aptitude': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.DO_NOTHING', 'null': 'True', 'to': "orm['main.Aptitude']"}),
            'attribute': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True', 'null': 'True'}),
            'halfRate': ('django.db.models.fields.BooleanField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True', 'null': 'True'}),
            'skillType': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True', 'null': 'True'}),
            'specialized': ('django.db.models.fields.BooleanField', [], {})
        },
        'main.character': {
            'Meta': {'object_name': 'Character'},
            'accessorySlot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedAccessories'", 'on_delete': 'models.DO_NOTHING', 'null': 'True', 'to': "orm['main.Item']"}),
            'accessorySlot2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedAccessories2'", 'on_delete': 'models.DO_NOTHING', 'null': 'True', 'to': "orm['main.Item']"}),
            'age': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'blank': 'True', 'null': 'True'}),
            'agility': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'}),
            'baseHP': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'}),
            'baseMP': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'}),
            'blurb': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True', 'null': 'True'}),
            'bodySlot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedBodies'", 'on_delete': 'models.DO_NOTHING', 'null': 'True', 'to': "orm['main.Item']"}),
            'bonusAptitudes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.Aptitude']"}),
            'characterImage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'characterImages'", 'null': 'True', 'to': "orm['main.ImageFile']"}),
            'gil': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'blank': 'True', 'null': 'True'}),
            'handSlot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedHands'", 'on_delete': 'models.DO_NOTHING', 'null': 'True', 'to': "orm['main.Item']"}),
            'headSlot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedHeads'", 'on_delete': 'models.DO_NOTHING', 'null': 'True', 'to': "orm['main.Item']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'characters'", 'on_delete': 'models.DO_NOTHING', 'null': 'True', 'to': "orm['main.Job']"}),
            'level': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'}),
            'magic': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'characters'", 'on_delete': 'models.DO_NOTHING', 'null': 'True', 'to': "orm['main.Race']"}),
            'secondWeaponSlot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedSecondaryWeapons'", 'on_delete': 'models.DO_NOTHING', 'null': 'True', 'to': "orm['main.Item']"}),
            'speed': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'}),
            'spirit': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'}),
            'strength': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'}),
            'traits': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.Trait']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'characters'", 'on_delete': 'models.DO_NOTHING', 'null': 'True', 'to': "orm['auth.User']"}),
            'vitality': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'}),
            'weaponSlot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedWeapons'", 'on_delete': 'models.DO_NOTHING', 'null': 'True', 'to': "orm['main.Item']"}),
            'xp': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'blank': 'True', 'null': 'True'})
        },
        'main.imagefile': {
            'Meta': {'object_name': 'ImageFile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '254'})
        },
        'main.item': {
            'Meta': {'object_name': 'Item'},
            'baseItem': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.DO_NOTHING', 'null': 'True', 'to': "orm['main.BaseItem']"}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'on_delete': 'models.DO_NOTHING', 'null': 'True', 'to': "orm['main.Character']"}),
            'damageAttribute': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'main.itemcategory': {
            'Meta': {'object_name': 'ItemCategory'},
            'baseSkill': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.DO_NOTHING', 'null': 'True', 'to': "orm['main.BaseSkill']"}),
            'craftPoints': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'subCategory': ('django.db.models.fields.IntegerField', [], {'max_length': '2'})
        },
        'main.job': {
            'Meta': {'object_name': 'Job'},
            'accuracyBonus': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'aptitude': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'on_delete': 'models.DO_NOTHING', 'blank': 'True', 'to': "orm['main.Aptitude']"}),
            'expertiseAttribute': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True', 'null': 'True'}),
            'expertiseSkill': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'on_delete': 'models.DO_NOTHING', 'blank': 'True', 'to': "orm['main.BaseSkill']"}),
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
            'baseSkill': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.DO_NOTHING', 'null': 'True', 'to': "orm['main.BaseSkill']"}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'skills'", 'on_delete': 'models.SET_NULL', 'null': 'True', 'to': "orm['main.Character']"}),
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
            'currentCharacter': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.DO_NOTHING', 'null': 'True', 'to': "orm['main.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['main']