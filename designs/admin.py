from django.contrib import admin
from .models import Services,Portfolio,Testimonial,Articles,Team,Office
# Register your models here.
@admin.register(Services)
class Services(admin.ModelAdmin):
    fields = (('service_name'),'description', 'service_image')

@admin.register(Portfolio)
class Portfolio(admin.ModelAdmin):
    fields =(('portfolio_name'), 'portfolio_image','date','location','service')

@admin.register(Testimonial)
class Testimonial(admin.ModelAdmin):
    fields = (('profile_name','profile_location','testimonial_quotation'),"profile_image","testimonial_image", "testimonial_desc",'approved')

@admin.register(Articles)
class Articles(admin.ModelAdmin):
    fields = (('article_header'), 'article_date','article_category','article_image')

@admin.register(Team)
class Team(admin.ModelAdmin):
    fields = (('profile_name'), 'profile_occupation', 'quote', 'profile_image')

@admin.register(Office)
class Office(admin.ModelAdmin):
    fields = (('city'),'phone_number','email_address','physical_address','office_pic','basic_desc')