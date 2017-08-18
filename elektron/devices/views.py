# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from devices.models import Device
from data.models import Data
from devices.serializers import DeviceSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from devices.permissions import IsOwnerOrReadOnly, IsDeviceOrNothing
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework import renderers
import json
import datetime

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'devices': reverse('device-list', request=request, format=format)
    })


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    #lookup_field = "device_ip"
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


    #permission_classes = (IsDeviceOrNothing,)


    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer, renderers.JSONRenderer])
    def data(self, request, *args, **kwargs):
        queryset = Data.objects.all()
        device = self.request.query_params.get('device', self.get_object())
        print device

        if device is not None:
            data_list_query = queryset.filter(device=device)

        data_list = []

        for data in data_list_query:
            data_json = data.__dict__
            data_json['date'] = data_json['date']
            data_list.append(data_json)

        return Response(json.dumps(data_list, default = myconverter))


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
