from rest_framework import serializers 
from .models import Theme,ThemesPack
class ThemeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Theme
        fields = ('id',
                  'title',
                  'file',
                  'presentimg')

class ThemesPackSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Theme
        fields = ('id',
                  'title',
                  'file',
                  'presentimg')