# Generated by Django 4.0.3 on 2022-04-28 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('location', models.CharField(max_length=100)),
                ('property_type', models.CharField(max_length=100)),
                ('year_build', models.IntegerField()),
                ('special_note', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='HouseSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_meausure', models.IntegerField()),
                ('room_type', models.CharField(choices=[('B', 'Bedroom'), ('T', 'BATHROOM'), ('O', 'Office')], default='B', max_length=1)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.house')),
            ],
        ),
    ]