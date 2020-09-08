from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import Route
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_202_ACCEPTED,
    HTTP_406_NOT_ACCEPTABLE,
    HTTP_401_UNAUTHORIZED,
)

from .aws_s3_control import store_route_aws_s3, get_route_aws_s3


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def route_detail_aws_s3(request, route_UUID):
    """ Return data of the route, basing on its id
    """
    try:
        data = get_route_aws_s3(route_UUID)
        return Response(data, status=HTTP_200_OK)
    except:
        return Response({'message': "Route doesn't exist"},
                        status=HTTP_404_NOT_FOUND)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def create_route_aws_s3(request):
    """ Create a new route data
    """
    route_data = request.data.get("route_data")
    route_id = store_route_aws_s3(route_data)

    message = {"route_id" : route_id}
    return Response(message, status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def route_detail(request, route_UUID):
    """ Return data of the route, basing on its id
    """
    try:
        routes = Route.objects.filter(uuid__startswith=route_UUID)
        data = {"route_data": routes[0].route_data}
        return Response(data, status=HTTP_200_OK)
    except:
        return Response({'message': "Route doesn't exist"},
                        status=HTTP_404_NOT_FOUND)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def create_route(request):
    """ Create a new route data
    """
    route_data = request.data.get("route_data")

    route = Route.objects.create(route_data=route_data)
    route.uuid = route.id
    route.save()

    message = {"route_id" : route.id, "creation_time": route.created_at}
    return Response(message, status=HTTP_200_OK)


@csrf_exempt
@api_view(["DELETE"])
@permission_classes((AllowAny,))
def delete_route(request, route_id):
    """ Delete route data
    """
    try:
        route = Route.objects.get(id=route_id).delete()
        return Response({'message': "Your route has been succesfully deleted"},
                        status=HTTP_200_OK)
    except Route.DoesNotExist:
        return Response({'message': "Route doesn't exist"},
                        status=HTTP_404_NOT_FOUND)
