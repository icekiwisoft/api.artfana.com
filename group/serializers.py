from rest_framework import serializers 
from .models import Post
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Post
        fields = ('id',
                  'title',
                  'file',
                  'presentimg')