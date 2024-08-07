from django.urls import path
from .views import qurulmalar_list, qurulmalar_detail, watch_list, watch_detail, bacground_list, bacground_detail

urlpatterns = [

    path('qurulmalar/', qurulmalar_list, name='qurulmalar-list'),
    path('qurulmalar/<int:pk>/', qurulmalar_detail, name='qurulmalar-detail'),


    path('watches/', watch_list, name='watch-list'),
    path('watches/<int:pk>/', watch_detail, name='watch-detail'),


    path('bacgrounds/', bacground_list, name='bacground-list'),
    path('bacgrounds/<int:pk>/', bacground_detail, name='bacground-detail'),
]
