from .models import Subjects
from rest_framework.serializers import ModelSerializer

class SubjectsSerializer(ModelSerializer):
    class Meta:
        model = Subjects
        fields = ['id','year','sem','subject_code','subject_name','created','updated']
