# Generated by Django 4.0.2 on 2022-02-21 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_doctor_city_alter_doctor_department_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patID', models.CharField(max_length=100)),
            ],
        ),
    ]