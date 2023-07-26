from django.contrib import admin
from .models import Project


# Register your models here.
# con esta clase hago que se fea las fecha en el admin
class ProjectAdmin(admin.ModelAdmin):

    readonly_fields = ('created', 'update')


admin.site.register(Project, ProjectAdmin)
