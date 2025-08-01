# Generated by Django 5.2.4 on 2025-07-19 10:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('watergis', '0003_alert_resolved_at_alert_resolved_by_alert_severity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComparativeAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analysis_type', models.CharField(max_length=50)),
                ('comparison_data', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Comparative Analyses',
            },
        ),
        migrations.CreateModel(
            name='SystemOverview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('total_stations', models.IntegerField(default=0)),
                ('active_stations', models.IntegerField(default=0)),
                ('total_samples', models.IntegerField(default=0)),
                ('samples_today', models.IntegerField(default=0)),
                ('avg_quality_score', models.FloatField(default=0.0)),
                ('stations_with_issues', models.IntegerField(default=0)),
                ('critical_alerts', models.IntegerField(default=0)),
                ('regions_covered', models.IntegerField(default=0)),
                ('provinces_covered', models.IntegerField(default=0)),
                ('stations_updated_today', models.IntegerField(default=0)),
                ('data_completeness', models.FloatField(default=0.0)),
            ],
            options={
                'verbose_name_plural': 'System Overviews',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='StationStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_samples', models.IntegerField(default=0)),
                ('samples_last_30_days', models.IntegerField(default=0)),
                ('samples_last_90_days', models.IntegerField(default=0)),
                ('avg_ph', models.FloatField(blank=True, null=True)),
                ('avg_turbidity', models.FloatField(blank=True, null=True)),
                ('avg_dissolved_oxygen', models.FloatField(blank=True, null=True)),
                ('avg_temperature', models.FloatField(blank=True, null=True)),
                ('quality_score', models.FloatField(default=0.0)),
                ('last_sample_date', models.DateTimeField(blank=True, null=True)),
                ('ph_trend', models.CharField(default='stable', max_length=20)),
                ('turbidity_trend', models.CharField(default='stable', max_length=20)),
                ('oxygen_trend', models.CharField(default='stable', max_length=20)),
                ('last_calculated', models.DateTimeField(auto_now=True)),
                ('station', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='statistics', to='watergis.waterqualitystation')),
            ],
            options={
                'verbose_name_plural': 'Station Statistics',
            },
        ),
        migrations.CreateModel(
            name='TrendAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter', models.CharField(max_length=50)),
                ('period', models.CharField(max_length=20)),
                ('trend_data', models.JSONField()),
                ('trend_direction', models.CharField(max_length=20)),
                ('trend_strength', models.FloatField()),
                ('forecast_data', models.JSONField(blank=True, null=True)),
                ('analysis_date', models.DateTimeField(auto_now_add=True)),
                ('data_points', models.IntegerField(default=0)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trends', to='watergis.waterqualitystation')),
            ],
            options={
                'verbose_name_plural': 'Trend Analyses',
                'unique_together': {('station', 'parameter', 'period')},
            },
        ),
    ]
