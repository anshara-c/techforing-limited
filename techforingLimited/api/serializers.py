from rest_framework import serializers
from .models import Users, Tasks, Projects, Project_Members, Comments

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class TasksSerializer(serializers.ModelSerializer):
    Assigned_to = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all()) 
    class Meta:
        model = Tasks
        fields = '__all__'

class ProjectsSerializer(serializers.ModelSerializer):
    Owner = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all()) 
    class Meta:
        model = Projects
        fields = '__all__'

class Project_MembersSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all()) 
    User = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all()) 
    class Meta:
        model = Project_Members
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    User = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all()) 
    Task = serializers.PrimaryKeyRelatedField(queryset=Tasks.objects.all()) 
    class Meta:
        model = Comments
        fields = '__all__'