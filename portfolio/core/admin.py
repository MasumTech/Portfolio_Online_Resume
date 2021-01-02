from core.models import About, Service, RecentWork, Client,\
    Skill, ProjectCategory,SocialMedia, TotalWorkCount
from django.conf import settings
from django.contrib import admin

# Register your models here.


admin.site.register(About)

admin.site.register(Service)

admin.site.register(RecentWork)

admin.site.register(Client)

admin.site.register(Skill)

admin.site.register(ProjectCategory)

admin.site.register(TotalWorkCount)

admin.site.register(SocialMedia)

