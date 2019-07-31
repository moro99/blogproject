from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Portfolio

def portfolio(request):
    portfolios = Portfolio.objects
    portfolios_list = Portfolio.objects.all() #블로그 모든 글 대상
    paginator = Paginator(portfolios_list,3) #3씩 한페이지
    page = request.GET.get('page') #request된 페이지를 알아네고 변수에 담음
    posts = paginator.get_page(page)

    return render(request, 'portfolio.html', {'portfolios': portfolios, 'posts':posts}) #Portfolio객체들을 받아 html로 넘겨주는 내용
# Create your views here.
