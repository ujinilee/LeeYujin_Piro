# Generated by Django 3.1.3 on 2022-01-18 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devtool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_name', models.CharField(max_length=100)),
                ('dev_type', models.CharField(max_length=100)),
                ('dev_content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea_name', models.CharField(max_length=200)),
                ('idea_image', models.ImageField(blank=True, null=True, upload_to='swidea')),
                ('idea_content', models.TextField()),
                ('idea_like', models.IntegerField(default=0)),
                ('devtool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swidea.devtool')),
            ],
        ),
    ]
