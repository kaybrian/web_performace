import time

class PageRenderTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        # Calculate rendering time
        end_time = time.time()
        rendering_time = end_time - start_time

        # Add rendering time to response headers (optional)
        response['X-Render-Time'] = str(rendering_time)

        return response
