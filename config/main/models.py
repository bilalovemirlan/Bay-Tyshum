from django.db import models


class Credit_Special(models.Model):
    full_name = models.CharField(max_length=100)
    job_title = models.ForeignKey(Job_titl, on_delete=models.CASCADE)
    id_klient = models.ForeignKey(ContrAgent, on_delete=models.CASCADE)

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
    full_name = models.CharField(max_length=100)
    STATUS = [
        'В браке', 'В браке'
        'Не в браке', 'Не в браке'
    ]
    status = models.CharField(
        max_length=30,
        choices=STATUS,
        default="Не в браке")
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

    id_clinet = models.ForeignKey(ContrClient, on_delete=models.CASCADE)
    id_spec = models.ForeignKey(Credit_Special, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Документ на КК:"
        verbose_name_plural = "Документы на КК:"


class ContrClient(models.Model):
    STATUS_CHOICES = [
        ('1', 'Можно давать кредит :'),
        ('2', 'Нельзя давать кредит:'),
    ]
    FAMILY = [
        ("1", "В браке:"),
        ("2", "Не в браке:"),
    ]

    full_name = models.CharField(verbose_name="ФИО:", max_length=150)
    views_credit = models.CharField(
        verbose_name="Вид кредита:", max_length=159)
    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default="2")
    sum_credit = models.DecimalField(max_digits=60, decimal_places=5)
    family = models.CharField(max_length=100, choices=FAMILY)
    credit_history = models.CharField(
        max_length=100, verbose_name="Кредитная история:")
    number_phone = models.CharField(
        verbose_name="Номер телефона:", max_length=30)
    address = models.CharField(verbose_name="Адресс:", max_length=100)
    zp_6_month = models.FileField(
        verbose_name="Док. ЗП: За последние 6 месяцев:")
    call_parlay = models.FileField(
        upload_to="parlay/%Y/%m/%d",
        verbose_name="Телефонные переговоры:")
    meeting_special = models.FileField(
        verbose_name="Встречи с специалистом:",
        upload_to="meeting/%Y/%m/%d")
    contracts = models.FileField(
        upload_to="contracts/%Y/%m/",
        verbose_name="Договор с подрядчиками и поставщиками:")
    report_contracts = models.FileField(
        upload_to="report_contracts/%Y/%m/%d",
        verbose_name="Отчет подрядчиков и поставщиков об оказанной услуг и.т.д:")
    monitoring_report = models.FileField(
        upload_to="monitoring/%Y/%m/%d",
        verbose_name="Отчет по мониторингу в Т.Ч. видео отчет:")

    id_guarant = models.ForeignKey(Guarantor, on_delete=models.CASCADE)
    id_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    id_pledge = models.ForeignKey(Property, on_delete=models.CASCADE)
    id_num_parley = models.ForeignKey(
        TelephoneConversations,
        on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Контрагент:"
        verbose_name_plural = "Контрагенты:"
