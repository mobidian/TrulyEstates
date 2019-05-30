# Generated by Django 2.2.1 on 2019-05-30 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=255)),
                ('is_mvp', models.BooleanField(default=False)),
                ('hire_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
