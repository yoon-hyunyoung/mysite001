from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Kleague1_2021_1r(models.Model):
    ranking = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=15, blank=True, null=True)
    matches = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    wons = models.IntegerField(blank=True, null=True)
    draws = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    getgoals = models.IntegerField(blank=True, null=True)
    lostgoals = models.IntegerField(blank=True, null=True)
    get_losts = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    fouls = models.IntegerField(blank=True, null=True)
    logos = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'k1_1라운드'
        ordering = ('-points', '-getgoals')
        #장고 데이터 이름별로 보이게한은 코드
    def __str__(self):
        return self.name 

class Kleague2_2021_1r(models.Model):
    ranking = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=15, blank=True, null=True)
    matches = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    wons = models.IntegerField(blank=True, null=True)
    draws = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    getgoals = models.IntegerField(blank=True, null=True)
    lostgoals = models.IntegerField(blank=True, null=True)
    get_losts = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    fouls = models.IntegerField(blank=True, null=True)
    logos = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'k2_1라운드'
        ordering = ('-points', '-getgoals')
        #장고 데이터 이름별로 보이게한은 코드
    def __str__(self):
        return self.name 


class Kleague1_2021_2r(models.Model):
    ranking = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=15, blank=True, null=True)
    matches = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    wons = models.IntegerField(blank=True, null=True)
    draws = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    getgoals = models.IntegerField(blank=True, null=True)
    lostgoals = models.IntegerField(blank=True, null=True)
    get_losts = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    fouls = models.IntegerField(blank=True, null=True)
    logos = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'k1_2라운드'
        ordering = ('-points', '-getgoals')
        #장고 데이터 이름별로 보이게한은 코드
    def __str__(self):
        return self.name 

class Kleague2_2021_2r(models.Model):
    ranking = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=15, blank=True, null=True)
    matches = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    wons = models.IntegerField(blank=True, null=True)
    draws = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    getgoals = models.IntegerField(blank=True, null=True)
    lostgoals = models.IntegerField(blank=True, null=True)
    get_losts = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    fouls = models.IntegerField(blank=True, null=True)
    logos = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'k2_2라운드'
        ordering = ('-points', '-getgoals')
        #장고 데이터 이름별로 보이게한은 코드
    def __str__(self):
        return self.name

class Kleague1_2021_3r(models.Model):
    ranking = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=15, blank=True, null=True)
    matches = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    wons = models.IntegerField(blank=True, null=True)
    draws = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    getgoals = models.IntegerField(blank=True, null=True)
    lostgoals = models.IntegerField(blank=True, null=True)
    get_losts = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    fouls = models.IntegerField(blank=True, null=True)
    logos = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'k1_3라운드'
        ordering = ('-points', '-getgoals')
        #장고 데이터 이름별로 보이게한은 코드
    def __str__(self):
        return self.name  