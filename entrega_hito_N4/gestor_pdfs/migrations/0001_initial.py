# Generated by Django 4.2.11 on 2024-11-05 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentoPDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('archivo', models.FileField(upload_to='pdfs/')),
                ('etiquetas', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
