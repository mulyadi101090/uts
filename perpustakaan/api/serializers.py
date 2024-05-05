# perpustakaan/serializers.py

from rest_framework import serializers
from .models import Penulis, Buku, Pinjaman, PinjamanBuku


class BukuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buku
        fields = '__all__'

class PenulisSerializer(serializers.ModelSerializer):
    buku = BukuSerializer(many=True, read_only=True)
    class Meta:
        model = Penulis
        fields = '__all__'
    
    
class PinjamanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pinjaman
        fields = '__all__'
        
class PinjamanBukuSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PinjamanBuku
        fields = '__all__'