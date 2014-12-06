# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'EmailAttachement.name'
        db.add_column('crm_emailattachement', 'name',
                      self.gf('django.db.models.fields.CharField')(default='fixme', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'EmailAttachement.name'
        db.delete_column('crm_emailattachement', 'name')


    models = {
        'accounts.ps1user': {
            'Meta': {'object_name': 'PS1User'},
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'object_guid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '48', 'primary_key': 'True', 'db_index': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'crm.cash': {
            'Meta': {'object_name': 'Cash'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paid_up_until': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'person': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['crm.CRMPerson']", 'unique': 'True', 'null': 'True'})
        },
        'crm.crmperson': {
            'Meta': {'object_name': 'CRMPerson'},
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_check_1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'id_checker_1'", 'null': 'True', 'to': "orm['accounts.PS1User']"}),
            'id_check_2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'id_checker_2'", 'null': 'True', 'to': "orm['accounts.PS1User']"}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'membership_start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'membership_status': ('django.db.models.fields.CharField', [], {'default': "'discontinued'", 'max_length': '128'}),
            'street_address': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['accounts.PS1User']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'crm.emailattachement': {
            'Meta': {'object_name': 'EmailAttachement'},
            'email': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'attachments'", 'to': "orm['crm.EmailTemplate']"}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'crm.emailrecord': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'EmailRecord'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'from_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.CRMPerson']"}),
            'reply_to_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.PS1User']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'pending'", 'max_length': '30'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'to_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'})
        },
        'crm.emailtemplate': {
            'Meta': {'object_name': 'EmailTemplate'},
            'from_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('ckeditor.fields.RichTextField', [], {}),
            'recipients': ('django.db.models.fields.CharField', [], {'default': "'full_members'", 'max_length': '128'}),
            'reply_to_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'crm.note': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Note'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.CRMPerson']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'crm.paypal': {
            'Meta': {'object_name': 'PayPal'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paid_up_until': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['crm.CRMPerson']", 'unique': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['crm']
