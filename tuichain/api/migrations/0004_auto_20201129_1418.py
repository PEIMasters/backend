# Generated by Django 3.1.2 on 2020-11-29 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_loanrequest_current_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanrequest',
            name='validated',
            field=models.BooleanField(default=False),
        ),
    ]
