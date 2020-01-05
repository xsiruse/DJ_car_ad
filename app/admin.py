from django.contrib import admin


from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    def count_reviews(self, obj):
        return super(CarAdmin, self).review_count()
    list_display = ('brand', 'model', 'review_count')


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    ordering = ['-id']
    list_display = ('car', 'title')
    list_filter = ('car', 'title', )
    search_fields = ['title', ]


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
