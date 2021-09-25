# Generated by Django 3.2.3 on 2021-09-22 17:07

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModelForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=100)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('msg', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EnrolledCoursedModelForm',
            fields=[
                ('myid', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('stdfullname', models.CharField(max_length=100)),
                ('stdemail', models.EmailField(max_length=100)),
                ('contactno', phonenumber_field.modelfields.PhoneNumberField(default='00000000000', max_length=128, region=None)),
                ('onlineoroffline', models.CharField(choices=[('Online', 'online'), ('Offline', 'offline')], max_length=10)),
                ('neet', models.BooleanField()),
                ('jee', models.BooleanField()),
                ('class12', models.BooleanField()),
                ('class11', models.BooleanField()),
                ('class11crashcourse', models.BooleanField()),
                ('class12crashcourse', models.BooleanField()),
                ('class6to10', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='FacultymembersDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fmname', models.CharField(max_length=100)),
                ('fmqualification', models.CharField(max_length=10)),
                ('fmspecility', models.CharField(max_length=20)),
                ('fmwords', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='JoinModelForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('stdortea', models.CharField(choices=[('TEACHER', 'teacher'), ('STUDENT', 'student')], max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('contactno', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('myid', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('profile', models.ImageField(upload_to='profilepic')),
            ],
        ),
        migrations.CreateModel(
            name='YourCommentModelForm',
            fields=[
                ('myid', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('firstletterofname', models.CharField(max_length=1)),
                ('comment', models.CharField(max_length=500)),
            ],
        ),
    ]
