from django.db import models


class Payment(models.Model):
      created_at = models.DateTimeField(auto_now_add=True)
      first_name = models.CharField(max_length=50)
      last_name = models.CharField(max_length=50)
      email = models.CharField(max_length=50)
      phonenumber = models.CharField(max_length=50)
      station_name = models.CharField(max_length=50)

      def __str__(self):
          return f"{self.first_name} {self.last_name}"


class Trans(models.Model):
       amount = models.CharField(max_length=50)
       transcode = models.CharField(max_length=100)

       def __str__(self):
            return f"{self.amount} {self.transcode}"