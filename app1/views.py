from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from app1.models import Users, Filters, Avti, Regkode
from avtoalert.serializers import UsersSerializer, AvtiSerializer, FiltersSerializer, RegkodeSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

def index(request):
    return HttpResponse("Hello world!")


@api_view(['GET', 'POST'])
def users_list(request):
    if request.method == 'GET':

        users = Users.objects.all().values()
        users_serializer = UsersSerializer(users, many=True)

        return JsonResponse(users_serializer.data, safe=False)

    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UsersSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def users_detail(request, userID):
    # izloci kljuc in dobi instanco
    try:
        user = Users.objects.get(userID=userID)
    except Users.DoesNotExist:
        return JsonResponse({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user_serializer = UsersSerializer(user)
        return JsonResponse(user_serializer.data)

    if request.method == 'PUT':
        return HttpResponse("PUT call")

    if request.method == 'DELETE':
        return HttpResponse("DELETE call")

    if request.method == 'PATCH':
        return HttpResponse("PATCH call")


@api_view(['GET', 'POST'])
def avti_list(request):
    if request.method == 'GET':
        avti = Avti.objects.all().values()
        avti_serializer = AvtiSerializer(avti, many=True)

        return JsonResponse(avti_serializer.data, safe=False)

    if request.method == 'POST':
        avto_data = JSONParser().parse(request)
        avti_serializer = AvtiSerializer(data=avto_data)
        if avti_serializer.is_valid():
            avti_serializer.save()
            return JsonResponse(avti_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(avti_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def avti_detail(request, carID):
    # izloci kljuc in dobi instanco
    try:
        avto = Avti.objects.get(carID=carID)
    except Avti.DoesNotExist:
        return JsonResponse({'message': 'Car does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        avto_serializer = AvtiSerializer(avto)
        return JsonResponse(avto_serializer.data)

    if request.method == 'PUT':
        return HttpResponse("PUT call")

    if request.method == 'DELETE':
        return HttpResponse("DELETE call")

    if request.method == 'PATCH':
        return HttpResponse("PATCH call")


@api_view(['GET', 'POST', 'DELETE'])
def filters_list(request):
    if request.method == 'GET':
        userID = int(request.GET.get('userID', -1))
        if userID == -1:
            filters = Filters.objects.all().values()
        else:
            try:
                filters = Filters.objects.filter(userID=userID)
            except Filters.DoesNotExist:
                return JsonResponse({'message': 'Filters does not exist'}, status=status.HTTP_404_NOT_FOUND)

        filters_serializer = FiltersSerializer(filters, many=True)
        return JsonResponse(filters_serializer.data, safe=False)

    if request.method == 'POST':
        filters_data = JSONParser().parse(request)
        filters_serializer = FiltersSerializer(data=filters_data)
        if filters_serializer.is_valid():
            filters_serializer.save()
            return JsonResponse(filters_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(filters_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        userID = int(request.GET.get('userID', -1))
        if userID == -1:
            return HttpResponse("Missing userID parameter")

        try:
            filters = Filters.objects.filter(userID=userID)
        except Filters.DoesNotExist:
            return JsonResponse({'message': 'Filters with userID=' + str(userID)} + ' does not exists', status=status.HTTP_404_NOT_FOUND)
        for filtr in filters:
            filtr.delete()

        return HttpResponse("Filters deleted")


@api_view(['GET', 'POST'])
def regkode_list(request):
    if request.method == 'GET':
        regkode = Regkode.objects.all().values()
        regkode_serializer = RegkodeSerializer(regkode, many=True)

        return JsonResponse(regkode_serializer.data, safe=False)

    if request.method == 'POST':
        regkode_data = JSONParser().parse(request)
        regkode_serializer = RegkodeSerializer(data=regkode_data)
        if regkode_serializer.is_valid():
            regkode_serializer.save()
            return JsonResponse(regkode_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(regkode_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def regkode_detail(request, koda):
    # izloci kljuc in dobi instanco
    try:
        regkoda = Regkode.objects.get(koda=koda)
    except Regkode.DoesNotExist:
        return JsonResponse({'message': 'Regkoda does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        regkoda_serializer = RegkodeSerializer(regkoda)
        return JsonResponse(regkoda_serializer.data)

    if request.method == 'PUT':
        return HttpResponse("PUT call")

    if request.method == 'DELETE':
        regkoda.delete()
        return JsonResponse({'message': 'Record deleted'}, status=status.HTTP_202_ACCEPTED)

    if request.method == 'PATCH':
        return HttpResponse("PATCH call")


@api_view(['GET'])
def liveliness(request):
    HttpResponse("OK")


@api_view(['GET'])
def readiness(request):
    # TODO: Tukaj preverim ali sem povezan na podatkovno bazo
    HttpResponse("OK")