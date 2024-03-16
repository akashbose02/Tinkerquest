from django.urls import path
from .views import DashboardAPI, SignUpAPI, LoginAPI, AddItemAPI, EditItemAPI, DeleteItemAPI

urlpatterns = [
    path('dashboard/', DashboardAPI.as_view(), name='dashboard_api'),
    path('signup/', SignUpAPI.as_view(), name='signup_api'),
     path('login/', LoginAPI.as_view(), name='login_api'),  
    path('add-item/', AddItemAPI.as_view(), name='add_item_api'),
    path('edit-item/<int:pk>/', EditItemAPI.as_view(), name='edit_item_api'),
    path('delete-item/<int:pk>/', DeleteItemAPI.as_view(), name='delete_item_api'),
]
