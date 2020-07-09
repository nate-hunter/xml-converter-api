from rest_framework import serializers


class ConverterSerializer(serializers.Serializer):
    """Serializes the input for our converter to receive from the frontend"""
    studio = serializers.CharField(max_length=100)
    directory = serializers.CharField(max_length=240)
    # pathTest = serializers.FilePathField(path=None)



