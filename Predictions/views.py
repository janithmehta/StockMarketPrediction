from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime

from Predictions.controllers import fundamental as fund
from Predictions.controllers import technical as tech
from Predictions.controllers import update as up

# Create your views here.

companies_list = [
        {'value':"AMBUJACEM", 'name':"Ambuja Cement"},
        {'value':"ASIANPAINT", 'name':"Asian Paints"},
        {'value':"BANKBARODA", 'name':"Bank Of Baroda"},
        {'value':"HDIL", 'name':"Housing Development & Infrastructure Ltd."},
        {'value':"HEROMOTOCO", 'name':"Hero Motor Corporation"},
        {'value':"HINDUNILVR", 'name':"Hindustan Unilever"},
        {'value':"INFY", 'name':"Infosys"},
        {'value':"ITC", 'name':"ITC"},
        {'value':"MARUTI", 'name':"Maruti Suzuki Ltd."},
        {'value':"TCS", 'name':"Tata Consultancy Services"},
    ]

def index(request):
    return render(request, "index.html", {})

def companies(request):
    return render(request, "companies.html", context={'companies_list':companies_list})

def selected_company(request):
    company = request.POST['company']
    return redirect('../technical_analysis/' + company)

def fundamental(company):
    investible = fund.predict(company)
    return investible

def technical(request, company):
    predicted_values = tech.predict(company)
    stock_prices = tech.stock_prices(company)
    company_latest = tech.company_latest(company)
    investible = fundamental(company)
    company_stock_data = tech.stock_prices(company)
    print(stock_prices)
    return render(request, "technical.html", context={'predicted_values':predicted_values, 'stock_prices':stock_prices, 'company_latest':company_latest, 'investible': investible, 'company_stock_data':company_stock_data})

def recommendation(request):
    suggestions = []
    if request.GET.get('amount'):
        amount = request.GET.get('amount')
        recommendations = tech.recommend(amount)
        suggestions = recommendations['suggestions']
        total_amount_invested = recommendations['total_amount_invested']
        amount_not_invested = recommendations['amount_not_invested']
    return render(request,  "recommendation.html", context={'suggestions':suggestions, 'total_amount_invested':total_amount_invested, 'amount_not_invested':amount_not_invested})

def update(request):
    print(datetime.now())
    last_updated_date = up.get_last_updated_data()
    if request.POST:
        print("Enter")
        if request.POST['confirm']:
            up.update()
    return render(request, "update.html", context={'last_updated_date': last_updated_date})

def accuracies(request):
    return render(request, "accuracies.html", context={'companies_list':companies_list})