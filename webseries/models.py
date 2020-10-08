from django.db import models


# Create your models here.


def image_path(instance, filename):
    return 'webseries/images/{0}/{1}'.format(instance.Name, filename)


def images_path(instance, filename):
    return 'webseries/images/{0}/{1}'.format(instance.ref.Name, filename)


class HindiMovies(models.Model):
    id = models.BigAutoField(primary_key=True)
    Name = models.CharField(unique=True, max_length=500, default="")
    Server_1 = models.URLField(max_length=500, blank=True)
    Server_2 = models.URLField(max_length=500, blank=True)
    desc = models.CharField(default="", max_length=5000)
    notice = models.CharField(max_length=500, default="")
    thumbnail = models.ImageField(upload_to=image_path)
    meta_description = models.CharField(max_length=20000, default="")
    title = models.CharField(max_length=20000, default="", blank=True, null=True)

    def __str__(self):
        return self.Name


class Movies(models.Model):
    id = models.BigAutoField(primary_key=True)
    Name = models.CharField(unique=True, max_length=500, default="")
    Server_1 = models.URLField(max_length=500, blank=True)
    Server_2 = models.URLField(max_length=500, blank=True)
    desc = models.CharField(default="", max_length=5000)
    notice = models.CharField(max_length=500, default="")
    thumbnail = models.ImageField(upload_to=image_path)
    meta_description = models.CharField(max_length=20000, default="")
    title = models.CharField(max_length=20000, default="", blank=True, null=True)

    def __str__(self):
        return self.Name


class HindiSeries(models.Model):
    id = models.BigAutoField(primary_key=True)
    Name = models.CharField(unique=True, max_length=500, default="")
    Server_1 = models.URLField(max_length=500, blank=True)
    Server_2 = models.URLField(max_length=500, blank=True)
    desc = models.CharField(default="", max_length=5000)
    notice = models.CharField(max_length=500, default="")
    thumbnail = models.ImageField(upload_to=image_path)
    meta_description = models.CharField(max_length=20000, default="")
    title = models.CharField(max_length=20000, default="", blank=True, null=True)

    def __str__(self):
        return self.Name


class Series(models.Model):
    id = models.BigAutoField(primary_key=True)
    Name = models.CharField(unique=True, max_length=500, default="")
    Server_1 = models.URLField(max_length=500, blank=True)
    Server_2 = models.URLField(max_length=500, blank=True)
    desc = models.CharField(default="", max_length=5000)
    notice = models.CharField(max_length=500, default="")
    thumbnail = models.ImageField(upload_to=image_path)
    meta_description = models.CharField(max_length=20000, default="", blank=True)
    title = models.CharField(max_length=20000, default="", blank=True, null=True)

    def __str__(self):
        return self.Name


class Images(models.Model):
    ref = models.ForeignKey(Series, default=None, on_delete=models.CASCADE, blank=True, null=True)
    # HindiSeries = models.ForeignKey(HindiSeries, default=None, on_delete=models.CASCADE, blank=True, null=True)
    # HindiMovies = models.ForeignKey(HindiMovies, default=None, on_delete=models.CASCADE, blank=True, null=True)
    img = models.ImageField(upload_to=images_path, null=True, blank=True)
    img1 = models.ImageField(upload_to=images_path, null=True, blank=True)
    img2 = models.ImageField(upload_to=images_path, null=True, blank=True)

    def __str__(self):
        return self.ref.Name


class DownloadProb(models.Model):
    name = models.CharField(default="", max_length=50)
    email = models.EmailField(default="", max_length=100)
    problem = models.CharField(default="", max_length=200)

    def __str__(self):
        return self.email + ',' + self.name


class NotAvailable(models.Model):
    name = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=100, default="")
    category = models.CharField(max_length=100, default="")
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


def TrendingImagePAth(instance, filename):
    return 'Trending/{3}/{2}/{0}/{1}'.format(instance.Name, filename, instance.language_category,
                                             instance.content_category)


class Trending(models.Model):
    Trending_CHOICES = (
        ('Series', 'Series'),
        ('Movies', 'Movies'),
    )
    Language_CHOICES = (
        ('Hindi', 'Hindi'),
        ('English', 'English'),
    )
    id = models.BigAutoField(primary_key=True)
    Name = models.CharField(unique=True, max_length=500, default="")
    Server_1 = models.URLField(max_length=500, blank=True)
    Server_2 = models.URLField(max_length=500, blank=True)
    desc = models.CharField(default="", max_length=5000)
    notice = models.CharField(max_length=500, default="", blank=True)
    thumbnail = models.ImageField(upload_to=TrendingImagePAth)
    content_category = models.CharField(max_length=200, choices=Trending_CHOICES, default="Series")
    language_category = models.CharField(max_length=200, choices=Language_CHOICES, default="Series")

    def __str__(self):
        return self.Name


class TrendingImages(models.Model):
    ref = models.ForeignKey(Trending, default=None, on_delete=models.CASCADE)
    img = models.ImageField(upload_to=images_path, null=True, blank=True)
    img1 = models.ImageField(upload_to=images_path, null=True, blank=True)
    img2 = models.ImageField(upload_to=images_path, null=True, blank=True)

    def __str__(self):
        return self.ref.Name
