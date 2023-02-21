from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Services, Portfolio,Testimonial,Articles,Team,Office
from .forms import ServicesForm,PortfolioForm,TestimonialForm,ArticleForm,TeamForm,OfficeForm
from json import dumps
import json
from django.contrib import messages

# Create your views here.
def trends_articles(request):
    trends_articles = Articles.objects.filter(article_category='TRENDS')
    return render(request, 'design/trends_blogs.html',{'trends_articles':trends_articles})
    
def resources_articles(request):
    resources_articles = Articles.objects.filter(article_category='RESOURCES')
    return render(request, 'design/resources_blogs.html',{'resources_articles':resources_articles})
    
def design_articles(request):
    design_articles = Articles.objects.filter(article_category='DESIGN')
    return render(request, 'design/design_blogs.html',{'design_articles':design_articles})

def show_services(request):
    all_services = Services.objects.all()
    return render(request, "design/all_services.html",{'all_services':all_services})

def delete_office(request,office_id):
    office = Office.objects.get(pk = office_id)
    office.delete()
    return redirect("list-offices")

def update_office(request,office_id):
    office = Office.objects.get(pk=office_id)
    form = OfficeForm(request.POST or None, request.FILES or None, instance=office)
    if form.is_valid():
        form.save()
        messages.success(request,("Office Updated Succesfully"))
        return redirect("list-offices")
    return render(request,"design/update_office.html",{'form':form,'office':office})

def add_office(request):
    submitted = False
    if request.method =="POST":
        form = OfficeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,("New Office Added Succesfully"))
            return HttpResponseRedirect("/add_office? submitted = True")
    else:
        form = OfficeForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request,"design/add_office.html",{'form':form,"submitted":submitted})

def list_offices(request):
    all_offices = Office.objects.all()
    return render(request,"design/list_office.html",{'all_offices':all_offices})

def delete_team(request,team_id):
    team_member = Team.objects.get(pk=team_id)
    team_member.delete()
    return redirect('list-team')

def update_team(request,team_id):
    team = Team.objects.get(pk=team_id)
    form = TeamForm(request.POST or None, request.FILES or None, instance=team)
    #form = TeamForm(request.POST or None, request.FILES or None,instance=team)
    if form.is_valid():
        form.save()
        messages.success(request,("Team Member Updated Succesfully"))
        return redirect("list-team")
    return render(request,"design/update_team.html",{"team":team,"form":form})
    
def list_team(request):
    team = Team.objects.all()
    print(team)
    return render(request, "design/list_team.html",{'team':team})

def add_team(request):
    submitted = False
    if request.method =="POST":
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ("Team member added succesfully"))
            return HttpResponseRedirect("/add_team? submitted = True")
    else:
        form = TeamForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "design/add_team.html",{'submitted':submitted,'form':form})
def admin_approval(request):
    testimonial_list = Testimonial.objects.all()
    if request.user.is_superuser:
        if request.method == "POST":
            str_list = request.POST.getlist('cboxes')
            print(str_list)
            id_list = [int(x.strip(',')) for x in str_list]
            print(id_list)
            #let's first uncheck all testimonies
            testimonial_list.update(approved = False)
            #update afterwards
            for x in id_list:
                Testimonial.objects.filter(pk=int(x)).update(approved = True)
            return redirect('list-testimonial')
        return render(request, 'design/admin_approval.html', {'testimonial_list':testimonial_list})
    else:
        messages.success(request, ("You are not authorized to view this page"))
        return redirect('index')

def delete_article(request,article_id):
    articles = Articles.objects.get(pk=article_id)
    articles.delete()
    return redirect('list-articles')

def update_article(request,article_id):
    articles = Articles.objects.get(pk=article_id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=articles)
    if form.is_valid():
        form.save()
        return redirect('list-articles')
    return redirect(request,"design/update_article.html",{'articles':articles,'form':form})

def list_articles(request):
    all_articles =Articles.objects.all()
    return render(request, "design/list_articles.html",{'all_articles':all_articles})

def add_article(request):
    submitted = False
    if request.method == "POST":
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ("Article added succesfully"))
            return HttpResponseRedirect("/add_article? submitted= True")
    else:
        form = ArticleForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'design/add_article.html',{'form':form, 'submitted':submitted})

def delete_testimonial(request, testimonial_id):
    testimonial = Testimonial.objects.get(pk = testimonial_id)
    testimonial.delete()
    return redirect("list-testimonial")
    

def update_testimonial(request,testimonial_id):
    testimonial = Testimonial.objects.get(pk = testimonial_id)
    form = TestimonialForm(request.POST or None, request.FILES or None, instance=testimonial)
    if form.is_valid():
        form.save()
        return redirect("list-testimonial")    
    return render(request, "design/update_testimonial.html", {'testimonial':testimonial,'form':form})

def add_testimonial(request):
    submitted = False
    if request.method == "POST":
        form = TestimonialForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ("Testimonial Added Succesfully"))
            return HttpResponseRedirect("/add_testimonial? submitted= True")
    else:
        form = TestimonialForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'design/add_testimonial.html',{'form':form, 'submitted':submitted})

def list_testimonial(request):
    all_testimonials = Testimonial.objects.all()
    return render(request, "design/list_testimonials.html",{'all_testimonials':all_testimonials})

def delete_portfolio(request,portfolio_id):
    portfolio =Portfolio.objects.get(pk=portfolio_id)
    portfolio.delete()
    return redirect("list-portfolios")

def update_portfolio(request,portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    form = PortfolioForm(request.POST or None, request.FILES or None, instance=portfolio)
    if form.is_valid():
        form.save()
        return redirect('list-portfolios')
    return render(request, 'design/update_portfolio.html',{'portfolio':portfolio, 'form':form})

def list_portfolio(request):
    all_portfolios = Portfolio.objects.all()
    return render(request,"design/list_portfolios.html",{'all_portfolios':all_portfolios})


def add_portfolio(request):
    submitted = False
    if request.method == "POST":
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_portfolio? submitted = True")
    else:
        form = PortfolioForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'design/add_portfolio.html',{'form':form, 'submitted':submitted})

def add_services(request):
    submitted = False
    if request.method == "POST":
        form = ServicesForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_services? submitted = True")
    else:
        form = ServicesForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'design/add_service.html',{'form':form, 'submitted':submitted})

def list_services(request):
    service_list = Services.objects.all()
    return render(request, "design/services_list.html",{'service_list':service_list})

def show_service(request, service_id):
    service = Services.objects.get(pk=service_id)
    return render(request,"design/show_service.html",{'service':service})


def update_service(request, service_id):
    service = Services.objects.get(pk=service_id)
    form = ServicesForm(request.POST or None, request.FILES or None, instance=service)
    if form.is_valid():
        form.save()
        return redirect('list-services')
    return render(request, 'design/update_service.html',{'service':service, 'form':form})

def delete_service(request, service_id):
    service = Services.objects.get(pk=service_id)
    service.delete()
    return redirect('list-services')

def contact(request):
    offices = Office.objects.all()
    return render(request, 'design/contact.html',{'offices':offices})

def portfolio(request):
    all_portfolios = Portfolio.objects.all()
    featured = Portfolio.objects.filter(portfolio_name = "OFFICES ARCHITECTURE DESIGN IN MANHATTAN, NEW YORK")
    return render(request,'design/portfolio.html',{'all_portfolios':all_portfolios,'featured':featured})

def blog(request):
    blog_details = Articles.objects.all()
    designs = Articles.objects.filter(article_category = "DESIGN")
    resources = Articles.objects.filter(article_category = "RESOURCES")
    trends = Articles.objects.filter(article_category ="TRENDS",pk = 2)
    return render(request, 'design/blog.html',{'blog_details':blog_details,'trends':trends,'designs':designs,'resources':resources})

def about(request):
    members = Team.objects.all()
    all_offices = Office.objects.all()
    return render(request, 'design/about.html',{'members':members,'all_offices':all_offices})
    
def index(request):
    service_list = Services.objects.all()
    all_portfolios = Portfolio.objects.all()
    all_testimonials = Testimonial.objects.all()
    all_articles = Articles.objects.all()
    #data = Services.objects.all().values()
    #data = service_list
    data = json.dumps(list(service_list.values()))
    #data  = dumps(data)
    return render(request, "design/index.html",{'service_list':service_list,'all_portfolios':all_portfolios,'all_testimonials':all_testimonials,'all_articles':all_articles,'data':data})
