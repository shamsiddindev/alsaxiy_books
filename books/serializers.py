from rest_framework import serializers
from .models import BookModel, AutherModel, BookImageModel, FeaturesModel


class FeaturesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturesModel
        fields = '__all__'


class BookImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookImageModel
        fields = '__all__'


class AutherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutherModel
        fields = '__all__'


class BookModelSerializer(serializers.ModelSerializer):
    auther = AutherModelSerializer()
    image = BookImageModelSerializer()

    class Meta:
        model = BookModel
        exclude = ['status', 'description', 'features', 'created_at', 'updated_at']


class BookModelDetailSerializer(serializers.ModelSerializer):
    auther = AutherModelSerializer()
    image = BookImageModelSerializer()
    features = FeaturesModelSerializer()

    class Meta:
        model = BookModel
        fields = '__all__'
