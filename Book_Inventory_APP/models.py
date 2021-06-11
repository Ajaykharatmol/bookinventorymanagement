from django.db import models


class Books(models.Model):
    book_name = models.CharField(max_length=120, unique=True)
    description = models.CharField(max_length=220)
    

    def __str__(self):
        return self.book_name