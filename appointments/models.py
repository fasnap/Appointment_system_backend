from django.db import models

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['date', 'time']

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"