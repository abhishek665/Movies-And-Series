from django.contrib import admin
from .models import Series, Images, DownloadProb, NotAvailable, HindiMovies, HindiSeries, Movies, TrendingImages, Trending

# Register your models here.

admin.site.register(HindiSeries)
admin.site.register(Series)
admin.site.register(HindiMovies)
admin.site.register(Movies)
admin.site.register(Images)
admin.site.register(DownloadProb)
admin.site.register(NotAvailable)
admin.site.register(Trending)
admin.site.register(TrendingImages)
