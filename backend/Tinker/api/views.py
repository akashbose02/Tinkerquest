from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from base.models import SKU, InventoryItem, SalesOrder, StockMovement
from .serializers import SKUSerializer, InventoryItemSerializer, SalesOrderSerializer, StockMovementSerializer

@api_view(['GET', 'POST'])
def sku_list(request):
    if request.method == 'GET':
        skus = SKU.objects.all()
        serializer = SKUSerializer(skus, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SKUSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def inventory_item_list(request):
    if request.method == 'GET':
        items = InventoryItem.objects.all()
        serializer = InventoryItemSerializer(items, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = InventoryItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def sales_order_list(request):
    if request.method == 'GET':
        orders = SalesOrder.objects.all()
        serializer = SalesOrderSerializer(orders, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SalesOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def stock_movement_list(request):
    if request.method == 'GET':
        movements = StockMovement.objects.all()
        serializer = StockMovementSerializer(movements, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StockMovementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
