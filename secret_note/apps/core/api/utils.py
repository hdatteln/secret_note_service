from rest_framework.response import Response
from rest_framework import status
class Request:
    @staticmethod
    def post(func):
        def wrapper(request, *args, **kwargs):
            if request.method == 'POST':
                return func(request, *args, **kwargs)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        return wrapper