# Generated by Django 4.1.3 on 2022-11-15 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoCivil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=500)),
                ('foto', models.CharField(max_length=500)),
                ('idade', models.IntegerField()),
                ('estadoCivil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.estadocivil')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.genero')),
            ],
        ),
        migrations.CreateModel(
            name='Tatuador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=500)),
                ('disponivel', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Pontos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=500)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.perfil')),
            ],
        ),
        migrations.CreateModel(
            name='FilaTatuador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugarFila', models.IntegerField()),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.perfil')),
                ('tatuador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.tatuador')),
            ],
        ),
    ]
