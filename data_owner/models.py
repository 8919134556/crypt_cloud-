from django.db import models
from datetime import datetime


# Create your models here.
class Data_Owner_Register(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(verbose_name='User_Name', db_column="user_name", max_length=50, blank=False,
                                  null=False)
    
    gender= models.CharField(verbose_name='Gender', db_column="gender", max_length=50, blank=False,
                                  null=False)
    
    user_phone = models.BigIntegerField(verbose_name='User_Phone', db_column="user_phone", blank=False,
                                  null=False)
    user_email = models.EmailField(db_column='user_email', verbose_name='User_Email', max_length=100, null=True, blank=True)
    user_pwd=models.CharField(verbose_name='User_Password',db_column="user_pwd",max_length=100,blank=False,null=False)
    user_image = models.FileField(verbose_name='User_Image', db_column="user_image", upload_to='User/Profile-image/', blank=True,)
    datetime_created = models.DateTimeField(default=datetime.now)
    status = models.CharField(verbose_name='Status', db_column="status", max_length=50, blank=False,
                                  default = 'Pending', null=True)
    
    class Meta:
        db_table='Data_Owner_Register'


class Upload_file(models.Model):
    id = models.AutoField(primary_key=True)

    owner= models.ForeignKey(Data_Owner_Register, max_length=100,null=True,on_delete=models.CASCADE)

    
    select = models.CharField(verbose_name='Select', db_column="select", max_length=50, blank=True,
                                  null=True)
    file_name = models.CharField(verbose_name='File_Name', db_column="file_name", max_length=50, blank=True,
                                  null=True)
    file_type = models.CharField(verbose_name='File_Type', db_column="file_type", max_length=50, blank=True,
                                  null=True)
    file_size = models.TextField(verbose_name='File_Size', db_column="file_size",  blank=True,
                                  null=True)
    Key= models.TextField(verbose_name='Key', db_column="key", max_length=500, blank=True,
                                  null=True)
    file_data= models.TextField(verbose_name='File_Data', db_column="file_data", max_length=100, blank=True,
                                  null=True)
    decription= models.TextField(verbose_name='Decription', db_column="decription", max_length=50, blank=True,
                                  null=True)

    files = models.FileField(verbose_name='Files', db_column="files", upload_to='User/Files/', blank=True,)

    status = models.CharField(verbose_name='Status', db_column="status", max_length=50, blank=False,
                                  default = 'Pending', null=True)
                                  
    datetime_created = models.DateTimeField(default=datetime.now)
    
    class Meta:
        db_table='Upload_file'
