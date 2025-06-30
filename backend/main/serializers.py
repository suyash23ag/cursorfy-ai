from rest_framework import serializers
from . import models

class VideoAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VideoAnalysis
        fields = '__all__' 
