# Generated by Django 4.1.3 on 2022-11-17 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='')),
                ('likes', models.IntegerField()),
                ('hashtags', models.ManyToManyField(blank=True, null=True, to='posts.hashtag')),
            ],
        ),
        migrations.AddField(
            model_name='hashtag',
            name='posts',
            field=models.ManyToManyField(blank=True, null=True, to='posts.post'),
        ),
    ]
