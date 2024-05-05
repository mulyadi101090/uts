from api.models import Penulis, Buku, Pinjaman, PinjamanBuku
from api.serializers import PenulisSerializer, BukuSerializer , PinjamanSerializer, PinjamanBukuSerializer
from rest_framework import generics

class PenulisList(generics.ListCreateAPIView):
    queryset = Penulis.objects.all()
    serializer_class = PenulisSerializer
    
class BukuList(generics.ListCreateAPIView):
    queryset = Buku.objects.all()
    serializer_class = BukuSerializer
    
class PinjamanList(generics.ListCreateAPIView):
    queryset = Pinjaman.objects.all()
    serializer_class = PinjamanSerializer

class PinjamanBukuList(generics.ListCreateAPIView):
    queryset = PinjamanBuku.objects.all()
    serializer_class = PinjamanBukuSerializer
