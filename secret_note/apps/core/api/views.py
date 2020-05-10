from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.datastructures import MultiValueDictKeyError

from apps.core.api.serializers import MessageSerializer
from apps.core.models import Message
from apps.core.api.utils import Request


@api_view(['POST'])
@Request.post
def create_message(request):
    try:
        text = request.data['text']
    except MultiValueDictKeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    new_message = Message.objects.create(
        text=text
    )
    serializer = MessageSerializer(new_message)

    return Response(serializer.data, status=status.HTTP_201_CREATED)
