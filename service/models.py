from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=150, null=True)
    location = models.CharField( max_length=150, null=True)
    logo =""
    description = models.CharField(max_length=150, null=True)
    employee_count = models.IntegerField()


class Specialty(models.Model):
    code =models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    picture =""

    def __str__(self):
        return self.code


class Vacancy(models.Model):
    title = models.CharField(max_length = 64, null=True)
    specialty = models.ForeignKey(Specialty, related_name='vacancies', on_delete=models.CASCADE, null=True)
    company = models.ForeignKey(Company, related_name='vacancies', on_delete=models.CASCADE, null=True)
    skills = models.CharField(max_length=150, null=True)
    description = models.CharField(max_length=150)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()




