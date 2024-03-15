from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import SKU, InventoryItem, SalesOrder, StockMovement
from .serializers import SKUSerializer, InventoryItemSerializer, SalesOrderSerializer, StockMovementSerializer

# @api_view(['GET'])
# def getAll(request):
#     data = {
#         "sku": getSKUData(),
#         "inventoryItem": getInventoryItemData(),
#         "salesOrder": getSalesOrderData(),
#         "stockMovement": getStockMovementData(),
#     }
#     return Response(data)

@api_view(['GET'])
def sku_list(request):
    skuObj = SKU.objects.all()
    serializerObj = SKUSerializer(skuObj, many=True)
    return Response(serializerObj.data)

@api_view(['POST'])
def sku_list(request):
    serializerObj = SKUSerializer(data=request.data)
    if(serializerObj.is_valid()):
        serializerObj.save()
    return Response(serializerObj.data)

@api_view(['GET'])
def inventory_item_list(request):
    iiObj = InventoryItem.objects.all()
    serializerObj = InventoryItemSerializer(iiObj, many=True)
    return Response(serializerObj.data)

@api_view(['POST'])
def inventory_item_list(request):
    serializerObj = InventoryItemSerializer(data=request.data)
    if(serializerObj.is_valid()):
        serializerObj.save()
    return Response(serializerObj.data)

@api_view(['GET'])
def sales_order_list(request):
    soObj = SalesOrder.objects.all()
    serializerObj = SalesOrderSerializer(soObj, many=True)
    return Response(serializerObj.data)

@api_view(['POST'])
def sales_order_list(request):
    serializerObj = SalesOrderSerializer(data=request.data)
    if(serializerObj.is_valid()):
        serializerObj.save()
    return Response(serializerObj.data)

@api_view(['GET'])
def stock_movement_list(request):
    smObj = StockMovement.objects.all()
    serializerObj = StockMovementSerializer(smObj, many=True)
    return Response(serializerObj.data)

@api_view(['POST'])
def stock_movement_list(request):
    serializerObj = StockMovementSerializer(data=request.data)
    if(serializerObj.is_valid()):
        serializerObj.save()
    return Response(serializerObj.data)