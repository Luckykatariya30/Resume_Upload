# Generated by Django 5.0.7 on 2024-08-26 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=121)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('dob', models.DateField()),
                ('state', models.CharField(choices=[('india', 'india'), ('dehli', 'dehli'), ('chomu', 'chomu'), ('sikar', 'sikar')], max_length=121)),
                ('gender', models.CharField(max_length=121)),
                ('location', models.CharField(max_length=121)),
                ('pro_image', models.ImageField(blank=True, upload_to='pro_image')),
                ('pro_doc', models.FileField(blank=True, upload_to='pro_file')),
            ],
        ),
    ]
