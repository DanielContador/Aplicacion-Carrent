# Generated by Django 3.2.13 on 2022-07-07 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='DireccionEnvio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200)),
                ('cpostal', models.CharField(max_length=200)),
                ('fecha_agregado', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tienda.cliente')),
                ('orden', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tienda.orden')),
            ],
        ),
    ]
