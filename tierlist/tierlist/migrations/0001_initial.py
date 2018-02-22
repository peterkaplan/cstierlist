# Generated by Django 2.0.2 on 2018-02-22 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('size', models.IntegerField()),
                ('logo', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tierlist.Company', verbose_name='company id')),
                ('lid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tierlist.Location', verbose_name='location id')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=39)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tierlist.Company', verbose_name='profile id')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tierlist.Profile', verbose_name='profile id')),
            ],
        ),
    ]
