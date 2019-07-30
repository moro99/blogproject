from django.shortcuts import render
from .models import Portfolio

def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios': portfolios}) #Portfolio객체들을 받아 html로 넘겨주는 내용
# Create your views here.
