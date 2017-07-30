# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-29 12:33
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('class_id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.IntegerField(validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)])),
                ('branch', models.CharField(max_length=10)),
                ('section', models.CharField(max_length=1, null=True)),
            ],
            options={
                'db_table': 'classes',
            },
        ),
        migrations.CreateModel(
            name='ClassFacSub',
            fields=[
                ('cfs_id', models.AutoField(primary_key=True, serialize=False)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.Classes')),
            ],
            options={
                'db_table': 'classFacSub',
            },
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=20, unique=True)),
                ('value', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('faculty_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'faculty',
            },
        ),
        migrations.CreateModel(
            name='FdbkQuestions',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('subcategory', models.CharField(max_length=30, null=True)),
                ('enabled', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_no', models.IntegerField()),
                ('ratings', models.CharField(max_length=80, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')])),
                ('questions', models.CharField(max_length=80, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')])),
                ('cfs_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.ClassFacSub')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackLoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_no', models.IntegerField()),
                ('ratings', models.CharField(max_length=80, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')])),
                ('questions', models.CharField(max_length=80, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')])),
            ],
        ),
        migrations.CreateModel(
            name='Initiation',
            fields=[
                ('initiation_id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('feedback_of', models.CharField(max_length=8)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.Classes')),
                ('initiated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LOAquestions',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('enabled', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('note_id', models.AutoField(primary_key=True, serialize=False)),
                ('note', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sem',
            fields=[
                ('sem_id', models.AutoField(primary_key=True, serialize=False)),
                ('frm', models.IntegerField()),
                ('to', models.IntegerField()),
                ('no', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'sem',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('session_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('hallticket_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.Classes')),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'db_table': 'subject',
            },
        ),
        migrations.CreateModel(
            name='SlaveSession',
            fields=[
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='master', serialize=False, to='feedback.Session')),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='initiation_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.Initiation'),
        ),
        migrations.AddField(
            model_name='session',
            name='taken_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='sem',
            unique_together=set([('frm', 'to', 'no')]),
        ),
        migrations.AddField(
            model_name='notes',
            name='session_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='feedback.Session'),
        ),
        migrations.AddField(
            model_name='loaquestions',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.Subject'),
        ),
        migrations.AddField(
            model_name='feedbackloa',
            name='session_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.Session'),
        ),
        migrations.AddField(
            model_name='feedbackloa',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.Subject'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='session_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.Session'),
        ),
        migrations.AddField(
            model_name='classfacsub',
            name='faculty_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.Faculty'),
        ),
        migrations.AddField(
            model_name='classfacsub',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.Subject'),
        ),
        migrations.AddField(
            model_name='classes',
            name='sem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.Sem'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='session_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.Session'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.Student'),
        ),
        migrations.AddField(
            model_name='slavesession',
            name='slave',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='slave', to='feedback.Session'),
        ),
        migrations.AlterUniqueTogether(
            name='feedbackloa',
            unique_together=set([('session_id', 'student_no', 'subject_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='feedback',
            unique_together=set([('session_id', 'student_no', 'cfs_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='classfacsub',
            unique_together=set([('class_id', 'faculty_id', 'subject_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='classes',
            unique_together=set([('year', 'branch', 'section', 'sem')]),
        ),
        migrations.AlterUniqueTogether(
            name='slavesession',
            unique_together=set([('master', 'slave')]),
        ),
    ]
