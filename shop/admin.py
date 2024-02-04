from django.contrib import admin
from .models import *

# admin panel header
admin.site.site_header = "My Shop"

# admin panel title
admin.site.site_title = "My Shop"

# admin panel index title
admin.site.index_title = "Admin"

class ProductAdmin(admin.ModelAdmin):
    def change_category_to_sports(self, request, queryset):
        queryset.update(category="Sports")

    def change_category_to_riding_gears(self, request, queryset):
        queryset.update(category="Riding Gears")

    def change_category_to_laptops(self, request, queryset):
        queryset.update(category="Laptops")

    def change_category_to_mobiles(self, request, queryset):
        queryset.update(category="Mobile Phones")

    change_category_to_sports.short_description = 'Sports Category'
    change_category_to_riding_gears.short_description = 'Riding Gears Category'
    change_category_to_laptops.short_description = 'Laptops Category'
    change_category_to_mobiles.short_description = 'Mobile Phones Category'


    list_display = ('title', 'price', 'discount_price', 'category', 'description', 'image')
    list_editable = ('price',)
    search_fields = ('title', 'category', 'description')
    actions = ('change_category_to_sports', 'change_category_to_riding_gears', 'change_category_to_laptops', 'change_category_to_mobiles')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)