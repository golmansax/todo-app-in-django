from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=200)
    due_date = models.DateTimeField('due date')
    completed_date = models.DateTimeField('completed date')

    def __unicode__(self):
        return self.name
