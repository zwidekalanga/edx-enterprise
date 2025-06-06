from django.db import connection, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('canvas', '0027_move_and_recrete_completed_timestamp'),
    ]

    db_engine = connection.settings_dict['ENGINE']

    if 'sqlite3' in db_engine:
        operations = [
            migrations.AlterIndexTogether(
                name='canvaslearnerdatatransmissionaudit',
                index_together={('enterprise_customer_uuid', 'plugin_configuration_id')},
            ),
        ]
    else:
        if 'postgresql' in db_engine:
            operations = [
                migrations.SeparateDatabaseAndState(
                    state_operations=[
                        migrations.AlterIndexTogether(
                            name='canvaslearnerdatatransmissionaudit',
                            index_together={('enterprise_customer_uuid', 'plugin_configuration_id')},
                        ),
                    ],
                    database_operations=[
                        migrations.RunSQL(sql="""
                            CREATE INDEX canvas_cldta_85936b55_idx
                            ON canvas_canvaslearnerdatatransmissionaudit (enterprise_customer_uuid, plugin_configuration_id)
                        """, reverse_sql="""
                            DROP INDEX CONCURRENTLY canvas_cldta_85936b55_idx
                        """),
                    ]
                ),
            ]
        else:
            # For MySQL or other non-sqlite and non-postgresql backends
            operations = [
                migrations.SeparateDatabaseAndState(
                    state_operations=[
                        migrations.AlterIndexTogether(
                            name='canvaslearnerdatatransmissionaudit',
                            index_together={('enterprise_customer_uuid', 'plugin_configuration_id')},
                        ),
                    ],
                    database_operations=[
                        migrations.RunSQL(sql="""
                            CREATE INDEX canvas_cldta_85936b55_idx
                            ON canvas_canvaslearnerdatatransmissionaudit (enterprise_customer_uuid, plugin_configuration_id)
                            ALGORITHM=INPLACE LOCK=NONE
                        """, reverse_sql="""
                            DROP INDEX canvas_cldta_85936b55_idx
                            ON canvas_canvaslearnerdatatransmissionaudit
                        """),
                    ]
                ),
            ]
