from django.db import models
from django.contrib.auth.models import User


class Payment(models.Model):
      user = models.ForeignKey(User, related_name="transact", default=1, on_delete=models.DO_NOTHING)
      created_at = models.DateTimeField(auto_now_add=True)
      first_name = models.CharField(max_length=50)
      last_name = models.CharField(max_length=50)
      email = models.CharField(max_length=50)
      phonenumber = models.CharField(max_length=50)
      station_name = models.CharField(max_length=50)

      def __str__(self):
          return f"{self.first_name} {self.last_name}"


class Trans(models.Model):
       user = models.ForeignKey(User, default=2, on_delete=models.CASCADE)
       amount = models.CharField(max_length=50)
       transcode = models.CharField(max_length=100)

       def __str__(self):
            return f"{self.amount} {self.transcode} {self.user}"