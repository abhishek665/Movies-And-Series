from django.shortcuts import render
from .models import Series, Images, DownloadProb, NotAvailable, Trending, TrendingImages, HindiSeries, HindiMovies, \
    Movies
from django.http import HttpResponse
import json
import math
import datetime
import pytz


def search(request):
    query = request.GET.get('search')
    check = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
             "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
             "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    response = []
    items = []
    sid = []
    thumbnail = []
    all = []
    if query == '':
        response += ["Enter To search"]
        itemss = [items, sid, thumbnail, response]
        return HttpResponse(json.dumps(itemss))
    for c in check:
        strcheck = str(c)
        if strcheck in query:
            web_series = Series.objects.all()
            hindi_series = HindiSeries.objects.all()
            movies = Movies.objects.all()
            hindi_movies = HindiMovies.objects.all()
            all += list(hindi_series.values()) + list(movies.values()) + list(hindi_movies.values()) + list(web_series.
                                                                                                            values())
            print(all)
            for i in all:
                for j in i:
                    if j == 'Name':
                        if query in i[j].lower() or query in i[j]:
                            item = ""
                            sid = sid + [i['id']]
                            item += i[j]
                            thumbnail += [i['thumbnail']]
                            items = items + [item]
            if len(items) > 0:
                itemss = [items, sid, thumbnail, response]
                return HttpResponse(json.dumps(itemss))
            else:
                response += ["Not Found"]
                print(response)
                itemss = [items, sid, thumbnail, response]
                return HttpResponse(json.dumps(itemss))
    response = ["Use only alphanumeric to search"]
    print(response)
    itemss = [items, sid, thumbnail, response]
    return HttpResponse(json.dumps(itemss))


def movies(request):
    global date1
    trend = Trending.objects.filter(content_category='Movies', language_category='English')
    trenditems = list(trend.values())
    items = []
    for i in range(1, 6):
        f_series = Movies.objects.filter(id=i)
        filtered_series = list(f_series.values())
        if len(filtered_series) != 0:
            items += filtered_series
    l = len(items)
    nslides = math.ceil(l / 4)
    if request.method == 'POST':
        email = request.POST.get('email')
        FileName = request.POST.get('FileName')
        category = request.POST.get('category')
        filt = NotAvailable.objects.filter(email=email)
        dt = len(filt)
        dates = pytz.utc.localize(datetime.datetime(2011, 8, 15, 8, 15, 12, 0))
        date1 = pytz.utc.localize(datetime.datetime(2011, 8, 15, 8, 15, 12, 0))
        ndate = pytz.utc.localize(datetime.datetime.utcnow())
        if dt > 4:
            for i in filt.values():
                for j in i:
                    if j == "date":
                        date1 = i[j]
                if date1 > dates:
                    dates = date1
            if dates + datetime.timedelta(days=1) < ndate:
                info = NotAvailable(email=email, name=FileName, category=category)
                info.save()
            else:
                return HttpResponse("<h1>You Have Requested Many Times. Please Come again After 24 Hours.</h1>")
        else:
            info = NotAvailable(email=email, name=FileName, category=category)
            info.save()
    return render(request, 'movies/movies.html', {'items': items, 'nslides': range(nslides), 'trend': trenditems})


def hindimovies(request):
    trend = Trending.objects.filter(content_category='Movies', language_category='Hindi')
    trenditems = list(trend.values())
    items = []
    for i in range(1, 6):
        f_series = HindiMovies.objects.filter(id=i)
        filtered_series = list(f_series.values())
        if len(filtered_series) != 0:
            items += filtered_series
    l = len(items)
    nslides = math.ceil(l / 4)
    return render(request, 'movies/hindimovies.html', {'items': items, 'nslides': range(nslides), 'trend': trenditems})


def hindiseries(request):
    items = []
    trend = Trending.objects.filter(content_category='Series', language_category='Hindi')
    trenditems = list(trend.values())
    for i in range(1, 6):
        f_series = HindiSeries.objects.filter(id=i)
        filtered_series = list(f_series.values())
        if len(filtered_series) != 0:
            items += filtered_series
    l = len(items)
    nslides = math.ceil(l / 4)
    return render(request, 'hindiseries.html', {'items': items, 'nslides': range(nslides), 'trend': trenditems})


def series(request):
    global date1
    trend = Trending.objects.filter(content_category='Series', language_category='English')
    trenditems = list(trend.values())
    items = []
    for i in range(2, 6):
        f_series = Series.objects.filter(id=i)
        filtered_series = list(f_series.values())
        if len(filtered_series) != 0:
            items += filtered_series
    l = len(trenditems)
    nslides = math.ceil(l / 4)
    if request.method == 'POST':
        email = request.POST.get('email')
        FileName = request.POST.get('FileName')
        category = request.POST.get('category')
        filt = NotAvailable.objects.filter(email=email)
        dt = len(filt)
        dates = pytz.utc.localize(datetime.datetime(2011, 8, 15, 8, 15, 12, 0))
        date1 = pytz.utc.localize(datetime.datetime(2011, 8, 15, 8, 15, 12, 0))
        ndate = pytz.utc.localize(datetime.datetime.utcnow())
        if dt > 4:
            for i in filt.values():
                for j in i:
                    if j == "date":
                        date1 = i[j]
                if date1 > dates:
                    dates = date1
            if dates + datetime.timedelta(days=1) < ndate:
                info = NotAvailable(email=email, name=FileName, category=category)
                info.save()
            else:
                return HttpResponse("<h1>You Have Requested Many Times. Please Come again After 24 Hours.</h1>")
        else:
            info = NotAvailable(email=email, name=FileName, category=category)
            info.save()
    return render(request, 'series.html', {'items': items, 'nslides': range(nslides), 'trend': trenditems})


def download(request, sid):
    images = Images.objects.filter(ref=sid)
    i = list(images.values())
    d = i[0]
    img = []
    for j in d:
        if 'img' in j:
            if d[j] != '':
                img = img + [d[j]]
    items = Series.objects.filter(id=sid)
    meta_description = items[0].meta_description
    title = items[0].title

    # download problem form handings
    if request.method == 'POST':
        email = request.POST.get('email')
        problem = request.POST.get('problem')
        sid = request.POST.get('sid')
        check = DownloadProb.objects.filter(email=email)
        print(len(check))
        if len(check) >= 1:
            return HttpResponse("<h1>Your Request Has Already been taken. PleaseWait For Our Mail.<a href='/'>Home</a>"
                                "</h1>")
        else:
            probsave = DownloadProb(email=email, problem=problem, name=sid)
            probsave.save()
    return render(request, 'download.html', {'images': img, 'items': items, 'title': title,
                                             'meta_description': meta_description})


# extending Series page with the ajax request
def contentextendserieshindi(request):
    loop = request.GET.get('count')
    category = request.GET.get('category')
    global extendesseries
    intloop = int(loop)
    startloop = intloop
    endloop = startloop + 4
    extendedcontent = []
    removeviewmore = ["remove"]
    if 'series' in category:
        for i in range(startloop, endloop):
            content = HindiSeries.objects.filter(id=i)
            extendesseries = list(content.values())
            if len(extendesseries) != 0:
                extendedcontent += extendesseries
            else:
                extendedcontent += removeviewmore
                print(extendesseries)
    print(extendedcontent)
    return HttpResponse(json.dumps(extendedcontent))


def contentextendseries(request):
    loop = request.GET.get('count')
    category = request.GET.get('category')
    global extendesseries
    intloop = int(loop)
    startloop = intloop
    endloop = startloop + 4
    extendedcontent = []
    removeviewmore = ["remove"]
    if 'series' in category:
        for i in range(startloop, endloop):
            content = Series.objects.filter(id=i)
            extendesseries = list(content.values())
            if len(extendesseries) != 0:
                extendedcontent += extendesseries
            else:
                extendedcontent += removeviewmore
                print(extendesseries)
    print(extendedcontent)
    return HttpResponse(json.dumps(extendedcontent))


def contentextendmovies(request):
    loop = request.GET.get('count')
    category = request.GET.get('category')
    global extendesseries
    intloop = int(loop)
    startloop = intloop
    endloop = startloop + 4
    extendedcontent = []
    removeviewmore = ["remove"]
    if 'series' in category:
        for i in range(startloop, endloop):
            content = Movies.objects.filter(id=i)
            extendesseries = list(content.values())
            if len(extendesseries) != 0:
                extendedcontent += extendesseries
            else:
                extendedcontent += removeviewmore
                print(extendesseries)
    print(extendedcontent)
    return HttpResponse(json.dumps(extendedcontent))


def contentextendmovieshindi(request):
    loop = request.GET.get('count')
    category = request.GET.get('category')
    global extendesseries
    intloop = int(loop)
    startloop = intloop
    endloop = startloop + 4
    extendedcontent = []
    removeviewmore = ["remove"]
    if 'series' in category:
        for i in range(startloop, endloop):
            content = HindiMovies.objects.filter(id=i)
            extendesseries = list(content.values())
            if len(extendesseries) != 0:
                extendedcontent += extendesseries
            else:
                extendedcontent += removeviewmore
                print(extendesseries)
    print(extendedcontent)
    return HttpResponse(json.dumps(extendedcontent))


def trendingSearch(request):
    query = request.GET.get('search')
    check = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
             "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
             "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    response = []
    items = []
    sid = []
    thumbnail = []
    if query == '':
        response += ["Enter To search"]
        itemss = [items, sid, thumbnail, response]
        return HttpResponse(json.dumps(itemss))
    for c in check:
        strcheck = str(c)
        if strcheck in query:
            trend = Trending.objects.all()
            for i in trend.values():
                for j in i:
                    if j == 'Name':
                        if query in i[j].lower() or query in i[j]:
                            item = ""
                            sid = sid + [i['id']]
                            item += i[j]
                            thumbnail += [i['thumbnail']]
                            items = items + [item]
            if len(items) > 0:
                itemss = [items, sid, thumbnail, response]
                return HttpResponse(json.dumps(itemss))
            else:
                response += ["Not Found"]
                print(response)
                itemss = [items, sid, thumbnail, response]
                return HttpResponse(json.dumps(itemss))
    response = ["Use only alphanumeric to search"]
    print(response)
    itemss = [items, sid, thumbnail, response]
    return HttpResponse(json.dumps(itemss))


def trending(request, sid):
    images = TrendingImages.objects.filter(ref=sid)
    i = list(images.values())
    d = i[0]
    img = []
    for j in d:
        if 'img' in j:
            if d[j] != '':
                img = img + [d[j]]
    items = Trending.objects.filter(id=sid)
    return render(request, 'trending.html', {'items': items, 'images': img})


def FileNotFound(request):
    return render(request, 'FileNotFound.html', {})
