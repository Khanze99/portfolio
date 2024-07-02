from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from .serializers import ServiceRequestSerializer
from .tasks import send_event_tg


class ServiceRequestView(APIView):
    serializer_class = ServiceRequestSerializer

    @swagger_auto_schema(
        operation_description="Create a new service request",
        request_body=ServiceRequestSerializer,
        responses={201: 'Created'}
    )
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        send_event_tg.delay(serializer.instance.pk)
        return Response(status=HTTP_201_CREATED)
