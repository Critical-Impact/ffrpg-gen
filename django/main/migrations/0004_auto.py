# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field armor on 'Job'
        db.delete_table(db.shorten_name('main_job_armor'))

        # Adding M2M table for field armour on 'Job'
        m2m_table_name = db.shorten_name('main_job_armour')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('job', models.ForeignKey(orm['main.job'], null=False)),
            ('armourcategory', models.ForeignKey(orm['main.armourcategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['job_id', 'armourcategory_id'])


    def backwards(self, orm):
        # Adding M2M table for field armor on 'Job'
        m2m_table_name = db.shorten_name('main_job_armor')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('job', models.ForeignKey(orm['main.job'], null=False)),
            ('armourcategory', models.ForeignKey(orm['main.armourcategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['job_id', 'armourcategory_id'])

        # Removing M2M table for field armour on 'Job'
        db.delete_table(db.shorten_name('main_job_armour'))


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'related_name': "'user_set'", 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'related_name': "'user_set'", 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
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
            'user': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'characters'", 'to': "orm['auth.User']"}),
            'vitality': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'xp': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True', 'max_length': '10'})
        },
        'main.job': {
            'Meta': {'object_name': 'Job'},
            'accuracyBonus': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'agility': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'aptitude': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['main.Aptitude']", 'null': 'True'}),
            'armour': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.ArmourCategory']", 'symmetrical': 'False'}),
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
            'weapons': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.WeaponCategory']", 'symmetrical': 'False'})
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
        'main.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'currentCharacter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Character']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'main.weaponcategory': {
            'Meta': {'object_name': 'WeaponCategory'},
            'baseSkill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BaseSkill']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'})
        }
    }

    complete_apps = ['main']