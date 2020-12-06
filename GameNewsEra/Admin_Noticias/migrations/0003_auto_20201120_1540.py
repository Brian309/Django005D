# Generated by Django 3.1.2 on 2020-11-20 18:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_Noticias', '0002_auto_20201103_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='tipo_de_noticia',
        ),
        migrations.AddField(
            model_name='noticia',
            name='bajadaimagen1',
            field=models.CharField(help_text='Descripcion de la imagen', max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(blank=True, default='default.jpg', help_text='Imagen central de la noticia', upload_to=''),
        ),
        migrations.AddField(
            model_name='noticia',
            name='parrafo1',
            field=models.TextField(default='Parrafo 1', help_text='Primer parrafo de la noticia', max_length=500),
        ),
        migrations.AddField(
            model_name='noticia',
            name='parrafo2',
            field=models.TextField(help_text='Segundo parrafo de la noticia opcional', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='noticia',
            name='portada',
            field=models.ImageField(default='default.jpg', help_text='Imagen que se mostrara como portada', upload_to=''),
        ),
        migrations.AddField(
            model_name='noticia',
            name='subtitulo',
            field=models.CharField(default='Subtitulo', help_text='Indique el subtitulo de la noticia', max_length=50),
        ),
        migrations.AddField(
            model_name='noticia',
            name='video',
            field=models.CharField(blank=True, help_text='Link del video que se quiera mostrar', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='id_noticia',
            field=models.UUIDField(default=uuid.uuid4, help_text='Indique el ID de la noticia', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='titulo',
            field=models.CharField(default='Titulo', help_text='Indique el titular de la noticia', max_length=50),
        ),
    ]
