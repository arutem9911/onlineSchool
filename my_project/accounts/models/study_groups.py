from django.db import models


class StudyGroup(models.Model):
    start_date = models.DateField(null=False, blank=False, verbose_name='Start Date')
    end_date = models.DateField(null=False, blank=False, verbose_name='End Date')
    lesson = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.lesson
