# Generated by Django 2.2.3 on 2019-07-21 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190711_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('myapp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='myapp.Myapp')),
            ],
        ),
    ]