# Generated by Django 5.0.4 on 2024-05-05 07:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Penulis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('biografi', models.TextField(blank=True)),
                ('tanggal_lahir', models.DateField(blank=True, null=True)),
                ('di_buat', models.DateTimeField(auto_now_add=True)),
                ('di_perbarui', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pinjaman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('di_buat', models.DateTimeField(auto_now_add=True)),
                ('di_perbarui', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Buku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=200)),
                ('keterangan', models.TextField(blank=True)),
                ('tanggal_dipublis', models.DateField(blank=True, null=True)),
                ('di_buat', models.DateTimeField(auto_now_add=True)),
                ('di_perbarui', models.DateTimeField(auto_now=True)),
                ('penulis', models.ManyToManyField(related_name='books', to='api.penulis')),
            ],
        ),
        migrations.CreateModel(
            name='PinjamanBuku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_pinjam', models.DateField()),
                ('tanggal_pengembalian', models.DateField(blank=True, null=True)),
                ('di_buat', models.DateTimeField(auto_now_add=True)),
                ('di_perbarui', models.DateTimeField(auto_now=True)),
                ('buku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.buku')),
                ('pinjaman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pinjaman')),
            ],
        ),
        migrations.AddField(
            model_name='pinjaman',
            name='pinjaman',
            field=models.ManyToManyField(through='api.PinjamanBuku', to='api.buku'),
        ),
    ]
