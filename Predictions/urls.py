from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'StockMarketPrediction.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'Predictions.views.index', name='index'),
    url(r'^companies/$', 'Predictions.views.companies', name='companies'),
    url(r'^selected_company/$', 'Predictions.views.selected_company', name='selected_company'),
    url(r'^fundamental_analysis/(?P<company>[A-Z]+$)', 'Predictions.views.fundamental', name='fundamental'),
    url(r'^technical_analysis/(?P<company>[A-Z]+$)', 'Predictions.views.technical', name='technical'),
    url(r'^recommendation/$', 'Predictions.views.recommendation', name='recommendation'),
    url(r'^update/$', 'Predictions.views.update', name='update'),
    url(r'^accuracies/$', 'Predictions.views.accuracies', name='accuracies'),


]
