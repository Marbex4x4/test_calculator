msg_HTTP={200:'OK',
            204:'No Content acceptable',
            500:'Internal Server Error',
            400:'Bad Request',
            401:'Unauthorized',
            503:'Service Unavailable',
            404:'Not Found',
            406:'Not Acceptable'
}

class ObjectResponseHttp:
    def __init__(self, code, data):
        self.message = msg_HTTP[code]
        self.code = code
        if (data):
            self.data = data