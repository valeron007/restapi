from django.db import models

# Create your models here.

class ToDoItem(models.Model):
    text = models.CharField(max_length=250)
    done = models.BooleanField()

    def __str__(self):
        done = ''
        if self.done == False:
            done = ''
        else:
            done = 'done'
        return "To do:{} {}".format(self.text, done)

