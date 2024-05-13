from django.shortcuts import render


def page_404(request, exception):
    return render(request, 'error.html', context={'status': 404, 'title': 'Error Page'}, status=404)


def page_500(request, *args, **kwargs):
    return render(request, 'error.html', context={'status': 500, 'title': 'Server Error'}, status=500)


def page_403(request, exception):
    return render(request, 'error.html', context={'status': 403, 'title': 'Permission Denied'}, status=403)


def page_400(request, exception):
    return render(request, 'error.html', context={'status': 400, 'title': 'Bad Request'}, status=400)


