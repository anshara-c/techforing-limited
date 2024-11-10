from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Users, Tasks, Projects, Project_Members, Comments
from .serializers import UsersSerializer, TasksSerializer, ProjectsSerializer, Project_MembersSerializer, CommentsSerializer

'''@api_view(['GET'])
def get_user(resquest):
    return Response(UsersSerializer({'Username':'Ansharac', 
                                    'Email' : 'Anshara.chowdhury@gmail.com',
                                    'Password' : '12345',
                                    'First_name' : 'Anshara',
                                    'Last_name': 'Chowdhury'}).data) '''

@api_view(['GET'])
def get_users(request):
    users = Users.objects.all()
    serializer = UsersSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def register_user(request):
    serializer = UsersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''@api_view(['GET'])
def get_user_details(request, id):
    try: 
        user = Users.objects.get(pk = id)
        serializer = UsersSerializer(user)
        return Response(serializer.data)
    except Users.DoesNotExist:
        return Response(status=status.HTTPS_404_NOT_FOUND)

@api_view(['PUT'])
def update_user(request, id):
    user = Users.objects.get(pk=id)
    serializer = UsersSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

@api_view(['GET', 'PUT', 'DELETE'])  
def user_detail(request, id):
    try:
        user = Users.objects.get(pk = id)
    except Users.DoesNotExist:
        return Response(status=status.HTTPS_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsersSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UsersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST', 'GET'])
def projects(request):
    if request.method == 'POST':
            serializer = ProjectsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()  
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        projects = Projects.objects.all()
        serializer = ProjectsSerializer(projects, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE']) 
def project_detail(request, id):
    try:
        project = Projects.objects.get(pk = id)
    except Projects.DoesNotExist:
        return Response(status=status.HTTPS_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProjectsSerializer(project)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProjectsSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST', 'GET'])
def tasks(request, id):
    if request.method == 'POST':
            serializer = TasksSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()  
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        tasks = Tasks.objects.all()
        serializer = TasksSerializer(tasks, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE']) 
def task_detail(request, id):
    try:
        task = Tasks.objects.get(pk = id)
    except Tasks.DoesNotExist:
        return Response(status=status.HTTPS_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TasksSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TasksSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST', 'GET'])
def comments(request, id):
    if request.method == 'POST':
            serializer = CommentsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()  
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        comments = Comments.objects.all()
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE']) 
def comment_detail(request, id):
    try:
        comment = Comments.objects.get(pk = id)
    except Comments.DoesNotExist:
        return Response(status=status.HTTPS_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommentsSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CommentsSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)