from django.contrib import admin
from .models import Projects, Cv, Skills, CoverLetter, Refrences, Webinfo


class ProjectsAdmin(admin.ModelAdmin):
   prepopulated_fields = {'slug': ('title',)}



admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Cv)
admin.site.register(Skills)
admin.site.register(CoverLetter)
admin.site.register(Refrences)
admin.site.register(Webinfo)