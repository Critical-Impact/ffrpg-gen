# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MonsterAttack'
        db.create_table('main_monsterattack', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('monster', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Character'])),
            ('name', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255, null=True)),
            ('actionType', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True)),
            ('attackType', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True)),
            ('target', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True)),
            ('damageAttribute', self.gf('django.db.models.fields.CharField')(blank=True, max_length=3, null=True)),
            ('damageType', self.gf('django.db.models.fields.CharField')(blank=True, max_length=4, null=True)),
            ('combatStat', self.gf('django.db.models.fields.CharField')(blank=True, max_length=3, null=True)),
            ('combatStatModifier', self.gf('django.db.models.fields.CharField')(blank=True, max_length=3, null=True)),
            ('statusStat', self.gf('django.db.models.fields.CharField')(blank=True, max_length=3, null=True)),
            ('statusStatModifier', self.gf('django.db.models.fields.CharField')(blank=True, max_length=3, null=True)),
        ))
        db.send_create_signal('main', ['MonsterAttack'])

        # Adding M2M table for field modifiers on 'MonsterAttack'
        m2m_table_name = db.shorten_name('main_monsterattack_modifiers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('monsterattack', models.ForeignKey(orm['main.monsterattack'], null=False)),
            ('monsterattackmodifier', models.ForeignKey(orm['main.monsterattackmodifier'], null=False))
        ))
        db.create_unique(m2m_table_name, ['monsterattack_id', 'monsterattackmodifier_id'])

        # Adding model 'MonsterAttackModifier'
        db.create_table('main_monsterattackmodifier', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255, null=True)),
            ('xpModifier', self.gf('django.db.models.fields.IntegerField')()),
            ('gilModifier', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('main', ['MonsterAttackModifier'])

        # Adding field 'BaseSkill.isMonsterSkill'
        db.add_column('main_baseskill', 'isMonsterSkill',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.category'
        db.add_column('main_character', 'category',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=200, null=True),
                      keep_default=False)

        # Adding field 'Character.family'
        db.add_column('main_character', 'family',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=200, null=True),
                      keep_default=False)

        # Adding field 'Character.location'
        db.add_column('main_character', 'location',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=200, null=True),
                      keep_default=False)

        # Adding field 'Character.intelligence'
        db.add_column('main_character', 'intelligence',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=200, null=True),
                      keep_default=False)

        # Adding field 'Character.reaction'
        db.add_column('main_character', 'reaction',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'Character.frequency'
        db.add_column('main_character', 'frequency',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'Character.encounterSizeMonsters'
        db.add_column('main_character', 'encounterSizeMonsters',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'Character.encounterSizePCs'
        db.add_column('main_character', 'encounterSizePCs',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'Character.monsterType'
        db.add_column('main_character', 'monsterType',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'Character.hitBase'
        db.add_column('main_character', 'hitBase',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'Character.magicBase'
        db.add_column('main_character', 'magicBase',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'Character.armourBase'
        db.add_column('main_character', 'armourBase',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'Character.magicArmourBase'
        db.add_column('main_character', 'magicArmourBase',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'MonsterAttack'
        db.delete_table('main_monsterattack')

        # Removing M2M table for field modifiers on 'MonsterAttack'
        db.delete_table(db.shorten_name('main_monsterattack_modifiers'))

        # Deleting model 'MonsterAttackModifier'
        db.delete_table('main_monsterattackmodifier')

        # Deleting field 'BaseSkill.isMonsterSkill'
        db.delete_column('main_baseskill', 'isMonsterSkill')

        # Deleting field 'Character.category'
        db.delete_column('main_character', 'category')

        # Deleting field 'Character.family'
        db.delete_column('main_character', 'family')

        # Deleting field 'Character.location'
        db.delete_column('main_character', 'location')

        # Deleting field 'Character.intelligence'
        db.delete_column('main_character', 'intelligence')

        # Deleting field 'Character.reaction'
        db.delete_column('main_character', 'reaction')

        # Deleting field 'Character.frequency'
        db.delete_column('main_character', 'frequency')

        # Deleting field 'Character.encounterSizeMonsters'
        db.delete_column('main_character', 'encounterSizeMonsters')

        # Deleting field 'Character.encounterSizePCs'
        db.delete_column('main_character', 'encounterSizePCs')

        # Deleting field 'Character.monsterType'
        db.delete_column('main_character', 'monsterType')

        # Deleting field 'Character.hitBase'
        db.delete_column('main_character', 'hitBase')

        # Deleting field 'Character.magicBase'
        db.delete_column('main_character', 'magicBase')

        # Deleting field 'Character.armourBase'
        db.delete_column('main_character', 'armourBase')

        # Deleting field 'Character.magicArmourBase'
        db.delete_column('main_character', 'magicArmourBase')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True', 'related_name': "'user_set'", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'related_name': "'user_set'", 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
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
            'itemType': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.PROTECT', 'to': "orm['main.ItemCategory']", 'null': 'True'}),
            'magicalArmour': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'magicalEvasion': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'target': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'tier': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'})
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
            'aptitude': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.PROTECT', 'to': "orm['main.Aptitude']", 'null': 'True'}),
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
            'accessorySlot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedAccessories'", 'on_delete': 'models.SET_NULL', 'to': "orm['main.Item']", 'null': 'True'}),
            'accessorySlot2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedAccessories2'", 'on_delete': 'models.SET_NULL', 'to': "orm['main.Item']", 'null': 'True'}),
            'age': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '4', 'null': 'True'}),
            'agility': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'armourBase': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'baseHP': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'baseMP': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'blurb': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '1000', 'null': 'True'}),
            'bodySlot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedBodies'", 'on_delete': 'models.SET_NULL', 'to': "orm['main.Item']", 'null': 'True'}),
            'bonusAptitudes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.Aptitude']", 'symmetrical': 'False'}),
            'category': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'characterImage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'characterImages'", 'on_delete': 'models.SET_NULL', 'to': "orm['main.ImageFile']", 'null': 'True'}),
            'encounterSizeMonsters': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'encounterSizePCs': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'family': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'frequency': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'gil': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '10', 'null': 'True'}),
            'handSlot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedHands'", 'on_delete': 'models.SET_NULL', 'to': "orm['main.Item']", 'null': 'True'}),
            'headSlot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedHeads'", 'on_delete': 'models.SET_NULL', 'to': "orm['main.Item']", 'null': 'True'}),
            'hitBase': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intelligence': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'characters'", 'on_delete': 'models.SET_NULL', 'to': "orm['main.Job']", 'null': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'magic': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'magicArmourBase': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'magicBase': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'monsterType': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'characters'", 'on_delete': 'models.SET_NULL', 'to': "orm['main.Race']", 'null': 'True'}),
            'reaction': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'secondWeaponSlot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedSecondaryWeapons'", 'on_delete': 'models.SET_NULL', 'to': "orm['main.Item']", 'null': 'True'}),
            'speed': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'spirit': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'strength': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'traits': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.Trait']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'characters'", 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']", 'null': 'True'}),
            'vitality': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'weaponSlot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equippedWeapons'", 'on_delete': 'models.SET_NULL', 'to': "orm['main.Item']", 'null': 'True'}),
            'xp': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'max_length': '10', 'null': 'True'})
        },
        'main.imagefile': {
            'Meta': {'object_name': 'ImageFile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '254'})
        },
        'main.item': {
            'Meta': {'object_name': 'Item'},
            'baseItem': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.PROTECT', 'to': "orm['main.BaseItem']", 'null': 'True'}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': "orm['main.Character']", 'null': 'True'}),
            'damageAttribute': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'main.itemcategory': {
            'Meta': {'object_name': 'ItemCategory'},
            'baseSkill': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.PROTECT', 'to': "orm['main.BaseSkill']", 'null': 'True'}),
            'craftPoints': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True'}),
            'defaultItemSlot': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'subCategory': ('django.db.models.fields.IntegerField', [], {'max_length': '2'})
        },
        'main.job': {
            'Meta': {'object_name': 'Job'},
            'accuracyBonus': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'aptitude': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['main.Aptitude']", 'null': 'True'}),
            'expertiseAttribute': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'expertiseSkill': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['main.BaseSkill']", 'null': 'True'}),
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
            'combatStat': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'combatStatModifier': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'damageAttribute': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'damageType': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '4', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modifiers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.MonsterAttackModifier']", 'symmetrical': 'False'}),
            'monster': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Character']"}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'statusStat': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'statusStatModifier': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '3', 'null': 'True'}),
            'target': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'main.monsterattackmodifier': {
            'Meta': {'object_name': 'MonsterAttackModifier'},
            'gilModifier': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
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
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'nightVision': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'smell': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
        },
        'main.skill': {
            'Meta': {'object_name': 'Skill'},
            'baseSkill': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.PROTECT', 'to': "orm['main.BaseSkill']", 'null': 'True'}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'skills'", 'to': "orm['main.Character']", 'null': 'True'}),
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
            'currentCharacter': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'to': "orm['main.Character']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['main']