# Generated by Django 3.2.8 on 2021-10-27 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('sr_no', models.SmallIntegerField(blank=True, default=0, primary_key=True, serialize=False)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='CompanyDetails',
            fields=[
                ('sno', models.SmallAutoField(default=0, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
                ('state', models.CharField(blank=True, db_column='State', max_length=255, null=True)),
                ('subcategory', models.CharField(blank=True, db_column='Subcategory', max_length=255, null=True)),
            ],
            options={
                'db_table': 'company_details',
            },
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('sno', models.SmallAutoField(default=0, primary_key=True, serialize=False)),
                ('company', models.CharField(blank=True, db_column='Company', max_length=255, null=True)),
                ('job_position', models.CharField(blank=True, db_column='Job_Position', max_length=255, null=True)),
                ('location', models.CharField(blank=True, db_column='Location', max_length=255, null=True)),
                ('subcategory', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'jobs',
            },
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('sr_no', models.SmallIntegerField(blank=True, primary_key=True, serialize=False)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'states',
            },
        ),
        migrations.CreateModel(
            name='Subcategories',
            fields=[
                ('sr_no', models.SmallIntegerField(blank=True, primary_key=True, serialize=False)),
                ('subcategory', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'subcategories',
            },
        ),
    ]