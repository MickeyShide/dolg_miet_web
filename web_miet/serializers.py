from rest_framework import serializers, exceptions
from web_miet.models import Subject, Prepod, Work


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'description']

class PrepodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prepod
        fields = ['id', 'name', 'subject']

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['id', 'name', 'description' ,'prepod', 'subject', 'likes']