from django import forms
from django.forms import ModelForm
from .models import Services,Portfolio,Testimonial,Articles,Team,Office

#create a services form
class ServicesForm(ModelForm):
    class Meta:
        model = Services
        fields = ("service_name","description","service_image")

#create a portfolio form
class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ("portfolio_name","portfolio_image","date","location","service")

#create a testimonial form
class TestimonialForm(ModelForm):
    class Meta:
        model = Testimonial
        fields = ("profile_name","profile_image", "profile_location", "testimonial_quotation", "testimonial_desc", "testimonial_image")

#create articles form
class ArticleForm(ModelForm):
    class Meta:
        model = Articles
        fields = ("article_category", "article_date","article_header","article_image")

#create a team form
class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ("profile_name","profile_occupation","profile_image","quote")


#create office form
class OfficeForm(ModelForm):
    class Meta:
        model = Office
        fields = ("city","phone_number","email_address","physical_address","office_pic","basic_desc")