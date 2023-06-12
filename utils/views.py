from django.http import JsonResponse


def error404(request, exception):
    message = {'code': 'noEndPoint'}
    response = JsonResponse(data=message)
    response.status_code = 404
    return response


def error500(request):
    message = {'code': 'serveIssue'}
    response = JsonResponse(data=message)
    response.status_code = 500
    return response


def error400(request, exception):
    message = {'code': 'badRequest'}
    response = JsonResponse(data=message)
    response.status_code = 400
    return response
