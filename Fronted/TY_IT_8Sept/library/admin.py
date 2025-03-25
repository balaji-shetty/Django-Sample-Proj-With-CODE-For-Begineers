from django.contrib import admin

from .models import books


# books : ['user','book_name','author']




class booksAdmin(admin.ModelAdmin):
    list_display = [['user','book_name','author']]

    exclude = ['user']
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(books,booksAdmin)
# Register your models here.
