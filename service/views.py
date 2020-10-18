from django.shortcuts import render
from django.views import View
from django.http import HttpResponseNotFound, HttpResponseServerError
from .models import Specialty, Vacancy, Company

def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')


def custom_handler500(request, exception):
    return HttpResponseServerError('Ой, что то сломалось... Простите извините!')


class MainView(View):
    def get(self, request):
        job =Vacancy.objects.all()
        countfronted = Vacancy.objects.filter(specialty=1).count()
        countbackend = Vacancy.objects.filter(specialty=2).count()
        specialties = Specialty.objects.all()
        companies = Company.objects.all()

        return render(request, 'index.html', {'specialties':specialties, 'job_list':job,
                                             'countbackend':countbackend, 'countfronted':countfronted,
                                              'companies':companies})


class VacanciesView(View):
    def get(self, request):
        job = Vacancy.objects.all()
        job_count = job.count
        return render(request, 'vacancies.html', {'job_list':job, 'job_count':job_count})

class VacancyView(View):
    def get(self, request, id):
        job = Vacancy.objects.filter(id=id)
        job = job[0]

 #       companie = Company.objects.filter(name=vacancies)

        return render(request, 'vacancy.html', {'job':job,})


class CatView(View):
    def get(self, request, name):
        insert = "Вакансий нет"
        specialties = Specialty.objects.all()
        if name == 'frontend':
            job = Vacancy.objects.filter(specialty=1)
            job_count = job.count
            if job_count:
                return render(request, 'vacancies.html', {'job_list': job, 'job_count': job_count})
            else:
                return render(request, 'test.html', {'insert':insert})

        elif name == 'backend':
            job = Vacancy.objects.filter(specialty=2)
            job_count = job.count
            if job_count:
                return render(request, 'vacancies.html', {'job_list': job, 'job_count': job_count})
            else:
                return render(request, 'test.html', {'insert': insert})
        else:
            return (request,'404.html')




class CompaniesView(View):
    def get(self, request, id):
        companies = Company.objects.all()
        job = Vacancy.objects.filter(company=id)
        job_count = job.count
        companies = Company.objects.filter(id=id)
        companie_name = companies[0].name
        return render(request, 'company.html', {'job_list': job, 'job_count': job_count, 'companie_name':companie_name})