# Generated by Django 4.1.7 on 2023-03-27 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fisrt_Name', models.TextField()),
                ('Email', models.TextField()),
                ('Pass_Word', models.TextField()),
                ('Phone_Number', models.TextField()),
                ('Classify', models.TextField()),
                ('Last_Name', models.TextField()),
                ('Date', models.DateField()),
            ],
        ),
    ]