from django.contrib import admin
from django.urls import path

from api.views import  companies_list, get_company, get_company_vacancies, vacancies_list, \
    get_top_vacancies, get_vacancy

urlpatterns = [
    path('companies/', companies_list),
    path('companies/<int:company_id>', get_company),
    path('companies/<int:company_id>/vacancies', get_company_vacancies),
    path('vacancies/', vacancies_list),
    path('vacancies/<int:vacancy_id>', get_vacancy),
    path('vacancies/top_ten/', get_top_vacancies),
]
