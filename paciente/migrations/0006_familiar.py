# Generated by Django 4.1.7 on 2023-05-20 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('familiar', '0003_alter_familiar_telefono'),
        ('paciente', '0005_alter_paciente_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('familiar', models.ForeignKey(on_delete=django.db.models.deletion.SET, to='familiar.familiar')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.SET, to='paciente.paciente')),
            ],
        ),
    ]