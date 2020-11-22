from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver

import cloudinary
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    profile_photo = CloudinaryField('image')
    bio = HTMLField(blank=True,default='I am a new user!')

    def __str__(self):
        return self.bio


    def __str__(self):
        return f'{self.user.username} Profile'

        

    def save_profile(self):
        self.save() 

    def delete_profile(self):
        self.delete()

    def update_bio(self,new_bio):
        self.bio = new_bio
        self.save()

    def update_image(self, user_id, new_image):
        user = User.objects.get(id = user_id)
        self.photo = new_image 
        self.save()              
    
class Image(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=40)
    image_caption = HTMLField() 
    date_posted = models.DateTimeField(auto_now_add=True)
    image_likes = models.PositiveIntegerField(default=0,blank=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def get_images(cls):
        all_images = cls.objects.all()
        return all_images 
    
    @classmethod
    def search_by_caption(cls,search_term):
        post = cls.objects.filter(caption__icontains=search_term)
        return post

    @classmethod
    def filter_images_by_user(cls,id):
        images_by_user = cls.objects.filter(profile = id).all() 
        return images_by_user    
    
    def __str__(self):
        return self.image_name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey('Image',on_delete=models.CASCADE)
    content = HTMLField()
    date_posted = models.DateTimeField(auto_now_add=True)  

    @classmethod
    def get_comments(cls,id):
        comments = cls.objects.filter(image_id=id)
        return comments     
     