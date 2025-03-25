from django.db import models



class books(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,blank=True,
    #                          blank=True, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    book_name = models.CharField(max_length=300, null=True, blank=True)
    author = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return '%s -%s' % (self.book_name, self.author)


# Create your models here.

# books : ['user','book_name','author']