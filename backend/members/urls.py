from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.member_list),          # GET
    path('members/create/', views.member_create), # POST
    path('members/<int:pk>/update/', views.member_update), # PUT
    path('members/<int:pk>/delete/', views.member_delete)
     # DELETE
]