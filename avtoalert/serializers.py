from rest_framework import serializers
from app1.models import Users, Filters, Avti, Regkode


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('userID', 'veljavnost', 'ime', 'opis')

class AvtiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avti
        fields = ('carID', 'ime', 'cena', 'registracija', 'km', 'fizicna_os', 'poskodovano', 'scrapeTime')

class FiltersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filters
        fields = ('filterID', 'userID', 'znamka', 'model', 'cena_od', 'cena_do', 'letnik_od', 'letnik_do')

class RegkodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regkode
        fields = ('id', 'koda', 'opis')