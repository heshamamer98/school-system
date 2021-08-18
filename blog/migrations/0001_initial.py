# Generated by Django 3.0.4 on 2021-06-13 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('stage', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('image', models.ImageField(default='default.jpg', upload_to='student_pics')),
            ],
        ),
    ]