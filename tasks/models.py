from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(get_user_model(), verbose_name='User', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Title', max_length=255, null=False, blank=False)
    description = models.TextField(verbose_name='Description')
    deadline = models.DateTimeField(verbose_name='Deadline', blank=False)
    complete = models.BooleanField(verbose_name='Complete', default=False)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title
