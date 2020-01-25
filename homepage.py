from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view


@api_view(['Get'])
def api_root(request,format=None):
    return Response({
        'user': reverse('user-list',request=request,format=format),
        'location': reverse('location-list', request=request,format=format),
        'loctionype': reverse('locationtype-list', request=request, format=format),
        'usertype': reverse('usertype-list', request=request,format=format),
        # 'sender': reverse('sender-list',request=request,format=format),
        # 'receiver': reverse('receiver-list',request=request,format=format),
        # 'man': reverse('man-list',request=request,format=format),
        # 'post':reverse('post-list',request=request,format=format),
        # 'staff': reverse('staff-list',request=request, format=format),
        'franchise': reverse('franchise-list',request=request,format=format),
        'package': reverse('package-list', request=request,format=format),
        'packagerates':reverse('packagerates-list',request=request,format=format),
        'packagestatus': reverse('packagestatus-list',request=request,format=format),
        'packagebill': reverse('packagebilling-list', request=request, format=format),
        'vehicle': reverse('vehicle-list', request=request, format=format),
        'vehicletype': reverse('vehicletype-list', request=request, format=format)

    })
