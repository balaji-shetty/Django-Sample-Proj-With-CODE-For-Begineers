from django.contrib import admin
from .models import Country, City, Student, Company
# from .models import CompanyProblems


# class Country = ['user','country_name']

class CountryAdmin(admin.ModelAdmin):
    list_display = ['country_name']

    exclude = ['user']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(Country, CountryAdmin)


# class City = ['user','city_name','country_name_column','population']    


class CityAdmin(admin.ModelAdmin):
    list_per_page = 6

    exclude = ['user']

    list_display = ['user', 'country', 'city_name']

    # search_fields = ['name','population']
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(City, CityAdmin)


# Company : ['user','company_name','website','city','location',
# 'person_name','mobile','estabilishment_year','email','company_type',
# 'company_name','company_product','company_branches']

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['user', 'company_name', 'company_type', 'company_product', 'city', 'location',
                    'person_name', 'mobile', 'estabilishment_year', 'email', 'website',
                    'company_branches']

    search_fields = ['user__username', 'company_name', 'website', 'city__city_name', 'city__country__country_name',
                     'location',
                     'person_name', 'mobile', 'estabilishment_year', 'email', 'company_type',
                     'company_name', 'company_product', 'company_branches']

    exclude = ['user']



    def get_queryset(self, request):
        qs = super(CompanyAdmin, self).get_queryset(request)

        if request.user.groups.filter(name__in=['group_company']).exists():
            qs = Company.objects.filter(user=request.user)
            return qs
        return qs


    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(Company, CompanyAdmin)


# Student : ['user','student_name','City','address','branch','education','experience']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'student_name', 'city', 'address', 'branch', 'education', 'experience']

    exclude = ['user']
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(Student, StudentAdmin)

