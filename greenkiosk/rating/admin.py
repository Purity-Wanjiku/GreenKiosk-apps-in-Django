from django.contrib import admin
from .models import Rating
# Register your models here.
class RatingAdmin(admin.ModelAdmin):
    list_display = ('name','review_message','sender','star_rating','value','date')
admin.site.register(Rating,RatingAdmin)