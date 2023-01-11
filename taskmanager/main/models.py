from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField('Name', max_length=50)
    task = models.TextField('Description')

    def __str__(self): #call this method when we try to show on screen object of this class
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'