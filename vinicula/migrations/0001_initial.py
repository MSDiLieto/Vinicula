# Generated by Django 3.0.8 on 2020-07-03 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vinicula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeVinicula', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('vinho', models.CharField(max_length=100)),
                ('produtor', models.CharField(max_length=100)),
            ],
        ),
    ]
