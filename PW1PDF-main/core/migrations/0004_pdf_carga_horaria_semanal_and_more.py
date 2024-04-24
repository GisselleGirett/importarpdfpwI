# Generated by Django 5.0.3 on 2024-04-09 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_pdf_bibliografia_pdf_evaluacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdf',
            name='carga_horaria_semanal',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pdf',
            name='carga_horaria_semestral',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pdf',
            name='condicion',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='pdf',
            name='curso',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='pdf',
            name='requisitos',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pdf',
            name='semestre',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
