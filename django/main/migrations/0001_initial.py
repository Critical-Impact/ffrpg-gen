# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Character'
        db.create_table('main_character', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=100)),
            ('age', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True, max_length=4)),
            ('blurb', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=1000)),
            ('strength', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True, max_length=3)),
            ('vitality', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True, max_length=3)),
            ('agility', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True, max_length=3)),
            ('speed', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True, max_length=3)),
            ('magic', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True, max_length=3)),
            ('spirit', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True, max_length=3)),
            ('baseHP', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True, max_length=3)),
            ('baseMP', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True, max_length=3)),
            ('level', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True, max_length=3)),
            ('xp', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True, max_length=10)),
            ('gil', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True, max_length=10)),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(related_name='characters', to=orm['main.Job'])),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(related_name='characters', to=orm['main.Race'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='characters', to=orm['auth.User'], null=True)),
        ))
        db.send_create_signal('main', ['Character'])

        # Adding model 'OverviewBox'
        db.create_table('main_overviewbox', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('viewName', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('main', ['OverviewBox'])

        # Adding model 'OverviewBoxSetting'
        db.create_table('main_overviewboxsetting', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('overviewBox', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.OverviewBox'])),
            ('spanFull', self.gf('django.db.models.fields.BooleanField')()),
            ('enabled', self.gf('django.db.models.fields.BooleanField')()),
            ('sortOrder', self.gf('django.db.models.fields.IntegerField')()),
            ('character', self.gf('django.db.models.fields.related.ForeignKey')(related_name='overviewBoxSettings', to=orm['main.Character'])),
        ))
        db.send_create_signal('main', ['OverviewBoxSetting'])

        # Adding model 'Race'
        db.create_table('main_race', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=20)),
            ('maxStrength', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('maxVitality', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('maxAgility', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('maxSpeed', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('maxMagic', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('maxSpirit', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('dayVision', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('nightVision', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('smell', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('hearing', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('lifeSense', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('magicSense', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
        ))
        db.send_create_signal('main', ['Race'])

        # Adding model 'Job'
        db.create_table('main_job', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=20)),
            ('hpDie', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('mpDie', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('hasMP', self.gf('django.db.models.fields.BooleanField')()),
            ('strength', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('vitality', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('agility', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('speed', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('magic', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('spirit', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('accuracyBonus', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('skillPoints', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('aptitude', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['main.Aptitude'], null=True)),
        ))
        db.send_create_signal('main', ['Job'])

        # Adding M2M table for field armor on 'Job'
        m2m_table_name = db.shorten_name('main_job_armor')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('job', models.ForeignKey(orm['main.job'], null=False)),
            ('armourcategory', models.ForeignKey(orm['main.armourcategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['job_id', 'armourcategory_id'])

        # Adding M2M table for field weapons on 'Job'
        m2m_table_name = db.shorten_name('main_job_weapons')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('job', models.ForeignKey(orm['main.job'], null=False)),
            ('weaponcategory', models.ForeignKey(orm['main.weaponcategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['job_id', 'weaponcategory_id'])

        # Adding model 'ArmourCategory'
        db.create_table('main_armourcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=20)),
        ))
        db.send_create_signal('main', ['ArmourCategory'])

        # Adding model 'WeaponCategory'
        db.create_table('main_weaponcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=20)),
            ('baseSkill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.BaseSkill'])),
        ))
        db.send_create_signal('main', ['WeaponCategory'])

        # Adding model 'Aptitude'
        db.create_table('main_aptitude', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=20)),
        ))
        db.send_create_signal('main', ['Aptitude'])

        # Adding model 'BaseSkill'
        db.create_table('main_baseskill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('aptitude', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Aptitude'])),
            ('name', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=20)),
            ('attribute', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=20)),
            ('skillType', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=20)),
            ('specialized', self.gf('django.db.models.fields.BooleanField')()),
            ('halfRate', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('main', ['BaseSkill'])

        # Adding model 'Skill'
        db.create_table('main_skill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('baseSkill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.BaseSkill'])),
            ('character', self.gf('django.db.models.fields.related.ForeignKey')(related_name='skills', to=orm['main.Character'])),
            ('specialization', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=20)),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('main', ['Skill'])


    def backwards(self, orm):
        # Deleting model 'Character'
        db.delete_table('main_character')

        # Deleting model 'OverviewBox'
        db.delete_table('main_overviewbox')

        # Deleting model 'OverviewBoxSetting'
        db.delete_table('main_overviewboxsetting')

        # Deleting model 'Race'
        db.delete_table('main_race')

        # Deleting model 'Job'
        db.delete_table('main_job')

        # Removing M2M table for field armor on 'Job'
        db.delete_table(db.shorten_name('main_job_armor'))

        # Removing M2M table for field weapons on 'Job'
        db.delete_table(db.shorten_name('main_job_weapons'))

        # Deleting model 'ArmourCategory'
        db.delete_table('main_armourcategory')

        # Deleting model 'WeaponCategory'
        db.delete_table('main_weaponcategory')

        # Deleting model 'Aptitude'
        db.delete_table('main_aptitude')

        # Deleting model 'BaseSkill'
        db.delete_table('main_baseskill')

        # Deleting model 'Skill'
        db.delete_table('main_skill')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']"})
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Group']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'}),
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
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'})
        },
        'main.armourcategory': {
            'Meta': {'object_name': 'ArmourCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'})
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
            'age': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '4'}),
            'agility': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'baseHP': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'baseMP': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'blurb': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '1000'}),
            'gil': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'characters'", 'to': "orm['main.Job']"}),
            'level': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'magic': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'characters'", 'to': "orm['main.Race']"}),
            'speed': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'spirit': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'strength': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'characters'", 'to': "orm['auth.User']", 'null': 'True'}),
            'vitality': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'xp': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '10'})
        },
        'main.job': {
            'Meta': {'object_name': 'Job'},
            'accuracyBonus': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'agility': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'aptitude': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['main.Aptitude']", 'null': 'True'}),
            'armor': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.ArmourCategory']"}),
            'hasMP': ('django.db.models.fields.BooleanField', [], {}),
            'hpDie': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'magic': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'mpDie': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'skillPoints': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'speed': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'spirit': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'strength': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'vitality': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'weapons': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.WeaponCategory']"})
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
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'nightVision': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'smell': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
        },
        'main.skill': {
            'Meta': {'object_name': 'Skill'},
            'baseSkill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BaseSkill']"}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'skills'", 'to': "orm['main.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'specialization': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'})
        },
        'main.weaponcategory': {
            'Meta': {'object_name': 'WeaponCategory'},
            'baseSkill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BaseSkill']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'})
        }
    }

    complete_apps = ['main']