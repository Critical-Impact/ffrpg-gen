# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'BaseSkill.aptitude'
        db.alter_column('main_baseskill', 'aptitude_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Aptitude'], null=True, on_delete=models.SET_NULL))

        # Changing field 'BaseItem.itemType'
        db.alter_column('main_baseitem', 'itemType_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.ItemCategory'], null=True, on_delete=models.SET_NULL))

        # Changing field 'ItemCategory.baseSkill'
        db.alter_column('main_itemcategory', 'baseSkill_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.BaseSkill'], null=True, on_delete=models.SET_NULL))

        # Changing field 'Item.character'
        db.alter_column('main_item', 'character_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Character'], null=True, on_delete=models.SET_NULL))

        # Changing field 'Item.baseItem'
        db.alter_column('main_item', 'baseItem_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.BaseItem'], null=True, on_delete=models.SET_NULL))

        # Changing field 'Character.bodySlot'
        db.alter_column('main_character', 'bodySlot_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Item'], null=True, on_delete=models.SET_NULL))

        # Changing field 'Character.handSlot'
        db.alter_column('main_character', 'handSlot_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Item'], null=True, on_delete=models.SET_NULL))

        # Changing field 'Character.weaponSlot'
        db.alter_column('main_character', 'weaponSlot_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Item'], null=True, on_delete=models.SET_NULL))

        # Changing field 'Character.headSlot'
        db.alter_column('main_character', 'headSlot_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Item'], null=True, on_delete=models.SET_NULL))

        # Changing field 'Character.secondWeaponSlot'
        db.alter_column('main_character', 'secondWeaponSlot_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Item'], null=True, on_delete=models.SET_NULL))

        # Changing field 'Character.job'
        db.alter_column('main_character', 'job_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Job'], null=True, on_delete=models.SET_NULL))

        # Changing field 'Character.race'
        db.alter_column('main_character', 'race_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Race'], null=True, on_delete=models.SET_NULL))

        # Changing field 'Character.accessorySlot2'
        db.alter_column('main_character', 'accessorySlot2_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Item'], null=True, on_delete=models.SET_NULL))

        # Changing field 'Character.accessorySlot'
        db.alter_column('main_character', 'accessorySlot_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Item'], null=True, on_delete=models.SET_NULL))

        # Changing field 'UserProfile.currentCharacter'
        db.alter_column('main_userprofile', 'currentCharacter_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Character'], null=True, on_delete=models.SET_NULL))

        # Changing field 'Skill.character'
        db.alter_column('main_skill', 'character_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Character'], null=True, on_delete=models.SET_NULL))

        # Changing field 'Skill.baseSkill'
        db.alter_column('main_skill', 'baseSkill_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.BaseSkill'], null=True, on_delete=models.SET_NULL))

        # Changing field 'Job.expertiseSkill'
        db.alter_column('main_job', 'expertiseSkill_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.BaseSkill'], null=True, on_delete=models.SET_NULL))

        # Changing field 'Job.aptitude'
        db.alter_column('main_job', 'aptitude_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Aptitude'], null=True, on_delete=models.SET_NULL))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'BaseSkill.aptitude'
        raise RuntimeError("Cannot reverse this migration. 'BaseSkill.aptitude' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'BaseSkill.aptitude'
        db.alter_column('main_baseskill', 'aptitude_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Aptitude']))

        # User chose to not deal with backwards NULL issues for 'BaseItem.itemType'
        raise RuntimeError("Cannot reverse this migration. 'BaseItem.itemType' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'BaseItem.itemType'
        db.alter_column('main_baseitem', 'itemType_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.ItemCategory']))

        # Changing field 'ItemCategory.baseSkill'
        db.alter_column('main_itemcategory', 'baseSkill_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.BaseSkill'], null=True))

        # User chose to not deal with backwards NULL issues for 'Item.character'
        raise RuntimeError("Cannot reverse this migration. 'Item.character' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Item.character'
        db.alter_column('main_item', 'character_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Character']))

        # User chose to not deal with backwards NULL issues for 'Item.baseItem'
        raise RuntimeError("Cannot reverse this migration. 'Item.baseItem' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Item.baseItem'
        db.alter_column('main_item', 'baseItem_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.BaseItem']))

        # Changing field 'Character.bodySlot'
        db.alter_column('main_character', 'bodySlot_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Item'], null=True))

        # Changing field 'Character.handSlot'
        db.alter_column('main_character', 'handSlot_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Item'], null=True))

        # Changing field 'Character.weaponSlot'
        db.alter_column('main_character', 'weaponSlot_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Item'], null=True))

        # Changing field 'Character.headSlot'
        db.alter_column('main_character', 'headSlot_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Item'], null=True))

        # Changing field 'Character.secondWeaponSlot'
        db.alter_column('main_character', 'secondWeaponSlot_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Item'], null=True))

        # User chose to not deal with backwards NULL issues for 'Character.job'
        raise RuntimeError("Cannot reverse this migration. 'Character.job' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Character.job'
        db.alter_column('main_character', 'job_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Job']))

        # User chose to not deal with backwards NULL issues for 'Character.race'
        raise RuntimeError("Cannot reverse this migration. 'Character.race' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Character.race'
        db.alter_column('main_character', 'race_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Race']))

        # Changing field 'Character.accessorySlot2'
        db.alter_column('main_character', 'accessorySlot2_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Item'], null=True))

        # Changing field 'Character.accessorySlot'
        db.alter_column('main_character', 'accessorySlot_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Item'], null=True))

        # Changing field 'UserProfile.currentCharacter'
        db.alter_column('main_userprofile', 'currentCharacter_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Character'], null=True))

        # User chose to not deal with backwards NULL issues for 'Skill.character'
        raise RuntimeError("Cannot reverse this migration. 'Skill.character' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Skill.character'
        db.alter_column('main_skill', 'character_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Character']))

        # User chose to not deal with backwards NULL issues for 'Skill.baseSkill'
        raise RuntimeError("Cannot reverse this migration. 'Skill.baseSkill' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Skill.baseSkill'
        db.alter_column('main_skill', 'baseSkill_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.BaseSkill']))

        # Changing field 'Job.expertiseSkill'
        db.alter_column('main_job', 'expertiseSkill_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.BaseSkill'], null=True))

        # Changing field 'Job.aptitude'
        db.alter_column('main_job', 'aptitude_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Aptitude'], null=True))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True', 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True', 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
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
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '20'})
        },
        'main.baseitem': {
            'Meta': {'object_name': 'BaseItem'},
            'armour': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'availability': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cost': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'damageAttribute': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '3'}),
            'damageDieCount': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '10'}),
            'damageDieSize': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '10'}),
            'damageScale': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'evasion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemSlot': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'max_length': '2'}),
            'itemType': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.ItemCategory']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'magicalArmour': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'magicalEvasion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'target': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'tier': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'main.baseitemability': {
            'Meta': {'object_name': 'BaseItemAbility'},
            'baseItem': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.BaseItem']", 'symmetrical': 'False', 'related_name': "'abilities'"}),
            'craftPoints': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'equippableTo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tier': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'usedInCrafting': ('django.db.models.fields.BooleanField', [], {})
        },
        'main.baseskill': {
            'Meta': {'object_name': 'BaseSkill'},
            'aptitude': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Aptitude']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'attribute': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '20'}),
            'halfRate': ('django.db.models.fields.BooleanField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '20'}),
            'skillType': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '20'}),
            'specialized': ('django.db.models.fields.BooleanField', [], {})
        },
        'main.character': {
            'Meta': {'object_name': 'Character'},
            'accessorySlot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Item']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'related_name': "'equippedAccessories'"}),
            'accessorySlot2': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Item']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'related_name': "'equippedAccessories2'"}),
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'max_length': '4'}),
            'agility': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'max_length': '3'}),
            'baseHP': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'max_length': '3'}),
            'baseMP': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'max_length': '3'}),
            'blurb': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '1000'}),
            'bodySlot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Item']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'related_name': "'equippedBodies'"}),
            'bonusAptitudes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.Aptitude']", 'symmetrical': 'False'}),
            'characterImage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.ImageFile']", 'null': 'True', 'related_name': "'characterImages'"}),
            'gil': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'max_length': '10'}),
            'handSlot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Item']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'related_name': "'equippedHands'"}),
            'headSlot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Item']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'related_name': "'equippedHeads'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Job']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'related_name': "'characters'"}),
            'level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'max_length': '3'}),
            'magic': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'max_length': '3'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Race']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'related_name': "'characters'"}),
            'secondWeaponSlot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Item']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'related_name': "'equippedSecondaryWeapons'"}),
            'speed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'max_length': '3'}),
            'spirit': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'max_length': '3'}),
            'strength': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'max_length': '3'}),
            'traits': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.Trait']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'related_name': "'characters'"}),
            'vitality': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'max_length': '3'}),
            'weaponSlot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Item']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'related_name': "'equippedWeapons'"}),
            'xp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'max_length': '10'})
        },
        'main.imagefile': {
            'Meta': {'object_name': 'ImageFile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '254'})
        },
        'main.item': {
            'Meta': {'object_name': 'Item'},
            'baseItem': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BaseItem']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Character']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'related_name': "'items'"}),
            'damageAttribute': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'main.itemcategory': {
            'Meta': {'object_name': 'ItemCategory'},
            'baseSkill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BaseSkill']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'craftPoints': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'subCategory': ('django.db.models.fields.IntegerField', [], {'max_length': '2'})
        },
        'main.job': {
            'Meta': {'object_name': 'Job'},
            'accuracyBonus': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'aptitude': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Aptitude']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'expertiseAttribute': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '20'}),
            'expertiseSkill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BaseSkill']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
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
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '20'}),
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
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '20'}),
            'nightVision': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'smell': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
        },
        'main.skill': {
            'Meta': {'object_name': 'Skill'},
            'baseSkill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BaseSkill']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Character']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'related_name': "'skills'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'specialization': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '20'})
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
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['main']