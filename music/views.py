from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> this is the music home page")

def details(request, album_id):
    return HttpResponse("<h2>Details of album id: " + str(album_id) + " </h2>")


