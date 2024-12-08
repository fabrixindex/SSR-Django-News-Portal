from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)  
    author = models.CharField(max_length=100)  
    content = models.TextField()  
    publication_date = models.DateTimeField(auto_now_add=True)  
    last_updated = models.DateTimeField(auto_now=True) 
    is_published = models.BooleanField(default=False)  

    def __str__(self):
        return self.title  
