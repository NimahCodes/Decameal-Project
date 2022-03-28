# Generated by Django 4.0.1 on 2022-02-07 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_roles_delete_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.CharField(choices=[('Decadev', 'Decadev'), ('Staff', 'Staff'), ('Kitchen Staff', 'Kitchen Staff')], default='Decadev', max_length=255, null=True),
        ),
    ]
