from django.contrib import admin
from .models import Album,Image,Permission,Gallery
# Register your models here.3

class ImagesAdmin(admin.ModelAdmin):

    list_display= ('image_img','img',)

class GalleryAdmin(admin.ModelAdmin):
    list_display= ('image_img','album',)
admin.site.register(Album)
admin.site.register(Image,ImagesAdmin)
admin.site.register(Gallery,GalleryAdmin)
admin.site.register(Permission)
