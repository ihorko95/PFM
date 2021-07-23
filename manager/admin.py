from django.contrib import admin
from .models import *

# Register your models here.
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug', 'category_id')
    list_display_links = ('id', 'title', 'slug', 'category_id')
    list_filter = ('title','category_id')
    prepopulated_fields = {'slug':('title', )}


admin.site.register(Transactions,TransactionsAdmin)

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug')
    list_display_links = ('id', 'title', 'slug')
    list_filter =('title', )
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Categories, CategoriesAdmin)



