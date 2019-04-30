# Generated by Django 2.2 on 2019-04-30 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.DateField()),
                ('genero', models.CharField(choices=[('f', 'Feminino'), ('m', 'Masculino'), ('o', 'Outro')], max_length=2)),
                ('dt_nascimento', models.DateField()),
                ('nacionalidade', models.CharField(max_length=50)),
                ('jatrabalha', models.BooleanField(default=True)),
                ('pretencao_salarial', models.DecimalField(decimal_places=2, default=0, max_digits=1000)),
                ('perfil', models.TextField()),
            ],
        ),
    ]
