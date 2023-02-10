# Generated by Django 4.1.6 on 2023-02-10 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=250)),
                ('subtitle', models.CharField(max_length=250)),
                ('button_text', models.CharField(max_length=250)),
                ('photo', models.ImageField(upload_to='media/slider/%y/')),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]