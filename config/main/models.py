from django.db import models


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
        ('1', 'Можно давать кредит:'),
        ('2', 'Нельзя давать кредит:'),
    ]

    full_name = models.CharField(verbose_name="ФИО:", max_length=150)
    views_credit = models.CharField(verbose_name="Вид кредита:", max_length=159)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="2")

