# Generated by Django 3.1.2 on 2020-11-21 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_Noticias', '0005_auto_20201120_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(blank=True, default='default.jpg', help_text='Imagen central de la noticia', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='portada',
            field=models.ImageField(blank=True, default='default.jpg', help_text='Imagen que se mostrara como portada', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='video',
            field=models.CharField(blank=True, help_text='Link del video que se quiera mostrar (Debe ser en formato EMBED)', max_length=100, null=True),
        ),
    ]
