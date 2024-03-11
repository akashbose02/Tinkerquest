from django.urls import path
from . import views

urlpatterns = [
    path('skus/', views.sku_list, name="sku_list"),
    path('inventory_items/', views.inventory_item_list, name="inventory_item_list"),
    path('sales_orders/', views.sales_order_list, name="sales_order_list"),
    path('stock_movements/', views.stock_movement_list, name="stock_movement_list"),
]
