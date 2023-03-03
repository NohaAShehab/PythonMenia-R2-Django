from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_all_categories(cls):
        return cls.objects.all()

    @classmethod
    def get_category(cls,id):
        try:
            category = cls.objects.get(pk=id)
            return category
        except Exception as e:
            return None