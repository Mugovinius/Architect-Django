from django.db import models

# Create your models here.

class Services(models.Model):
    service_name = models.CharField("Service Name",max_length=30)
    description = models.TextField(blank=False)
    #well use filefield instead of imagefield because we want to save svg imagefiles
    service_image = models.FileField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.service_name

class Portfolio(models.Model):
    portfolio_name = models.CharField("Portfolio Name", max_length=50)
    portfolio_image = models.ImageField(null=True,blank=True,max_length=150,upload_to="images/")
    date = models.CharField(max_length=10)
    location = models.CharField(max_length=30)
    service = models.CharField(max_length=20)

    def __str__(self):
        return self.portfolio_name

class Testimonial(models.Model):
    testimonial_image = models.ImageField(null=True, blank=True, max_length=150, upload_to="images/")
    testimonial_quotation = models.CharField(max_length=70)
    testimonial_desc = models.CharField(max_length=150)
    profile_image = models.ImageField(null=True, blank=True,upload_to="images/")
    profile_name = models.CharField(max_length=20)
    profile_location = models.CharField(max_length=30)
    approved = models.BooleanField('Approved',default=False)

    def __str__(self):
        return self.profile_name

class Articles(models.Model):
    article_category = models.CharField(max_length=20)
    article_date = models.CharField(max_length=30)
    article_header = models.CharField(max_length=150)
    article_image =models.ImageField(null=True, blank=True, max_length=150, upload_to="images/")

    def __str__(self):
        return self.article_category

class Team(models.Model):
    profile_image = models.ImageField(upload_to="images/", max_length=150)
    profile_name = models.CharField(max_length=50)
    profile_occupation = models.CharField(max_length=70)
    quote = models.TextField(max_length=300)

    def __str__(self):
        return self.profile_name

class Office(models.Model):
    city = models.CharField( max_length=50)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField("Email Address")
    physical_address = models.CharField(max_length=80)
    office_pic = models.ImageField(null=True,blank=True, upload_to="images/")
    basic_desc = models.TextField(max_length=200)

    def __str__(self):
        return self.city