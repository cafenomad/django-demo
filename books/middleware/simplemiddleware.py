class SimpleMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

        print("[Middleware] init")

    def __call__(self, request):

        print("[Middleware] before the view")

        response = self.get_response(request)

        print("[Middleware] after the view")

        return response
