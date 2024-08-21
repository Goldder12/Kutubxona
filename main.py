import datetime
hozir = datetime.date.today()
hozir = str(hozir)
yil = hozir[:4]
d = int(yil)
kerakli_sana = d-45
a = hozir.replace(str(d),str(kerakli_sana))
print(kerakli_sana)
print(hozir)
print(a)