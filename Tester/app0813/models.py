from django.db import models
class Yonalish(models.Model):
    nom = models.CharField(max_length=30)
    aktive = models.BooleanField()

    def __str__(self):
        return self.nom

class Fan(models.Model):
    nom = models.CharField(max_length=30)
    yonalish = models.ForeignKey(Yonalish,on_delete=models.CASCADE)
    asosiy = models.BooleanField()

    def __str__(self):
        return self.nom
class Ustoz(models.Model):
    ism = models.CharField(max_length=30)
    jinsi = models.CharField(max_length=30)
    yoshi = models.SmallIntegerField()
    daraja = models.CharField(max_length=30)

    def __str__(self):
        return self.ism

class Universitet(models.Model):
    ustoz = models.ForeignKey(Ustoz,on_delete=models.CASCADE)
    yonalish = models.ForeignKey(Yonalish,on_delete=models.CASCADE)
    Fan = models.ForeignKey(Fan,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ustoz},{self.Fan}"
