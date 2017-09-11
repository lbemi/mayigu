from django.db import models

# Create your models here.
import pymysql


class user_info(models.Model):
    id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=10)
    user_pwd = models.CharField(max_length=20)

    def __str__(self):
        return self.user_name

class customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=20)
    customer_phone = models.CharField(max_length=11)
    customer_addr = models.TextField()
    def __str__(self):
        return self.customer_name
