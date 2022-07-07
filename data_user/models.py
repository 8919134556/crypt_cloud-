from django.db import models
from datetime import datetime
from data_owner.models import Data_Owner_Register


# Create your models here.
class Data_User_Register(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(verbose_name='User_Name', db_column="user_name", max_length=50, blank=False,
                                  null=False)
    user_lastname = models.CharField(verbose_name='User_Lastname', db_column="user_lastname", max_length=50, blank=False,
                                  null=False)
    gender= models.CharField(verbose_name='Gender', db_column="gender", max_length=50, blank=False,
                                  null=False)
    date_of_birth = models.DateField(verbose_name='Date_Of_Birth', db_column="date_of_birth", blank=False,
                                  null=False)
    user_phone = models.BigIntegerField(verbose_name='User_Phone', db_column="user_phone", blank=False,
                                  null=False)
    user_email = models.EmailField(db_column='user_email', verbose_name='User_Email', max_length=100, null=True, blank=True)
    user_pwd=models.CharField(verbose_name='User_Password',db_column="user_pwd",max_length=100,blank=False,null=False)
    user_image = models.FileField(verbose_name='User_Image', db_column="user_image", upload_to='User/Profile-image/', blank=True,)
    status = models.CharField(verbose_name='Status', db_column="status", max_length=50, blank=False,
                                  default = 'Pending', null=True)
    datetime_created = models.DateTimeField(default=datetime.now)
    
    class Meta:
        db_table='Data_User_Register'
    

class Request_file(models.Model):
    id = models.AutoField(primary_key=True)

    owner= models.ForeignKey(Data_Owner_Register, max_length=100,null=True,on_delete=models.CASCADE)

    file_id = models.CharField(verbose_name='File_Id', db_column="file_id", max_length=50, blank=True,
                                  null=True)
    file_name = models.CharField(verbose_name='File_Name', db_column="file_name", max_length=50, blank=True,
                                  null=True)
    file_type = models.CharField(verbose_name='File_Type', db_column="file_type", max_length=50, blank=True,
                                  null=True)
    file_size = models.TextField(verbose_name='File_Size', db_column="file_size",  blank=True,
                                  null=True)
    screat_key = models.TextField(verbose_name='Screat_Key', db_column="screat_key", max_length=100, blank=True,
                                  null=True)
    Key= models.TextField(verbose_name='Key', db_column="key", max_length=500, blank=True,
                                  null=True)
    status = models.CharField(verbose_name='Status', db_column="status", max_length=50, blank=True,
                                  default="Pending")
    request_mail = models.EmailField(db_column='request_mail', verbose_name='Request_Mail', max_length=100, null=True, blank=True)

    
    user_file = models.FileField(verbose_name='User_File', db_column="user_file", upload_to='Data-User/Files/', blank=True,)
    class Meta:
        db_table='Request_file'
    
class Attack_file(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(verbose_name='User_Name', db_column="user_name", max_length=50, blank=False,
                                  null=False)
    user_email = models.EmailField(db_column='user_email', verbose_name='User_Email', max_length=100, null=True, blank=True)
    user_image = models.FileField(verbose_name='User_Image', db_column="user_image", upload_to='Attack_file/Profile-image/', blank=True,)
    attack_file = models.CharField(verbose_name='Attack_File', db_column="attack_file", max_length=100, null=True, blank=True)
    status = models.CharField(verbose_name='Status', db_column="status", max_length=50, blank=True,
                                  default="Pending")
    datetime_created = models.DateTimeField(default=datetime.now)
    class Meta:
        db_table='Attack_file'

class Download_file(models.Model):
    id = models.AutoField(primary_key=True)
    user_email = models.EmailField(db_column='user_email', verbose_name='User_Email', max_length=100, null=True, blank=True)
    file_name = models.CharField(verbose_name='File_Name', db_column="file_name", max_length=50, blank=False,
                                  null=False)
    file_size = models.CharField(verbose_name='File_Size', db_column="file_size", max_length=50, blank=False,
                                  null=False)
    datetime_created = models.DateTimeField(default=datetime.now)
    class Meta:
        db_table='Download_file'
    
    
