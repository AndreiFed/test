from django.urls import path
from .views import *

urlpatterns = [
    path('', MainView.as_view()),
    path('vacancies/', VacanciesView.as_view()),
    path('vacancies/<int:id>', VacancyView.as_view()),
    path('vacancies/cat/<str:name>', CatView.as_view()),
    path('companies/<int:id>', CompaniesView.as_view()),
]
