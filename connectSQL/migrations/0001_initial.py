# Generated by Django 4.1.7 on 2023-03-10 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info_1',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=254)),
                ('Mobile_no', models.CharField(max_length=14)),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
    ]