from rest_framework.generics import UpdateAPIView, CreateAPIView
from rest_framework.response import Response

from .serializers import *


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response({"success": True})

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)



