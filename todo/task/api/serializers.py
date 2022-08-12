from rest_framework import serializers

from task.models import Task

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    slug = serializers.SlugField(read_only=True)
    class Meta:
        model = Task
        fields = ['description','slug','user']

    