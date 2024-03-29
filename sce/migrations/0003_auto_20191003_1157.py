# Generated by Django 2.2.6 on 2019-10-03 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sce', '0002_ativos_ti_senha_wifi'),
    ]

    operations = [
        migrations.AddField(
            model_name='ativos_ti',
            name='tipo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sce.Tipo_Equipamento'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Manutencao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_manutencao', models.DateTimeField(auto_now_add=True)),
                ('manutencao', models.TextField(max_length=4096)),
                ('equipamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sce.Tipo_Equipamento')),
            ],
        ),
    ]
