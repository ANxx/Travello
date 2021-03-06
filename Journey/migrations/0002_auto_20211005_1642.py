# Generated by Django 3.2.7 on 2021-10-05 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Journey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='des',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='place',
            name='img',
            field=models.ImageField(default='', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='place',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='place',
            name='offer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='place',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
