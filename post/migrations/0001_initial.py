# Generated by Django 3.1.2 on 2020-10-07 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Название')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='')),
                ('date', models.DateTimeField(verbose_name='Время проведения')),
                ('location', models.TextField(verbose_name='Место проведения')),
            ],
        ),
    ]
