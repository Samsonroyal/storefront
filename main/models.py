from django.db import models
from users.models import IMUser

# Create your models here.
class ClassSchedule(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date_and_time = models.DateField()
    end_date_and_time = models.DateField()
    is_repeated = models.BooleanField(default=False)
    repeat_frequency = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    organizer = models.ForeignKey('users.IMUser', on_delete=models.CASCADE)
    cohort = models.ForeignKey('users.Cohort', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class ClassAttendance(models.Model):
    class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)
    attendee = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='attendances')
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='authored_attendances')
    is_present = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    

class Query(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey('users.IMUser', on_delete=models.CASCADE, related_name='assigned_to')
    resolution_status = models.CharField(max_length=20, default='OPEN')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='authored_queries')
    submitted_by = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='submitted_queries')


class QueryComment(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)    
    author = models.ForeignKey('users.IMUser', on_delete=models.CASCADE)