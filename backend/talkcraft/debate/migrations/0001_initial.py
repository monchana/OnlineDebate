# Generated by Django 2.2.1 on 2019-06-20 06:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Debate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=50)),
                ('mainTopic', models.CharField(blank=True, default='', max_length=100)),
                ('startTime', models.DateTimeField()),
                ('summary', models.TextField()),
                ('candidateA', models.CharField(blank=True, default='', max_length=30)),
                ('candidate', models.CharField(blank=True, default='', max_length=30)),
                ('textA', models.TextField()),
                ('textB', models.TextField()),
                ('wordLimit', models.IntegerField(default=150)),
                ('totalTimeLimit', models.DurationField(default=15)),
                ('pictureA', models.ImageField(blank=True, upload_to='debate/%Y/%m/%d')),
                ('pictureB', models.ImageField(blank=True, upload_to='debate/%Y/%m/%d')),
                ('openStatus', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debate', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='DebateUserComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(blank=True, default='', max_length=200)),
                ('like', models.IntegerField(default=0, null=True)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='debate.Debate')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]