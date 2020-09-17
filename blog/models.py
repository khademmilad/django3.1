from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateField(auto_now_add=True)



class ContactBlog(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()

    def __str__(self):
        return self.name
