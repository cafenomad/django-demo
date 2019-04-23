class SimpleMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        print("[SimpleMiddleware] init")

    def __call__(self, request):
        self.process_request(request)  # Before process
        response = self.get_response(request)  # View process
        self.process_response(request, response)  # After process
        return response

    def process_request(self, request):
        print("[SimpleMiddleware] process request")

    def process_response(self, request, response):
        print("[SimpleMiddleware] process response")
