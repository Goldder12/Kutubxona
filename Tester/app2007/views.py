from django.shortcuts import render,redirect
from .models import *

def oquvchi(request):
    qidiruv = request.GET.get('qidir4')
    hamma = Oquvchi.objects.all()
    if qidiruv == "on":
        hamma = Oquvchi.objects.filter(bitiruvchi = True)
    data={
        'oquvchi' : hamma
    }
    return render(request,'index.html', data)

def muallif(request ):
    qidiruv = request.GET.get('qidir1')
    hamma = Muallif.objects.all()
    if qidiruv:
        hamma = Muallif.objects.filter(ism = qidiruv)
    data={
        'muallif' : hamma
    }
    return render(request,'index2.html', data)
def ochirish(request, son):
    Muallif.objects.get(id=son).delete()
    return redirect('/muallif/')

def muallif3(request):
    qidiruv = request.GET.get('qidir2')
    hamma = Muallif.objects.all()
    if qidiruv == "on":
        hamma = Muallif.objects.filter(tirik = True)
    data={
        'muallif3' : hamma
    }
    return render(request,'index7.html', data)

def oquvchi2(b):
    data={
        'oquvchi2' : Oquvchi.objects.exclude(kitob_soni=0)
    }
    return render(b,'index1.html', data)

def muallif2(d,son):
    data={
        'muallif2' : Muallif.objects.filter(id=son)
    }
    return render(d,'index3.html', data)

def kitob2(h,son):
    data={
        'kitob2' : Kitob.objects.filter(id=son)
    }
    return render(h,'index5.html', data)

def kitobb2(h,nomi):
    data={
        'kitobb2' : Kitob.objects.filter(nom=nomi)
    }
    return render(h,'mustaql1.html', data)

def oquvchii(h,nomi):
    data={
        'oquvchii' : Oquvchi.objects.filter(ism=nomi)
    }
    return render(h,'mustaql2.html', data)

def mualliff2(h,nomi):
    data={
        'mualliff2' : Muallif.objects.filter(ism=nomi)
    }
    return render(h,'mustaql4.html', data)

def kutubxonachi(h,nomi):
    data={
        'kutubxonachi' : Kutubxonachi.objects.filter(ism=nomi)
    }
    return render(h,'mustaql3.html', data)

def record3(hd,son):
    data={
        'record3' : Kutubxona.objects.filter(id=son)
    }
    return render(hd,'index15.html', data)

def record4(ht):
    data={
        'record4' : Kutubxona.objects.filter(oquvchi__bitiruvchi=True)
    }
    return render(ht,'index16.html', data)

def kitob(request ):
    qidiruv = request.GET.get('qidir3')
    hamma = Kitob.objects.all()
    if qidiruv:
        hamma = Kitob.objects.filter(nom = qidiruv)
    data={
        'kitob' : hamma
    }
    return render(request,'index4.html', data)

def ochirish2(request, son):
    Kitob.objects.get(id=son).delete()
    return redirect('/kitob/')

def kitob4(gx):
    data={
        'kitob4' : Kitob.objects.filter(muallif__tirik=True)
    }
    return render(gx,'index11.html', data)

def kitob6(request ):
    qidiruv = request.GET.get('qidir1')
    hamma = Kitob.objects.all()
    if qidiruv:
        hamma = Kitob.objects.filter(sahifa = qidiruv)
    data={
        'kitob6' : hamma
    }
    return render(request,'index14.html', data)

def kitob5(gx):
    data={
        'kitob5' : Kitob.objects.filter(janr="Badiiy")
    }
    return render(gx,'index12.html', data)

def kitob3(gv):
    data={
        'kitob3' : Kitob.objects.order_by('-sahifa')[:3]
    }
    return render(gv,'index8.html', data)

def muallif4(gh):
    data={
        'muallif4' : Muallif.objects.order_by('-kitob_soni')[:3]
    }
    return render(gh,'index9.html', data)

def muallif5(gt):
    data={
        'muallif5' : Muallif.objects.order_by('tugigan_yil')[:3]
    }
    return render(gt,'index13.html', data)

def record2(gd):
    data={
        'record2' : Kutubxona.objects.order_by('olgan_vaqt')[:3]
    }
    return render(gd,'index10.html', data)

def record(request ):
    qidiruv = request.GET.get('qidir')
    hamma = Kutubxona.objects.all()
    if qidiruv:
        hamma = Kutubxona.objects.filter(oquvchi__ism = qidiruv)
    data={
        'record' : hamma
    }
    return render(request,'index6.html', data)

def mustaql(vx):
    data={
        'mustaql' : Kutubxona.objects.all()
    }
    return render(vx,'Mustaqil.html', data)

def ochir(vx,son):
    data={
        'ochir' : Muallif
    }
    return redirect("/muallif/")