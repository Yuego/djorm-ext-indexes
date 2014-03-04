#coding: utf-8
from __future__ import unicode_literals, absolute_import

import sys
from django.db.backends.postgresql_psycopg2.creation import DatabaseCreation

try:
    import psycopg2
except ImportError:
    print("psycopg2 import error, djorm_indexes modulue "
          "is only compatible with postgresql_psycopg2 backend")
    sys.exit(-1)

from djorm_pgarray.fields import ArrayField

try:
    from djorm_hstore.fields import HStoreField
except ImportError:
    HStoreField = type('FakeField')

pg_fields = (ArrayField, HStoreField)

if not hasattr(DatabaseCreation, '_sql_indexes_for_field'):
    def sql_indexes_for_field(self, model, f, style):
        qn = self.connection.ops.quote_name
        db_table = model._meta.db_table

        if isinstance(f, pg_fields) and f.db_index:
            output = [(style.SQL_KEYWORD('CREATE INDEX ') +
                       style.SQL_TABLE(qn('%s_%s_gin' % (db_table, f.column))) +
                       style.SQL_KEYWORD(' ON ') +
                       style.SQL_TABLE(qn(db_table)) +
                       style.SQL_KEYWORD(' USING ') +
                       style.SQL_COLTYPE('GIN') + ' ( ' +
                       style.SQL_FIELD(qn(f.column)) + ' );')]
        else:
            output = self._sql_indexes_for_field(model, f, style)

        return output

    DatabaseCreation._sql_indexes_for_field = DatabaseCreation.sql_indexes_for_field
    DatabaseCreation.sql_indexes_for_field = sql_indexes_for_field
