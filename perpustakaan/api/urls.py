from django.urls import path
from api.views import PenulisList, BukuList, PinjamanList, PinjamanBukuList

urlpatterns = [
    path('penulis/', PenulisList.as_view()),
    path('buku/', BukuList.as_view()),
    path('pinjaman/', PinjamanList.as_view()),
    path('pinjamanbuku/', PinjamanBukuList.as_view()),
]