# Generated by Django 4.2.16 on 2024-10-18 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0223_default_enrollments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprisegroup',
            name='applies_to_all_contexts',
            field=models.BooleanField(default=False, help_text='When enabled, all learners connected to the org will be considered a member.', null=True, verbose_name='Set group membership to the entire org of learners.'),
        ),
        migrations.AlterField(
            model_name='historicalenterprisegroup',
            name='applies_to_all_contexts',
            field=models.BooleanField(default=False, help_text='When enabled, all learners connected to the org will be considered a member.', null=True, verbose_name='Set group membership to the entire org of learners.'),
        ),
    ]
