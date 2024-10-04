# Generated by Django 5.0.6 on 2024-07-19 08:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0009_remove_commenttbl_postidf_commenttbl_postidpf_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='liketbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likeaction', models.BooleanField(default=True)),
                ('postidPF', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.posttbl')),
                ('useridUF', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.usertbl')),
            ],
        ),
    ]