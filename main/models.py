from django.db import models
from django.utils import timezone
from datetime import datetime as dt
from . import managers
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    COUNTRIES = (
        ('Бишкек', 'Бишкек'),
        ('Ош', 'Ош'),
        ('Нарын', 'Нарын'),
        ('Каракол', 'Каракол'),
        ('Жалал-Абад', 'Жалал-Абад'),
        ('Баткен', 'Баткен'),
        ('Талас', 'Талас'),
    )

    ROLES = (
        ('ADM', "Administrator"),
        ('MNG', "Manager"),
        ('GST', "Guest")
    )

    email = models.EmailField(
        verbose_name=_('Email Adress'),
        max_length=65,
        unique=True,
        db_index=True,
        db_column='admin_email',
    )

    username = models.CharField(
        verbose_name=_('Username'),
        max_length=26,
        db_index=True,
        db_column='username'
    )


    date_joined = models.DateField(verbose_name='Date Joined', default=timezone.now)
    active = models.BooleanField(verbose_name='Is_Active', default=True)
    staff = models.BooleanField(verbose_name='Is_Staff', default=False)
    admin = models.BooleanField(verbose_name='Is_Admin', default=False)
    role = models.CharField(verbose_name='Position', choices=ROLES, default=ROLES[2:1], max_length=20)
    country = models.CharField(verbose_name='Country', max_length=25, choices=COUNTRIES, default=COUNTRIES[0][1])

    objects = managers.UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')
    
    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    def __str__(self):
        return self.email

   

class PhoneBook(models.Model):
    '''Модель телефонного справочника'''

    GENDER = (
        ('Мужской','Мужской'),
        ('Женский','Женский')
    )

    WORK_STATUS = (
        ('Работает','Работает'),
        ('Уволен','Уволен'),
        ('Отпуск','Отпуск'),
        ('Больничный','Больничный')
    )

    COUNTRIES = (
        ('Бишкек', 'Бишкек'),
        ('Ош', 'Ош'),
        ('Нарын', 'Нарын'),
        ('Каракол', 'Каракол'),
        ('Жалал-Абад', 'Жалал-Абад'),
        ('Баткен', 'Баткен'),
        ('Талас', 'Талас'),
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Владелец'
    )

    first_name = models.CharField(
        max_length=50,
        verbose_name='Имя'
    )

    last_name = models.CharField(
        max_length=50,
        verbose_name='Фамилия'
    )
    
    phone_number = models.DecimalField(
        max_digits=12,
        decimal_places=0,
        unique=True,
        verbose_name='Номер телефона'
    )

    email = models.EmailField(
        max_length= 60,
        unique=True
    )

    city = models.CharField(
        max_length=30,
        verbose_name='Город проживания',
        choices=COUNTRIES, 
        default=COUNTRIES[0][1]
    )

    age = models.IntegerField(
        verbose_name='Возраст'
    )

    gender = models.CharField(
        max_length=25,
        verbose_name='Пол',
        choices=GENDER,
        default=GENDER[0:1]
    )


    work_status = models.CharField(
        max_length=25,
        verbose_name='Статус работы',
        choices=WORK_STATUS,
        default=WORK_STATUS[0:1]
    )

    employment_date = models.DateField(
        default=timezone.now,
        verbose_name='Дата приема на работу'
    )

    date_of_dismissal = models.DateField(
        verbose_name='Дата увольнения',
        blank=True,
        null=True
    
    )
    @property
    def count_experience(self):
        if self.date_of_dismissal:
            experience = self.date_of_dismissal - self.employment_date
        else:
            experience = dt.now().date() - self.employment_date
        
        years = int(experience.days // 365.25)
        
        month = int(experience.days // 30)
       
        days = int(experience.days)

        if month%12==0:
            month=0
        elif month%12!=0:
            month=month%12   

        if days%30==0:
            days=0
        elif days%30!=0:
            days=days%30 
        
        if years > 0:

            return f'{years} лет {month} месяцев {days} дней'
        else:
            return f'{month} месяцев {days} дней'

    class Meta:
        verbose_name_plural = 'Телефонная книга'
        verbose_name = 'Абонент'
        ordering = ('first_name',)

    def __str__(self):
        '''Описание объекта PhoneBook'''
        return f'{self.phone_number} {self.first_name} {self.last_name}'






