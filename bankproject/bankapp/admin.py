# from django.contrib import admin
# from .models import District,Branch
# # Register your models here.
#
# class BranchInline(admin.TabularInline):
#     model = Branch
#
# @admin.register(District)
# class DistrictAdmin(admin.ModelAdmin):
#     inlines = [
#         BranchInline,
#     ]
#
# @admin.register(Branch)
# class BranchAdmin(admin.ModelAdmin):
#     list_display = ('name', 'district')

from django.contrib import admin

# Register your models here.
from .models import Branch, District, Person

admin.site.register(Branch)
admin.site.register(District)
