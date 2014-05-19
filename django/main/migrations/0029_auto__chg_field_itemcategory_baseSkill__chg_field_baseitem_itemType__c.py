# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ItemCategory.baseSkill'
        db.alter_column('main_itemcategory', 'baseSkill_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.BaseSkill'], on_delete=models.PROTECT, null=True))

        # Changing field 'BaseItem.itemType'
        db.alter_column('main_baseitem', 'itemType_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.ItemCategory'], on_delete=models.PROTECT, null=True))

        # Changing field 'BaseSkill.aptitude'
        db.alter_column('main_baseskill', 'aptitude_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Aptitude'], on_delete=models.PROTECT, null=True))

        # Changing field 'UserProfile.currentCharacter'
        db.alter_column('main_userprofile', 'currentCharacter_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Character'], on_delete=models.SET_NULL, null=True))

        # Changing field 'Item.baseItem'
        db.alter_column('main_item', 'baseItem_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.BaseItem'], on_delete=models.PROTECT, null=True))

        # Changing field 'Item.character'
        db.alter_column('main_item', 'character_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Character'], null=True))

        # Changing field 'Job.aptitude'
        db.alter_column('main_job', 'aptitude_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Aptitude'], on_delete=models.PROTECT, null=True))

        # Changing field 'Job.expertiseSkill'
        db.alter_column('main_job', 'expertiseSkill_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.BaseSkill'], on_delete=models.PROTECT, null=True))

        # Changing field 'Skill.baseSkill'
        db.alter_column('main_skill', 'baseSkill_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.BaseSkill'], on_delete=models.PROTECT, null=True))

        # Changing field 'Skill.character'
        db.alter_column('main_skill', 'character_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Character'], null=True))

        # Changing field 'Character.characterImage'
        db.alter_column('main_character', 'characterImage_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.ImageFile'], on_delete=models.SET_NULL, null=True))

        # Changing field 'Character.bodySlot'
        db.alter_column('main_character', 'bodySlot_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Item'], on_delete=models.SET_NULL, null=True))

        # Changing field 'Character.accessorySlot'
        db.alter_column('main_character', 'accessorySlot_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Item'], on_delete=models.SET_NULL, null=True))

        # Changing field 'Character.handSlot'
        db.alter_column('main_character', 'handSlot_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Item'], on_delete=models.SET_NULL, null=True))

        # Changing field 'Character.headSlot'
        db.alter_column('main_character', 'headSlot_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Item'], on_delete=models.SET_NULL, null=True))

        # Changing field 'Character.accessorySlot2'
        db.alter_column('main_character', 'accessorySlot2_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Item'], on_delete=models.SET_NULL, null=True))

        # Changing field 'Character.race'
        db.alter_column('main_character', 'race_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Race'], on_delete=models.SET_NULL, null=True))

        # Changing field 'Character.job'
        db.alter_column('main_character', 'job_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Job'], on_delete=models.SET_NULL, null=True))

        # Changing field 'Character.user'
        db.alter_column('main_character', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], on_delete=models.SET_NULL, null=True))

        # Changing field 'Character.secondWeaponSlot'
        db.alter_column('main_character', 'secondWeaponSlot_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Item'], on_delete=models.SET_NULL, null=True))

        # Changing field 'Character.weaponSlot'
        db.alter_column('main_character', 'weaponSlot_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Item'], on_delete=models.SET_NULL, null=True))

    def backwards(self, orm):

        # Changing field 'ItemCategory.baseSkill'
        db.alter_column('main_itemcategory', 'baseSkill_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.BaseSkill'], on_delete=models.DO_NOTHING, null=True))

        # Changing field 'BaseItem.itemType'
        db.alter_column('main_baseitem', 'itemType_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.ItemCategory'], on_delete=models.DO_NOTHING, null=True))

        # Changing field 'BaseSkill.aptitude'
        db.alter_column('main_baseskill', 'aptitude_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Aptitude'], on_delete=models.DO_NOTHING, null=True))

        # Changing field 'UserProfile.currentCharacter'
        db.alter_column('main_userprofile', 'currentCharacter_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Character'], on_delete=models.DO_NOTHING, null=True))

        # Changing field 'Item.baseItem'
        db.alter_column('main_item', 'baseItem_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.BaseItem'], on_delete=models.DO_NOTHING, null=True))

        # Changing field 'Item.character'
        db.alter_column('main_item', 'character_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, to=orm['main.Character'], null=True))

        # Changing field 'Job.aptitude'
        db.alter_column('main_job', 'aptitude_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, to=orm['main.Aptitude'], null=True))

        # Changing field 'Job.expertiseSkill'
        db.alter_column('main_job', 'expertiseSkill_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, to=orm['main.BaseSkill'], null=True))

        # Changing field 'Skill.baseSkill'
        db.alter_column('main_skill', 'baseSkill_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.BaseSkill'], on_delete=models.DO_NOTHING, null=True))

        # Changing field 'Skill.character'
        db.alter_column('main_skill', 'character_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, to=orm['main.Character'], null=True))

        # Changing field 'Character.characterImage'
        db.alter_column('main_character', 'characterImage_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.ImageFile'], null=True))

        # Changing field 'Character.bodySlot'
        db.alter_column('main_character', 'bodySlot_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, to=orm['main.Item'], null=True))

        # Changing field 'Character.accessorySlot'
        db.alter_column('main_character', 'accessorySlot_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, to=orm['main.Item'], null=True))

        # Changing field 'Character.handSlot'
        db.alter_column('main_character', 'handSlot_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, to=orm['main.Item'], null=True))

        # Changing field 'Character.headSlot'
        db.alter_column('main_character', 'headSlot_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, to=orm['main.Item'], null=True))

        # Changing field 'Character.accessorySlot2'
        db.alter_column('main_character', 'accessorySlot2_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, to=orm['main.Item'], null=True))

        # Changing field 'Character.race'
        db.alter_column('main_character', 'race_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, to=orm['main.Race'], null=True))

        # Changing field 'Character.job'
        db.alter_column('main_character', 'job_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, to=orm['main.Job'], null=True))

        # Changing field 'Character.user'
        db.alter_column('main_character', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, to=orm['auth.User'], null=True))

        # Changing field 'Character.secondWeaponSlot'
        db.alter_column('main_character', 'secondWeaponSlot_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, to=orm['main.Item'], null=True))

        # Changing field 'Character.weaponSlot'
        db.alter_column('main_character', 'weaponSlot_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.DO_NOTHING, to=orm['main.Item'], null=True))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
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
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'related_name': "'user_set'", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'related_name': "'user_set'", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'db_table': "'django_content_type'"},
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
            'tier': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'main.baseitemability': {
            'Meta': {'object_name': 'BaseItemAbility'},
            'baseItem': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.BaseItem']", 'related_name': "'abilities'", 'symmetrical': 'False'}),
            'craftPoints': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'equippableTo': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tier': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'usedInCrafting': ('django.db.models.fields.BooleanField', [], {})
        },
        'main.baseskill': {
            'Meta': {'object_name': 'BaseSkill'},
            'aptitude': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Aptitude']", 'on_delete': 'models.PROTECT', 'null': 'True'}),
            'attribute': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'halfRate': ('django.db.models.fields.BooleanField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'baseHP': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'baseMP': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'blurb': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '1000', 'null': 'True'}),
            'bodySlot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Item']", 'on_delete': 'models.SET_NULL', 'related_name': "'equippedBodies'", 'null': 'True'}),
            'bonusAptitudes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.Aptitude']", 'symmetrical': 'False'}),
            'characterImage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.ImageFile']", 'on_delete': 'models.SET_NULL', 'related_name': "'characterImages'", 'null': 'True'}),
            'gil': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '10', 'null': 'True'}),
            'handSlot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Item']", 'on_delete': 'models.SET_NULL', 'related_name': "'equippedHands'", 'null': 'True'}),
            'headSlot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Item']", 'on_delete': 'models.SET_NULL', 'related_name': "'equippedHeads'", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Job']", 'on_delete': 'models.SET_NULL', 'related_name': "'characters'", 'null': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'magic': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Race']", 'on_delete': 'models.SET_NULL', 'related_name': "'characters'", 'null': 'True'}),
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'subCategory': ('django.db.models.fields.IntegerField', [], {'max_length': '2'})
        },
        'main.job': {
            'Meta': {'object_name': 'Job'},
            'accuracyBonus': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'aptitude': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Aptitude']", 'on_delete': 'models.PROTECT', 'blank': 'True', 'null': 'True'}),
            'expertiseAttribute': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'expertiseSkill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BaseSkill']", 'on_delete': 'models.PROTECT', 'blank': 'True', 'null': 'True'}),
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
            'currentCharacter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Character']", 'on_delete': 'models.SET_NULL', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['main']