# Generated by Django 3.0.7 on 2020-06-30 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=128)),
                ('breed', models.CharField(blank=True, max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='photos')),
                ('description', models.TextField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('size', models.CharField(choices=[('L', 'Large'), ('M', 'Medium'), ('S', 'Small')], default='M', max_length=1)),
                ('passport', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registry.Passport')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=128)),
                ('breed', models.CharField(blank=True, max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='photos')),
                ('description', models.TextField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('litter_box', models.BooleanField()),
                ('color', models.CharField(max_length=32)),
                ('fur', models.CharField(choices=[('L', 'Long'), ('S', 'Short'), ('H', 'Hairless')], default='S', max_length=1)),
                ('passport', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registry.Passport')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=128)),
                ('breed', models.CharField(blank=True, max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='photos')),
                ('description', models.TextField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('passport', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registry.Passport')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]