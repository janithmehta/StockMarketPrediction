from django.shortcuts import render, redirect
from django.http import HttpResponse

from Predictions.controllers import fundamental as fund
from Predictions.controllers import technical as tech

# Create your views here.

def index(request):
    return render(request, "index.html", {})

def companies(request):
    companies_list = [
        {'value':"AMBUJACEM", 'name':"Ambuja Cement"},
        {'value':"ASIANPAINT", 'name':"Asian Paints"},
        {'value':"BANKBARODA", 'name':"Bank Of Baroda"},
        {'value':"HDIL", 'name':"Housing Develoopment & Infrastructure Ltd."},
        {'value':"HEROMOTOCO", 'name':"Hero Motor Corporation"},
        {'value':"HINDUNILVR", 'name':"Hindustan Unilever"},
        {'value':"INFY", 'name':"Infosys"},
        {'value':"ITC", 'name':"ITC"},
        {'value':"MARUTI", 'name':"Maruti Suzuki Ltd."},
        {'value':"TCS", 'name':"Tata Consultancy Services"},
    ]
    return render(request, "companies.html", context={'companies_list':companies_list})

def selected_company(request):
    company = request.POST['company']
    return redirect('../fundamental_analysis/' + company)

def fundamental(request, company):
    investible = fund.predict(company)
    return render(request, "fundamental.html", context={'investible':investible, 'company': company})

def technical(request, company):
    predicted_values = tech.predict(company)
    stock_prices = tech.stock_prices(company)
    return render(request, "technical.html", context={'predicted_values':predicted_values, 'stock_prices':stock_prices})
