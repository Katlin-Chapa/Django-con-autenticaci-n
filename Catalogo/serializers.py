from .models import *
from rest_framework import serializers

# Serializer para pais

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['nombre', 'codigo']

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ['nombre', 'codigo']

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = ['nombre', 'codigo']