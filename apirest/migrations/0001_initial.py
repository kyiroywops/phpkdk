# Generated by Django 4.1.3 on 2022-12-28 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='productos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ean13', models.CharField(max_length=13)),
                ('nombre', models.CharField(max_length=100)),
                ('creacion', models.DateTimeField()),
                ('minimo', models.IntegerField(null=True)),
            ],
        ),
    ]
