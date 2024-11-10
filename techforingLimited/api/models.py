from django.db import models

class Users(models.Model):
    Username = models.CharField(max_length=50, unique=True)
    Email = models.EmailField(max_length=254, unique=True)
    Password = models.CharField(max_length=50)
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Username


class Projects(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    Owner = models.ForeignKey(Users, on_delete=models.CASCADE)
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name


class Project_Members(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Member', 'Member'),
    ]

    Project = models.ForeignKey(Projects,on_delete=models.CASCADE)
    User = models.ForeignKey(Users, on_delete=models.CASCADE)
    Role = models.CharField(choices=ROLE_CHOICES, max_length=10, default='Member')

    def __str__(self):
        return self.Role

class Tasks(models.Model):
    ROLE_CHOICES_STATUS = [
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
    ]

    ROLE_CHOICES_PRIORITY = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    Title = models.CharField(max_length=50, unique=True)
    Description = models.CharField(max_length=50)
    Status = models.CharField(max_length=15, choices=ROLE_CHOICES_STATUS, default='To Do')
    Priority = models.CharField(max_length=15, choices=ROLE_CHOICES_PRIORITY, default='High')
    Assigned_to = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Title

class Comments(models.Model):
    Content = models.CharField(max_length=50)
    User = models.ForeignKey(Users, on_delete=models.CASCADE)
    Task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Content
    
    
