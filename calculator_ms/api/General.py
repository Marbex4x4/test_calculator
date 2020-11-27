
HTTP_SUCCESS_CODE = 200
HTTP_NO_CONTENT_ACCEPTABLE_CODE = 204
HTTP_BAD_REQUEST_CODE = 400
HTTP_UNAUTHORIZED_CODE = 401
HTTP_NOT_FOUND_CODE = 404
HTTP_NOT_ACCEPTABLE_CODE = 406
HTTP_INTERNAL_SERVER_ERROR_CODE = 500
HTTP_SERVICE_UNAVAILABLE_CODE = 503

def obj_to_dict(obj):
    return obj.__dict__


def clean_exp(expression):
        expression = expression.lower().replace(" ", "").replace("x", "*")
        return expression