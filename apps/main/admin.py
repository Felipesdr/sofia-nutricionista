from django.contrib import admin
from apps.main.models import Carousel, About, Expertise

class ShowMain(admin.ModelAdmin):
    list_display =('id','title', 'active')
    list_display_links = ('id','title')
    list_per_page = 10
    list_editable = ('active', )


admin.site.register(Carousel, ShowMain)

class ShowAbout(admin.ModelAdmin):
    list_display = ('id', 'title','date', 'active')
    list_display_links = ('id', 'title')
    list_per_page = 10
    list_editable = ('active',)

admin.site.register(About, ShowAbout)

class ShowExpertise(admin.ModelAdmin):
    list_display = ('id', 'title','date', 'active')
    list_display_links = ('id', 'title')
    list_per_page = 10
    list_editable = ('active',)

admin.site.register(Expertise, ShowExpertise)