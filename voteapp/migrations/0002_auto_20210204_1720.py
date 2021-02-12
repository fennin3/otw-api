# Generated by Django 3.1.6 on 2021-02-04 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voteapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postcategory',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='weeklypost',
            name='category',
        ),
        migrations.AddField(
            model_name='weeklypost',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='voteapp.postcategory'),
        ),
    ]