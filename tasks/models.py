from django.db import models

class Task(models.Model):

    inspection_name = models.CharField(max_length=255)
    description = models.TextField()
    link_path_pdf = models.TextField()
    link_path_xlsx = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.inspection_name














""" 
 STATUS = (
        (1, 'Doing'),
        (2, 'Done')
    )
 done = models.CharField(
        max_length=1,
        choices=STATUS,
    ) """