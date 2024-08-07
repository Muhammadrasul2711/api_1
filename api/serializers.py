from rest_framework import serializers
from apiapp.models  import Qurulmalar, Watch, Bacground


class QurulmalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qurulmalar
        fields = '__all__'

class WatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watch
        fields = '__all__'

class BacgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bacground
        fields = '__all__'
