from django.http import HttpResponse, JsonResponse


def credits(request):
    content = "Lala\nMaz"
    return HttpResponse(content, content_type="text/plain")


def about(request):
    content = "<html><body><h1>About Page</h1></body></html>"
    return HttpResponse(content, content_type="text/html")


def version_info(request):
    data = {"site_version": "1.0.0"}
    return JsonResponse(data, content_type="application/json")
