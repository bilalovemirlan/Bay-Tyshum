from django.db import models

class Credit_Special(models.Model):
    full_name = models.CharField(max_length=100)
    job_title = models.ForeignKey('Job_titl', on_delete=models.CASCADE)
    #id_klient = models.ForeignKey(ContrAgent, on_delete=models.CASCADE)
    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Кредитный специалист'
class Job_titl(models.Model):
    name_job_title = models.CharField(max_length=100)

    def __str__(self):
        return self.name_job_title

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

class Guarantor(models.Model):
    #id_guarantor= models.ForeignKey('Job_titl', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    STATUS = [
        'В браке', 'В браке'
        'Не в браке', 'Не в браке'
    ]
    status  = models.CharField(max_length=30, choices=STATUS, default="Не в браке")
    credit_history = models.CharField(max_length=200)
    telephone = models.CharField(max_length=30)
    addres = models.CharField(max_length=100)
    zp_6_month = models.FileField(upload_to='zp_6_month/%Y/%m/%d')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Поручитель'




class Company(models.Model):
    company_names = models.CharField(max_length=50)
    legal_address = models.CharField(max_length=100)
    The_actu_aladdress = models.CharField(max_length=100)
    telephone = models.CharField(max_length=30)
    field_activity = models.CharField(max_length=100)

    def __str__(self):
        return self.company_names


    class Meta:
        verbose_name = 'Компания'





class Property(models.Model):
    name = models.CharField(max_length=100)
    document = models.FileField(upload_to='document/%Y/%m/%d')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Имущество'





class TelephoneConversations(models.Model):
    name = models.CharField(max_length=100)
    date = models.CharField(max_length=30)
    time = models.CharField(max_length=30)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Телефонные переговоры'



class DataKK(models.Model):
    data_created = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания:")
    credit_spec = models.FileField(
        verbose_name="Заключение кредитного эксперта (скан):",
        upload_to="credit_spec/%Y/%m/%d")
    answer = models.FileField(
        verbose_name="Решение КК (скан):",
        upload_to="answer/%Y/%m/%d")
    all_dogovor = models.FileField(
        verbose_name="Все заключенные договора, перечень и сканы:",
        upload_to="all_dogovor/%Y/%m/%d")
    scoring = models.CharField(verbose_name="Скоринг:", max_length=150)
    # id_clinet = models.ForeignKey(KontrClient, on_delete=models.CASCADE)


class ContrClient(models.Model):
    STATUS_CHOICES = [
        ('1', 'Можно давать кредит :'),
        ('2', 'Нельзя давать кредит:'),
    ]

    full_name = models.CharField(verbose_name="ФИО:", max_length=150)
    views_credit = models.CharField(verbose_name="Вид кредита:", max_length=159)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="2")