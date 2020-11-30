# Generated by Django 3.1.2 on 2020-11-29 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20201129_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanrequest',
            name='current_amount',
            field=models.DecimalField(decimal_places=2, default='0.00', editable=False, max_digits=8),
        ),
        migrations.AlterField(
            model_name='loanrequest',
            name='validated',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
