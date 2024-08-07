from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apiapp.models import Qurulmalar, Watch, Bacground
from .serializers import QurulmalarSerializer, WatchSerializer, BacgroundSerializer



@api_view(['GET'])
def qurulmalar_list(request):
    if request.method == 'GET':
        qurulmalar = Qurulmalar.objects.all()
        serializer = QurulmalarSerializer(qurulmalar, many=True)
        return Response(serializer.data)
    else:
        return Response(watch_list)




@api_view(['GET', 'PUT', 'DELETE'])
def qurulmalar_detail(request, pk):
    try:
        qurulmalar = Qurulmalar.objects.get(pk=pk)
    except Qurulmalar.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QurulmalarSerializer(qurulmalar)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = QurulmalarSerializer(qurulmalar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        qurulmalar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def watch_list(request):
    if request.method == 'GET':
        watches = Watch.objects.all()
        serializer = WatchSerializer(watches, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def watch_detail(request, pk):
    try:
        watch = Watch.objects.get(pk=pk)
    except Watch.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WatchSerializer(watch)
        return Response(serializer.data)


@api_view(['GET'])
def bacground_list(request):
    if request.method == 'GET':
        bacgrounds = Bacground.objects.all()
        serializer = BacgroundSerializer(bacgrounds, many=True)
        return Response(serializer.data)




@api_view(['GET'])
def bacground_detail(request, pk):
    try:
        bacground = Bacground.objects.get(pk=pk)
    except Bacground.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BacgroundSerializer(bacground)
        return Response(serializer.data)







