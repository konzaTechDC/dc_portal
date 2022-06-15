# Generated by Django 4.0 on 2022-06-15 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_rename_service_name_service_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='historicalcategory',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical category', 'verbose_name_plural': 'historical Categories'},
        ),
        migrations.RemoveField(
            model_name='historicalservicetype',
            name='image',
        ),
        migrations.RemoveField(
            model_name='servicetype',
            name='image',
        ),
        migrations.AddField(
            model_name='service',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='historicalcategory',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='historicalservicetype',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
