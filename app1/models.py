from django.db import models


class Users(models.Model):
  userID = models.IntegerField(primary_key=True)
  veljavnost = models.DateField()
  ime = models.CharField(max_length=255, default='')
  opis = models.CharField(max_length=255, default='')


class Filters(models.Model):
  filterID = models.AutoField(primary_key=True)
  userID = models.IntegerField()
  znamka = models.CharField(max_length=255, null=True)
  model = models.CharField(max_length=255, null=True)
  cena_od = models.IntegerField(null=True)
  cena_do = models.IntegerField(null=True)
  letnik_od = models.IntegerField(null=True)
  letnik_do = models.IntegerField(null=True)


class Avti(models.Model):
  carID = models.IntegerField(primary_key=True)
  ime = models.CharField(max_length=255, default='')
  cena = models.IntegerField()
  registracija = models.DateField()
  km = models.IntegerField()
  fizicna_os = models.SmallIntegerField()
  poskodovano = models.SmallIntegerField()
  scrapeTime = models.DateTimeField()

  def __str__(self):
    return self.ime

class Regkode(models.Model):
  id = models.AutoField(primary_key=True)
  koda = models.IntegerField()
  opis = models.CharField(max_length=255, default='')
