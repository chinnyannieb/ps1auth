# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Transaction.status'
        db.alter_column('paypal_integration_transaction', 'status', self.gf('django.db.models.fields.CharField')(max_length=33))

    def backwards(self, orm):

        # Changing field 'Transaction.status'
        db.alter_column('paypal_integration_transaction', 'status', self.gf('django.db.models.fields.CharField')(max_length=32))

    models = {
        'paypal_integration.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'amount': ('djmoney.models.fields.MoneyField', [], {'max_digits': '10', 'decimal_places': '2', 'default_currency': "'XYZ'"}),
            'amount_currency': ('djmoney.models.fields.CurrencyField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fee_amount': ('djmoney.models.fields.MoneyField', [], {'max_digits': '10', 'decimal_places': '2', 'default_currency': "'XYZ'"}),
            'fee_amount_currency': ('djmoney.models.fields.CurrencyField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'net_amount': ('djmoney.models.fields.MoneyField', [], {'max_digits': '10', 'decimal_places': '2', 'default_currency': "'XYZ'"}),
            'net_amount_currency': ('djmoney.models.fields.CurrencyField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '33'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['paypal_integration']