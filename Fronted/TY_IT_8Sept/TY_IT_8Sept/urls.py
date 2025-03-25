
from django.contrib import admin
from django.urls import path

from student.views import view_hello,view_record,view_hello_20

# from student.views import view_django


#from django.urls import url



#   https://django-tables2.readthedocs.io/en/latest/pages/tutorial.html    REPORTS GEN

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^hello1/', view_hello),
    path(r'^hello20/', view_hello_20),
    path(r'^record1/', view_record),
    # url(r'^django/', view_django),




]
