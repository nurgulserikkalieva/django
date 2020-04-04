from django.shortcuts import render
from django.http import Http404
from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse

# Create your views here.
from api.models import Company, Vacancy


def hello_page(request):
    return HttpResponse('<h1>Tursynbekov Mubarak</h1>')


def companies_list(request):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    return JsonResponse(companies_json, safe=False)


def get_company(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        raise Http404
    return JsonResponse(company.to_json())


def get_company_vacancies(requets, company_id):
    company_vacancies = []
    vacancies = Vacancy.objects.all()
    for vacancy in vacancies:
        if vacancy.company_id.id == company_id:
            company_vacancies.append(vacancy.to_json())
    return JsonResponse(company_vacancies, safe=False)


def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def get_vacancy(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        raise Http404
    return JsonResponse(vacancy.to_json())


def get_top_vacancies(request):
    top_vacancies = Vacancy.objects.order_by('-salary')[:10]
    top_vacancies_json = [vacancy.to_json() for vacancy in top_vacancies]
    return JsonResponse(top_vacancies_json, safe=False)
