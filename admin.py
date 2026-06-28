from django.contrib import admin
from .models import TourPackage, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display  = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}   # auto-fills slug from name


@admin.register(TourPackage)
class TourPackageAdmin(admin.ModelAdmin):
    list_display   = ['title', 'destination', 'price_per_person', 'duration_days', 'is_featured', 'is_active']
    list_filter    = ['category', 'is_featured', 'is_active', 'difficulty']
    search_fields  = ['title', 'destination']
    prepopulated_fields = {'slug': ('title',)}
    list_editable  = ['is_featured', 'is_active']   # edit directly from list