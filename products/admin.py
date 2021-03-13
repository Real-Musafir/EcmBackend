from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("title",)}
	class Meta:
		model = Product

admin.site.register(Product, ProductAdmin)