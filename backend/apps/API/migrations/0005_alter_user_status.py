# Generated by Django 4.1.4 on 2023-04-11 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_remove_user_gender_remove_user_religion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('Student', 'Student'), ('Teacher', 'Teacher'), ('Parent', 'Parent'), ('Admain', 'Admain')], default='none', max_length=15),
        ),
    ]
