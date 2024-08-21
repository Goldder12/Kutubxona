from django.db import models
class Oquvchi(models.Model):
    ism = models.CharField(max_length=30)
    guruh = models.SmallIntegerField()
    yosh = models.SmallIntegerField()
    yonalish = models.CharField(max_length=30)
    bitiruvchi = models.BooleanField()
    kitob_soni = models.SmallIntegerField(null=True,blank=True)

    def __str__(self):
        return f"{self.ism}"

class Muallif(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.SmallIntegerField()
    tirik = models.BooleanField()
    tugigan_yil = models.DateField(null=True , blank=True)
    jinsi = models.CharField(max_length=30, null=True, blank=True)
    kitob_soni = models.SmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.ism

class Kitob(models.Model):
    nom = models.CharField(max_length=30)
    muallif = models.ForeignKey(Muallif,on_delete=models.CASCADE)
    janr = models.CharField(max_length=30)
    sahifa = models.SmallIntegerField()
    turi = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.nom

class Kutubxonachi(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.SmallIntegerField()

    def __str__(self):
        return self.ism

class Kutubxona(models.Model):
    oquvchi = models.ForeignKey(Oquvchi,on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob,on_delete=models.CASCADE)
    olgan_vaqt = models.DateField()
    qaytarish_vaqti = models.DateField(null=True,blank=True)
    kutubxonachi = models.ForeignKey(Kutubxonachi,on_delete=models.CASCADE)
    qaytargan = models.BooleanField()

    def __str__(self):
        return f"{self.oquvchi},{self.kitob}"
