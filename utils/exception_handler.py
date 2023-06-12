from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    handlers = {
        'ValidationError': _handle_validation_error,
        'Http404': _handle_http404_error,
        'NotAuthenticated': _handle_notauthenticated_error,
        'AuthenticationFailed': _handle_authenticationfailed_error,
        'PermissionDenied': _handle_permissiondenied_error,
        'NotFound': _handle_notfound_error,
        'MethodNotAllowed': _handle_methodnotallowed_error,
        'UnsupportedMediaType': _handle_unsupportedmediatype_error,
        'APIException': _handle_apiexception_error,
        'InvalidToken': _handle_invalid_token,
    }
    response = exception_handler(exc, context)
    if response is not None:
        # import pdb
        # pdb.set_trace()
        response.data['status_code'] = response.status_code
    exception_class = exc.__class__.__name__
    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)
    return response


def _handle_http404_error(exc, context, response):
    response.data = {
        'code': 'http404',
        'details': exc.detail
    }
    return response


def _handle_notauthenticated_error(exc, context, response):
    response.data = {
        'code': 'notAuthenticated',
        'details': exc.detail
    }
    return response


def _handle_authenticationfailed_error(exc, context, response):
    response.data = {
        'code': 'authenticationFailed',
        'details': exc.detail
    }
    return response


def _handle_permissiondenied_error(exc, context, response):
    response.data = {
        'code': 'permissionDenied',
        'details': exc.detail
    }
    return response


def _handle_notfound_error(exc, context, response):
    response.data = {
        'code': 'notFound',
        'details': exc.detail
    }
    return response


def _handle_methodnotallowed_error(exc, context, response):
    response.data = {
        'code': 'methodNotAllowed',
        'details': exc.detail
    }
    return response


def _handle_unsupportedmediatype_error(exc, context, response):
    response.data = {
        'code': 'unsupportedMedia',
        'details': exc.detail
    }
    return response


def _handle_invalid_token(exc, context, response):
    response.data = {
        'code': 'invalidToken',
        'details': exc.detail
    }
    return response


def _handle_validation_error(exc, context, response):
    response.data = {
        'code': 'missingData',
        'details':exc.detail
    }
    return response


def _handle_apiexception_error(exc, context, response):
    response.data = {
        'code': 'error',
        'details': exc.detail
    }
    return response

