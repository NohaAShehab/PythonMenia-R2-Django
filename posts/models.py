from django.db import models

# Create your models here.

## Model class represent table in the database
class Post(models.Model):
    # all fields generated by model ---> default not null,
    title = models.CharField(max_length=100)
    description  = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='posts/images', null=True, blank=True)
    version = models.IntegerField(default=1)
    publisher_email= models.EmailField(null=True,  blank=True)
    privacy = models.CharField(max_length=2, choices=[('1', 'Public'),('2', 'Private')])
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return self.title

    def get_image_url(self):
        return f"/media/{self.image}"