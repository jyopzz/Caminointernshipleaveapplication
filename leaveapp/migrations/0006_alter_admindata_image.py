# Generated by Django 4.0.5 on 2022-08-26 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveapp', '0005_rename_department_admindata_adminid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admindata',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]
