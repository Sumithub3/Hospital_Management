from django.db import models

class Instuments_Details(models.Model):
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=50)
    warranty_in_Years = models.DateField(null=True)
    Guaranty_in_years = models.DateField(null=True)
    amc = models.DateField()

    def __str__(self):
        return self.name

class Vendoor_Details(models.Model):
    vendoor_name = models.CharField(max_length=50)
    instument_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return  str(self.instument_name)
