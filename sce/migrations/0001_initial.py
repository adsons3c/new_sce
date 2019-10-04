# Generated by Django 2.2.6 on 2019-10-01 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Equipamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_equipamento', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Modelos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=10)),
                ('modelo', models.CharField(max_length=100, unique=True)),
                ('equipamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sce.Tipo_Equipamento')),
            ],
        ),
        migrations.CreateModel(
            name='Ativos_TI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tombamento', models.IntegerField(unique=True)),
                ('numero_serie', models.CharField(max_length=100, unique=True)),
                ('sistema_oper', models.CharField(choices=[('Windows XP Profissional', 'Windows XP Profissional'), ('Windows 7 Home', 'Windows 7 Home'), ('Windows 7 Profissional', 'Windows 7 Profissional'), ('Windows 7 Ultimate', 'Windows 7 Ultimate'), ('Windows 8', 'Windows 8'), ('Windows 10 Profissional', 'Windows 10 Profissional')], default='Windows 10 Profissional', max_length=50)),
                ('licenca_so', models.CharField(max_length=100, unique=True)),
                ('ip', models.GenericIPAddressField(unique=True)),
                ('mac', models.CharField(max_length=50, unique=True)),
                ('processador', models.CharField(max_length=30)),
                ('memoria', models.CharField(choices=[('2GB', '2GB'), ('3GB', '3GB'), ('4GB', '4GB'), ('6GB', '6GB'), ('8GB', '8GB'), ('16GB', '16GB'), ('32GB', '32GB')], default='4GB', max_length=4)),
                ('hd', models.CharField(choices=[('240GB', '240GB'), ('250GB', '250GB'), ('500GB', '500GB'), ('1000GB', '1000GB'), ('2000GB', '2000GB'), ('SSD 240GB', 'SSD 240GB')], default='500GB', max_length=10)),
                ('status', models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo'), ('Manutenção', 'Manutenção')], default='Ativo', max_length=11)),
                ('vinculo_pc', models.IntegerField(blank=True, null=True)),
                ('usuario_principal', models.CharField(max_length=50)),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sce.Modelos')),
            ],
        ),
    ]