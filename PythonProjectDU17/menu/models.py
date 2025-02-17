from django.db import models

class Film(models.Model):
    nazev = models.CharField(max_length=255)
    zanr = models.CharField(max_length=100)
    rok = models.IntegerField()

    def __str__(self):
        return self.nazev

class Kniha(models.Model):
    nazev = models.CharField(max_length=255)
    zanr = models.CharField(max_length=100, default="Neurčeno")  # ✅ Přidání pole zanr
    autor = models.CharField(max_length=100)
    rok = models.IntegerField()

    def __str__(self):
        return self.nazev

class Hra(models.Model):
    nazev = models.CharField(max_length=255)
    zanr = models.CharField(max_length=100, default="Neurčeno")  # ✅ Přidali jsme výchozí hodnotu
    platforma = models.CharField(max_length=100)
    rok = models.IntegerField()

    def __str__(self):
        return self.nazev

