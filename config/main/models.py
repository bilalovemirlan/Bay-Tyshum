from django.db import models

class Credit_Special(models.Model):
    full_name = models.CharField(max_length=100)
    job_title = models.ForeignKey('Job_titl', on_delete=models.CASCADE)
    #id_klient = models.ForeignKey(ContrAgent, on_delete=models.CASCADE)

class Job_titl(models.Model):
    name_job_title = models.CharField(max_length=100)


class Guarantor(models.Model):
    #id_guarantor= models.ForeignKey('Job_titl', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)








    full_status =
    Credit_history = models.CharField(max_length=200)