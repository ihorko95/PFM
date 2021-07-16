# Generated by Django 3.2.5 on 2021-07-16 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=80)),
                ('slug', models.SlugField(max_length=80, unique=True)),
                ('description', models.TextField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=80)),
                ('slug', models.SlugField(max_length=80, unique=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.TextField(blank=True, db_index=True, max_length=150)),
                ('date', models.DateField(auto_now_add=True)),
                ('category', models.ManyToManyField(blank=True, related_name='gifts', to='manager.Categories')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]