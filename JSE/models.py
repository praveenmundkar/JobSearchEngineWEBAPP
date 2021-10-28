# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categories(models.Model):
    sr_no = models.SmallIntegerField(blank=True,  primary_key=True,default=0)
    category = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'categories'


class CompanyDetails(models.Model):
    sno = models.SmallAutoField(primary_key=True,default=0)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True)  # Field name made lowercase.
    subcategory = models.CharField(db_column='Subcategory', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'company_details'





class Jobs(models.Model):
    sno = models.SmallAutoField(primary_key=True,default=0)
    company = models.CharField(db_column='Company', max_length=255, blank=True, null=True)  # Field name made lowercase.
    job_position = models.CharField(db_column='Job_Position', max_length=255, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    subcategory = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'jobs'



class States(models.Model):
    sr_no = models.SmallIntegerField(blank=True, null=False, primary_key=True)
    state = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'states'


class Subcategories(models.Model):
    sr_no = models.SmallIntegerField(blank=True, null=False, primary_key=True)
    subcategory = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'subcategories'
