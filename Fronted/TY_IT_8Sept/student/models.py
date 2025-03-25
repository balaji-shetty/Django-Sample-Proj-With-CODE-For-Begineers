from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

TYPE = (
    ('MECH', 'MECH-Type'),
    ('ELECTRICAL', 'ELECTRICAL-Type'),
    ('CHEM', 'Chemical-Type'),
    ('IT', 'IT-Type'),
    ('ROBOTICS', 'Robotics-Type')
)

STAGE = (
    ('0-25 Percent', '0-25 Percent'),
    ('25-50 Percent', '25-50 Percent'),
    ('50-75 Percent', '50-75 Percent'),
    ('75-99 Percent', '75-99 Percent'),
    ('100 Percent', '100 Percent--'),
)


class Country(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
    #                          blank=True, on_delete=models.CASCADE)
    country_name = models.CharField(max_length=30)
    #
    # @property
    def __str__(self):
        return self.country_name


class City(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,blank=True,
    #                          blank=True, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    city_name = models.CharField(max_length=300, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    #
    def __str__(self):
        return '%s -%s' % (self.country, self.city_name)


#
# def __str__(self):
#     return self.country_name

# class Country = ['user','country_name']

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)

    # user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
    #                          blank=True, on_delete=models.SET_NULL)
    student_name = models.CharField(max_length=30)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)

    branch = models.CharField(max_length=30)
    education = models.CharField(max_length=30)
    experience = models.CharField(max_length=30)

    def __str__(self):
        return '%s --%s--%s' % (self.user,self.branch, self.experience)

    class Meta:
        verbose_name = "Students Information"
        verbose_name_plural = "Students Informations"
    #
    # 'company__user__username','company__company_name','company__city',
    # 'company__company_type','company__person_name',
    #     'company__website','company__company_product','company__company_branches']
# CompanyProblems__company__user
class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)

    # user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
    #                          blank=True, on_delete=models.SET_NULL)
    company_name = models.CharField(max_length=50)
    website = models.URLField(max_length=250)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    location = models.CharField(max_length=70)
    person_name = models.CharField(max_length=50)
    mobile = models.IntegerField(default='9898666666')
    estabilishment_year = models.IntegerField(default='5')
    email = models.EmailField(default='balaji@gmail.com')
    company_type = models.CharField(max_length=250, choices=TYPE)
    company_product = models.CharField(max_length=100)
    company_branches = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return '%s -%s  -%s' % (self.user,self.company_name, self.company_type)
    class Meta:
        verbose_name = "Company Information"
        verbose_name_plural = "Company Informations"
