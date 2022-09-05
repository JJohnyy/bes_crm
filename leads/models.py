from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Lead(models.Model):
    ''' lead model  '''
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    agent = models.ForeignKey(
        User, null=True, blank=True,
        on_delete=models.CASCADE
        )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
