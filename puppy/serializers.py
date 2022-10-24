from rest_framework import serializers
from .models import Breed, Dog


class BreedSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, required=True)
    size = serializers.CharField(max_length=10, required=True)
    friendliness = serializers.IntegerField(required=True)
    trainability = serializers.IntegerField(required=True)
    sheddingamount = serializers.IntegerField(required=True)
    exerciseneeds = serializers.IntegerField(required=True)

    class Meta:
        model = Breed
        fields = ('id', 'name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds')


class DogSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)
    age = serializers.IntegerField(required=True)
    breed = serializers.PrimaryKeyRelatedField(queryset=Breed.objects.all(), required=True)
    gender = serializers.CharField(max_length=1, required=True)
    color = serializers.CharField(max_length=100, required=True)
    favoritefood = serializers.CharField(max_length=100, required=True)
    favoritetoy = serializers.CharField(max_length=100, required=True)

    class Meta:
        model = Dog
        fields = ('id', 'name', 'age', 'breed', 'gender', 'color', 'favoritefood', 'favoritetoy')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['breed'] = instance.breed.name
        return ret
