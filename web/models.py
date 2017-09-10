from django.db import models

# Create your models here.
import pymysql


class user_info(models.Model):
    id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=10)
    user_pwd = models.CharField(max_length=20)

    def __str__(self):
        return self.user_name