# Generated by Django 4.1.3 on 2023-02-03 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Polls_and_surveys', '0014_myquiz_picture_alter_myquestion_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myquiz',
            name='picture',
            field=models.ImageField(upload_to=''),
        ),
    ]
