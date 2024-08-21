from django.contrib import admin
from django.urls import path
from app2007.views import *
from app0808.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('oquvchi/', oquvchi),
    path('oquvchi2/', oquvchi2),
    path('muallif/', muallif),
    path('muallif2/<int:son>/', muallif2),
    path('kitob/', kitob),
    path('kitob2/<int:son>/', kitob2),
    path('kitobb2/<str:nomi>/', kitobb2),
    path('oquvchii/<str:nomi>/', oquvchii),
    path('mualiff2/<str:nomi>/', mualliff2),
    path('kutubxonachi/<str:nomi>/', kutubxonachi),
    path('record3/<int:son>/', record3),
    path('record/', record),
    path('mustaql/', mustaql),
    path('record2/', record2),
    path('record4/', record4),
    path('muallif3/', muallif3),
    path('muallif4/', muallif4),
    path('muallif5/', muallif5),
    path('kitob3/', kitob3),
    path('kitob4/', kitob4),
    path('kitob5/', kitob5),
    path('kitob6/', kitob6),
    path('muallif/ochirish/<int:son>/', ochirish),
    path('kitob/ochirish/<int:son>/', ochirish2),
    path('todo/', todo1),
    path('todo/ochirish/<int:son>/', ochirish),
]