# Generated by Django 4.1 on 2024-03-05 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fillale', models.CharField(max_length=255)),
                ('annee_de_reference', models.CharField(max_length=255)),
                ('systeme', models.CharField(max_length=255)),
                ('processus', models.CharField(max_length=255)),
                ('site', models.CharField(max_length=255)),
                ('criticite_issue_de_la_cartographie_des_risques', models.CharField(max_length=255)),
                ('annee_theorique_du_dernier_audit', models.CharField(max_length=255)),
                ('annee_de_realisation', models.CharField(max_length=255)),
                ('criticite_issue_de_la_mission_d_audit', models.CharField(max_length=255)),
                ('annee_de_la_prochaine_mission_d_audit', models.CharField(max_length=255)),
            ],
        ),
    ]
