from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode

# Create your models here.
class Image(models.Model):
    img=models.ImageField()
    caption=models.CharField(max_length=500)
    date_added=models.DateTimeField(auto_now=True,null=True,blank=True)
    def image_img(self):
        if self.img:
            return u'<img src="/media/%s" width="25%%"/> <br> %s' % (self.img,self.caption)
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True
    def __str__(self):              # __unicode__ on Python 2
        return self.img.name

class Album(models.Model):
    name=models.CharField(max_length=500)
    cover=models.ForeignKey(Image,blank=True,null=True)
    date_added=models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name
class Gallery(models.Model):
    album=models.ForeignKey(Album)
    img=models.ForeignKey(Image)
    date_added=models.DateTimeField(auto_now=True,null=True,blank=True)
    def image_img(self):
        if self.img:
            return u'<img src="/media/%s" width="25%%"/> <br> %s' % (self.img.img,self.img.caption)
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

class Permission(models.Model):
    date_added=models.DateTimeField(auto_now=True,null=True,blank=True)
    user=models.ForeignKey(User)
    album=models.ForeignKey(Album)
    def __str__(self):              # __unicode__ on Python 2
        return self.user.username