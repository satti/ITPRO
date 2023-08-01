# Generated by Django 4.2.3 on 2023-08-01 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetableapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='subject_code',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='sem',
            field=models.CharField(blank=True, choices=[('I-Semester', 'I-semester'), ('II-Semester', 'II-sem'), ('III-Semester', 'III-sem'), ('IV-Semester', 'IV-sem'), ('V-Semester', 'V-sem'), ('VI-Semester', 'VI-sem'), ('VII-Semester', 'VII-sem'), ('VIII-Semester', 'VIII-sem')], max_length=100),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='year',
            field=models.CharField(blank=True, choices=[('I-Year', 'I-year'), ('II-Year', 'II-year'), ('III-Year', 'III-year'), ('IV-Year', 'IV-year')], max_length=100),
        ),
    ]
