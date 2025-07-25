from django.http import HttpResponse


def credits(request):
    content = "Lala\nMaz"
    return HttpResponse(content, content_type="text/plain")
