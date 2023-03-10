from django.db import models

# Create your models here.

class Info_1(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Mobile_no = models.CharField(max_length=14)

    def __str__(self):
        return self.Name

    class Meta:
        db_table = "userinfo"

